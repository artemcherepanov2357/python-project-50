import ast

import pytest

from gendiff.formatters.stylish import format_stylish


@pytest.fixture
def diff_example():
    with open('tests/fixtures/nested/nested_diff.txt', 'r') as f:
        return ast.literal_eval(f.read())


def test_stylish_format(diff_example):
    with open('tests/fixtures/expected/nested.txt', 'r') as f:
        expected = f.read()
    assert format_stylish(diff_example) == expected