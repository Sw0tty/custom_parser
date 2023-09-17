"""
!!!-NOW NOT WORKING-!!!
Parser module with MasterParser class
Have methods to parse the site and site for other parsers
!!!-NOW NOT WORKING-!!!
"""
import os
import pyexcel
import datetime
import requests
import pyexcel_xls  # For excel module!
from pyexcel_io import writers  # For excel module!
from time import sleep
from colorama import init
from copy import deepcopy
from bs4 import BeautifulSoup as bS
from classes.parent import MasterExcel
from tkinter.filedialog import askopenfilename, askdirectory
from app_config.settings import TODAY_DATE, EXCEL_TEMPLATE, PARSER_DIVS_DICT
from app_config.app_notices import ERROR, SUCCESS, INFO, CANCELLED, FILE_CREATED


init()
COUNT_DAYS = 3
SEARCH = ''
DEFAULT_RESULTS = 20

DAYS_AGO = (datetime.datetime.now() - datetime.timedelta(days=COUNT_DAYS)).strftime("%d.%m.%Y")

MAIN_URL = f'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searhString={SEARCH}morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&recordsPerPage=_{DEFAULT_RESULTS}&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&priceFromGeneral=500000&currencyIdGeneral=-1&publishDateFrom={DAYS_AGO}&publishDateTo={TODAY_DATE}'


TEST_URL = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html'

DEFAULT_URL = TEST_URL

TEST = f'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?searhString={SEARCH}morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&recordsPerPage=_50&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&priceFromGeneral=500000&currencyIdGeneral=-1&publishDateFrom={DAYS_AGO}&publishDateTo={TODAY_DATE}'

TEST2 = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&recordsPerPage=_20&sortBy=UPDATE_DATE&fz44=on&fz223=on&af=on&priceFromGeneral=500000&currencyIdGeneral=-1&publishDateFrom=20.08.2023&publishDateTo=23.08.2023'

# URL_PARSE = "https://zakupki.gov.ru/epz/order/extendedsearch/results.html"
# URL_PARSE = "https://stackoverflow.com/questions"

# print(TEST)
URL_PARSE = TEST


class MasterParser:

    def parse(self):
        pass

    # def excel_import(self):
    #     pass


class ConnectionFailed(Exception):
    pass


class NoneInfo(Exception):
    pass


class Parser(MasterExcel):
    URL = DEFAULT_URL
    SEARCHING_WORD = None
    SEARCHING_INFO = None
    LIST_PARSE_OBJECTS = None

    _EXCEL_TEMPLATE = EXCEL_TEMPLATE

    IMPORT_DATA = deepcopy(_EXCEL_TEMPLATE)

    def __init__(self, commands: dict):
        super().__init__(commands)
        self.__request_type = None

    def get_request_type(self):
        if self.__request_type:
            return f'[{INFO}] Now request type is: {self.__request_type}'
        return f'[{ERROR}] Request type is undefined!'

    def set_request_type(self):
        while True:
            print(f"[{INFO}]What's type a request?")
            request_type = input("File - parse file\nLink - parse link\nType: ").lower().strip()
            if request_type == 'file' or request_type == 'link':
                self.__request_type = request_type
                return self.get_request_type()
            return f'[{ERROR}] Unexpected parser type!'

    def set_change_url(self, new_url):
        self.URL = new_url
        return f'[{INFO}] Now parse the: {self.URL}'
    
    def get_searching_word(self):
        if self.SEARCHING_WORD:
            return f'Searching for {self.SEARCHING_WORD}'
        return 'Now searching without word param'
    
    def set_searching_word(self, new_word):
        self.SEARCHING_WORD = new_word
        return f'''Now searching for: '{self.get_searching_word()}'. Please, reparse site!'''

    def parse(self):
        if not self.__request_type:
            return self.get_request_type()

        if not self._file_path:
            return self.get_file_name()

        if self.__request_type == 'link':
            try_count = 0

            while True:
                if try_count:
                    print('Retrying...')
                connection = requests.get(self.URL)
                if connection.status_code == 200:
                    self.SEARCHING_INFO = bS(connection.text, "html.parser")
                    self.parse_info()
                    return 'Connected'

                if try_count >= 5:
                    raise ConnectionFailed(f'Something wrong! {connection.status_code}')

                try_count += 1
                print("Connection...")
                sleep(3)
        else:
            with open(self._file_path, 'r', encoding='utf-8') as open_file:
                self.SEARCHING_INFO = bS(open_file.read(), 'lxml')
            self.parse_info()
            return f'[{INFO}] File ready to parse'

    def parse_info(self):
        self.LIST_PARSE_OBJECTS = \
            self.SEARCHING_INFO.find_all('div', class_="search-registry-entry-block box-shadow-search-input")

    def excel_import(self, div_dict):
        if not self.SEARCHING_INFO:
            return self.get_file_path()

        values_list = []

        for parse_obj in self.LIST_PARSE_OBJECTS:
            values_list.clear()
            for class_key in div_dict.keys():
                _ = parse_obj.find('div', class_=div_dict[class_key][0])
                if _ is None:
                    _ = '--None value--'
                else:
                    if class_key != 'org_href' and class_key != 'end_date':
                        _ = _.text.strip()
                        _ = _[:-1].rstrip() if class_key == 'price' else _

                    if class_key == 'purchases':
                        _ = _[0:6] if _[0] == '4' else _[0:7]

                    if class_key == 'end_date':
                        _ = _.findChildren('div', class_='data-block__value', recursive=False)
                        if _:
                            _ = _[0].text.strip()
                        else:
                            _ = '--None date--'

                    if class_key == 'org_href':
                        values_list.append('')
                        values_list.append('')
                        children = _.findChildren('a')
                        children = children[0].get('href')
                        _ = f'https://zakupki.gov.ru{children}'

                values_list.append(_)

            self.IMPORT_DATA[next(iter(self.IMPORT_DATA))].append(values_list.copy())

        path_dir = askdirectory(initialdir=os.getcwd(), title="Save in...")
        if path_dir:
            os.chdir(path_dir)
            pyexcel.save_book_as(bookdict=self.IMPORT_DATA, dest_file_name=f"Выгрузка {TODAY_DATE}.xls")
            return FILE_CREATED
        return CANCELLED

# count = 0
# while True:
#     r = requests.get(URL_PARSE)
#     print(r.status_code)
#     print(r.ok)
#     if r.status_code == 200:
#         break
#
#     count += 1
#     if count >= 5:
#         break
#
# if r.status_code == 200:
#     soup = bs(r.text, "html.parser")
#     list_parse_objects = soup.find_all('div', class_="search-registry-entry-block box-shadow-search-input")
#
#     for object in list_parse_objects:
#         print("-"*20)
#         _ = object.find('div', class_="col-9 p-0 registry-entry__header-top__title text-truncate").text.strip()
#         _ = _[0:6] if _[0] == '4' else _[0:7]
#         print(f'Закупки по: {_}')
#
#         _ = object.find('div', class_='registry-entry__body-value').text.strip()
#         print(f'Наименование закупки: {_}')
#
#
#         _ = object.find('div', class_='price-block__value').text.strip()[:-1]
#         print(f'Цена: {_}')
#
#
#         _ = object.find('div', class_='registry-entry__body-href').text.strip()
#         print(f'Заказчик: {_}')
#
#         _ = object.find('div', class_='data-block__value').text.strip()
#         print(f'Дата окончания: {_}')
#
#         _ = object.find('div', class_='registry-entry__header-mid__number')
#         children = _.findChildren('a')
#         children = children[0].get('href')
#         print(f'Ссылка: https://zakupki.gov.ru{children}')
#
#         print("-"*20)


if __name__ == '__main__':
    parser = Parser(request_type=None)

    while True:

        command = input(f"[{INFO}] Print 'help' for call list commands.\n")

        if command == 'help':
            parser.help()

        match command:
            case '1':
                parser.help()
            case '2':
                print(parser.get_request_type())
            case '3':
                print(parser.set_request_type())
            case '4':
                print(parser.get_name_file())
            case '5':
                print(parser.set_path_parse_file())
            case '6':
                print(parser.parse())
            case '7':
                print(parser.check_info())
            case '8':
                pass
            case '9':
                print(parser.excel_import(parser.DIVS_DICT))
            case '10':
                break
            case _:
                print("Unexpected command!")
