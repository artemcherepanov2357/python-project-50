import os
import pytest

from gendiff import generate_diff


def get_fixture_path(*args):
    return os.path.join(os.path.dirname(__file__), 'fixtures', *args)


def read_file(path):
    with open(path) as f:
        return f.read().strip()


@pytest.mark.parametrize("test_case,ext", [
    ("flat", "json"),
    ("flat", "yml"),
    ("nested", "json"),
    ("nested", "yml")
])
def test_generate_diff(test_case, ext):
    file1 = get_fixture_path(test_case, f"file1.{ext}")
    file2 = get_fixture_path(test_case, f"file2.{ext}")
    expected = read_file(get_fixture_path("expected", f"{test_case}.txt"))

    result = generate_diff(file1, file2)
    assert result == expected