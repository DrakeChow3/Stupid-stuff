#! python3
#In this project, you’ll write a program to update cells in a spreadsheet of produce sales. 
# Your program will look through the spreadsheet, find specific kinds of produce, and update their prices

import openpyxl

wb=openpyxl.load_workbook('produceSales.xlsx')
sheet=wb.get_sheet_by_name('Sheet')

updatePrice={'Garlic': 3.07,
                 'Celery': 1.19,
                 'Lemon': 1.27}

for i in range(2,sheet.max_row+1):
    name=sheet['A'+str(i)].value
    if name in updatePrice.keys():
        sheet['B'+str(i)]=updatePrice[name]
wb.save('updatedproductSales.xlsx')