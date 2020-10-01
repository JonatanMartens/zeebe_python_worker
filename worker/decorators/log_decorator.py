from loguru import logger
from pyzeebe import Job, JobStatus


def log_decorator(job: Job) -> Job:
    if job.status == JobStatus.Running:
        logger.info(f"Received job: {job}")
    elif job.status == JobStatus.Completed:
        logger.info(f"Completed job: {job}")
    elif job.status in [JobStatus.Failed, JobStatus.ErrorThrown]:
        logger.warning(f"Failed to complete job: {job}")
    return job
