import io

from docx import Document
from PyPDF2 import PdfFileReader


def process_docx(doc: bytes) -> str:
    document = Document(io.BytesIO(doc))
    return '\n'.join([paragraph.text for paragraph in document.paragraphs])


def process_pdf(pdf: bytes) -> str:
    text = []
    # Use BytesIO to handle the byte content of the PDF
    with io.BytesIO(pdf) as file:
        reader = PdfFileReader(file)

        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text.append(page.extractText())

        return '\n'.join(text)
