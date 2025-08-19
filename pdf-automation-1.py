# pip install PyPDF2
# pip install fpdf2

import PyPDF2
from fpdf import FPDF

# opening & extracting text from local pdf file
# rb = read binary

pdfFileObj = open('meetingminutes.pdf', 'rb')
Reader = PyPDF2.PdfReader(pdfFileObj)

# print(len(Reader.pages))

activePage = Reader.pages[4]
print(activePage.extract_text())