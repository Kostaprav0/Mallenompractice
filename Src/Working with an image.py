import os
from PIL import Image

def convert_image(input_path, output_path, new_extension):
    image = Image.open(input_path)
    new_file_name = os.path.splitext(os.path.basename(input_path))[0] + '.' + new_extension
    new_file_path = os.path.join(output_path, new_file_name)
    image.save(new_file_path)

# Пример использования
input_image_path = 'input_folder/image.png'
output_folder = 'output_folder'

# Изменение PNG в JPG
convert_image(input_image_path, output_folder, 'jpg')

# Изменение JPG в PNG
convert_image(input_image_path, output_folder, 'png')

# Перемещение файла в другую папку
os.rename(input_image_path, os.path.join(output_folder, os.path.basename(input_image_path)))