"""
"""
import os
import csv

from openpyxl import Workbook
from tkinter.filedialog import asksaveasfilename
from app_config.settings import DEFAULT_NAME_SAVE_FILE, SUPPORTED_FORMATS
from app_config.app_notices import CANCELLED, ERROR, FILE_CREATED


# class HelpMethod:

#     def __init__(self, commands: dict):
#         self.__commands = commands

#     def help(self):
#         for key in self.__commands.keys():
#             print(f'\t{key} - {self.__commands[key]}')


class MainMethods():

    # def __init__(self, commands: dict):
    #     self.__commands = commands
        # self.EXPORT_DATA = deepcopy(EXCEL_TEMPLATE)
        # self.OPEN_ = deepcopy(OPENPX_EXCEL_TEMPLATE)

    # def help(self):
    #     for key in self.__commands.keys():
    #         print(f'\t{key} - {self.__commands[key]}')

    @staticmethod
    def _save_as_file(import_data: list, file_extension: str) -> str:
        
        file = asksaveasfilename(
                    initialfile=DEFAULT_NAME_SAVE_FILE,
                    title="Save file",
                    initialdir=os.getcwd(),
                    filetypes=(*SUPPORTED_FORMATS, ('All files', '*')),
                    defaultextension=True
                    )
        
        if not file:
            return CANCELLED
        try:
            match file_extension(file):
                case '.xlsx':
                    work_book = Workbook()
                    work_sheet = work_book.active
                    work_sheet.title = DEFAULT_NAME_SAVE_FILE

                    for row in import_data:
                        work_sheet.append(row)
                    work_book.save(file)

                case '.csv':
                    with open(file, 'w') as csv_file:
                        csv_writer = csv.writer(csv_file, lineterminator="\r", delimiter = ";")
                        
                        for row in import_data:
                            csv_writer.writerow(row)
                case _:
                    return f'[{ERROR}] Unexpected extension!'
            return FILE_CREATED
        except PermissionError:
            return f'[{ERROR}] File open in other program!'
    