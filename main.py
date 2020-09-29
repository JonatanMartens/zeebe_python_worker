import logging
from configparser import ConfigParser

from pyzeebe import ZeebeWorker

from worker.decorators.logging_decorators import before_task_logging_decorator, after_task_logging_decorator
from worker.tasks.example_task import example_task_router
from worker.utils.config import get_credentials

logging.basicConfig(filename='example.log', level=logging.DEBUG)

config = ConfigParser()
config.read("config/worker.ini")

credentials = get_credentials(config)

zeebe_hostname = config.get("zeebe", "hostname")
zeebe_port = config.getint("zeebe", "port")
zeebe_request_timeout = config.getint("zeebe", "request_timeout")
zeebe_secure_connection = config.getboolean("zeebe", "secure_connection")

zeebe_worker = ZeebeWorker(hostname=zeebe_hostname, port=zeebe_port, secure_connection=zeebe_secure_connection,
                           request_timeout=zeebe_request_timeout, credentials=credentials)

zeebe_worker.before(before_task_logging_decorator)
zeebe_worker.after(after_task_logging_decorator)

zeebe_worker.include_router(example_task_router)

if __name__ == '__main__':
    logging.info(f"Connecting to gateway at address: {zeebe_worker.zeebe_adapter.connection_uri}")
    zeebe_worker.work()
