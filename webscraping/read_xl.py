import openpyxl

wb=openpyxl.load_workbook("test.xlsx")
sheet=wb.active

for val in range (1,3) :
    print(sheet.cell(row=val , column=2).value)

