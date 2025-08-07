import pytest
from gendiff.formatters.stylish import format_stylish, format_diff, format_value


def test_format_value():
    assert format_value(True, 0) == 'true'
    assert format_value(False, 0) == 'false'
    assert format_value(None, 0) == 'null'
    assert format_value(42, 0) == '42'
    assert format_value("hello", 0) == 'hello'
    assert format_value({"a": 1}, 0) == '{\n    a: 1\n}'


def test_format_diff_flat():
    diff = [
        {'key': 'a', 'type': 'unchanged', 'value': 1},
        {'key': 'b', 'type': 'added', 'value': 2},
        {'key': 'c', 'type': 'removed', 'value': 3},
        {'key': 'd', 'type': 'changed', 'old_value': 4, 'new_value': 5}
    ]
    expected = """    a: 1
  + b: 2
  - c: 3
  - d: 4
  + d: 5"""
    assert format_diff(diff) == expected


def test_format_diff_nested():
    diff = [
        {
            'key': 'a',
            'type': 'nested',
            'children': [
                {'key': 'b', 'type': 'added', 'value': 2}
            ]
        }
    ]
    expected = """    a: {
      + b: 2
    }"""
    assert format_diff(diff) == expected


def test_format_stylish():
    diff = [
        {'key': 'a', 'type': 'unchanged', 'value': 1},
        {'key': 'b', 'type': 'added', 'value': 2}
    ]
    expected = """{
    a: 1
  + b: 2
}"""
    assert format_stylish(diff) == expected


def test_format_stylish_empty():
    assert format_stylish([]) == '{\n\n}'