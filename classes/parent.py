"""
File with MasterExcel class
"""
import os
from os import getcwd, path, chdir, listdir
import pyexcel
from app_config.app_notices import FILE_UNDEFINED, CANCELLED, ERROR_FILE_EXTENSION, INFO, ERROR, WARNING, SUCCESS, FILE_CREATED
from tkinter.filedialog import askopenfilename, askdirectory
from app_config.settings import TODAY_DATE, DEFAULT_NAME_SAVE_FILE


class MasterExcel:

    def __init__(self, commands: dict):
        self.__commands = commands

    def help(self):
        for key in self.__commands.keys():
            print(f'\t{key} - {self.__commands[key]}')

    @staticmethod
    def _save_file(import_data):

        path_dir = askdirectory(initialdir=getcwd(), title="Save in...")

        if not path_dir:
            return CANCELLED

        chdir(path_dir)

        if DEFAULT_NAME_SAVE_FILE in [file_name[:file_name.rfind('.')] for file_name in listdir()]:
            answer = input(f"""[{WARNING}] File already exist. Overwrite file? 'Yes' to accept. """ +
                           """'no' to save as copy name.\nAnswer: """)

            match answer:
                case 'Yes':
                    try:
                        pyexcel.save_book_as(bookdict=import_data, dest_file_name=f"{DEFAULT_NAME_SAVE_FILE}.xls")
                        return f'[{SUCCESS}] File created!'
                    except PermissionError:
                        return f'[{ERROR}] Overwritten file is open in another program!'
                case 'no':
                    count_try = 1
                    while True:
                        if not path.exists(f"{DEFAULT_NAME_SAVE_FILE}({count_try}).xls"):
                            pyexcel.save_book_as(bookdict=import_data,
                                                 dest_file_name=f"{DEFAULT_NAME_SAVE_FILE}({count_try}).xls")
                            return FILE_CREATED
                        count_try += 1
                case _:
                    return CANCELLED

        pyexcel.save_book_as(bookdict=import_data, dest_file_name=f"{DEFAULT_NAME_SAVE_FILE}.xls")
        return FILE_CREATED

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
