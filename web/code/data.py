import json

def get_data(filename: str) -> list[dict]:
    messages: list[dict] = []

    with open(filename, 'r') as data_file:
        messages = json.load(data_file)

    return messages


