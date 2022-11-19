from bs4 import BeautifulSoup
import requests
url= "https://www.google.com/search?sa=X&rlz=1C5CHFA_enPK942PK942&tbs=lf:1,lf_ui:14&tbm=lcl&sxsrf=ALiCzsZePxp2NeUn5sy0IieGKEjCYNjT7w:1668413912068&q=california+real+estate+agents&rflfq=1&num=10&ved=2ahUKEwitmcSUnq37AhXl_7sIHYIzAAsQjGp6BAghEAE&biw=2560&bih=1309&dpr=1#rlfi=hd:;si:;mv:[[38.193787199999996,-117.29034940000001],[33.5970426,-122.5788144]]"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', {'class' : 'xpdopen'}).find_all('div', {'class': 'SPZz6b'}).find_all('h2', {'class': 'qrShPb kno-ecr-pt PZPZlf q8U8x PPT5v EaHP9c'}).find_all('span')
len(lists)
# for list in lists:
#      title = list.find('span', class_="OSrXXb")
#      stars = list.find('span', class_="YDIN4c YrbPuc")
#      experience = list.find('div')
#      address = list.find('span', class_="LrzXr")
#      service = list.find('span', 'aria-label')
#      info = [title, stars, experience, address, service]
#      print(info)
    