import requests
from bs4 import BeautifulSoup

url = "http://mfd.ru/currency/?currency=USD"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200: 
    soup = BeautifulSoup(response.text, "html.parser")
    
    rates = soup.find_all("td", class_="mfd-table-cell")
    
    if rates:
        for rate in rates[:5]: 
            print(rate.text.strip())  
    else:
        print("Не удалось найти курсы валют.")
else:
    print(f"Ошибка запроса: {response.status_code}")