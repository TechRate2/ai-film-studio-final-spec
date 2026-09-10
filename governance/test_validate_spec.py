"""Negative specification mutations. No application/provider code."""
import json
import csv
import io
import shutil
import tempfile
import unittest
import yaml
from pathlib import Path
from validate_spec import validate

class GovernanceTests(unittest.TestCase):
    source = Path(__file__).resolve().parents[1]

    def test_valid_tree(self):
        self.assertEqual([], validate(self.source)[0])

    def mutate(self, change, expected):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)/'repo'
            shutil.copytree(self.source,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
            change(root)
            errors=validate(root)[0]
            self.assertTrue(any(expected in e for e in errors), errors)

    @staticmethod
    def json_change(root,path,change):
        p=root/path;d=json.loads(p.read_text());change(d);p.write_text(json.dumps(d))

    def test_missing_required(self):
        self.mutate(lambda r:(r/'spec/00_SPEC_LOCK.md').unlink(),'Missing required file')

    def test_job_vocabulary(self):
        self.mutate(lambda r:self.json_change(r,'schemas/job.schema.json',lambda d:d['properties'].update(status={'enum':['QUEUED']})),'Invariant mismatch job_status')

    def test_paid_certainty(self):
        self.mutate(lambda r:self.json_change(r,'schemas/common.schema.json',lambda d:d['$defs']['paid_certainty']['enum'].remove('UNKNOWN')),'Invariant mismatch paid_certainty')

    def test_missing_authorization(self):
        self.mutate(lambda r:self.json_change(r,'schemas/paid_attempt.schema.json',lambda d:d['required'].remove('authorization_id')),'Critical required fields missing')

    def test_auto_retry(self):
        self.mutate(lambda r:self.json_change(r,'schemas/qa_report.schema.json',lambda d:d['properties']['auto_paid_retry_allowed'].update(const=True)),'Invariant mismatch auto_paid_retry_allowed')

    def test_open_timeline(self):
        self.mutate(lambda r:self.json_change(r,'schemas/composition_timeline.schema.json',lambda d:d['properties']['export_target'].update(type='object')),'untyped open object')

    def test_broken_reference(self):
        self.mutate(lambda r:self.json_change(r,'schemas/common.schema.json',lambda d:d['$defs'].update(bad={'$ref':'missing.schema.json'})),'unresolved $ref')

    def test_task_reading(self):
        def change(r):
            p=next((r/'tasks').glob('TASK_025_*.md'));p.write_text(p.read_text().replace('`schemas/universal_video_spec.schema.json`','omitted'))
        self.mutate(change,'missing required reading')

    def test_paid_order(self):
        def change(d):
            d['execution_order'].remove('TASK-024');d['execution_order'].insert(0,'TASK-024')
        self.mutate(lambda r:self.json_change(r,'governance/contract_index.json',change),'paid safety prerequisite violated')

    def test_false_implemented(self):
        def change(r):
            p=r/'traceability/REQUIREMENTS_TRACEABILITY.csv';p.write_text(p.read_text().replace('NOT_STARTED','IMPLEMENTED',1))
        self.mutate(change,'false IMPLEMENTED')

    def test_duplicate_requirement(self):
        def change(r):
            p=r/'traceability/REQUIREMENTS_TRACEABILITY.csv';p.write_text(p.read_text().replace('R-002,','R-001,',1))
        self.mutate(change,'Duplicate requirement IDs')

    def test_unproven_measured(self):
        def change(r):
            p=r/'profiles/models/seedance_2_0.yaml';p.write_text(p.read_text().replace('verification_status: PARTIAL','verification_status: MEASURED'))
        self.mutate(change,'MEASURED without scoped samples')

    def test_task_index_omission(self):
        self.mutate(lambda r:self.json_change(r,'governance/contract_index.json',lambda d:d['tasks'].pop('TASK-026')),'Task index coverage mismatch')

    def test_task_index_wrong_path(self):
        self.mutate(lambda r:self.json_change(r,'governance/contract_index.json',lambda d:d['tasks']['TASK-026'].update(path=d['tasks']['TASK-025']['path'])),'task index path mismatch')

    def test_empty_fixture_suite(self):
        self.mutate(lambda r:self.json_change(r,'evals/contract_fixtures.json',lambda d:d.update(cases=[])),'Fixture index coverage mismatch')

    def test_duplicate_fixture(self):
        self.mutate(lambda r:self.json_change(r,'evals/contract_fixtures.json',lambda d:d['cases'].append(d['cases'][0])),'Missing/duplicate fixture IDs')

    def test_removed_negative_fixtures(self):
        self.mutate(lambda r:self.json_change(r,'evals/contract_fixtures.json',lambda d:d.update(cases=[c for c in d['cases'] if c['valid']])),'positive/negative fixture coverage missing')

    def test_fixture_requirement_drift(self):
        self.mutate(lambda r:self.json_change(r,'evals/contract_fixtures.json',lambda d:d['cases'][0].update(requirements=['R-001'])),'schema/requirement drift')

    def test_capability_condition_removed(self):
        self.mutate(lambda r:self.json_change(r,'schemas/effective_capability.schema.json',lambda d:d.pop('allOf')),'Fixture capability-supported-rejects-')

    def test_claim_promotion_condition_removed(self):
        self.mutate(lambda r:self.json_change(r,'schemas/common.schema.json',lambda d:d['$defs']['claim'].pop('allOf')),'Fixture profile-rejects-promoted-')

    def test_provider_measured_claim_shape(self):
        # Synthetic metadata exercises the provider branch, not real measurement.
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)/'repo'
            shutil.copytree(self.source,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
            cases = json.loads((root/'evals/contract_fixtures.json').read_text())['cases']
            sample = next(c['instance']['capabilities']['first_frame'] for c in cases if c['id']=='profile-observed-scoped-samples')
            path = root/'profiles/providers/PROVIDER_PROFILE_TEMPLATE.yaml'
            data = yaml.safe_load(path.read_text())
            data['verification_status'] = 'MEASURED'
            data['capability_exposure'] = {'synthetic_feature': sample}
            path.write_text(yaml.safe_dump(data,sort_keys=False))
            self.assertEqual([], validate(root)[0])

    def test_localization_release_partition(self):
        self.mutate(lambda r:self.json_change(r,'governance/contract_index.json',lambda d:d['release_gates']['CORE']['requirements'].append('R-089')),'Release gate partition drift')

    def test_localization_trace_gate(self):
        def change(r):
            p=r/'traceability/REQUIREMENTS_TRACEABILITY.csv'
            rows=list(csv.DictReader(io.StringIO(p.read_text())))
            next(x for x in rows if x['requirement_id']=='R-089')['release_gate']='CORE'
            with p.open('w',newline='') as f:
                writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
        self.mutate(change,'release gate mismatch')

    def test_localization_core_first(self):
        self.mutate(lambda r:self.json_change(r,'governance/contract_index.json',lambda d:d['tasks']['TASK-044'].update(depends_on=[])),'localization core-first prerequisite violated')

    def test_localization_no_video(self):
        self.mutate(lambda r:self.json_change(r,'schemas/localization_project.schema.json',lambda d:d['properties']['video_generation_allowed'].update(const=True)),'Invariant mismatch video_generation_allowed')

    def test_localization_mode_condition(self):
        self.mutate(lambda r:self.json_change(r,'schemas/localization_project.schema.json',lambda d:d.pop('allOf')),'Fixture localization-rejects-subtitle-voice')

    def test_localization_snapshot_required(self):
        self.mutate(lambda r:self.json_change(r,'schemas/localization_review.schema.json',lambda d:d['required'].remove('expected_project_version_id')),'Critical required fields missing')

    def test_handoff_read_omission(self):
        def change(r):
            p=r/'CLAUDE.md';p.write_text(p.read_text().replace('`governance/IMPLEMENTATION_HANDOFF.md`','omitted'))
        self.mutate(change,'missing mandatory handoff reading')

    def test_handoff_index_omission(self):
        self.mutate(lambda r:self.json_change(r,'governance/contract_index.json',lambda d:d['handoff_readers'].pop()),'Handoff reader index drift')

    def test_handoff_guide_missing(self):
        self.mutate(lambda r:(r/'governance/IMPLEMENTATION_HANDOFF.md').unlink(),'Missing required file')

if __name__=='__main__':
    unittest.main()
