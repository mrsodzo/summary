from PIL import Image
import pytesseract
import cv2
import numpy as np
import os

# Укажите путь к установленному Tesseract OCR, если он не в PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def process_image(filepath):
    """
    Извлекает текст, используя .traineddata файлы из корня проекта.
    """
    try:
        pil_img = Image.open(filepath).convert('L')
        cv_img = np.array(pil_img)

        processed_img = cv2.adaptiveThreshold(
            cv_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 11, 2
        )

        text = pytesseract.image_to_string(processed_img, lang='rus+eng')

        return f"Саммари для изображения {filepath}:\n{text[:500].strip()}...\n"
    except pytesseract.TesseractNotFoundError:
        return (f"Ошибка для {filepath}: Tesseract OCR не найден. "
                f"Убедитесь, что он установлен и путь '{pytesseract.pytesseract.tesseract_cmd}' корректен.\n")
    except Exception as e:
        return f"Неизвестная ошибка при обработке изображения {filepath}: {e}\n"
