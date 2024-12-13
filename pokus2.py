import pymupdf  # PyMuPDF

# Open the PDF document
doc = pymupdf.open("PRG_LCA.pdf")
page = doc[0]  # Access the first page

# Texts to replace and their respective replacements
disliked = "259,00"
# better = "2 379,00"
better = disliked

# text_color = (5 / 255, 3 / 255, 141 / 255)  # RGB for #05038d
text_color = (198 / 255, 0 / 255, 126 / 255)  # RGB for #c6007e


disliked2 = "4 237,00"
# better2 = "38 564,00"
better2 = disliked2
# text_color2 = (198 / 255, 0 / 255, 126 / 255)  # RGB for #c6007e
text_color2 = (5 / 255, 3 / 255, 141 / 255)  # RGB for #05038d


# Search for the disliked texts
hits = page.search_for(disliked)  # List of rectangles for disliked
hits2 = page.search_for(disliked2)

# Replace disliked text with better text (first case)
for index, rect in enumerate(hits):
    adjusted_rect = pymupdf.Rect(rect.x0, rect.y0, rect.x1, rect.y1)  # Ensure proper rect format
    if index < 6:
        start_point = pymupdf.Point(rect.x0, (rect.y0 + rect.y1 + 6.) / 2)
        # Replace with the first color
        page.insert_text(
            start_point,
            better,  # Replacement text
            fontsize=9,  # Font size
            fontname="helv",  # Font name
            color=text_color,  # Text color
        )
    else:
        start_point = pymupdf.Point(rect.x0, (rect.y0 + rect.y1 + 5.45) / 2)
        # Replace with the second color
        page.insert_text(
            start_point,
            better,
            fontsize=8.1,
            fontname="helv",
            color=text_color2,
        )

# Replace disliked2 text with better2 text (second case)
for rect in hits2:
    adjusted_rect = pymupdf.Rect(rect.x0, rect.y0, rect.x1, rect.y1)  # Ensure proper rect format
    start_point = pymupdf.Point(rect.x0, (rect.y0 + rect.y1 + 5.45) / 2)

    page.insert_text(
        start_point,
        better2,
        fontsize=8.1,
        fontname="helv",
        color=text_color2,
    )

# Save the document
output_file = "test_all.pdf"
doc.save(output_file, garbage=3, deflate=True)
doc.close()

print(f"Updated PDF saved as '{output_file}'")