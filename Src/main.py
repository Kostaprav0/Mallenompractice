import os
import sys
from PyQt5.QtWidgets import QApplication, QGroupBox, QMessageBox, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from brains import convert_file

class ImageProcessor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Утилита работы с изображениями, практикант: Громов Иван Владимирович")
        self.setWindowIcon(QIcon('C:\\Users\\ig075\\Desktop\\Practis\\Q.png'))
        self.setGeometry(100, 100, 800, 600)

        # Основной layout
        main_layout = QHBoxLayout()

        # Левая часть
        left_layout = QVBoxLayout()

        # Группа функциональных кнопок
        button_group = QGroupBox()
        button_layout = QVBoxLayout()

        self.load_button = QPushButton("Загрузить изображение")
        self.load_button.clicked.connect(self.load_image)
        button_layout.addWidget(self.load_button)

        # Добавляем выпадающий список для выбора формата
        self.format_combo = QComboBox()
        self.format_combo.addItems(["PNG", "JPG"])
        button_layout.addWidget(self.format_combo)

        # Кнопка конвертации
        self.convert_button = QPushButton("Конвертировать")
        self.convert_button.clicked.connect(self.convert_file)
        self.convert_button.setEnabled(False)
        button_layout.addWidget(self.convert_button)

        button_group.setLayout(button_layout)
        left_layout.addWidget(button_group)

        # Блок информации
        self.info_label = QLabel("Блок информации")
        self.info_label.setAlignment(Qt.AlignTop)
        self.info_label.setStyleSheet("border: 1px solid black;")
        left_layout.addWidget(self.info_label)

        main_layout.addLayout(left_layout)

        # Правая часть (область изображения)
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 1px solid black;")
        main_layout.addWidget(self.image_label, 2)

        self.setLayout(main_layout)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл для конвертации", "", "Image files (*.png *.jpg *.jpeg)")
        if file_path:
            # Загрузить изображение и отобразить его
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)
            self.convert_button.setEnabled(True)

    def convert_file(self):
        # Выбор файла для конвертации
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл для конвертации", "", "Image files (*.png *.jpg *.jpeg)")
        if file_path:
            # Выбор формата для конвертации
            format = self.format_combo.currentText().lower()
            if format:
                # Передаем данные в модуль brains.py
                result = convert_file(file_path, format)
                if result is not None:
                    # Выводим результат
                    if result:
                        QMessageBox.information(self, "Результат", "Файл успешно конвертирован")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    processor = ImageProcessor()
    processor.show()
    sys.exit(app.exec_())