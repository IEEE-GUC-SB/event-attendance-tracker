from googleSheetsEditor import editMembersDataFromGSheets
from localExcelEditor import editMembersDataFromExcel

choice = ""
while choice.upper() not in ['Y', 'N']:
    choice = input("If you'd like to edit a google sheet press 'Y'.\n"
                   "If you'd like to edit a local excel file press 'N'.\n\n")
    if choice.lower() == "y":
        editMembersDataFromGSheets()
    else:
        editMembersDataFromExcel()

print("\n\nYour new edited sheet is ready : )")
