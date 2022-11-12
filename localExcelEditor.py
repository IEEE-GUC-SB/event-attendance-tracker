import os.path

from pathlib import Path


from pandas import read_excel, DataFrame

from commonEditor import editMembersData


def getFilePath(request_message, warning_message, initial_path, end_point):
    file_path = input(request_message)

    if len(initial_path) != 0:
        file_path = Path(f"{initial_path}/{file_path}{end_point}")
    path_found = os.path.exists(file_path)

    while not path_found:
        print(warning_message)
        file_path = input(request_message)

        if len(initial_path) != 0:
            file_path = Path(f"{initial_path}/{file_path}{end_point}")
        path_found = os.path.exists(file_path)
    return file_path


def getFileLocation():
    path_example = r"C:\Users\pc\Desktop"
    file_path = getFilePath(f"Enter current excel local file path: (example: '{path_example}')\n",
                            "File path entered is Invalid. Try again",
                            "",
                            "")

    file_name = getFilePath("Enter current excel file name: (name entered must be exactly like the file name)\n",
                            "File name does not exist. Try again", file_path,
                            ".xlsx")

    return file_name


def storeEditedDataLocally(dataframe: DataFrame) -> None:
    file_found = False
    while not file_found:
        try:

            new_path = str(input(f"Enter desired edited local file path:\n"))
            name = str(input("Enter new edited file name:\n"))

            dataframe.to_excel(Path(f"{new_path}/{name}.xlsx"))
            file_found = True
        except FileNotFoundError:
            print("File path entered is invalid. Try Again")


def editMembersDataFromExcel():
    dataframe = read_excel(getFileLocation())
    editMembersData(dataframe)
    storeEditedDataLocally(dataframe)
