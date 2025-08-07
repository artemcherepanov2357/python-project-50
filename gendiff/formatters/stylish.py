

def format_value(value, depth):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, dict):
        indent = ' ' * ((depth + 1) * 4)
        closing_indent = ' ' * (depth * 4)
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}{k}: {format_value(v, depth + 1)}")
        return '{\n' + '\n'.join(lines) + '\n' + closing_indent + '}'
    return str(value)


def format_diff(diff, depth=0):
    lines = []
    for node in diff:
        indent = ' ' * (depth * 4)
        key = node['key']

        if node['type'] == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.append(format_diff(node['children'], depth + 1))
            lines.append(f"{indent}    }}")
        elif node['type'] == 'added':
            lines.append(f"{indent}  + {key}: {format_value(node['value'], depth + 1)}")
        elif node['type'] == 'removed':
            lines.append(f"{indent}  - {key}: {format_value(node['value'], depth + 1)}")
        elif node['type'] == 'changed':
            value = format_value(node['old_value'], depth + 1)
            lines.append(f"{indent}  - {key}:" + (f" {value}" if value else ""))
            lines.append(f"{indent}  + {key}: {format_value(node['new_value'], depth + 1)}")
        else:  # unchanged
            lines.append(f"{indent}    {key}: {format_value(node['value'], depth)}")

    result = '\n'.join(lines)
    return result


def format_stylish(diff):
    inner = format_diff(diff)
    result = '{\n' + inner + '\n}'
    # with open("actual_output.txt", "w") as f:
    #     f.write(result)
    return result
