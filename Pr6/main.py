import json
import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'https://www.olx.ua/uk/transport/avtobusy/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
name = soup.find_all('h6', class_='css-16v5mdi er34gjf0')
price = soup.find_all('p', class_='css-tyui9s er34gjf0')
locate = soup.find_all('p', class_='css-1a4brun er34gjf0')
# tags = soup.find_all('div', class_='tags')
data = {}
print(response, soup)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
SQL = '''INSERT INTO quotes (_BUS_, _Price_, _Locate_)
VALUES (?,?,?)'''
for _ in range(len(name)):
    # print(name[_].text)
    # print(price[_].text)
    # print(tags[_].text.split()[1:])
    # tag = ', '.join(tags[_].text.split()[1:])
    cursor.execute(SQL, [name[_].text, price[_].text, locate[_].text])
    print(name[_].text, price[_].text, locate[_].text)
conn.commit()
conn.close()
for _ in range(len(name)):
    data[price[_].text] = {name[_].text: locate[_].text.split()[1:] }

# print(data)
# with open('result.json', 'w',encoding='utf-8') as file:
#     json.dump(data, file)