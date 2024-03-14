import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("text_files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=filename.capitalize(), ln=1)

    # Extracting the content of the text file
    with open(filepath, "r") as file:
        content = file.read()
    # Add the text file content to the pdf file
    pdf.set_font(family="Times",size=13)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("pdf_file/output.pdf")

