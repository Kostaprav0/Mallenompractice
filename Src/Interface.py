import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QGroupBox, QComboBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from PIL import Image

class ImageProcessor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.current_image = None

    def initUI(self):
        self.setWindowTitle("Утилита работы с изображениями, практикант: Громов Иван Владимирович")
        self.setWindowIcon(QIcon('C:\\Users\\ig075\\Desktop\\Practis\\Q.png'))  # Путь к иконке
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
        self.convert_button.clicked.connect(self.convert_image)
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
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Image Files (*.png *.jpg *.bmp)")
        if file_name:
            self.current_image = Image.open(file_name)
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.info_label.setText(f"Загружено изображение: {file_name}")
            self.convert_button.setEnabled(True)

    def convert_image(self):
        if self.current_image:
            output_format = self.format_combo.currentText().lower()
            file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить как", "", f"{output_format.upper()} Files (*.{output_format})")
            if file_name:
                try:
                    self.current_image.save(file_name, format=output_format)
                    self.info_label.setText(f"Изображение сконвертировано и сохранено как: {file_name}")
                except Exception as e:
                    self.info_label.setText(f"Ошибка при конвертации: {str(e)}")
        else:
            self.info_label.setText("Сначала загрузите изображение")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageProcessor()
    ex.show()
    sys.exit(app.exec_())