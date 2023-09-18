"""
Working with excel file for rebuild raw site information
Support (*.csv) format
"""
import os
import csv
import pyexcel
import requests
import pyexcel_xls  # For excel module!
from pyexcel_io import writers  # For excel module!
from time import sleep
from copy import deepcopy
from os import getcwd, chdir
from os.path import basename
from bs4 import BeautifulSoup as bS
from tkinter.filedialog import askopenfilename, askdirectory

from classes.mas_parser import MasterExcel
from modules.parser.site_parser import URL_TEMPLATE
from app_config.settings import EXCEL_TEMPLATE, ZAK_44, PARSER_HEADERS, MAIN_PARSER_BLOCK, PARSER_DIVS_DICT, price_styler, SUPPORTED_FORMATS
from app_config.app_notices import ERROR, SUCCESS, INFO, WARNING, CANCELLED, FILE_NAME, FILE_PATH, FILE_UNDEFINED, APPLY_STRING


class Rebuilder(MasterExcel):

    _EXCEL_TEMPLATE = EXCEL_TEMPLATE
    IMPORT_DATA = deepcopy(_EXCEL_TEMPLATE)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__file_path = None
        self.__file_name = None
        self.__already_rebuild = False

    def get_file_name(self):
        if self.__file_path:
            return FILE_NAME + self.__file_name
        return FILE_UNDEFINED

    def get_selected_file_path(self, reset=False):
        if reset:
            return f'[{SUCCESS}] Path to new selected file: {self.__file_path}'

        if self.__file_path:
            return FILE_PATH + self.__file_path
        return FILE_UNDEFINED

    def set_selected_file(self):
        if self.__file_path:
            answer = input(APPLY_STRING)
            if answer != 'Yes':
                return CANCELLED

        filepath = askopenfilename(initialdir=getcwd(),
                                   title="Open file",
                                   filetypes=(*SUPPORTED_FORMATS, ('all files', '*'))
                                   )

        if filepath:
            if filepath.endswith('.csv'):
                self.__file_path = filepath
                self.__file_name = basename(self.__file_path)
                self.__already_rebuild = False
                return self.get_selected_file_path(True)
            return f"""[{ERROR}] File must have ({', '.join([i[1] for i in SUPPORTED_FORMATS])}) extension!"""
        return CANCELLED

    def get_rebuild_status(self, rebuilding=False):
        if self.__already_rebuild:
            status = SUCCESS if rebuilding else INFO
            return f'[{status}] Data ready to export!'
        return f'[{ERROR}] Nothing to export!'

    def prepare_rebuild(self, columns_name=True):
        if not self.__file_path:
            return self.get_file_name()

        if self.__already_rebuild:
            answer = input(APPLY_STRING)
            if answer != 'Yes':
                return CANCELLED
            self.IMPORT_DATA = deepcopy(self._EXCEL_TEMPLATE)

        # with open(self.__file_path, 'r') as open_file:
        #     open_file.readline()

        #     while True:
        #         values_list = open_file.readline().strip().split(';')

        #         if len(values_list) <= 1:
        #             break
        #         replays_value = values_list.pop(1)[1:]
        #         values_list[2] = price_styler(values_list[2])
        #         values_list.append('')
        #         values_list.append(3)

        #         if '223' in values_list[0]:
        #             for i in range(0, 4):
        #                 connection = requests.get(URL_TEMPLATE + replays_value, headers=PARSER_HEADERS)
        #                 sleep(2)

        #                 if connection.status_code == 200:
        #                     self.SEARCHING_INFO = bS(connection.text, "html.parser")
        #                     list_parse_objects = self.SEARCHING_INFO.find_all('div', class_=MAIN_PARSER_BLOCK)

        #                     for parse_obj in list_parse_objects:
        #                         _ = parse_obj.find('div', class_=PARSER_DIVS_DICT['org_href'][0])
        #                         children = _.findChildren('a')
        #                         children = children[0].get('href')
        #                         replays_value = f'https://zakupki.gov.ru{children}'
        #                     break
        #             values_list.append(replays_value)
        #         else:
        #             values_list.append(ZAK_44 + replays_value)
        #         self.IMPORT_DATA[next(iter(self.IMPORT_DATA))].append(values_list.copy())

        # self.__already_rebuild = True

        # return self.get_rebuild_status(True)

        with open(self.__file_path, 'r') as csvfile:
            reader = [*csv.reader(csvfile, delimiter=';')]
            
            cut_first_row = 1 if columns_name else 0

            for row in reader[cut_first_row:]:
                values_list = row

                replays_value = values_list.pop(1)[1:]
                values_list[2] = price_styler(values_list[2])
                values_list.append('')
                values_list.append(3)

                if '223' in values_list[0]:
                    for i in range(0, 4):
                        connection = requests.get(URL_TEMPLATE + replays_value, headers=PARSER_HEADERS)
                        sleep(2)

                        if connection.status_code == 200:
                            data = bS(connection.text, "html.parser")
                            list_parse_objects = data.find_all('div', class_=MAIN_PARSER_BLOCK)

                            for parse_obj in list_parse_objects:
                                _ = parse_obj.find('div', class_=PARSER_DIVS_DICT['org_href'][0])
                                children = _.findChildren('a')
                                children = children[0].get('href')
                                replays_value = f'https://zakupki.gov.ru{children}'
                            break
                    values_list.append(replays_value)
                else:
                    values_list.append(ZAK_44 + replays_value)
                self.IMPORT_DATA[next(iter(self.IMPORT_DATA))].append(values_list.copy())

        self.__already_rebuild = True

        return self.get_rebuild_status(True)

    def excel_export(self):
        if not self.__file_path:
            return self.get_selected_file_path()

        if not self.__already_rebuild:
            return self.get_rebuild_status()

        return self._save_file(self.IMPORT_DATA)

        # path_dir = askdirectory(initialdir=getcwd(), title="Save in...")
        #
        # if not path_dir:
        #     return CANCELLED
        #
        # chdir(path_dir)
        #
        # if os.path.exists(f"Выгрузка {TODAY}.xls"):
        #     answer = input(f"""[{WARNING}] File already exist. Overwrite file? 'Yes' to accept. """ +
        #                    """'no' to save as copy name.\nAnswer: """)
        #
        #     match answer:
        #         case 'Yes':
        #             try:
        #                 pyexcel.save_book_as(bookdict=self.IMPORT_DATA, dest_file_name=f"Выгрузка {TODAY}.xls")
        #                 return f'[{SUCCESS}] File created!'
        #             except PermissionError:
        #                 return f'[{ERROR}] Overwritten file is open in another program!'
        #         case 'no':
        #             count_try = 1
        #             while True:
        #                 if not os.path.exists(f"Выгрузка {TODAY}({count_try}).xls"):
        #                     pyexcel.save_book_as(bookdict=self.IMPORT_DATA,
        #                                          dest_file_name=f"Выгрузка {TODAY}({count_try}).xls")
        #                     return f'[{SUCCESS}] File created!'
        #                 count_try += 1
        #         case _:
        #             return CANCELLED


if __name__ == '__main__':
    from app_config.help_commands import REBUILDER_COMMANDS_DICT
    rebuilder = Rebuilder(commands=REBUILDER_COMMANDS_DICT)

    os.chdir('')
    print(rebuilder.set_selected_file())
    print(rebuilder.prepare_rebuild())
    print(rebuilder.excel_export())
