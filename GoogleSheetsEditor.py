import google.auth.exceptions
import gspread

from pandas import DataFrame
from CommonEditor import editMembersData
import requests.exceptions
from oauth2client.service_account import ServiceAccountCredentials


def getSheetName(obj, sheet_type):
    sheet_found = False
    while not sheet_found:
        sheet_name = input(f"Enter google {sheet_type} name: (name entered must be exactly like the spreadsheet name)\n")
        print("Please wait a few seconds .........")
        try:
            if sheet_type == "Spreadsheet":
                obj.open(sheet_name)
            else:
                obj.worksheet(sheet_name)
            return sheet_name
        except gspread.exceptions.SpreadsheetNotFound:
            print("Spreadsheet Name is not found. Try again")
        except google.auth.exceptions.TransportError:
            print("Internet Connection is very weak. Check your connection.")
        except requests.exceptions.ConnectionError:
            print("Internet Connection is very weak. Check your connection.")
        except gspread.exceptions.WorksheetNotFound:
            print("Worksheet Name is not found. Try again")


def editMembersDataFromGSheets():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('ieee-qr-367619-2921caea1982.json', scope)
    client = gspread.authorize(creds)
    sheet_name = getSheetName(client, "Spreadsheet")
    sheet = client.open(sheet_name)
    worksheet_name = getSheetName(sheet, "Worksheet")
    worksheet = sheet.worksheet(worksheet_name)
    data = DataFrame.from_dict(worksheet.get_all_records())
    editMembersData(data)

    new_worksheet_name = input("Enter desired new worksheet name: (name entered must be exactly like the worksheet name)\n")
    try:
        sheet.add_worksheet(rows=len(worksheet.get_all_records()) + 10, cols=10, title=new_worksheet_name)
    except gspread.exceptions.APIError:
        print("Worksheet Already Exists")
        return

    qr_worksheet = sheet.worksheet(new_worksheet_name)

    qr_worksheet.insert_rows(
        DataFrame([['ID', 'Name', 'Email', 'Phone Number', 'Participation As', 'QRCODE']]).values.tolist())
    qr_worksheet.insert_rows(data.values.tolist(), row=2)
