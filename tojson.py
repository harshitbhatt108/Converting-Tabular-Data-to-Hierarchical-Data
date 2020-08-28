import json
import pandas as pd

df = pd.read_excel (r'hierarchy_case_20May2020.xlsx')

tree = {}

for d in df:
    node = None
    for item in d.split():
        name = item.strip()  # dont need spaces
        current_dict = tree if node is None else node
        node = current_dict.get(name)
        if not node:
            node = {}
            current_dict[name] = node


def walker(src, res):
    for name, value in src.items():
        node = {'name': name, 'size': 1}
        if 'children' not in res:
            res['children'] = []
        res['children'].append(node)
        walker(value, node)

result = {'name': 'TEST'}
walker(tree, result)

print (json.dumps(result, indent = True))
