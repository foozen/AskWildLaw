import fitz  # PyMuPDF

pdf_path = "2024-01-24_SSSI-Regulation-Std_External_library_Version 3.5_A2E.pdf"
output_path = "sssi_regulation_standard.txt"

doc = fitz.open(pdf_path)
text = "\n".join(page.get_text() for page in doc)
doc.close()

with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"✅ Extracted and saved: {output_path}")
