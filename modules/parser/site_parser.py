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
from app_config.settings import TODAY_DATE, EXCEL_TEMPLATE, PARSER_DIVS_DICT, PARSER_HEADERS, MAIN_PARSER_BLOCK
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
        return f'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={self.__SEARCH}&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber={self.__PAGE_NUMBER}&recordsPerPage=_{self.__RESULTS_PER_PAGE}&fz44=on&fz223=on&af=on&priceFromGeneral={self.__PRICE}&currencyIdGeneral=-1&publishDateFrom={DATE_DAYS_AGO}&publishDateTo={TODAY_DATE}'

    def get_custom_url(self, search_str, page=1):
        return f'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searchString={search_str}&morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber={page}&recordsPerPage=_{self.__RESULTS_PER_PAGE}&fz44=on&fz223=on&af=on&priceFromGeneral={self.__PRICE}&currencyIdGeneral=-1&publishDateFrom={DATE_DAYS_AGO}&publishDateTo={TODAY_DATE}'

    def get_search_string(self):
        return self.__SEARCH
    
    def set_search_string(self):
        return 1
 
    def get_page(self):
        return self.__PAGE_NUMBER
    
    @staticmethod
    def check_url_info(url):

        response = requests.get(url, headers=PARSER_HEADERS)
        
        soup = bs(response.text, 'html.parser')
        main_info_block = soup.find('div', class_=MAIN_PARSER_BLOCK)
        if not main_info_block:
            return
        pagination = soup.find('div', class_='paginator-block')
        pages = pagination.find_all('span', class_='link-text')

        if pages:
            return soup, int(pages[-1].text)
        return soup
    
    def excel_export(self):
        # if not self.SEARCHING_INFO:
        #     return self.get_file_path()

        return self._save_as_file(self.EXPORT_DATA, self.get_file_extansion)

    def parse_site(self):

        answer = input("""Print 'default' to parse default settings. 'search' to set search string.\nAnswer: """)

        if answer == 'default':
            url = self.get_url()
        elif answer == 'search':
            search_str = input("What's searching?\nAnswer: ")
            if search_str:
                self.__SEARCH = search_str
                url = self.get_custom_url(search_str)
            else:
                return CANCELLED
        else:
            return CANCELLED
        
        parse_result = self.check_url_info(url)

        if isinstance(parse_result, bs):
            return self.parse_page(parse_result)

        if isinstance(parse_result, tuple):
            return self.parse_paginate(*parse_result)

        return f'[{ERROR}] Connection failed!'
    
    def parse_page(self, soup):
        self.block_parser(soup)
        return f'[{SUCCESS}] File ready to export'

    def parse_paginate(self, soup, max_pages):
        self.block_parser(soup)
        for page in range(2, max_pages + 1):
            response = requests.get(self.get_custom_url(search_str=self.__SEARCH, page=page), headers=PARSER_HEADERS)       
            soup = bs(response.text, 'html.parser')
            self.block_parser(soup)
        return f'[{SUCCESS}] File ready to export'

    def block_parser(self, soup):

        # if not self.__file_path:
        #     return self.get_file_name()

        # if self.__ready_to_export:
        #     answer = input(APPLY_STRING)
        #     if answer != 'Yes':
        #         return CANCELLED
        #     self.reset_export_data()


        
        LIST_PARSE_OBJECTS = soup.find_all('div', class_=MAIN_PARSER_BLOCK)

        values_list = []

        for parse_obj in LIST_PARSE_OBJECTS:
            values_list.clear()
            for class_key in PARSER_DIVS_DICT.keys():
                _ = parse_obj.find('div', class_=PARSER_DIVS_DICT[class_key])
                if _ is None:
                    _ = '--None value--'
                else:
                    if class_key != 'org_href' and class_key != 'end_date':
                        _ = _.text.strip()
                        _ = _[:-1].rstrip() if class_key == 'price' else _

                    if class_key == 'purchases':
                        _ = _[0:5] if _[0] == '4' else _[0:6]

                    if class_key == 'end_date':
                        _ = _.findChildren('div', class_='data-block__value', recursive=False)
                        if _:
                            _ = _[0].text.strip()
                        else:
                            _ = '--None date--'

                    if class_key == 'org_href':
                        values_list.append('')
                        values_list.append(3)
                        children = _.findChildren('a')
                        children = children[0].get('href')
                        _ = f'https://zakupki.gov.ru{children}'

                values_list.append(_)


            self.EXPORT_DATA.append(values_list.copy())

        
        
    

