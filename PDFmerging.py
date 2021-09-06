'''we gonna merge pdf given in output'''''
import sys
import os
import PyPDF2

inputs = sys.argv[1:] #This gonna grab all inputs and change to list

def pdf_combiner():
    merger = PyPDF2.PdfFileMerger()

    for pdf in os.listdir('./PDF_files/'):
        print(pdf)
        merger.append(f'./PDF_files/{pdf}') # you have to give actual pdf path because all files are inside directory

    merger.write('Super.pdf') # It creates new one if not exists


pdf_combiner()
