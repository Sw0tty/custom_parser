import openpyxl
import datetime
import os
import csv
from tkinter import filedialog
import pandas

SUPPORTED_FORMATS = [('CSV file', '*.csv'), ('Excel book', '*.xlsx'), ]

OPENPX_EXCEL_TEMPLATE = [
    ['Закупки по', 'Наименование закупки', 'Начальная (максимальная) цена контракта',
         'Наименование заказчика', 'Дата окончания подачи заявок', 'Интерес',
         'Категория', 'Ссылка']
         ]

os.chdir(os.getcwd() + r'\test_folder')

wb = openpyxl.Workbook()

# grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells
ws['A1'] = "TEST"

# # Rows can also be appended
# ws.append([1, 2, 3])

# # Python types will automatically be converted
# ws['A2'] = datetime.datetime.now()

# # Rename active sheet
# ws.title = 'TEST'

# Save the file


# sheet = pandas.read_excel(r'C:\Users\Егор\Desktop\testxls.xls')

class A:

    def __init__(self, vla) -> None:
        self.a_param = vla
    
    @property
    def a_param(self):
        return self.a
    
    @a_param.setter
    def a_param(self, new):
        self.a = new

a = A(1)

print(a.a_param)

a.a_param = 45

print(a.a_param)


# try:
#     file = filedialog.asksaveasfilename(initialfile='name', title="Save file", initialdir=os.getcwd(), filetypes=(*SUPPORTED_FORMATS, ('All files', '*')), defaultextension=True)
#     if not file:
#         print(12313)
# except FileNotFoundError:   
#     print('123')


# extansion = file[file.rfind('.'):]

# match extansion:
#     case '.xlsx':
#         wb.save(file)

#     case '.csv':
#         with open(file, 'w') as csvfilewrite:
#             writer = csv.writer(csvfilewrite, lineterminator="\r", delimiter = ";")
            
#             for i in OPENPX_EXCEL_TEMPLATE:
#                 writer.writerow(i)




# path_dir = filedialog.asksaveasfile(filetypes=(*SUPPORTED_FORMATS, ('All files', '*')))

# path_dir = filedialog.askopenfilename(filetypes=(*SUPPORTED_FORMATS, ('All files', '*')))

# print(path_dir)

# worksheet = openpyxl.load_workbook(os.getcwd() + "\sample2.xlsx").active
# reader = []
# data = []

# for i in range(0, worksheet.max_row):
#     count = 0
#     for col in worksheet.iter_cols(1, worksheet.max_column):
#         value = col[i].value if col[i].value else ''
#         if count == worksheet.max_column - 1:
#             print(col[i].value)
#         data.append(value)
#         count += 1
#     reader.append(data.copy())
#     data.clear()   

# print(reader)
