"""
File with MasterExcel class
"""
from os import getcwd
from os.path import basename
from tkinter.filedialog import askopenfilename
from app_config.app_notices import FILE_UNDEFINED, FILE_PATH, FILE_NAME, CANCELLED, ERROR_FILE_EXTENSION, INFO, ERROR


class MasterExcel:

    def __init__(self, commands: dict):
        self.__commands = commands
        # self._file_path = None
        # self._file_name = None

    def help(self):
        for key in self.__commands.keys():
            print(f'\t{key} - {self.__commands[key]}')

    # def get_parser_type(self):
    #     return f'[{INFO}] Now parser type is: {self.__parser_type}'

    # def set_request_type(self):
    #     while True:
    #         print(f"[{INFO}]What's type a request?")
    #         parser_type = input("File - parse file\nLink - parse link\nType: ").lower().strip()
    #         if parser_type == 'file' or parser_type == 'link':
    #             self.__parser_type = parser_type
    #             return self.get_parser_type()
    #         return f'[{ERROR}] Unexpected parser type!'
