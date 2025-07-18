import PyPDF2

def extract_text(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
    return text

def search_text(text, query):
    lines = text.splitlines()
    results = [(i+1, line) for i, line in enumerate(lines) if query.lower() in line.lower()]
    return results

if __name__ == "__main__":
    pdf_file = input("PDF file path: ").strip()
    text = extract_text(pdf_file)
    if not text:
        print("Failed to load PDF or PDF is empty.")
        exit(1)
    print("PDF loaded. You can now search.\n")

    while True:
        q = input("Search query (or 'exit'): ").strip()
        if q.lower() == "exit":
            break
        matches = search_text(text, q)
        if matches:
            print(f"Found {len(matches)} matching lines:")
            for lineno, line in matches:
                print(f"Line {lineno}: {line}")
        else:
            print("No matches found.")
        print()
