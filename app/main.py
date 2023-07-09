from faker import Faker

def generate_name():
    faker=Faker()
    name=faker.name()
    print(name)

def main():
    generate_name()