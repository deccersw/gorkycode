import requests
from bs4 import BeautifulSoup

url = 'https://sport.acgnn.ru/eventCalendar'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)