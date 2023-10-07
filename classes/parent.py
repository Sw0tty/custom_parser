"""
File with MasterExcel class
"""
import os
from os import getcwd, chdir, listdir
import xlrd
# import pyexcel
import openpyxl
import csv
from copy import deepcopy
from tkinter import filedialog
from tkinter.commondialog import Dialog
from app_config.app_notices import CANCELLED, ERROR_FILE_EXTENSION, ERROR, WARNING, SUCCESS, FILE_CREATED, INFO
from tkinter.filedialog import askopenfilename, askdirectory, asksaveasfile, asksaveasfilename
from app_config.settings import DEFAULT_NAME_SAVE_FILE, EXCEL_TEMPLATE, SUPPORTED_FORMATS
from openpyxl import Workbook


class MasterExcel:

    EXPORT_DATA = deepcopy(EXCEL_TEMPLATE)

    # def __init__(self):
    #     # self.__commands = commands
    #     self.EXPORT_DATA = deepcopy(EXCEL_TEMPLATE)

    def reset_export_data(self, reset=False):        
        self.EXPORT_DATA = deepcopy(EXCEL_TEMPLATE)
        return f'[{SUCCESS}] Data reset!'

    def _check_export_data(self):
        if self.EXPORT_DATA is None:
            return f'[{INFO}] Data undefined!'

        if len(self.EXPORT_DATA[DEFAULT_NAME_SAVE_FILE]) > 1:
            answer = input("""Data not default. 'Yes' to set to default. 'no' to add data.\nAnswer: """)
            match answer:
                case 'Yes':
                    return self.reset_export_data(True)
                case 'no':
                    return f'[{INFO}] Data be added.'
                case _:
                    return CANCELLED                

    @staticmethod
    def get_file_extension(file_name: str) -> str:
        return file_name[file_name.rfind('.'):]

    @staticmethod
    def _file_reader(file_extension, file_path) -> list:
        match file_extension:
            case '.csv':
                with open(file_path, 'r') as csvfile:
                    reader = [*csv.reader(csvfile, delimiter=';')]
            # case '.xls':
            #     reader = pyexcel.get_array(file_path)

            #     reader = xlrd.open_workbook(r'C:\Users\Егор\Desktop\testxls.xls')
            #     sheet = reader.sheet_by_index(0)

            #     data = []
            #     for row in range(sheet.nrows):
            #         for cell in sheet.row(row):
            #             data.append(cell.value)
            case '.xlsx':
                worksheet = openpyxl.load_workbook(file_path).active
                reader = []
                data = []

                for i in range(0, worksheet.max_row):
                    for col in worksheet.iter_cols(1, worksheet.max_column):
                        value = col[i].value if col[i].value else ''
                        data.append(value)
                    reader.append(data.copy())
                    data.clear()                  
            case _:
                return f'[{ERROR}] Unexpected extension!'
        return reader

    @staticmethod
    def left_titles():
        answer = input("""Left the titles of columns? Yes to accept, no to cut.\nAnswer: """).strip()
        match answer:
            case 'Yes':
                return True
            case 'no':
                return False
            case _:
                return None

    # @staticmethod
    # def _save_file(import_data, file_extension):
        
    #     file = asksaveasfilename(
    #                 initialfile=DEFAULT_NAME_SAVE_FILE,
    #                 title="Save file",
    #                 initialdir=os.getcwd(),
    #                 filetypes=(*SUPPORTED_FORMATS, ('All files', '*')),
    #                 defaultextension=True
    #                 )
        
    #     if not file:
    #         return CANCELLED

    #     match file_extension(file):
    #         case '.xlsx':
    #             wb = Workbook()
    #             ws = wb.active
    #             ws.title = DEFAULT_NAME_SAVE_FILE

    #             for row in import_data:
    #                 ws.append(row)
    #             wb.save(file)

    #         case '.csv':
    #             with open(file, 'w') as csvfilewrite:
    #                 writer = csv.writer(csvfilewrite, lineterminator="\r", delimiter = ";")
                    
    #                 for i in import_data:
    #                     writer.writerow(i)
    #         case _:
    #             return f'[{ERROR}] Unexpected extansion!'
    #     return FILE_CREATED

    
        # path_dir = askdirectory(initialdir=getcwd(), title="Save in...")

        # if not path_dir:
        #     return CANCELLED

        # chdir(path_dir)

        

        # if DEFAULT_NAME_SAVE_FILE in [file_name[:file_name.rfind('.')] for file_name in listdir()]:
        #     answer = input(f"""[{WARNING}] File already exist. Overwrite file? 'Yes' to accept. """ +
        #                    """'no' to save as copy name.\nAnswer: """)

        #     match answer:
        #         case 'Yes':
        #             try:
        #                 pyexcel.save_book_as(bookdict=import_data, dest_file_name=f"{DEFAULT_NAME_SAVE_FILE}.xls")
        #                 return f'[{SUCCESS}] File created!'
        #             except PermissionError:
        #                 return f'[{ERROR}] Overwritten file is open in another program!'
        #         case 'no':
        #             count_try = 1
        #             while True:
        #                 if not os.path.exists(f"{DEFAULT_NAME_SAVE_FILE}({count_try}).xls"):
        #                     pyexcel.save_book_as(bookdict=import_data,
        #                                          dest_file_name=f"{DEFAULT_NAME_SAVE_FILE}({count_try}).xls")
        #                     return FILE_CREATED
        #                 count_try += 1
        #         case _:
        #             return CANCELLED
        
        # try:
        #     wb.save(
        #         asksaveasfilename(
        #             initialfile=DEFAULT_NAME_SAVE_FILE,
        #             title="Save file",
        #             initialdir=os.getcwd(),
        #             filetypes=(SUPPORTED_FORMATS[1], ('All files', '*')),
        #             defaultextension=True
        #             )
        #     )
        #     return FILE_CREATED
        # except FileNotFoundError:
        #     return CANCELLED
        
        

        # pyexcel.save_book_as(bookdict=import_data, dest_file_name=f"{DEFAULT_NAME_SAVE_FILE}.xls")

        # 
        # wb = Workbook()

        # ws = wb.active
        # ws.title = DEFAULT_NAME_SAVE_FILE

        # for row in import_data_open:
        #     ws.append(row)

        # wb.save(f"{DEFAULT_NAME_SAVE_FILE}.xlsx")
        # wb.save(f"{DEFAULT_NAME_SAVE_FILE}openpyxlxls.xls")
        # 

        

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
