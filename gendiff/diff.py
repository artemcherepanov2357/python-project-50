from gendiff.diff_builder import build_diff
from gendiff.formatters import json, plain
from gendiff.formatters.stylish import format_stylish
from gendiff.parsers import parse_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)

    if format_name == 'json':
        return json.format_json(diff)
    elif format_name == 'plain':
        return plain.format_plain(diff)
    elif format_name == 'stylish':
        return format_stylish(diff)
    raise ValueError(f"Unknown format: {format_name}")

