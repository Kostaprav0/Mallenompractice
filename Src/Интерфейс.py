import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QComboBox
from PyQt5.QtGui import QPixmap
from PIL import Image

class ImageConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Конвертер изображений")
        self.title_label = QLabel("Утилита работает с изображениями, практикант: Громов Иван Владимирович")
        self.image_label = QLabel()
        self.image_label.setFixedSize(300, 300)
        self.select_button = QPushButton("Выбрать изображение")
        self.select_button.clicked.connect(self.select_image)
        self.format_combo = QComboBox()
        self.format_combo.addItems(["JPG", "PNG"])
        self.convert_button = QPushButton("Конвертировать")
        self.convert_button.clicked.connect(self.convert_image)
        self.convert_button.setEnabled(False)
        self.view_button = QPushButton("Просмотр изображения")
        self.view_button.clicked.connect(self.view_image)
        self.view_button.setEnabled(False)
        
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.title_label)
        hbox1.addStretch(1)
        hbox1.addWidget(self.select_button)
        hbox1.addWidget(self.format_combo)
        hbox1.addWidget(self.convert_button)
        
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.view_button)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.image_label)
        
        self.setLayout(vbox)
        self.selected_image_path = ""
    
    def select_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Файлы изображений (*.jpg *.jpeg *.png)")
        if filename:
            self.selected_image_path = filename
            self.load_image(filename)
            self.convert_button.setEnabled(True)
            self.view_button.setEnabled(True)
    
    def load_image(self, filename):
        try:
            pixmap = QPixmap(filename)
            pixmap = pixmap.scaled(self.image_label.width(), self.image_label.height())
            self.image_label.setPixmap(pixmap)
        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")
    
    def convert_image(self):
        if self.image_label.pixmap() is None:
            return
        
        output_format = self.format_combo.currentText().lower()
        filename, _ = QFileDialog.getSaveFileName(self, "Сохранить как", "", f"Файлы изображений (*.{output_format})")
        if filename:
            try:
                qim = self.image_label.pixmap().toImage()
                buffer = qim.constBits().asstring(qim.byteCount())
                pil_image = Image.frombuffer("RGBA", [qim.width(), qim.height()], buffer, "raw", "RGBA", 0, 1)
                pil_image.save(filename)
                print("Изображение успешно сконвертировано!")
            except Exception as e:
                print(f"Ошибка конвертации изображения: {e}")
    
    def view_image(self):
        if self.selected_image_path:
            image_viewer = ImageViewer(self.selected_image_path)
            image_viewer.show()

class ImageViewer(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("Просмотр изображения")
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(self.width() * 0.4, self.height())
        image_label.setPixmap(pixmap)
        image_label.setAlignment(QtCore.Qt.AlignRight)
        
        layout = QVBoxLayout()
        layout.addWidget(image_label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = ImageConverter()
    converter.show()
    sys.exit(app.exec_())