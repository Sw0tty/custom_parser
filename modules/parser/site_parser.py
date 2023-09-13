"""

"""
import requests
from bs4 import BeautifulSoup as bS
from time import sleep
from classes.parent import MasterExcel

import os
import pyexcel
import datetime
import pyexcel_xls  # For excel module!
from pyexcel_io import writers  # For excel module!
from time import sleep
from colorama import init
from copy import deepcopy
from tkinter.filedialog import askopenfilename, askdirectory
from app_config.settings import TODAY, EXCEL_TEMPLATE, PARSER_DIVS_DICT
from app_config.app_notices import ERROR, SUCCESS, INFO, CANCELLED, FILE_CREATED


init()
DAYS_AGO = 3
SEARCH = ''
DEFAULT_RESULTS = 50

DATE_DAYS_AGO = (datetime.datetime.now() - datetime.timedelta(days=DAYS_AGO)).strftime("%d.%m.%Y")

MAIN_URL = f'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searhString={SEARCH}morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&recordsPerPage=_{DEFAULT_RESULTS}&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&priceFromGeneral=500000&currencyIdGeneral=-1&publishDateFrom={DATE_DAYS_AGO}&publishDateTo={TODAY}'




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
