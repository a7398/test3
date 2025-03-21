import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from tabulate import tabulate
from datetime import datetime

url = "http://mfd.ru/currency/?currency=USD"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) like Gecko YaBrowser/25.2.0.0"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Ошибка при получении данных: {e}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_="mfd-currency-table")

if table:
    dates = []
    rates = []
    
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        if len(cells) >= 2:
            date_str = cells[0].text.strip()
            rate = cells[1].text.strip()
            
            if "с " in date_str:
                date_str = date_str.replace("с ", "")
            date = datetime.strptime(date_str, "%d.%m.%Y")
            
            dates.append(date)
            rates.append(float(rate))

    data = []
    for i in range(len(dates)):
        data.append([dates[i].strftime("%d.%m.%Y"), rates[i]])

    print(tabulate(data, headers=["Дата", "Курс USD"], tablefmt="grid"))

    plt.figure(figsize=(10, 6))
    plt.plot(dates, rates, 'bo-', label='Курс USD')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))
    plt.title('Курс USD по датам')
    plt.xlabel('Дата')
    plt.ylabel('Курс')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

else:
    print("Таблица с курсами валют не найдена.")