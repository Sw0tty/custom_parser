"""
!!!-IN PROCESS-!!!
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
from app_config.settings import TODAY_DATE, EXCEL_TEMPLATE, PARSER_DIVS_DICT
from app_config.app_notices import ERROR, SUCCESS, INFO, CANCELLED, FILE_CREATED
from bs4 import BeautifulSoup as bs

from classes.modules_default import MainMethods

URL_TEMPLATE = f'''https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString='''

init()
DAYS_AGO = 2
SEARCH = ''
DEFAULT_RESULTS = 50
DEFAULT_PAGE_NUMBER = 1
DEFAULT_PRICE = 500000

DATE_DAYS_AGO = (datetime.datetime.now() - datetime.timedelta(days=DAYS_AGO)).strftime("%d.%m.%Y")

MAIN_URL = f'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searhString={SEARCH}morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber={DEFAULT_PAGE_NUMBER}&recordsPerPage=_{DEFAULT_RESULTS}&fz44=on&fz223=on&af=on&priceFromGeneral={DEFAULT_PRICE}&currencyIdGeneral=-1&publishDateFrom={DATE_DAYS_AGO}&publishDateTo={TODAY_DATE}'



try_count = 0

class SiteParser(MainMethods, MasterExcel):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__SEARCH = ''
        self.__RESULTS_PER_PAGE = 50
        self.__PAGE_NUMBER = DEFAULT_PAGE_NUMBER
        self.__PRICE = DEFAULT_PRICE

    def get_url(self):
        return f'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searhString={self.__SEARCH}morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber={self.__RESULTS_PER_PAGE}&recordsPerPage=_{self.__PAGE_NUMBER}&fz44=on&fz223=on&af=on&priceFromGeneral={self.__PRICE}&currencyIdGeneral=-1&publishDateFrom={DATE_DAYS_AGO}&publishDateTo={TODAY_DATE}'

    def pars_url(self, search_str, page):
        return f'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searhString={search_str}morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber={self.__RESULTS_PER_PAGE}&recordsPerPage=_{page}&fz44=on&fz223=on&af=on&priceFromGeneral={self.__PRICE}&currencyIdGeneral=-1&publishDateFrom={DATE_DAYS_AGO}&publishDateTo={TODAY_DATE}'

    def get_search_string(self):
        return self.__SEARCH
    
    def set_search_string(self):
        return 1
 
    def get_page(self):
        return self.__PAGE_NUMBER
    
    @staticmethod
    def check_paginate(url):
        response = requests.get(url, headers= {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        })
        
        soup = bs(response.text, 'html.parser')
        pagination = soup.find('div', class_='paginator-block')
        pages = pagination.find_all('span', class_='link-text')

        if pages:
            return pages[-1].text

    def parse_results(self):
        pass

    # def page(self, page_num):
    #     self.__PAGE_NUMBER = page_num
    #     return self.page


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
