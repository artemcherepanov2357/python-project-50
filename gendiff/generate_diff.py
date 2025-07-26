from gendiff.parsers import get_extension, parse


def generate_diff(file_path1, file_path2):
    """Generates differences between two files (JSON/YAML)."""
    ext1 = get_extension(file_path1)
    ext2 = get_extension(file_path2)

    with open(file_path1) as f1, open(file_path2) as f2:
        data1 = parse(f1.read(), ext1)
        data2 = parse(f2.read(), ext2)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_lines = []

    for key in all_keys:
        if key not in data2:
            diff_lines.append(f"  - {key}: {data1[key]}")
        elif key not in data1:
            diff_lines.append(f"  + {key}: {data2[key]}")
        elif data1[key] == data2[key]:
            diff_lines.append(f"    {key}: {data1[key]}")
        else:
            diff_lines.append(f"  - {key}: {data1[key]}")
            diff_lines.append(f"  + {key}: {data2[key]}")

    return "{\n" + "\n".join(diff_lines) + "\n}"
