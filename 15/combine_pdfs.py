"""
Combines all the PDFs in the current working directory into  a single PDF.
"""
from os import listdir
from os.path import dirname
from PyPDF2 import PdfFileWriter, PdfFileReader


def wrapper():
    """
    Get all the PDF filenames.
    Loop through all the PDF files.
    Loop through all the pages (except the first) and add them.
    Save the resulting PDF to a file.
    """
    path = dirname(__file__) + "\\"
    pdf_files = []
    for filename in listdir(path):
        if filename.endswith(".pdf"):
            pdf_files.append(filename)
    pdf_files.sort()
    pdf_writer = PdfFileWriter()
    for filename in pdf_files:
        with open(path + filename, "rb") as pdf_file_obj:
            pdf_reader = PdfFileReader(pdf_file_obj)
            for page_num in range(1, pdf_reader.numPages):
                page_obj = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page_obj)
    with open(f"{path}allminutes.pdf", "wb") as pdf_output:
        pdf_writer.write(pdf_output)


if __name__ == "__main__":
    wrapper()
