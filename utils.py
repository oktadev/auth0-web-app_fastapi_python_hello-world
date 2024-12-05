import json


def to_pretty_json(obj: dict) -> str:
    return json.dumps(obj, default=lambda o: dict(o), indent=4)