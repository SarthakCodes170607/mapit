import openpyxl

wb = openpyxl.load_workbook("students3.xlsx")
sheet = wb["Students"]

# iter_rows() gives you one row at a time as a tuple of cells
for row in sheet.iter_rows():
    for cell in row:
        print(cell.value, end="\t")
    print()

print("---")

# With values_only=True — skip the cell object, get just the value
for row in sheet.iter_rows(values_only=True):
    for cell in row:
        print(cell, end='\t')
    # print(row)
    print()
# ('Name', 'Age', 'City')
# ('Rahul', 20, 'Delhi')
# ('Priya', 22, 'Mumbai')