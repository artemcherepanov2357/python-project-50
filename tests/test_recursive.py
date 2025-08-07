import json
import pytest
from gendiff import generate_diff

def get_fixture_path(filename):
    return f'tests/fixtures/{filename}'

def read_file(filename):
    with open(get_fixture_path(filename)) as f:
        return f.read().strip()

@pytest.fixture
def expected_stylish():
    return read_file('expected_stylish.txt')

def test_recursive_json(expected_stylish):
    file1 = get_fixture_path('file1_recursive.json')
    file2 = get_fixture_path('file2_recursive.json')
    assert generate_diff(file1, file2) == expected_stylish

def test_recursive_yaml(expected_stylish):
    file1 = get_fixture_path('file1_recursive.yml')
    file2 = get_fixture_path('file2_recursive.yml')
    assert generate_diff(file1, file2) == expected_stylish