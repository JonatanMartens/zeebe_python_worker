import logging

from pyzeebe import Job
from pyzeebe.job.job_status import JobStatus


def before_task_logging_decorator(job: Job) -> Job:
    logging.info(f"Received job: {job}")
    return job


def after_task_logging_decorator(job: Job) -> Job:
    if job.status == JobStatus.Completed:
        logging.info(f"Completed job: {job}")
    return job
