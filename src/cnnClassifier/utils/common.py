import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read yaml file from the given filepath
    :param filepath: str: Filepath of the yaml file
    :return: Any: Data from the yaml file
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} read successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """
    Create directories from the given list of paths
    :param path_to_directories: list: List of paths to create directories
    :param verbose: bool: Whether to print logs or not
    :return: None
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")


@ensure_annotations
def save_json(path: Path, data:dict):
    """
    Save data to a json file
    :param path: Path: Path to save the json file
    :param data: dict: Data to save in the json file
    :return: None
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        logger.info(f"Data saved to json file: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size of the file
    :param path: Path: Path of the file
    :return: str: Size of the file
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"