import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QListView, QMainWindow, QSplitter, QLabel


class ImageViewer(QMainWindow):
    def __init__(self, path):
        super().__init__()

        # 设置主窗口标题
        self.setWindowTitle('Image Viewer')

        # 创建QFileSystemModel并设置目录
        model = QFileSystemModel()
        model.setRootPath(path)

        # 创建QListView并将其连接到QFileSystemModel
        list_view = QListView()
        list_view.setModel(model)
        list_view.setRootIndex(model.index(path))
        list_view.setEditTriggers(QListView.NoEditTriggers)  # 禁用编辑功能
        list_view.clicked.connect(self.on_clicked)

        # 创建QLabel以显示图像预览
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        # 创建一个分割窗口，将QListView和QLabel放在一起
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(list_view)
        splitter.addWidget(self.image_label)

        # 将分割窗口设置为主窗口的中央部件
        self.setCentralWidget(splitter)

        # 设置初始图像
        self.image_label.setPixmap(QPixmap(''))

    def on_clicked(self, index):
        # 获取所选文件的完整路径
        path = self.sender().model().filePath(index)

        # 如果选择的文件是图像，则在右边的标签中显示它
        if os.path.isfile(path) and path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            self.image_label.setPixmap(QPixmap(path))


if __name__ == '__main__':
    app = QApplication([])
    viewer = ImageViewer('.')
    viewer.show()
    app.exec_()



