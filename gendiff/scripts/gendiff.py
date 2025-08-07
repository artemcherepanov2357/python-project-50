import sys

from gendiff import generate_diff
from gendiff.parser_args import parse_args


def main():
    try:
        args = parse_args()
        print(generate_diff(args.first_file, args.second_file, args.format))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()