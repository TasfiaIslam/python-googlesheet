from googleapiclient.discovery import build
from google.oauth2 import service_account
from decouple import config

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = config('SAMPLE_SPREADSHEET_ID')


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet1!A1:H90").execute()
values = result.get('values', [])

testvalues = [["1",20],["2",400],["3",50]]

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
    range="Sheet2!A1", valueInputOption="USER_ENTERED", body={"values": testvalues}).execute()
print(values)
