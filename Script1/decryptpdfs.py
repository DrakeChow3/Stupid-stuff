#! python3
# write a script that will go through every PDF in a folder 
# (and its subfolders) and encrypt the PDFs using a password provided on the command line

import os,PyPDF2,sys,logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

password='andandand'
#get the absolute path
folder=os.path.abspath('.')
for foldername,subfolder,filenames in os.walk(folder):
    for file in filenames:
        if file.endswith('.pdf'):
            pdfReader=PyPDF2.PdfFileReader(open(os.path.join(foldername,file),'rb'))
            if pdfReader.isEncrypted:
                if pdfReader.decrypt(password):
                    pdfWriter=PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))
                    pdfWriter.write(open(os.path.join(folder,file[:-4]+'_decrypted.pdf'),'wb'))
                else:
                    print(str(password)+' is not the correct password for '+str(file))