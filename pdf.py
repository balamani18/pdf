import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
from PIL import Image
import img2pdf

class PDFProcessor:
    def _init_(self):
        pass

    def combine_pdfs(self, pdf_files, output_path):
        pdf_writer = PdfFileWriter()
        for pdf_file in pdf_files:
            pdf_reader = PdfFileReader(pdf_file)
            for page_num in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page)

        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

    def separate_pdf_pages(self, pdf_file, start_page, end_page, output_path):
        pdf_reader = PdfFileReader(pdf_file)
        pdf_writer = PdfFileWriter()

        for page_num in range(start_page - 1, end_page):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

    def remove_password(self, pdf_file, output_path):
        pdf_reader = PdfFileReader(pdf_file)
        pdf_writer = PdfFileWriter()
        pdf_writer.cloneDocumentFromReader(pdf_reader)

        # Remove password security if any
        pdf_writer.encrypt('', '')

        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

    def extract_text(self, pdf_file, txt_file):
        pdf_reader = PdfFileReader(pdf_file)
        text = ''
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

        with open(txt_file, 'w', encoding='utf-8') as text_file:
            text_file.write(text)

    def convert_images_to_pdf(self, image_files, output_pdf):
        with open(output_pdf, 'wb') as pdf_file:
            pdf_file.write(img2pdf.convert(image_files))

# Example usage:
if __name__ == '_main_':
    pdf_processor = PDFProcessor()

    # Combine PDFs
    pdf_processor.combine_pdfs(['file1.pdf', 'file2.pdf'], 'combined.pdf')

    # Separate PDF pages
    pdf_processor.separate_pdf_pages('original.pdf', 2, 4, 'separated.pdf')

    # Remove PDF password security
    pdf_processor.remove_password('secured.pdf', 'unsecured.pdf')

    # Extract text from PDF
    pdf_processor.extract_text('text.pdf', 'output.txt')

    # Convert images to PDF
    pdf_processor.convert_images_to_pdf(['image1.jpg', 'image2.png'], 'images.pdf')