scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('secure-air-394815-6ca60e653ca3.json', scope) #Change to your downloaded JSON file name 
client = gspread.authorize(creds)
