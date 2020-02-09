from PyPDF2 import PdfFileReader
import os

#pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']


pdffiles = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]
totalFiles = 0
totalPages = 0
for pdffile in pdffiles:
    pdf = PdfFileReader(pdffile)
    print(pdffile + " -- " + str(pdf.getNumPages()))
    if pdffile != "result.pdf":
        totalFiles = totalFiles + 1
        totalPages = totalPages + pdf.getNumPages();

print("Total files : " + str(totalFiles))
print("Total Pages : " + str(totalPages))
print("Merged Pages (except 1st and last of each ppt) : " + str(totalPages - (totalFiles * 2)))
