import requests
from bs4 import BeautifulSoup

url = "http://mfd.ru/currency/?currency=USD"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, features:"html.parser")

table = soup.find(name:"table", class_="mfd-currency-table")

if table:
    rows = table.find_all("tr")[1:]

    for row in rows:
        cells = row.find_all("td")

        if len(cells) >= 2:
            date = cells[0].text.strip()
            rate = cells[1].text.strip()
            print(f"Дата: {date}, Курс: {rate}")
else:
    print("Таблица с курсами валют не найдена.")            