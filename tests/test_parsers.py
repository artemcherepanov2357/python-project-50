import pytest

from gendiff.parsers import get_extension, parse


@pytest.mark.parametrize("extension, data", [
    ('.json', '{"key": "value"}'),
    ('.yml', 'key: value'),
    ('.yaml', 'key: value')
])
def test_parse(extension, data):
    result = parse(data, extension)
    assert result == {"key": "value"}


def test_parse_unsupported_format():
    with pytest.raises(ValueError):
        parse("data", ".txt")


def test_get_extension():
    assert get_extension("/path/to/file.json") == ".json"
    assert get_extension("/path/to/file.YML") == ".yml"