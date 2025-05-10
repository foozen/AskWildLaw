import fitz  # PyMuPDF
import os
import re

# PDF input
pdf_path = "2024-01-24_SSSI-Regulation-Std_External_library_Version 3.5_A2E.pdf"
output_folder = "sections_from_pdf2"
os.makedirs(output_folder, exist_ok=True)

# Read the PDF
doc = fitz.open(pdf_path)
full_text = "\n".join(page.get_text() for page in doc)
doc.close()

# Split sections: match lines like "1 Protection of wild birds. E+W"
section_pattern = re.compile(r"\n(?=\d+\s+.+?\.\s+[A-Z]{1,3})")
split_sections = section_pattern.split(full_text)

# Save each section to file
for idx, section_text in enumerate(split_sections):
    lines = section_text.strip().splitlines()
    if not lines:
        continue
    header_line = lines[0].strip()
    match = re.match(r"(\d+)", header_line)
    section_number = match.group(1) if match else f"unknown_{idx}"
    filename = f"section_{section_number}.txt"
    filepath = os.path.join(output_folder, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(section_text.strip())
    print(f"✅ Saved: {filename}")

print(f"\n✅ All PDF sections saved to ./{output_folder}/")
