import openpyxl
wb = openpyxl.Workbook()
sheet=wb.active
sheet["A1"].value="name"
sheet["A2"].value="rahul"
sheet["A3"].value="sarthak"

sheet.cell(row=1,column=2).value ="Age"
sheet.cell(row=2,column=2).value ="20"
sheet.cell(row=3,column=2).value ="19"

wb.save("test.xlsx")