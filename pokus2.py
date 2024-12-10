import fitz  # import PyMuPDF

doc = fitz.open("PRG_LCA_invoice_.pdf")
page = doc[0]  # page number 0-based
disliked = "259,00"
better = "2 379,00"
hits = page.search_for(disliked)  # list of rectangles where to replace
text_color = (5 / 255, 3 / 255, 141 / 255)  # RGB for #05038d
text_color2 = (198 / 255, 0 / 255, 126 / 255)  # RGB for #c6007e

disliked2 = "259,00"
better2 = "2 379,00"
hits2 = page.search_for(disliked2)  # list of rectangles where to replace

for index,rect in enumerate(hits):
    if index < 6:
        # Enlarge the rectangle for bigger text
        adjusted_rect = rect + (0, 0, 6, 4.2)  # Fine-tuned for slightly larger text
        page.add_redact_annot(
            adjusted_rect,  # Use the enlarged rectangle
            better, 
            fontname="helv",  # Font name (Helvetica)
            fontsize=24,  # Suggested size (depends on rectangle size)
            text_color=text_color,  # Set text color
        )
    else: 
        adjusted_rect = rect + (0, 0, 5.5, 3.2)  # (0, -1.8, 7, 4.05) #  Fine-tuned for slightly larger text
        page.add_redact_annot(
            adjusted_rect,  # Use the enlarged rectangle
            better, 
            fontname="helv",  # Font name (Helvetica)
            fontsize=12,  # Suggested size (depends on rectangle size)
            text_color=text_color2,  # Set text color
        )

for index,rect in enumerate(hits2):
    adjusted_rect = rect + (0, 0, 5.5, 3.2)  # (0, -1.8, 7, 4.05) #  Fine-tuned for slightly larger text
    page.add_redact_annot(
        adjusted_rect,  # Use the enlarged rectangle
        better, 
        fontname="helv",  # Font name (Helvetica)
        fontsize=12,  # Suggested size (depends on rectangle size)
        text_color=text_color2,  # Set text color
    )

page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
doc.save("PRG_LCA_invoice_2.pdf", garbage=3, deflate=True)