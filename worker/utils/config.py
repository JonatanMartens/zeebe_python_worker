from configparser import ConfigParser
from typing import Dict

from pyzeebe import OAuthCredentials, CamundaCloudCredentials


def get_credentials(config: ConfigParser):
    credentials = None

    if config.getboolean("zeebe", "oauth"):
        credentials = OAuthCredentials(**config["oauth"])
    elif config.getboolean("zeebe", "camunda_cloud"):
        credentials = CamundaCloudCredentials(**config["camunda_cloud"])

    return credentials


def get_zeebe_config(config: ConfigParser) -> Dict:
    return dict(hostname=config.get("zeebe", "hostname"),
                port=config.getint("zeebe", "port"),
                request_timeout=config.getint("zeebe", "request_timeout"),
                secure_connection=config.getboolean("zeebe", "secure_connection"))
