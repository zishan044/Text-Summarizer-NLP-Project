import yaml
from pathlib import Path
from typing import Union, List

from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations

from text_summarizer.logging import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML configuration file and return its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        ConfigBox: A dictionary-like object with attribute-style access to keys.

    Raises:
        ValueError: If the YAML file is empty or cannot be parsed.
        Exception: If any other error occurs while reading the file.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file) or {}
            if not content:
                raise ValueError(f"YAML file {path_to_yaml} is empty")
            logger.info(f"✅ YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"YAML file error at {path_to_yaml}: {e}")
    except Exception as e:
        logger.error(f"❌ Failed to read YAML file {path_to_yaml}: {e}")
        raise


@ensure_annotations
def create_directories(
    path_to_directories: list,
    verbose: bool = True
) -> list:
    """
    Create one or more directories if they do not already exist.

    Args:
        path_to_directories (list[str | Path]): A list of directory paths to create.
        verbose (bool, optional): If True, log each directory creation. Defaults to True.

    Returns:
        list[Path]: A list of Path objects corresponding to the created directories.
    """

    created_paths = []
    for path in path_to_directories:
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        created_paths.append(path)
        if verbose:
            logger.info(f"📁 Created directory at {path.resolve()}")
    return created_paths


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the approximate size of a file in kilobytes.

    Args:
        path (Path): Path to the file.

    Returns:
        str: File size formatted as a string in kilobytes (e.g., "~ 42 KB").
    """
    size_in_kb = round(path.stat().st_size / 1024)
    return f'~ {size_in_kb} KB'