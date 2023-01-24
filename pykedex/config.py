"""Module that provides the Pykedex config functionality"""

import typer, configparser
from pathlib import Path

from pykedex import (
    DB_WRITE_ERROR, FILE_ERROR, DIR_ERROR, SUCCESS, __app_name__
)

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__)) #path to the apps dir
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"       #path to the config file

#initializes the config file & database
def init_app(db_path: str) -> int:
    """Initialize the application."""
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code

    database_code = _create_database(db_path)

    if database_code != SUCCESS:
        return database_code

    return SUCCESS


""" 
    creates the configuration directory using Path.mkdir()
    creates the configuration file using Path.touch()
    returns the proper error codes if something wrong happens during the creation of the directory and file
    returns SUCCESS if everything goes okay
"""
def _init_config_file() -> int:
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        return DIR_ERROR

    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return FILE_ERROR

    return SUCCESS


def _create_database(db_path: str) -> int:
    config_parser = configparser.ConfigParser()
    config_parser["General"] = {"database": db_path}

    try:
        with CONFIG_FILE_PATH.open("w") as file:
            config_parser.write(file)
    except OSError:
        return DB_WRITE_ERROR

    return SUCCESS