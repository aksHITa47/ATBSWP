import openpyxl
import os
print(os.getcwd())
os.chdir("/home/akki")
wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))
print(wb.sheetnames)
sheet = wb['Sheet1']
print(sheet)
print(type(sheet))
print(sheet.title)
anotherSheet = wb.active # Get the active sheet.
print(anotherSheet)

print(sheet['A1']) # Get a cell from the sheet.
print(sheet['A1'].value) 
print(type(sheet['A1'].value))
c = sheet['B1']
print(c.value)
print('Row %s, Column %s is %s' % (c.row, c.column, c.value))