from autoscraper import AutoScraper

url = 'https://www.pararius.com/apartments/amsterdam'

wanted_list = ["Apartment Maasstraat","€2,500","3 rooms","102 m²","Furnished"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)