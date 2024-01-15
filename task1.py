# TODO решите задачу
import json


FILENAME = "input.json"


def task() -> float:
    with open(FILENAME, "r") as f:
        json_data = json.load(f)

    l = [i["score"] * i["weight"] for i in json_data]
    return round(sum(l), 3)


print(task())
