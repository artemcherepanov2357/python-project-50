import json
from os.path import splitext

import yaml


def parse(data, extension):
    """Parses data depending on file extension."""
    if extension == '.json':
        return json.loads(data)
    elif extension in ('.yml', '.yaml'):
        return yaml.safe_load(data)
    raise ValueError(f"Unsupported file extension: {extension}")


def get_extension(file_path):
    """Returns the file extension in lowercase."""
    return splitext(file_path)[1].lower()

