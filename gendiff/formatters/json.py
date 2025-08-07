import json


def format_json(diff):
    result = json.dumps(build_json_output(diff), indent=2)
    with open("json_out", "w") as f:
        f.write(result)
    return result


def build_json_output(diff):
    result = []

    for node in diff:
        current = {
            'key': node['key'],
            'type': node['type']
        }

        if node['type'] == 'nested':
            current['children'] = build_json_output(node['children'])
        elif node['type'] == 'added':
            current['value'] = node['value']
        elif node['type'] == 'removed':
            current['value'] = node['value']
        elif node['type'] == 'changed':
            current['old_value'] = node['old_value']
            current['new_value'] = node['new_value']
        elif node['type'] == 'unchanged':
            current['value'] = node['value']

        result.append(current)

    return result