import PyPDF2

def process_pdf(filepath):
    """
    Извлекает текст из PDF-файла.
    """
    summary = ""
    try:
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                summary += page.extract_text() or ""
        return f"Саммари для PDF {filepath}:\n{summary[:500]}...\n"
    except Exception as e:
        return f"Ошибка при обработке PDF {filepath}: {e}\n"