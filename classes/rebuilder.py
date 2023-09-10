"""
Rebuilder module
"""
from modules.notice_module import ERROR, INFO
from tkinter.filedialog import askopenfilename, askdirectory, askopenfile
from classes.parent import MasterExcel

import os.path
from os import getcwd, chdir
from os.path import basename
import pyexcel
import requests
from classes.parser.site_parser import URL_TEMPLATE
import pyexcel_xls  # For excel module!
from pyexcel_io import writers  # For excel module!
from time import sleep
from colorama import init
from copy import deepcopy
from bs4 import BeautifulSoup as bS
from classes.parent import MasterExcel
from tkinter.filedialog import askopenfilename, askdirectory
from modules.parser_params import TODAY, EXCEL_TEMPLATE, PARSER_DIVS_DICT, ZAK_44
from modules.notice_module import ERROR, SUCCESS, INFO, CANCELLED, FILE_CREATED, FILE_NAME, FILE_PATH, FILE_UNDEFINED, ERROR_FILE_EXTENSION


class Rebuilder(MasterExcel):

    _EXCEL_TEMPLATE = EXCEL_TEMPLATE
    IMPORT_DATA = deepcopy(_EXCEL_TEMPLATE)
    SEARCHING_INFO = None
    LIST_PARSE_OBJECTS = None

    def __init__(self, commands: dict):
        super().__init__(commands)
        self.__file_path = None
        self.__file_name = None
        self.__rebuild = None

    def get_file_name(self):
        if self.__file_path:
            return FILE_NAME + self.__file_name
        return FILE_UNDEFINED

    def get_file_path(self):
        if self.__file_path:
            return FILE_PATH + self.__file_path
        return FILE_UNDEFINED

    def set_file_path(self):
        filepath = askopenfilename(initialdir=getcwd(),
                                   title="Open file",
                                   filetypes=(('csv file', '*.csv'), ('all files', '*'))
                                   )

        if filepath:
            if 'csv' in filepath:
                self.__file_path = filepath
                self.__file_name = basename(self.__file_path)
                return self.get_file_path()
            return f'[{ERROR}] File must have csv extension!'
        return CANCELLED

    def check_rebuild(self):
        if self.__rebuild:
            return f'[{INFO}] File ready to export!'
        return f'[{ERROR}] Nothing to export!'

    def prepare_rebuild(self):
        if not self.__file_path:
            return self.get_file_name()

        with open(self.__file_path, 'r') as open_file:
            open_file.readline()

            while True:
                values_list = open_file.readline().strip().split(';')
                if len(values_list) <= 1:
                    break
                replays_value = values_list.pop(1)[1:]
                values_list.append('')
                values_list.append('')

                if '223' in values_list[0]:
                    for i in range(0, 4):
                        headers = {
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
                        }
                        connection = requests.get(URL_TEMPLATE + replays_value, headers=headers)
                        sleep(2)
                        if connection.status_code == 200:
                            self.SEARCHING_INFO = bS(connection.text, "html.parser")

                            self.LIST_PARSE_OBJECTS = \
                                self.SEARCHING_INFO.find_all('div',
                                                             class_="search-registry-entry-block box-shadow-search-input")
                            for parse_obj in self.LIST_PARSE_OBJECTS:
                                _ = parse_obj.find('div', class_='registry-entry__header-mid__number')
                                children = _.findChildren('a')
                                children = children[0].get('href')
                                replays_value = f'https://zakupki.gov.ru{children}'
                            break
                    values_list.append(replays_value)
                else:
                    values_list.append(ZAK_44 + replays_value)
                self.IMPORT_DATA[next(iter(self.IMPORT_DATA))].append(values_list.copy())

    def parse_info(self):
        self.LIST_PARSE_OBJECTS = \
            self.SEARCHING_INFO.find_all('div', class_="search-registry-entry-block box-shadow-search-input")

    def excel_import(self):
        if not self.SEARCHING_INFO:
            return self.get_file_path()

        path_dir = askdirectory(initialdir=getcwd(), title="Save in...")
        if path_dir:
            chdir(path_dir)
            # if os.path.exists(f"Выгрузка {TODAY}.xls"):
            #     pyexcel.save_book_as(bookdict=self.IMPORT_DATA, dest_file_name=f"Выгрузка {TODAY}.xls")
            pyexcel.save_book_as(bookdict=self.IMPORT_DATA, dest_file_name=f"Выгрузка {TODAY}.xls")
            return f'[{SUCCESS}] File created!'
        return CANCELLED
