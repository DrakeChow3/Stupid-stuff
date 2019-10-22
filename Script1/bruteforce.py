#! python3
# hard bruteforce a pdf file

import PyPDF2,os

pdfFileObj = open('sample_encrypted.pdf', 'rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
textfile=open('dictionary.txt','r')
for line in textfile.readlines():
    line=line.strip()
    if pdfReader.decrypt(line.lower()):
        print('The password is '+line.lower())
        break
    elif pdfReader.decrypt(line.upper()):
        print('The password is '+line.upper())
        break
    else:
        print(line+',Nope')
        continue