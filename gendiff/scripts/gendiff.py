import argparse
import json


def read_file(file_path):
    """Reading and parsing a JSON file."""
    with open(file_path) as file:
        return json.load(file)


def generate_diff():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish',
    )
    args = parser.parse_args()

    data1 = read_file(args.first_file)
    data2 = read_file(args.second_file)

    print("File 1:", data1)
    print("File 2:", data2)
    print("Output format:", args.format)


def main():
    generate_diff()


if __name__ == '__main__':
    main()
