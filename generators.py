from faker import Faker
import random

fake = Faker()

#Generate Names
def generateNames(num: int):
    names = list()

    for i in range(num):
        names.append(fake.name())

    return names

#Generate Ages
def generateAge(num: int):
    ages = list()
    for i in range(num):
        ages.append(random.randint(1,100))
    return ages

#Generate EMails
def generateEmail(num: int, names: list):
    # emails = list()
    # for i in range(num):
    #     emails.append(fake.email())
    # return emails

    emails = list()

    for i in names:
        name = i.split(" ")
        firstName = name[0].lower()
        lastName = name[1].lower()
        emails.append(f"{firstName}{lastName}@example.org")

    return emails


#Generate Phone NUmbers
def generatePhoneNumber(num: int):
    phone_numbers = list()
    for i in range(num):
        phone_numbers.append(fake.phone_number())
    return phone_numbers

#Generate Cities
def generateCity(num: int):
    cities = list()
    for i in range(num):
        cities.append(fake.city())
    return cities

#Generate Countries
def generateCounty(num: int):
    countries = list()
    for i in range(num):
        countries.append(fake.country())
    return countries

def birthYear(num: int, ages: list):
    birthYears = list()
    for i in ages:
        birthYears.append(2025 - i)
    return birthYears