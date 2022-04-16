import yaml


def read_yaml(path):
    with open(path, mode='r', encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data
