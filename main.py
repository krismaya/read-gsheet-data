import gspread
from google.oauth2.service_account import Credentials

def read_data(request):
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    credentials = Credentials.from_service_account_file(
        'secret.json', # Downloaded json from Google service
        scopes=scopes
    )

    gc = gspread.authorize(credentials)

    sht1 = gc.open_by_key("WORKSHEET_ID") # FIND IN THE URL OF YOUR GOOGLE SHEET
    worksheet = sht1.worksheet("WORKSHEET_NAME") 
    list_of_dicts = worksheet.get_all_records()
    item_list = []
    for single in list_of_dicts:
        print(single["Item Name"]) # "Item Name" is the column name from the Sheet
        item_list.append(single["Item Name"])

    return result.return_response(item_list)
