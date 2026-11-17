import json

DEFAULTS = {
    "host": "localhost",
    "port": 8080,
    "debug": False
}


def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return {**DEFAULTS, **json.load(f)}

    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {path}: {e}")
        return DEFAULTS


print(load_config("config.json"))
print(load_config("broken.json"))
