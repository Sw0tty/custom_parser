"""
"""
import os
import csv

from openpyxl import Workbook
from tkinter.filedialog import asksaveasfilename
from app_config.settings import DEFAULT_NAME_SAVE_FILE, SUPPORTED_FORMATS
from app_config.app_notices import CANCELLED, ERROR, FILE_CREATED

class MainMethods:

    def __init__(self, commands: dict):
        self.__commands = commands
        # self.EXPORT_DATA = deepcopy(EXCEL_TEMPLATE)
        # self.OPEN_ = deepcopy(OPENPX_EXCEL_TEMPLATE)

    def help(self):
        for key in self.__commands.keys():
            print(f'\t{key} - {self.__commands[key]}')

    @staticmethod
    def _save_as_file(import_data, file_extansion):
        
        file = asksaveasfilename(
                    initialfile=DEFAULT_NAME_SAVE_FILE,
                    title="Save file",
                    initialdir=os.getcwd(),
                    filetypes=(*SUPPORTED_FORMATS, ('All files', '*')),
                    defaultextension=True
                    )
        
        if not file:
            return CANCELLED

        match file_extansion(file):
            case '.xlsx':
                wb = Workbook()
                ws = wb.active
                ws.title = DEFAULT_NAME_SAVE_FILE

                for row in import_data:
                    ws.append(row)
                wb.save(file)

            case '.csv':
                with open(file, 'w') as csvfilewrite:
                    writer = csv.writer(csvfilewrite, lineterminator="\r", delimiter = ";")
                    
                    for i in import_data:
                        writer.writerow(i)
            case _:
                return f'[{ERROR}] Unexpected extansion!'
        return FILE_CREATED
    