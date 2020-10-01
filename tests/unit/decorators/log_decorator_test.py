from unittest.mock import MagicMock

from loguru import logger
from pyzeebe import JobStatus

from tests.test_utils.random import random_job
from worker.decorators.log_decorator import log_decorator


def test_log_decorator_running():
    logger.info = MagicMock()
    job = random_job(JobStatus.Running)
    log_decorator(job)
    logger.info.assert_called_with(f"Received job: {job}")


def test_log_decorator_completed():
    logger.info = MagicMock()
    job = random_job(JobStatus.Completed)
    log_decorator(job)
    logger.info.assert_called_with(f"Completed job: {job}")


def test_log_decorator_failed():
    logger.warning = MagicMock()
    job = random_job(JobStatus.Failed)
    log_decorator(job)
    logger.warning.assert_called_with(f"Failed to complete job: {job}")


def test_log_decorator_error():
    logger.warning = MagicMock()
    job = random_job(JobStatus.ErrorThrown)
    log_decorator(job)
    logger.warning.assert_called_with(f"Failed to complete job: {job}")
