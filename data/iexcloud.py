import requests, json, csv

TOKEN  = "YOUR IEX CLOUD KEY"
SYMBOL = "PTON"

r = requests.get("https://sandbox.iexapis.com/stable/stock/{}/chart/max?token={}".format(SYMBOL, TOKEN))

items = json.loads(r.content)

csv_file = open('stock.csv', 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['date', 'open', 'high', 'low', 'close'])

for item in items:
    csv_writer.writerow([item['date'], item['open'], item['high'], item['low'], item['close']])

csv_file.close()