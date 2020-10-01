from configparser import ConfigParser
from unittest.mock import MagicMock

import pytest

from worker.utils.config import get_credentials, get_zeebe_config

config: ConfigParser


@pytest.fixture(autouse=True)
def run_around_tests():
    global config
    config = ConfigParser()
    yield
    config = ConfigParser()


def test_get_zeebe_config():
    config.get = MagicMock()
    config.getint = MagicMock()
    config.getboolean = MagicMock()

    get_zeebe_config(config)

    config.get.assert_called_with("zeebe", "hostname")

    assert config.getint.call_count == 2
    config.getint.assert_any_call("zeebe", "port")
    config.getint.assert_any_call("zeebe", "request_timeout")

    config.getboolean.assert_called_with("zeebe", "secure_connection")


def test_get_credentials():
    config.getboolean = MagicMock()
    config.getboolean.return_value = False

    get_credentials(config)

    config.getboolean.assert_any_call("zeebe", "oauth")
    config.getboolean.assert_any_call("zeebe", "camunda_cloud")
