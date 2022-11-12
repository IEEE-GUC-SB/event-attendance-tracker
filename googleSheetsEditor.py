import google.auth.exceptions
import gspread
import requests.exceptions
from oauth2client.service_account import ServiceAccountCredentials
from pandas import DataFrame

from commonEditor import editMembersData


def getSheetName(client, sheet, sheet_type):
    sheet_found = False
    while not sheet_found:
        sheet_name = input(
            f"Enter google {sheet_type} name: (name entered must be exactly like the {sheet_type} name)\n")
        print("Please wait a few seconds .........")
        try:
            if sheet_type == "Spreadsheet":
                testSpreadSheetExistence(client, sheet_name)
            else:
                testWorkSheetExistence(sheet, sheet_name)
            return sheet_name
        except gspread.exceptions.SpreadsheetNotFound:
            print("Spreadsheet Name is not found. Try again")
        except gspread.exceptions.APIError:
            print("Spreadsheet Name is invalid. Try again")
        except google.auth.exceptions.TransportError:
            print("Internet Connection is very weak. Check your connection.")
        except requests.exceptions.ConnectionError:
            print("Internet Connection is very weak. Check your connection.")
        except gspread.exceptions.WorksheetNotFound:
            print("Worksheet Name is not found. Try again")


def getClient():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds_file_name = input("Enter your credentials file name:\n")
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file_name, scope)
    except FileNotFoundError:
        print("\nPlease enter the correct file name or download it if it doesn't exist\n")
        return None

    return gspread.authorize(creds)


def getNewWorkSheet(sheet, worksheet):
    new_worksheet_name = input("Enter desired new worksheet name:\n")

    try:
        sheet.add_worksheet(rows=len(worksheet.get_all_records()) + 10, cols=10, title=new_worksheet_name)
        return new_worksheet_name
    except gspread.exceptions.APIError:
        print("Worksheet Already Exists")
        return None


def createNewWorksheet(sheet, worksheet):
    data = DataFrame.from_dict(worksheet.get_all_records())
    editMembersData(data)
    new_worksheet_name = getNewWorkSheet(sheet, worksheet)
    if not new_worksheet_name:
        return

    qr_worksheet = sheet.worksheet(new_worksheet_name)

    qr_worksheet.insert_rows(
        DataFrame([['ID', 'Name', 'Email', 'Phone Number', 'Participation As', 'QRCODE']]).values.tolist())
    qr_worksheet.insert_rows(data.values.tolist(), row=2)


def editMembersDataFromGSheets():
    client = getClient()
    sheet_name = getSheetName(client, None, "Spreadsheet")
    sheet = client.open(sheet_name)
    worksheet_name = getSheetName(None, sheet, "Worksheet")
    worksheet = sheet.worksheet(worksheet_name)
    createNewWorksheet(sheet, worksheet)


def testSpreadSheetExistence(client, spreadsheet_name) -> None:
    client.open(spreadsheet_name)


def testWorkSheetExistence(sheet, worksheet_name) -> None:
    sheet.worksheet(worksheet_name)
