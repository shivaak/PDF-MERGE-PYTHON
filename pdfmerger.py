from PyPDF2 import PdfFileMerger
import os
import re

#pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

merger = PdfFileMerger()

cwd = os.getcwd()
files = os.listdir(cwd)
pdffiles = [f for f in files if f.endswith((".pdf"))]
pdffiles.sort(key=lambda f: int(re.sub('\D', '', f)))
for pdffile in pdffiles:
    print(pdffile)
    merger.append(pdffile)

merger.write("result.pdf")
merger.close()