import requests
from bs4 import BeautifulSoup

url = "http://mfd.ru/currency/?currency=USD"
headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) like Gecko YaBrowser/25.2.0.0"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Ошибка при получении данных: {e}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_="mfd-currency-table")

if table:
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        
        if len(cells) >= 2:
            date = cells[0].text.strip()
            rate = cells[1].text.strip()
            print(f"Дата: {date}, Курс: {rate}")
else:
    print("Таблица с курсами валют не найдена.")          
           