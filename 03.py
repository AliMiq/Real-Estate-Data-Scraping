from bs4 import BeautifulSoup
import requests
url= "https://thecalagents.com"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="CR1S4b")
for list in lists:
    title = list.find('span', class_="OSrXXb")
    stars = list.find('span', class_="YDIN4c YrbPuc")
    experience = list.find('div')
    address = list.find('span', class_="LrzXr")
    service = list.find('span', 'aria-label')
    info = [title, stars, experience, address, service]
    print(info)
    