import PyPDF2

'''watermark the super.pdf '''
# we are reading pd and wtr files

pdf = PyPDF2.PdfFileReader(open('Super.pdf', 'rb'))
watermark_page = PyPDF2.PdfFileReader(open('./PDF_files/wtr.pdf', 'rb'))
merger = PyPDF2.PdfFileWriter() #because we have to add new pages at end

for i in range(pdf.getNumPages()): #because we can't iterate the int directly
    pages = pdf.getPage(i)
    pages.mergePage(watermark_page.getPage(0))
    merger.addPage(pages)

                # This gonna create new pdf so wb
    with open('./PDF_files/watermarked.pdf', 'wb') as create_pdf:
        merger.write(create_pdf)

'''THis writes everything in merger to new file becuase merger is writerObject'''