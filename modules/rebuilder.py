"""
Working with excel file for rebuild raw site information
Support (*.csv, *.xlsx) format
"""
import csv
import requests
from time import sleep
from os import getcwd, chdir
from os.path import basename
from bs4 import BeautifulSoup as bS
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import messagebox

from classes.parent import MasterExcel
from classes.modules_default import MainMethods
from modules.parser.site_parser import URL_TEMPLATE
from app_config.settings import ZAK_44, PARSER_HEADERS, MAIN_PARSER_BLOCK, PARSER_DIVS_DICT, price_styler, SUPPORTED_FORMATS
from app_config.app_notices import ERROR, SUCCESS, INFO, WARNING, CANCELLED, FILE_NAME, FILE_PATH, FILE_UNDEFINED, APPLY_STRING


class Rebuilder(MainMethods, MasterExcel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__file_path = None
        self.__file_name = None
        self.__already_rebuild = False

    def get_params_status(self):
        return messagebox.showinfo(title='Parameters status',
                                   message=f'File path: {self.get_selected_file_path()}\nFile name: {self.get_selected_file_path()}')

    def get_file_name(self):
        if self.__file_path:
            return FILE_NAME + self.__file_name
        return FILE_UNDEFINED

    def get_selected_file_path(self, reset=False):
        if reset:
            self.reset_export_data()
            return f'[{SUCCESS}] Path to new selected file: {self.__file_path}'

        if self.__file_path:
            return FILE_PATH + self.__file_path
        return FILE_UNDEFINED

    def get_rebuild_status(self, rebuilding=False):
        if self.__already_rebuild:
            status = SUCCESS if rebuilding else INFO
            return f'[{status}] Data ready to export!'
        return f'[{ERROR}] Nothing to export!'

    def set_selected_file(self):
        if self.__file_path:
            answer = input(APPLY_STRING)
            if answer != 'Yes':
                return CANCELLED

        filepath = askopenfilename(initialdir=getcwd(),
                                   title="Open file",
                                   filetypes=(*SUPPORTED_FORMATS[:2], ('All files', '*'))
                                   )

        if filepath:
            for extension in SUPPORTED_FORMATS:
                if filepath.endswith(extension[1][1:]):
                    self.__file_path = filepath
                    self.__file_name = basename(self.__file_path)
                    self.__already_rebuild = False
                    return self.get_selected_file_path(True)
            return f"""[{ERROR}] File must have ({', '.join([i[1] for i in SUPPORTED_FORMATS])}) extension!"""
        return CANCELLED

    def prepare_rebuild(self, columns_name=True):
        if not self.__file_path:
            return self.get_file_name()

        if self.__already_rebuild:
            answer = input(APPLY_STRING)
            if answer != 'Yes':
                return CANCELLED
            self.reset_export_data()

        reader = self._file_reader(self.get_file_extension(self.__file_name), self.__file_path)

        if reader is None:
            return f'[{ERROR}] Extension error!'
            
        cut_first_row = 1 if columns_name else 0

        for row in reader[cut_first_row:]:
            values_list = row

            replays_value = values_list.pop(1)[1:]
            values_list[2] = price_styler(values_list[2])
            values_list.append('')
            values_list.append(3)

            if '223' in values_list[0]:
                for i in range(0, 4):
                    response = requests.get(URL_TEMPLATE + replays_value, headers=PARSER_HEADERS)
                    
                    if response.status_code == 200:
                        data = bS(response.text, "html.parser")
                        list_parse_objects = data.find_all('div', class_=MAIN_PARSER_BLOCK)

                        for parse_obj in list_parse_objects:
                            _ = parse_obj.find('div', class_=PARSER_DIVS_DICT['org_href'])
                            children = _.findChildren('a')
                            children = children[0].get('href')
                            replays_value = f'https://zakupki.gov.ru{children}'
                        break

                values_list.append(replays_value)
            else:
                values_list.append(ZAK_44 + replays_value)

            self.EXPORT_DATA.append(values_list.copy())

        self.__already_rebuild = True

        return self.get_rebuild_status(True)

    def excel_export(self):
        if not self.__file_path:
            return self.get_selected_file_path()

        if not self.__already_rebuild:
            return self.get_rebuild_status()

        return self._save_as_file(self.EXPORT_DATA, self.get_file_extension)


if __name__ == '__main__':
    from app_config.help_commands import REBUILDER_COMMANDS_DICT
    rebuilder = Rebuilder(commands=REBUILDER_COMMANDS_DICT)

    # os.chdir('')
    print(rebuilder.set_selected_file())
    print(rebuilder.prepare_rebuild())
    # print(rebuilder.prepare_rebuild())
    print(rebuilder.excel_export())
