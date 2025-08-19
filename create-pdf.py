import PyPDF2
from fpdf import FPDF
from fpdf.enums import XPos, YPos

# Open an existing PDF
pdfFileObj = open('meetingminutes.pdf', 'rb')
Reader = PyPDF2.PdfReader(pdfFileObj)

# Create a simple PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)

# First line (centered, then move to next line)
pdf.cell(200, 20, text="Hello World", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

# Second line (default left aligned)
pdf.cell(0, 10, text="This is a line of text on the PDF")

# Save PDF
pdf.output("HelloWorld.pdf")
