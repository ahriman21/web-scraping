""" how to read from xlsx files """
import xlrd

# open workbook (excel file) :
workbook = xlrd.open('path')

# open sheet :
sheet = workbook.sheet_by_index(0)

# get total number of rows:
rows = sheet.nrows

# read rows from worksheet :
for no in range(rows):
    first_col,second_col = sheet.row_values(row)
    print(first_col,'   ',second_col)

# =====================================================================================
""" how to write in xlsx files """

from xlsxwriter import Workbook

# add workbook to excel :
workbook = Workbook('name.xlsx')

# add worksheet to excel :
sheet = Workbook.add_worksheet()

# row number, col number, content :
sheet.write(0,0,'text')

# example : write numbers from 0 to 9 in column 0 in rows below each ohter :
for i in range(10):
    sheet.write(i,0,i)
