import random

from faker import Faker
from pandas import DataFrame

from commonEditor import editMembersData
from localExcelEditor import storeEditedDataLocally

fake = Faker()


def fake_phone_number() -> str:
    return f'{fake.msisdn()[3:]}'


def fake_participation_state():
    return random.choice(['L', 'LS', 'LD'])


def generateRandomLocalExcelFile() -> None:
    row_number = None
    while not isinstance(row_number, int):
        row_number = int(input("\nHow many rows of data would you like to generate?\n"))

    data = DataFrame(columns=['Name', 'Email', 'Phone Number', 'Participation As'])
    for i in range(row_number):
        data.loc[len(data.index)] = [fake.name(), fake.email(), fake_phone_number(), fake_participation_state()]
    editMembersData(data)
    storeEditedDataLocally(data)


generateRandomLocalExcelFile()
print("\n\nYour new edited sheet is ready : )")
