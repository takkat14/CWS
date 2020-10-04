import numpy as np
import pandas as pd


import gspread
from oauth2client.service_account import ServiceAccountCredentials

# google service project accesses to the sheet
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds_json = '/content/drive/My Drive/НКРЯ/ruzhcorp-cws-tester-925657a643d4.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scope)
client = gspread.authorize(creds)

# access by name or by ID (then use .open_by_key('large string between 3rd and 4th slashes'))
# check if service has permission to edit sheets
main_table = '1btPbk3E1TTt1fBcsCwOUY0_eZjkZakVfxd0T3xFAVXA'
test_table = '13ub_4-HjqV1IdFuFhqj6oCet0OQSE6WsuBvyTMEZh84'
sheet = client.open_by_key(main_table)
tests_sheet = sheet.get_worksheet(2) # indexing from 0