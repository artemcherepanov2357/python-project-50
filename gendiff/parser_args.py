import argparse


def create_parser():
    """Create and configure argument parser for gendiff CLI"""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Generate differences between two configuration files.'
    )
    parser.add_argument(
        'first_file',
        metavar='FIRST_FILE',
        help='path to the first configuration file'
    )
    parser.add_argument(
        'second_file',
        metavar='SECOND_FILE',
        help='path to the second configuration file'
    )
    parser.add_argument(
        '-f', '--format',
        choices=['stylish', 'plain', 'json'],
        default='stylish',
        help='output format (default: %(default)s)'
    )
    return parser


def parse_args(args=None):
    """Parse command line arguments"""
    return create_parser().parse_args(args)