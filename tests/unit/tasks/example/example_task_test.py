from random import randint
from unittest.mock import MagicMock

from tests.test_utils.random import random_job
from worker.tasks import example_task, add_one, example_exception_handler


def test_example_task():
    assert example_task("John") == {"output": "Hello World, John!"}


def test_add_one():
    integer = randint(0, 10000)
    assert add_one(integer) == integer + 1


def test_exception_handler():
    job = random_job()
    job.set_failure_status = MagicMock()
    exception = Exception()
    example_exception_handler(exception, job)
    job.set_failure_status.assert_called_with(f"Error: {exception}")
