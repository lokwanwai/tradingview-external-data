import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

print(config)

if __name__ == "__main__":
    pass
