from faker import Faker

faker = Faker()

def login_generator():
    return f"{faker.user_name()}"

def password_generator():
    return f"{faker.password()}"

def name_generator():
    return f"{faker.first_name()}"