"""

"""
import requests
from bs4 import BeautifulSoup as bS
from time import sleep
from classes.parent import MasterExcel


URL_TEMPLATE = f'''https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString='''

try_count = 0

class SiteParser(MasterExcel):
    pass

# while True:
#     if try_count:
#         print('Retrying...')
#     connection = requests.get(URL_TEMPLATE)
#     if connection.status_code == 200:
#         SEARCHING_INFO = bS(connection.text, "html.parser")
#         print(connection.status_code)
#         break
#     sleep(2)
#     try_count += 1
#     print("Connection...")
