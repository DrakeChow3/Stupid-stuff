#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for
# each county.

import openpyxl,pprint
wb=openpyxl.load_workbook('censuspopdata.xlsx')
sheet=wb.get_sheet_by_name('Population by Census Tract')
dic={}
for i in range(2,sheet.max_row+1):
    statem1=sheet['B'+str(i)].value
    county=sheet['C'+str(i)].value
    pop=sheet['D'+str(i)].value
    dic.setdefault(statem1,{})
    dic[statem1].setdefault(county,{'tract':0,'pop':0})
    dic[statem1][county]['tract']+=1
    dic[statem1][county]['pop']+=pop
print("Writing result...")
file=open('census2010.py','w')
file.write('AllData='+pprint.pformat(dic))
file.close()
print('Done')
    
    