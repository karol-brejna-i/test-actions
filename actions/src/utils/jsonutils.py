import json


def read_json_from_file(file):
    with open(file, 'r') as f:
        return json.load(f)
