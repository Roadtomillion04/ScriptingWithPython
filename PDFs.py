import PyPDF2
'''use rb mode in Pdf - read binary values'''

with open('PDF_files/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file) #pyPDF can read binary values of file object
    print(reader.numPages)
    print(reader.getPage(0))

    # we can't reader.rotate because reader is an object
    page = reader.getPage(0)
    page.rotateClockwise(180) # we are rotating page of the PDF here
    print(page)
                                    #write binary
    with open("./PDF_files/rotated.pdf", 'wb') as new_file:
        writer = PyPDF2.PdfFileWriter()
                       #page object
        writer.addPage(page) # we have to manually add the page before writing to new created PDF files because rotated.pdf dosen't exist

        writer.write(new_file)

'''To see what in pdf'''
read_page = PyPDF2.PdfFileReader(open('./PDF_files/twopage.pdf', 'rb'))
page1 = read_page.getPage(0)
page2 = read_page.getPage(1)

print(page1.extractText())
print(page2.extractText())
