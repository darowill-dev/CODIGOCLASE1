from faker import Faker
import random

dominios_correos = ("gmail.com", "hotmail.com", "yahoo.com", "outlook.com")

#Constructor de faker
fake = Faker()

#Los ... se llaman elipses y sirven para no marcar error tipo pass.

def get (n_people: int = 5):
    for _ in range(n_people):
        name = fake.name()
        print(f"Persona: {name} con email {name.replace(" ", "")}@{random.choice(dominios_correos)}")
    return n_people


get(100)