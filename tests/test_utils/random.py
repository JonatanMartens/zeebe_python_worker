from random import randint
from uuid import uuid4

from pyzeebe import JobStatus, Job

RANDOM_RANGE = 1000000


def random_job(status: JobStatus = JobStatus.Running) -> Job:
    return Job(key=randint(0, RANDOM_RANGE), _type=str(uuid4()), workflow_instance_key=randint(0, RANDOM_RANGE),
               bpmn_process_id=str(uuid4()), deadline=randint(0, RANDOM_RANGE), workflow_key=randint(0, RANDOM_RANGE),
               element_id=str(uuid4()), element_instance_key=randint(0, RANDOM_RANGE), custom_headers={}, variables={},
               retries=randint(0, 3), status=status, workflow_definition_version=randint(0, 100), worker=str(uuid4()))
