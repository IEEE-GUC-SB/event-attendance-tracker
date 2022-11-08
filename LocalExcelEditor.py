from faker import Faker
import random
import os.path
from pandas import read_excel, DataFrame
from CommonEditor import editMembersData


def checkFileExistence(request_message, warning_message, initial_path, end_point):
    file_path = input(request_message)

    file_location = file_path
    if len(initial_path) != 0:
        file_location = f"{initial_path}\{file_path}{end_point}"
    path_found = os.path.exists(file_location)

    while not path_found:
        print(warning_message)
        file_path = input(request_message)
        file_location = file_path
        if len(initial_path) != 0:
            file_location = f"{initial_path}\{file_path}{end_point}"
        path_found = os.path.exists(file_location)
    return file_path


def getFileLocation():
    path_example = r"C:\Users\pc\Desktop"
    file_path = checkFileExistence(f"Enter current excel local file path: (example: '{path_example}')\n",
                                   "File path entered is Invalid. Try again",
                                   "",
                                   "")

    file_name = checkFileExistence("Enter current excel file name: (name entered must be exactly like the file name)\n", "File name does not exist. Try again", file_path,
                                   ".xlsx")

    file_location = f"{file_path}\{file_name}.xlsx"
    return file_location


def storeEditedDataLocally(dataframe):
    file_found = False
    path_example = r"C:\Users\pc\Desktop"
    while not file_found:
        try:

            new_path = str(input(f"Enter desired edited local file path: (example: '{path_example}')\n"))
            name = str(input("Enter new edited file name:\n"))

            dataframe.to_excel(f"{new_path}\{name}.xlsx")
            file_found = True
        except FileNotFoundError:
            print("File path entered is invalid. Try Again")


def editMembersDataFromExcel():
    dataframe = read_excel(getFileLocation())
    editMembersData(dataframe)
    storeEditedDataLocally(dataframe)


fake = Faker()


def fake_phone_number() -> str:
    return f'{fake.msisdn()[3:]}'


def fake_participation_state():
    return random.choice(['L', 'LS', 'LD'])


def generateRandomQRCodes(rows_number):
    data = DataFrame(columns=['Name', 'Email', 'Phone Number', 'Participation As'])
    for i in range(rows_number):
        data.loc[len(data.index)] = [fake.name(), fake.email(), fake_phone_number(), fake_participation_state()]
    editMembersData(data)
    storeEditedDataLocally(data)
