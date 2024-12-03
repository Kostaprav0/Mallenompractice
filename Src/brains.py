import os
from PyQt5.QtWidgets import QFileDialog

def convert_file(file_path, format):
    if not file_path:
        return False

    # Проверка формата файла
    file_format = os.path.splitext(file_path)[1].lower()
    if format == "png" and file_format in [".jpg", ".jpeg"]:
        # Конвертация JPG в PNG
        new_file_path = os.path.splitext(file_path)[0] + ".png"
        try:
            os.rename(file_path, new_file_path)
        except OSError as e:
            print(f"Ошибка переименования файла: {e}")
            return False
    elif format == "jpg" and file_format == ".png":
        # Конвертация PNG в JPG
        new_file_path = os.path.splitext(file_path)[0] + ".jpg"
        try:
            os.rename(file_path, new_file_path)
        except OSError as e:
            print(f"Ошибка переименования файла: {e}")
            return False
    else:
        return False

    # Выбор места для сохранения файла
    new_file_name, _ = QFileDialog.getSaveFileName(None, "Выберите место для сохранения файла", os.path.basename(new_file_path), "Image files (*.png *.jpg *.jpeg)")
    if not new_file_name:
        return False

    try:
        os.replace(new_file_path, new_file_name)
        return True
    except OSError as e:
        print(f"Ошибка сохранения файла: {e}")
        return False