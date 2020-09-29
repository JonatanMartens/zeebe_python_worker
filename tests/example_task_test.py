from random import randint

from worker.tasks.example_task import example_task, add_one


def test_example_task():
    assert example_task("John") == {"output": "Hello World, John!"}


def test_add_one():
    integer = randint(0, 10000)
    assert add_one(integer) == integer + 1
