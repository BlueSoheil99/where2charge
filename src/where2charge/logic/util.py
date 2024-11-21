import yaml


def read_config(file_path='config.yaml'):
    with open(file_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

