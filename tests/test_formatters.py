import ast

import pytest

from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


@pytest.fixture
def diff_example():
    with open('tests/fixtures/expected/nested_diff.txt', 'r') as f:
        return ast.literal_eval(f.read())


def test_format_stylish(diff_example):
    with open('tests/fixtures/expected/nested.txt', 'r') as f:
        expected = f.read()
    assert format_stylish(diff_example) == expected


def test_format_plain(diff_example):
    with open('tests/fixtures/expected/result_plain.txt', 'r') as result:
        assert format_plain(diff_example) == result.read()


def test_format_json(diff_example):
    with open('tests/fixtures/expected/result_json.txt', 'r') as result:
        assert format_json(diff_example) == result.read()