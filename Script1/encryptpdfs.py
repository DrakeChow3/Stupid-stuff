#! python3
# write a script that will go through every PDF in a folder 
# (and its subfolders) and encrypt the PDFs using a password provided on the command line

import os,PyPDF2,sys,logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

password='swordfish'
#make sure the path is absolute
folder=os.path.abspath('.')
logging.debug(folder)
for foldername,subfolder,files in os.walk(folder):
    logging.debug('Entering folder:'+foldername)
    for file in files:
        logging.debug('file:'+str(file)+' in '+str(files))
        if file.endswith('.pdf'):
            logging.debug('Creating file '+os.path.join(foldername,file[:-4]+'_encrypted.pdf'))
            notC_file=open(os.path.join(foldername,file),'rb')
            notC_pdf=PyPDF2.PdfFileReader(notC_file)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(notC_pdf.numPages):
                pdfWriter.addPage(notC_pdf.getPage(pageNum)) 
            pdfWriter.encrypt(password)
            C_file=open(os.path.join(foldername,file[:-4]+'_encrypted.pdf'),'wb')
            pdfWriter.write(C_file)
            C_file.close()
            logging.debug('Deleting file '+os.path.join(foldername,file))

notC_file.close()