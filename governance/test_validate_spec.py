"""Negative specification mutations. No application/provider code."""
import json
import shutil
import tempfile
import unittest
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

if __name__=='__main__':
    unittest.main()
