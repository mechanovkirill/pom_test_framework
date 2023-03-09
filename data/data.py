from dataclasses import dataclass
from faker import Faker

faker_en = Faker('en_US')
Faker.seed()


@dataclass()
class Person:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address(),
    )







