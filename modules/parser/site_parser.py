"""
!!!-IN PROCESS-!!!
"""
import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from classes.parent import MasterExcel

import datetime
from time import sleep
from colorama import init
from copy import deepcopy
from tkinter.filedialog import askopenfilename, askdirectory
from app_config.settings import TODAY_DATE, EXCEL_TEMPLATE, PARSER_DIVS_DICT, PARSER_HEADERS
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

    def get_custom_url(self, search_str):
        return f'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searhString={search_str}morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber={self.__RESULTS_PER_PAGE}&recordsPerPage=_{self.__PAGE_NUMBER}&fz44=on&fz223=on&af=on&priceFromGeneral={self.__PRICE}&currencyIdGeneral=-1&publishDateFrom={DATE_DAYS_AGO}&publishDateTo={TODAY_DATE}'

    def get_search_string(self):
        return self.__SEARCH
    
    def set_search_string(self):
        return 1
 
    def get_page(self):
        return self.__PAGE_NUMBER
    
    @staticmethod
    def check_paginate(url):
        response = requests.get(url, headers=PARSER_HEADERS)
        
        soup = bs(response.text, 'html.parser')
        pagination = soup.find('div', class_='paginator-block')
        pages = pagination.find_all('span', class_='link-text')

        if pages:
            return soup, pages[-1].text
        return soup

    def parse_site(self):

        answer = input("""Print 'default' to parse default settings. 'search' to set search string.\nAnswer: """)

        if answer == 'default':
            url = self.get_url()
        elif answer == 'search':
            search_str = input("What's searching?\nAnswer: ")
            if search_str:
                url = self.get_custom_url(search_str)
            else:
                return CANCELLED
        else:
            return CANCELLED
        
        parse_result = self.check_paginate(url)

        if isinstance(parse_result, bs):
            return parse_result(parse_result)

        if isinstance(parse_result, tuple):
            return self.parse_paginate(*parse_result)

        return f'[{ERROR}] Connection failed!'
    
    def parse_page(self):
        pass

    def parse_paginate(self, soup, max_pages):
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
