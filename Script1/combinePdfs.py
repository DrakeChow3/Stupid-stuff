#! python3
# merging several dozen PDF documents into a single PDF file
#Each of them has a cover sheet as the first page, 
# but you don’t want the cover sheet repeated in the final result

import os,PyPDF2

list_file=[]
for file in os.listdir('.'):
    if file.endswith('.pdf'):
        list_file.append(file)

list_file.sort(key=str.lower)

file=PyPDF2.PdfFileWriter()

for i in range(len(list_file)):
    copied_name=open(list_file[i],'rb')
    copied_file=PyPDF2.PdfFileReader(copied_name)
    for page in range(copied_file.numPages):
        if i!=0 and page==0:
            continue
        else:
            PageOb=copied_file.getPage(page)
            file.addPage(PageOb)
    
f_name=open('sumfile.pdf','wb')
file.write(f_name)
f_name.close()
copied_name.close()

    