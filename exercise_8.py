from PyPDF4 import PdfFileMerger
import os

merger = PdfFileMerger()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()