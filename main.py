import os
import sys
from configparser import ConfigParser

from loguru import logger
from pyzeebe import ZeebeWorker

from worker.decorators.log_decorator import log_decorator
from worker.tasks.example_task import example_task_router
from worker.utils.config import get_credentials, get_zeebe_config

logger.add(sys.stderr, format="{time} {level} {message}", filter="root", level="INFO")

config = ConfigParser()
config.read(os.getenv("CONFIG_FILE_LOCATION") or "/src/config/worker.ini")

credentials = get_credentials(config)
zeebe_config = get_zeebe_config(config)

zeebe_worker = ZeebeWorker(credentials=credentials, **zeebe_config)

zeebe_worker.before(log_decorator)
zeebe_worker.after(log_decorator)

zeebe_worker.include_router(example_task_router)

if __name__ == '__main__':
    logger.info(f"Connecting to gateway at address: {zeebe_worker.zeebe_adapter.connection_uri}")
    zeebe_worker.work()
