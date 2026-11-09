from pathlib import Path

text = Path("wellbeing_guide.txt").read_text(encoding="utf-8")

def fixed_size_chunks(text, size=300, overlap=50):
    chunks, start = [], 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap
    return chunks

def section_chunks(text):
    parts = text.split("## ")
    return ["## " + p.strip() for p in parts if p.strip()]

for name, chunks in [("FIXED SIZE", fixed_size_chunks(text)),
                     ("BY SECTION", section_chunks(text))]:
    print(f"\n===== {name}: {len(chunks)} chunks =====")
    for i, c in enumerate(chunks, 1):
        print(f"\n--- chunk {i} ({len(c)} chars) ---\n{c}")
