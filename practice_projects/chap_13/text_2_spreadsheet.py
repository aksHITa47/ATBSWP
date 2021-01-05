import openpyxl
from openpyxl.styles import Font
from pathlib import Path
path=Path.cwd()
wb=openpyxl.Workbook()
sheet=wb.active
Index=1
for file in list(path.glob('*.txt')):
    fileobj=open(file)
    data=fileobj.readlines()
    for j in range(len(data)):
        sheet.cell(row=j+1,column=Index).value=str(data[j])
        Index+=1
    fileobj.close()
wb.save("t2s.xlsx")
wb.close()

