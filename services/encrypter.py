#!/usr/bin/env python3

import PyPDF2
import os
def passProtect(_filename, password):
    filename, _ = os.path.splitext(_filename)
    try:
        pdfFile = open('uploads/'+filename+'.pdf', 'rb')
    except:
        return '''Could not open File.\nPlease make sure the file is in the same path\nOR\nEnter the file name correctly'''
    # Create reader and writer object
    if not len(password):
        return "Hey! You forgot to enter the Password!!!"
    try:
        pdfReader = PyPDF2.PdfReader(pdfFile)
        pdfWriter = PyPDF2.PdfWriter()
        # Add all pages to writer (accepted answer results into blank pages)
        for pageNum in range(len(pdfReader.pages)):
            pdfWriter.add_page(pdfReader.pages[pageNum])
        # Encrypt with your password
        pdfWriter.encrypt(password)
        # Write it to an output file. (you can delete unencrypted version now)
        resultPdf = open(f'encrypted/encrypted_{filename}.pdf', 'wb')
        pdfWriter.write(resultPdf)
        resultPdf.close()
        return "Success"
    except Exception as e:
        print(e)
        return "Something's wrong! Failed to protect the file :'( "
    