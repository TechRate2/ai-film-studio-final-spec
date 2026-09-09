"""Offline canonical contract checks. This validates specification, not application behavior."""
from __future__ import annotations

import argparse
import csv
import json
import io
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urldefrag

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource


def walk(value, pointer=""):
    if isinstance(value, dict):
        yield pointer, value
        for key, child in value.items():
            yield from walk(child, pointer + "/" + key)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            yield from walk(child, pointer + "/" + str(i))


def pointer(document, fragment):
    if not fragment:
        return document
    if not fragment.startswith("/"):
        raise ValueError("Only local JSON pointers are supported: " + fragment)
    for part in fragment[1:].split("/"):
        part = unquote(part).replace("~1", "/").replace("~0", "~")
        document = document[int(part)] if isinstance(document, list) else document[part]
    return document


def validate(root: Path):
    errors, checks = [], Counter()

    def check(condition, message, category):
        checks[category] += 1
        if not condition:
            errors.append(message)

    def read_json(path):
        try:
            return json.loads(path.read_text())
        except (OSError, ValueError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            return {}

    idx = read_json(root / "governance/contract_index.json")
    required = ["AGENTS.md", "CLAUDE.md", "CODEX.md", "README.md", "MANIFEST.md", "SPEC_VERSION", "spec/00_SPEC_LOCK.md", "tasks/00_IMPLEMENTATION_ORDER.md", "evals/GOLDEN_SCENARIOS.md", "traceability/REQUIREMENTS_TRACEABILITY.csv", ".github/workflows/spec-governance.yml", "governance/validate_spec.py", "governance/test_validate_spec.py"]
    for path in sorted(set(required + idx.get("required_canonical_paths", []))):
        check((root / path).is_file(), f"Missing required file: {path}", "required_files")
    if errors:
        return errors, dict(checks)
    versions = dict(line.split("=", 1) for line in (root / "SPEC_VERSION").read_text().splitlines() if "=" in line)
    check(versions.get("AI_FILM_STUDIO_SPEC_VERSION") == idx["version"], "SPEC_VERSION/index version mismatch", "version")
    for path in ["README.md", "MANIFEST.md"]:
        check(f'V{idx["version"]}' in (root / path).read_text(), path + " version mismatch", "version")
    spec_numbers = sorted(p.name[:2] for p in (root / "spec").glob("*.md"))
    check(spec_numbers == [f"{n:02}" for n in range(idx["counts"]["specs"])], "Spec numbering mismatch", "spec_numbering")
    schema_paths = sorted((root / "schemas").glob("*.schema.json"))
    schemas = {p.name: read_json(p) for p in schema_paths}
    registry = Registry().with_resources((p.as_uri(), Resource.from_contents(schemas[p.name])) for p in schema_paths)
    validators = {p.name: Draft202012Validator({"$ref": p.as_uri()}, registry=registry, format_checker=FormatChecker()) for p in schema_paths}
    titles = [s.get("title") for s in schemas.values()]
    check(len(titles) == len(set(titles)) and all(titles), "Duplicate/missing schema titles", "schema_titles")
    for p in schema_paths:
        schema = schemas[p.name]
        try:
            Draft202012Validator.check_schema(schema)
            checks["metaschemas"] += 1
        except Exception as exc:
            errors.append(f"{p.name}: invalid metaschema: {exc}")
        for loc, node in walk(schema):
            if "$ref" in node:
                target, fragment = urldefrag(node["$ref"])
                check(not re.match(r"^[a-zA-Z]+:", target), f"{p.name}{loc}: nonlocal $ref", "local_refs")
                try:
                    linked = (p.parent / target).resolve() if target else p
                    check(linked.is_relative_to(root / "schemas"), f"{p.name}: $ref escapes schemas", "local_refs")
                    pointer(json.loads(linked.read_text()), fragment)
                except (OSError, KeyError, ValueError, IndexError) as exc:
                    errors.append(f"{p.name}{loc}: unresolved $ref {node['$ref']}: {exc}")
            if node.get("type") == "object":
                check("properties" in node or isinstance(node.get("additionalProperties"), dict), f"{p.name}{loc}: untyped open object", "typed_objects")
                if "properties" in node:
                    check(node.get("additionalProperties") is False, f"{p.name}{loc}: open record", "typed_objects")
                    check(set(node.get("required", [])) <= set(node["properties"]), f"{p.name}{loc}: required unknown field", "typed_objects")
    def resolve(node, path):
        while "$ref" in node:
            target, fragment = urldefrag(node["$ref"])
            path = (path.parent / target).resolve() if target else path
            node = pointer(json.loads(path.read_text()), fragment)
        return node
    for invariant in idx["invariants"]:
        spec = (root / invariant["spec"]).read_text()
        section = spec.split("## Machine-checkable invariants\n", 1)[1]
        normative = json.loads(re.search(r"```json\s*\n(.*?)\n```", section, re.S)[1])
        for target in invariant["targets"]:
            path = root / target["schema"]
            node = resolve(pointer(json.loads(path.read_text()), target["pointer"]), path)
            check(node.get(target["keyword"]) == normative[invariant["key"]], f"Invariant mismatch {invariant['key']} at {target['schema']}", "invariants")
    for schema_name, names in idx["required_fields"].items():
        check(set(names) <= set(schemas[schema_name]["required"]), f"Critical required fields missing: {schema_name}", "critical_required")
    rows = list(csv.DictReader(io.StringIO((root / "traceability/REQUIREMENTS_TRACEABILITY.csv").read_text())))
    req_ids = [r["requirement_id"] for r in rows]
    check(len(req_ids) == len(set(req_ids)), "Duplicate requirement IDs", "traceability")
    check(req_ids == [f"R-{n:03}" for n in range(1, len(req_ids)+1)], "Requirement ID numbering mismatch", "traceability")
    golden_text = (root / "evals/GOLDEN_SCENARIOS.md").read_text()
    goldens = re.findall(r"^## (GS\d\d) —", golden_text, re.M)
    check(len(goldens) == len(set(goldens)), "Duplicate Golden IDs", "goldens")
    check(goldens == [f"GS{n:02}" for n in range(1, len(goldens)+1)], "Golden numbering mismatch", "goldens")
    task_files = sorted((root / "tasks").glob("TASK_[0-9][0-9][0-9]_*.md"))
    task_ids = ["TASK-" + p.name[5:8] for p in task_files]
    check(task_ids == [f"TASK-{n:03}" for n in range(1,idx["counts"]["tasks"]+1)], "Task file numbering mismatch", "tasks")
    check(set(idx["tasks"]) == set(task_ids), "Task index coverage mismatch", "task_graph")
    actual_task_paths = {"TASK-" + p.name[5:8]: str(p.relative_to(root)) for p in task_files}
    for tid, packet in idx["tasks"].items():
        check(packet.get("path") == actual_task_paths.get(tid), f"{tid}: task index path mismatch", "task_graph")
    if errors:
        return errors, dict(checks)
    order = idx["execution_order"]
    check(len(order) == len(set(order)) and set(order) == set(task_ids), "Invalid execution order", "task_graph")
    # Accepted ADR-0002 partitions intentionally fixed release scopes, preventing
    # a future task from making the core gate wait on its own later extension.
    gates = idx.get("release_gates", {})
    expected_gates = {
        "CORE": {"requirements": [f"R-{n:03}" for n in range(1, 89)], "goldens": [f"GS{n:02}" for n in range(1, 29)], "terminal_task": "TASK-043"},
        "LOCALIZATION": {"requirements": [f"R-{n:03}" for n in range(89, 97)], "goldens": [f"GS{n:02}" for n in range(29, 34)], "terminal_task": "TASK-046", "requires": "CORE"},
    }
    check(gates == expected_gates, "Release gate partition drift", "release_gates")
    for row in rows:
        expected_gate = "CORE" if row["requirement_id"] in expected_gates["CORE"]["requirements"] else "LOCALIZATION"
        check(row.get("release_gate") == expected_gate, f"{row['requirement_id']}: release gate mismatch", "release_gates")
    for child, parent in [("TASK-044", "TASK-043"), ("TASK-045", "TASK-044"), ("TASK-046", "TASK-045")]:
        check(parent in idx["tasks"].get(child, {}).get("depends_on", []) and parent in order and child in order and order.index(parent) < order.index(child), f"{child}: localization core-first prerequisite violated", "release_gates")
    covered_tasks, covered_gs, covered_schemas = set(), set(), set()
    for row in rows:
        rid = row["requirement_id"]
        check((root / row["canonical_spec"]).is_file(), f"{rid}: broken canonical source", "traceability")
        for column, valid, covered in [("implementation_task", set(task_ids), covered_tasks), ("golden_scenarios", set(goldens), covered_gs), ("schemas", {str(p.relative_to(root)) for p in schema_paths}, covered_schemas)]:
            values = set(filter(None, row[column].split(",")))
            check(bool(values) or column == "schemas", f"{rid}: empty {column}", "traceability")
            check(values <= valid, f"{rid}: invalid {column}: {values-valid}", "traceability")
            covered.update(values)
        check(row["status"] in ["NOT_STARTED", "PARTIAL", "BLOCKED", "IMPLEMENTED"], f"{rid}: invalid status", "traceability")
        if row["status"] == "IMPLEMENTED":
            check(bool(row["implementation_refs"].strip()) and bool(row["test_refs"].strip()), f"{rid}: false IMPLEMENTED without evidence", "traceability")
    check(covered_tasks == set(task_ids), f"Orphan tasks: {set(task_ids)-covered_tasks}", "coverage")
    check(covered_gs == set(goldens), f"Orphan goldens: {set(goldens)-covered_gs}", "coverage")
    check(covered_schemas == {str(p.relative_to(root)) for p in schema_paths}, "Orphan schemas", "coverage")
    for tid, packet in idx["tasks"].items():
        text = (root / packet["path"]).read_text()
        for dep in packet["depends_on"]:
            check(dep in order and order.index(dep)<order.index(tid), f"{tid}: forward/cyclic dependency {dep}", "task_graph")
            check(dep in text, f"{tid}: dependency absent from packet", "tasks")
        for path in packet["specs"] + packet["schemas"]:
            check((root / path).is_file() and f"`{path}`" in text, f"{tid}: missing required reading {path}", "tasks")
        linked = [r for r in rows if tid in r["implementation_task"].split(",")]
        for field, expected in [("requirements", {r["requirement_id"] for r in linked}), ("goldens", {g for r in linked for g in r["golden_scenarios"].split(",")})]:
            check(set(packet[field]) == expected, f"{tid}: {field} mapping drift", "tasks")
            check(all(x in text for x in expected), f"{tid}: {field} absent from packet", "tasks")
        check(text.count("- [ ]") >= 3, f"{tid}: insufficient auditable acceptance", "tasks")
    for task in ["TASK-024", "TASK-030", "TASK-037", "TASK-031"]:
        check(order.index("TASK-032") < order.index(task) and order.index("TASK-033") < order.index(task), f"{task}: paid safety prerequisite violated", "task_graph")
    phase_rows = list(csv.DictReader(io.StringIO((root / "traceability/PHASE_GATE_MATRIX.csv").read_text())))
    for row in phase_rows:
        check((root / row["gate_document"]).is_file(), "Broken phase gate document", "phases")
        check(all(t in task_ids or t == "PROVIDER_EXPANSION_TEMPLATE" for t in row["required_tasks"].split(",")), "Broken phase task reference", "phases")
    for p in (root / "profiles").rglob("*.yaml"):
        try:
            data = yaml.safe_load(p.read_text())
            name = "provider_profile.schema.json" if "provider_id" in data else "model_profile.schema.json"
            for err in validators[name].iter_errors(data):
                errors.append(f"{p.relative_to(root)} {list(err.path)}: {err.message}")
            checks["profiles"] += 1
            if data.get("routable"):
                check(bool(data.get("version")) and data.get("modality") != "FAMILY", f"{p}: routable without exact version", "profile_evidence")
            if data.get("verification_status") == "MEASURED":
                claims = [node for _, node in walk(data) if {"status", "value", "evidence_label"} <= set(node)]
                check(any(c.get("evidence_label") == "PRODUCT_OBSERVED" and c.get("sample_count",0)>0 and c.get("sample_refs") and c.get("provider_scope") for c in claims), f"{p}: MEASURED without scoped samples", "profile_evidence")
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f"Profile parse: {p}: {exc}")
    skill_ids = []
    for p in (root / "skills").rglob("*.md"):
        if p.name == "README.md":
            continue
        text = p.read_text()
        try:
            meta = yaml.safe_load(text.split("---",2)[1])
            skill_ids.append(meta["skill_id"])
            check((root / meta["knowledge"]).is_file() and meta["version"]>=1, f"{p}: invalid skill metadata", "skills")
            check(all(h in text for h in ["## Retrieve when", "## Decision", "## Trade-offs and when not to use", "## Output and check"]), f"{p}: missing decision sections", "skills")
        except (IndexError, KeyError, TypeError, yaml.YAMLError) as exc:
            errors.append(f"Skill metadata {p}: {exc}")
    check(len(skill_ids)==len(set(skill_ids)), "Duplicate skill IDs", "skills")
    # Only exact file-looking references are checked; wildcard/range prose is not a path.
    for p in root.rglob("*.md"):
        if ".git" in p.parts:
            continue
        text = p.read_text()
        paths = re.findall(r"`((?:spec|schemas|tasks|phases|governance|evals|traceability|knowledge|skills|profiles|prompts|examples|evidence)/[^`\s*]+\.(?:md|json|csv|yaml|py))`", text)
        for path in paths:
            if "..." in path:
                continue
            check((root / path).is_file(), f"{p.relative_to(root)}: broken internal reference {path}", "internal_paths")
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"[a-zA-Z][\w+.-]*:", link) or link.startswith("#"):
                continue
            target, fragment = urldefrag(link)
            linked = (p.parent / target).resolve()
            check(linked.is_file(), f"{p.relative_to(root)}: broken Markdown link {link}", "markdown_links")
            if linked.is_file() and fragment:
                headings = re.findall(r"^#+\s+(.+)$", linked.read_text(), re.M)
                anchors = [re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings]
                check(fragment in anchors, f"{p}: broken anchor {link}", "markdown_links")
    actual = {"specs":len(list((root/"spec").glob("*.md"))), "tasks":len(task_files), "schemas":len(schema_paths), "goldens":len(goldens), "requirements":len(rows), "phases":len(phase_rows)}
    version_keys = dict(specs="SPEC_DOC_COUNT",tasks="TASK_COUNT",schemas="SCHEMA_COUNT",goldens="GOLDEN_SCENARIO_COUNT",requirements="TRACEABILITY_REQUIREMENT_COUNT",phases="PHASE_COUNT")
    manifest = (root / "MANIFEST.md").read_text()
    for key, count in actual.items():
        check(count == idx["counts"][key] == int(versions[version_keys[key]]), f"Count drift: {key}", "counts")
        check(f"{version_keys[key]}={count}" in manifest, f"Manifest count drift: {key}", "counts")
    check(len(list((root/"phases").glob("PHASE_*.md")))==idx["counts"]["phases"], "Phase files mismatch", "counts")
    fixtures = read_json(root / "evals/contract_fixtures.json")
    cases = fixtures.get("cases", [])
    case_ids = [case.get("id") for case in cases]
    expected_ids = idx.get("fixture_ids", [])
    check(bool(case_ids) and all(isinstance(i, str) and i for i in case_ids) and len(case_ids) == len(set(case_ids)), "Missing/duplicate fixture IDs", "fixture_integrity")
    check(bool(expected_ids) and len(expected_ids) == len(set(expected_ids)) and set(case_ids) == set(expected_ids), "Fixture index coverage mismatch", "fixture_integrity")
    for name in ["keyframe_generation_pack.schema.json", "effective_capability.schema.json", "model_profile.schema.json", "paid_attempt.schema.json", "localization_project.schema.json", "localization_review.schema.json"]:
        check({c.get("valid") for c in cases if c.get("schema") == name} == {True, False}, f"{name}: positive/negative fixture coverage missing", "fixture_integrity")
    for case in cases:
        check(case.get("schema") in validators and type(case.get("valid")) is bool and "instance" in case, f"Malformed fixture {case.get('id')}", "fixture_integrity")
        check(bool(case.get("requirements")) and set(case.get("requirements", [])) <= set(req_ids), f"Fixture {case.get('id')}: invalid requirement mapping", "fixture_integrity")
        check(bool(case.get("goldens")) and set(case.get("goldens", [])) <= set(goldens), f"Fixture {case.get('id')}: invalid Golden mapping", "fixture_integrity")
        linked_rows = [r for r in rows if r["requirement_id"] in case.get("requirements", [])]
        check(all("schemas/" + case.get("schema", "") in r["schemas"].split(",") for r in linked_rows), f"Fixture {case.get('id')}: schema/requirement drift", "fixture_integrity")
        allowed_goldens = {g for r in linked_rows for g in r["golden_scenarios"].split(",")}
        check(set(case.get("goldens", [])) <= allowed_goldens, f"Fixture {case.get('id')}: requirement/Golden drift", "fixture_integrity")
        if case.get("schema") not in validators or type(case.get("valid")) is not bool or "instance" not in case:
            continue
        validator = validators[case["schema"]]
        instance_errors = list(validator.iter_errors(case["instance"]))
        check(bool(instance_errors) != case["valid"], f"Fixture {case['id']}: expected valid={case['valid']}; {[e.message for e in instance_errors[:2]]}", "contract_fixtures")
    return errors, dict(checks)


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json",action="store_true")
    args=parser.parse_args()
    errors,checks=validate(args.root.resolve())
    print(json.dumps({"status":"FAIL" if errors else "PASS","checks":checks,"errors":errors},indent=2) if args.json else f"{'FAIL' if errors else 'PASS'}: {sum(checks.values())} checks\n"+"\n".join(errors))
    raise SystemExit(bool(errors))
