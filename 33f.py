import requests
from bs4 import BeautifulSoup

url = "http://mfd.ru/currency/?currency=USD"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

rates = soup.find_all("td", class_="mfd-table-cell")

for rate in rates[:5]: 
    print(rate.text)