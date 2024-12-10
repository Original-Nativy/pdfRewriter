import fitz  # import PyMuPDF

# Open the PDF
doc = fitz.open("w1.pdf")
page = doc[0]  # page number 0-based

# Search for the text to replace
disliked = "9,99"
better = "99,99"
hits = page.search_for(disliked)  # list of rectangles where to replace

# Define text color (for new text)
text_color = (5 / 255, 3 / 255, 141 / 255)  # RGB for #05038d

for rect in hits:
    # Step 1: Draw a white rectangle to cover the old text
    page.draw_rect(rect, color=(1, 1, 1), fill=True)  # Covers the original text with a white rectangle

    # Step 2: Insert new text (better) at the same position
    page.insert_text(
        rect.tl,  # Top-left corner of the rectangle
        better,  # Replacement text
        fontsize=14,  # Font size
        color=text_color,  # Font color
        fontname="helv",  # Font (Helvetica)
    )

# Save the updated PDF
doc.save("replaced.pdf", garbage=3, deflate=True)
doc.close()

print("Text replaced and saved as 'replaced.pdf'!")