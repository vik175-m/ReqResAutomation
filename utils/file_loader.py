import json


def load_json_file(file_path):
    """
    Utility function to load a JSON file.
    :param file_path: The path to the JSON file.
    :return: The contents of the JSON file as a Python object.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError("The file at " + file_path + " was not found.")
    except json.JSONDecodeError:
        raise ValueError("Failed to decode JSON from the file: " + file_path)