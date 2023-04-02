import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListView, QSizePolicy, QAbstractItemView
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QDir, QModelIndex


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")

        # 创建左侧列表
        self.list_view = QListView(self)
        self.list_view.setSelectionMode(QAbstractItemView.SingleSelection)
        self.list_view.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.list_view.clicked.connect(self.on_list_clicked)
        self.setCentralWidget(self.list_view)

        # 创建右侧图片显示区域
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.image_label)

        # 设置默认路径
        self.folder_path = QDir.homePath()

    def on_list_clicked(self, index: QModelIndex):
        # 获取所选图片路径
        image_path = self.list_model.filePath(index)
        if image_path:
            # 显示所选图片
            pixmap = QPixmap(image_path)
            pixmap_scaled = pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(pixmap_scaled)

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open Folder", self.folder_path)
        if folder_path:
            self.folder_path = folder_path
            self.setWindowTitle(f"Image Viewer - {folder_path}")

            # 获取所有图片路径并加载到左侧列表
            self.list_model = QDirModel()
            self.list_model.setFilter(QDir.Files | QDir.NoSymLinks | QDir.NoDotAndDotDot)
            self.list_model.setNameFilters(["*.jpg", "*.jpeg", "*.png", "*.bmp"])
            self.list_model.setNameFilterDisables(False)
            self.list_model.setRootPath(folder_path)
            self.list_view.setModel(self.list_model)
            self.list_view.setRootIndex(self.list_model.index(folder_path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.open_folder()
    sys.exit(app.exec_())