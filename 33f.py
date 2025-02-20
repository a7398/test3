import requests
from bs4 import BeautifulSoup

url = "http://mfd.ru/currency/?currency=USD"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")