import json
import os

def load_json_and_set_env(json_file: str):
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            
            for key, value in data.items():
                os.environ[key.upper()] = value
                print(f"Set environment variable: {key.upper()} = {value}")
    except Exception as e:
        print(f"Error loading JSON file: {e}")