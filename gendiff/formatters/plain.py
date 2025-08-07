
def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)


def format_plain(diff, parent_key=''):
    lines = []
    for node in diff:
        key = node['key']
        type_ = node['type']
        full_path = f"{parent_key}{key}"

        if type_ == 'nested':
            lines.append(format_plain(node['children'], f"{full_path}."))
        elif type_ == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{full_path}' was added with value: {value}")
        elif type_ == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        elif type_ == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(
                f"Property '{full_path}' was updated. From {old_value} to {new_value}"
            )
    return '\n'.join(lines)