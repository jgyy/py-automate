"""
read word documents
"""
from os.path import dirname
from docx import Document


def get_text(filename):
    """
    wrapper function
    """
    doc = Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n\n".join(full_text)


if __name__ == "__main__":
    PATH = dirname(__file__) + "\\"
    print(get_text(PATH + "demo.docx"))
