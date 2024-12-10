from PyPDF2 import PdfReader, PdfWriter

# Read the PDF
reader = PdfReader("w1.pdf")
writer = PdfWriter()

for page in reader.pages:
    text = page.extract_text()  # Extract text
    print(text)
    updated_text = text.replace("INVOICE", "xdd")  # Edit text
    page.set_text(updated_text)  # Update text
    page_content = page  # Update page content (if supported)
    writer.add_page(page_content)

# Save the updated PDF
with open("updated2.pdf", "wb") as output_file:
    writer.write(output_file)