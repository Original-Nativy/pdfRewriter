import fitz  # import PyMuPDF

doc = fitz.open("eticket.pdf")
page = doc[0]  # page number 0-based
disliked = "364"
better   = "664"
hits = page.search_for("364")  # list of rectangles where to replace
text_color = (5 / 255, 3 / 255, 141 / 255)  # RGB for #05038d
text_color2 = (198 / 255, 0 / 255, 126 / 255)  # RGB for #c6007e

if len(hits) == 0:
    print("No text found!")
    exit()
if len(hits) > 1:
    print("Multiple texts found!")
    exit()
for index,rect in enumerate(hits):
    # Enlarge the rectangle for bigger text
    adjusted_rect = rect + (0, 0, 1, 4)  # Fine-tuned for slightly larger text
    page.add_redact_annot(
        adjusted_rect,  # Use the enlarged rectangle
        better, 
        fontname="helv",  # Font name (Helvetica)
        fontsize=24,  # Suggested size (depends on rectangle size)
    )


page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
doc.save("newRegio.pdf", garbage=3, deflate=True)
