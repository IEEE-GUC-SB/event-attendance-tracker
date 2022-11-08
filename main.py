from LocalExcelEditor import editMembersDataFromExcel, generateRandomQRCodes
from GoogleSheetsEditor import editMembersDataFromGSheets

choice = ""
while choice.lower() != "y" and choice.lower() != "n":
    choice = str(input("Would you like to use randomly generated values?:(Y/N)\n"))
if choice.lower() == "y":
    row_number = ""
    while not isinstance(row_number, int):
        row_number = int(input("How many rows of data would you like to generate?\n"))

    generateRandomQRCodes(row_number)
else:
    choice = ""
    while choice.lower() != "y" and choice.lower() != "n":
        choice = str(input("Would you like to to update a google spreadsheet of users with QRCodes?:(Y/N)\n"))
    if choice.lower() == "y":
        editMembersDataFromGSheets()
    else:
        editMembersDataFromExcel()

print("\n\nYour new edited sheet is ready : )")
