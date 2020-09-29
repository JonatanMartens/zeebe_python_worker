from configparser import ConfigParser

from pyzeebe import OAuthCredentials, CamundaCloudCredentials


def get_credentials(config: ConfigParser):
    credentials = None

    if config.getboolean("zeebe", "oauth"):
        credentials = OAuthCredentials(**config["oauth"])

    if config.getboolean("zeebe", "camunda_cloud"):
        credentials = CamundaCloudCredentials(**config["camunda_cloud"])

    return credentials
