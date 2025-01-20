import configparser
import os


CONFIG = configparser.ConfigParser()
ENV = "dev"

if os.environ.get("ENV"):
    ENV = os.environ.get("ENV")


def get_config(CONFIG_DIR):
    if ENV == "dev":
        CONFIG.read(f"{CONFIG_DIR}/development.cfg")
    elif ENV == "prod":
        CONFIG.read(f"{CONFIG_DIR}/production.cfg")
    return CONFIG
