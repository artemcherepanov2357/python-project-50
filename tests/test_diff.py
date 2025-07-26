import os

import pytest

from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join('tests', 'test_data', filename)


def read_expected(filename):
    with open(get_fixture_path(filename)) as f:
        return f.read().strip()


@pytest.mark.parametrize("file1, file2", [
    ('file1.json', 'file2.json'),
    ('file1.yml', 'file2.yml'),
])
def test_generate_diff(file1, file2):
    expected = read_expected('expected_result.txt')
    result = generate_diff(
        get_fixture_path(file1),
        get_fixture_path(file2)
    )
    assert result == expected