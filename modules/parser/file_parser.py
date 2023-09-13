"""

"""
import os.path
from os import getcwd, chdir
from os.path import basename
import pyexcel
import pyexcel_xls  # For excel module!
from pyexcel_io import writers  # For excel module!
from time import sleep
from colorama import init
from copy import deepcopy
from bs4 import BeautifulSoup as bS
from classes.parent import MasterExcel
from tkinter.filedialog import askopenfilename, askdirectory
from app_config.settings import TODAY, EXCEL_TEMPLATE, price_styler
from app_config.app_notices import ERROR, SUCCESS, CANCELLED, FILE_NAME, FILE_PATH, FILE_UNDEFINED, INFO

init()


class FileParser(MasterExcel):

    SEARCHING_INFO = None

    LIST_PARSE_OBJECTS = None

    _EXCEL_TEMPLATE = EXCEL_TEMPLATE

    IMPORT_DATA = deepcopy(_EXCEL_TEMPLATE)

    def __init__(self, commands: dict):
        super().__init__(commands)
        self.__file_path = None
        self.__file_name = None
        self.__ready_to_import = False

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
                                   filetypes=(('html file', '*.html'), ('all files', '*'))
                                   )

        if filepath:
            if filepath.endswith('.html'):
                self.__file_path = filepath
                self.__file_name = basename(self.__file_path)
                return self.get_file_path()
            return f'[{ERROR}] File must have html extension!'
        return CANCELLED

    def parse_file(self):

        if not self.__file_path:
            return self.get_file_name()

        with open(self.__file_path, 'r', encoding='utf-8') as open_file:
            self.SEARCHING_INFO = bS(open_file.read(), 'lxml')
        self.parse_info()
        return f'[{SUCCESS}] File ready to export'

    def parse_info(self):
        self.LIST_PARSE_OBJECTS = \
            self.SEARCHING_INFO.find_all('div', class_="search-registry-entry-block box-shadow-search-input")

    def file_ready(self):
        if self.__ready_to_import:
            return f'[{INFO}] Data ready to import.'
        return f'[{ERROR}] Data undefined!'

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
                        _ = children[0].get('href')

                values_list.append(_)

            self.IMPORT_DATA[next(iter(self.IMPORT_DATA))].append(values_list.copy())

        path_dir = askdirectory(initialdir=getcwd(), title="Save in...")
        if path_dir:
            chdir(path_dir)
            # if os.path.exists(f"Выгрузка {TODAY}.xls"):
            #     pyexcel.save_book_as(bookdict=self.IMPORT_DATA, dest_file_name=f"Выгрузка {TODAY}.xls")
            pyexcel.save_book_as(bookdict=self.IMPORT_DATA, dest_file_name=f"Выгрузка {TODAY}.xls")
            return f'[{SUCCESS}] File created!'
        return CANCELLED
