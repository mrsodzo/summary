def process_image(filepath):
    """
    Извлекает текст из файла изображения с помощью OCR или возвращает информацию о файле.
    """
    # Проверяем наличие необходимых библиотек
    try:
        from PIL import Image
        import pytesseract
        
        # Укажите путь к установленному Tesseract OCR, если он не в PATH
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Пытаемся открыть изображение
        img = Image.open(filepath)
        
        # Пытаемся выполнить OCR
        text = pytesseract.image_to_string(img, lang='rus+eng')
        return f"Саммари для изображения {filepath}:\n{text[:500].strip()}...\n"
    except ImportError as e:
        # Обработка случая, когда pytesseract не установлен
        if "pytesseract" in str(e):
            return f"Саммари для изображения {filepath}:\n[OCR skipped - pytesseract library not installed]\n"
        else:
            return f"Саммари для изображения {filepath}:\n[Import error: {str(e)}]\n"
    except FileNotFoundError:
        return f"Саммари для изображения {filepath}:\n[File not found]\n"
    except pytesseract.TesseractNotFoundError:
        return (f"Ошибка для {filepath}: Tesseract OCR не найден. "
                f"Убедитесь, что он установлен и путь '{pytesseract.pytesseract.tesseract_cmd}' корректен.\n")
    except Exception as e:
        return f"Неизвестная ошибка при обработке изображения {filepath}: {e}\n"
