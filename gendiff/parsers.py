import json
from os.path import splitext

import yaml


def get_extension(file_path):
    """Returns the file extension in lowercase."""
    return splitext(file_path)[1].lower()


def parse_file(file_path):
    with open(file_path) as f:
        content = f.read()
        extension = splitext(file_path)[1].lower()

        if extension == '.json':
            return json.loads(content)
        elif extension in ('.yml', '.yaml'):
            return yaml.safe_load(content)
        raise ValueError(f"Unsupported file format: {extension}")