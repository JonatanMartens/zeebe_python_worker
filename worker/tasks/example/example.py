from typing import Dict

from pyzeebe import ZeebeTaskRouter, Job

example_task_router = ZeebeTaskRouter()


def example_exception_handler(exception: Exception, job: Job) -> None:
    job.set_failure_status(f"Error: {exception}")


@example_task_router.task(task_type="example", exception_handler=example_exception_handler)
def example_task(input: str) -> Dict:
    return dict(output=f"Hello World, {input}!")


@example_task_router.task(task_type="add_one", exception_handler=example_exception_handler, single_value=True,
                          variable_name="y")
def add_one(x):
    return x + 1
