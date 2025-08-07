def format_value(value, depth):
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{' ' * (depth * 4 + 4)}{k}: {format_value(v, depth + 1)}")
        return '{\n' + '\n'.join(lines) + '\n' + ' ' * depth * 4 + '}'
    return str(value)


def format_diff(diff, depth=0):
    lines = []
    for node in diff:
        indent = ' ' * (depth * 4 + 2)
        key = node['key']

        if node['type'] == 'nested':
            lines.append(f"{indent}  {key}: {{")
            lines.append(format_diff(node['children'], depth + 1))
            lines.append(f"{indent}  }}")
        elif node['type'] == 'added':
            lines.append(f"{indent}+ {key}: {format_value(node['value'], depth)}")
        elif node['type'] == 'removed':
            lines.append(f"{indent}- {key}: {format_value(node['value'], depth)}")
        elif node['type'] == 'changed':
            lines.append(f"{indent}- {key}: {format_value(node['old_value'], depth)}")
            lines.append(f"{indent}+ {key}: {format_value(node['new_value'], depth)}")
        else:  # unchanged
            lines.append(f"{indent}  {key}: {format_value(node['value'], depth)}")

    return '\n'.join(lines)


def format_stylish(diff):
    return '{\n' + format_diff(diff) + '\n}'