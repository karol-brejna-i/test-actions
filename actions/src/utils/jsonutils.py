import json


def readJsonFromFile(file):
    with open(file, 'r') as f:
        return json.load(f)
