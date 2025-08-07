import os
import tempfile

import pytest

from gendiff.parsers import get_extension, parse_file


@pytest.mark.parametrize("extension, data, expected", [
    ('.json', '{"key": "value"}', {"key": "value"}),
    ('.yml', 'key: value', {"key": "value"}),
    ('.yaml', 'key: value', {"key": "value"})
])
def test_parse(extension, data, expected):
    with tempfile.NamedTemporaryFile(mode='w', suffix=extension, delete=False) as f:
        f.write(data)
        f.flush()
        temp_path = f.name

    try:
        result = parse_file(temp_path)
        assert result == expected
    finally:
        # Удаляем временный файл после теста
        os.unlink(temp_path)


def test_parse_unsupported_format():
    with tempfile.NamedTemporaryFile(suffix='.txt') as f:
        with pytest.raises(ValueError):
            parse_file(f.name)


def test_get_extension():
    assert get_extension("/path/to/file.json") == ".json"
    assert get_extension("/path/to/file.YML") == ".yml"