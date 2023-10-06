"""
!!!-NOW ON REFACTORING-!!!
Parse the HTML files.
!!!-NOW ON REFACTORING-!!!
"""
from os import getcwd, chdir
from os.path import basename
# import pyexcel
# import pyexcel_xls  # For excel module!
# from pyexcel_io import writers  # For excel module!
from colorama import init
from bs4 import BeautifulSoup as bS
from classes.parent import MasterExcel
from classes.modules_default import MainMethods
from tkinter.filedialog import askopenfilename, askdirectory
from app_config.settings import price_styler, MAIN_PARSER_BLOCK
from app_config.app_notices import ERROR, SUCCESS, CANCELLED, FILE_NAME, FILE_PATH, FILE_UNDEFINED, INFO, APPLY_STRING

init()


class FileParser(MainMethods, MasterExcel):

    SEARCHING_INFO = None

    LIST_PARSE_OBJECTS = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__file_path = None
        self.__file_name = None
        self.__ready_to_export = False

    def get_file_name(self):
        if self.__file_path:
            return FILE_NAME + self.__file_name
        return FILE_UNDEFINED

    def get_file_path(self):
        if self.__file_path:
            return FILE_PATH + self.__file_path
        return FILE_UNDEFINED

    def set_file_path(self):
        if self.__file_path:
            answer = input(APPLY_STRING)
            if answer != 'Yes':
                return CANCELLED

        filepath = askopenfilename(initialdir=getcwd(),
                                   title="Open file",
                                   filetypes=(('HTML file', '*.html'), ('All files', '*'))
                                   )

        if filepath:
            if filepath.endswith('.html'):
                self.__file_path = filepath
                self.__file_name = basename(self.__file_path)
                return self.get_file_path()
            return f'[{ERROR}] File must have html extension!'
        return CANCELLED

    def parse_file(self, div_dict):

        if not self.__file_path:
            return self.get_file_name()

        if self.__ready_to_export:
            answer = input(APPLY_STRING)
            if answer != 'Yes':
                return CANCELLED
            self.reset_export_data()

        with open(self.__file_path, 'r', encoding='utf-8') as open_file:
            self.SEARCHING_INFO = bS(open_file.read(), 'lxml')
        
        self.LIST_PARSE_OBJECTS = \
            self.SEARCHING_INFO.find_all('div', class_=MAIN_PARSER_BLOCK)

        values_list = []

        for parse_obj in self.LIST_PARSE_OBJECTS:
            values_list.clear()
            for class_key in div_dict.keys():
                _ = parse_obj.find('div', class_=div_dict[class_key])
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
                        _ = children[0].get('href')

                values_list.append(_)

            # self.EXPORT_DATA[next(iter(self.EXPORT_DATA))].append(values_list.copy())
            self.EXPORT_DATA.append(values_list.copy())

        # ----

        self.__ready_to_export = True
        
        return f'[{SUCCESS}] File ready to export'

    def file_ready(self):
        if self.__ready_to_export:
            return f'[{INFO}] Data ready to export.'
        return f'[{ERROR}] Data undefined!'

    def excel_export(self):
        if not self.SEARCHING_INFO:
            return self.get_file_path()

        return self._save_as_file(self.EXPORT_DATA, self.get_file_extansion)
