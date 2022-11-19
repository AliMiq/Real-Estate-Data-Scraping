import requests
from bs4 import BeautifulSoup
url = "https://www.google.com/search?sa=X&rlz=1C5CHFA_enPK942PK942&tbs=lf:1,lf_ui:14&tbm=lcl&sxsrf=ALiCzsZePxp2NeUn5sy0IieGKEjCYNjT7w:1668413912068&q=california+real+estate+agents&rflfq=1&num=10&ved=2ahUKEwitmcSUnq37AhXl_7sIHYIzAAsQjGp6BAghEAE&biw=2560&bih=1309&dpr=1#rlfi=hd:;si:;mv:[[38.193787199999996,-117.29034940000001],[33.5970426,-122.5788144]]"
response = requests.get(url)
response = response.content
soup = BeautifulSoup(response, 'html.parser')
