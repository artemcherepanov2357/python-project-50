from unittest.mock import patch

import pytest

from gendiff.parser_args import create_parser


def test_parser_with_required_args():
    """Тест парсера с обязательными аргументами"""
    parser = create_parser()
    args = parser.parse_args(['file1.json', 'file2.json'])
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format == 'stylish'  # значение по умолчанию


def test_parser_with_format_arg():
    """Тест парсера с указанием формата"""
    parser = create_parser()
    args = parser.parse_args(['file1.yml', 'file2.yml', '--format', 'plain'])
    assert args.format == 'plain'


def test_parser_missing_args():
    """Тест парсера без обязательных аргументов"""
    parser = create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([])


@patch('sys.argv', ['gendiff', 'file1.json', 'file2.json'])
def test_parse_args_function():
    """Тест функции parse_args"""
    from gendiff.parser_args import parse_args
    args = parse_args()
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'