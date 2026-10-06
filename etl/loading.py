import os
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe
import gspread

def load_data(df_final):
    print("Loading process started.")

    load_dotenv()
    credentials_path = os.getenv('GOOGLE_CREDENTIALS_PATH')
    
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    cliente = gspread.authorize(creds)

    NOMBRE_DEL_SHEET = 'SLF-Analytics-Dashboard_Data'
    sheet = cliente.open(NOMBRE_DEL_SHEET).sheet1

    sheet.clear()

    print("Subiendo datos, por favor espera...")
    set_with_dataframe(sheet, df_final)