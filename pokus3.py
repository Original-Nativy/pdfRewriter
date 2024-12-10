import pdf_redactor

# Define text redaction settings
options = pdf_redactor.RedactorOptions()

# Define replacement rules (e.g., "INVOICE" -> "xdd")
options.content_filters = [
    (r"INVOICE", "xdd"),
]

# Process the PDF
with open("w1.pdf", "rb") as input_file:
    with open("pokus3.pdf", "wb") as output_file:
        pdf_redactor.redactor(input_file, output_file, options)

print("PDF text replaced and saved as 'updated2.pdf'!")