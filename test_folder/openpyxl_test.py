import openpyxl
import datetime
import os
from tkinter import filedialog
SUPPORTED_FORMATS = [('CSV file', '*.csv'), ('Excel book', '*.xlsx'), ]

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
wb.save(filedialog.asksaveasfilename(initialfile='test', title="Save file", initialdir=os.getcwd(), filetypes=(*SUPPORTED_FORMATS, ('All files', '*')), defaultextension=True))



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
