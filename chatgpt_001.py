import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class ImageListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setViewMode(QListWidget.IconMode)
        # self.setIconSize(Qt.QSize(200, 200))
        self.setResizeMode(QListWidget.Adjust)

        self.addItem('image1.jpg')
        self.addItem('image2.jpg')
        self.addItem('image3.jpg')
        self.addItem('image4.jpg')
        self.addItem('image5.jpg')
        self.addItem('image6.jpg')
        self.addItem('image7.jpg')
        self.addItem('image8.jpg')


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.image_list_widget = ImageListWidget()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(400, 400)

        # Create layouts
        self.main_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()

        # Add widgets to layouts
        self.left_layout.addWidget(self.image_list_widget)
        self.right_layout.addWidget(self.image_label)

        # Set layout spacing and add to main layout
        self.left_layout.setSpacing(10)
        self.right_layout.setSpacing(10)
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.right_layout)
        self.main_layout.setSpacing(20)

        # Set main layout
        self.setLayout(self.main_layout)

        # Connect signals
        self.image_list_widget.itemClicked.connect(self.update_image)

    def update_image(self, item):
        image_path = f"images/{item.text()}"
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())
