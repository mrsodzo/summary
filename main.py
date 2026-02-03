import os
import os
from processors.pdf_processor import process_pdf

def safe_process_image(filepath):
    """
    Безопасная обработка изображения с обработкой ошибок.
    """
    try:
        from processors.image_processor import process_image
        return process_image(filepath)
    except Exception as e:
        error_msg = f"Ошибка при обработке изображения {filepath}: {e}"
        print(error_msg)
        return f"[Изображение: {os.path.basename(filepath)} - Обработка пропущена из-за ошибки: {str(e)}]"

def main():
    """
    Главная функция для сканирования директории и обработки файлов.
    """
    data_folder = 'data'
    summaries = []
    for filename in os.listdir(data_folder):
        filepath = os.path.join(data_folder, filename)
        if not os.path.isfile(filepath):
            continue

        print(f"Найден файл: {filepath}")
        summary = ""
        if filename.lower().endswith('.pdf'):
            summary = process_pdf(filepath)
        elif filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            summary = safe_process_image(filepath)
        
        if summary:
            summaries.append(summary)

    # Вывод общего саммари
    print("\n--- Общее саммари ---\n")
    for s in summaries:
        print(s)

if __name__ == "__main__":
    main()