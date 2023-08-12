scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Tutorial Louis-985b5d882f76.json', scope) #Change to your downloaded JSON file name 
client = gspread.authorize(creds)
