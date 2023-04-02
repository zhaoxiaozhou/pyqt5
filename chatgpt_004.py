import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidget, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 初始化界面
        self.init_ui()

        # 初始化列表
        self.init_list()

        # 初始化下拉框
        self.init_combobox()

    def init_ui(self):
        self.setWindowTitle("图片查看器")
        self.resize(800, 600)

        # 左边为列表，右边为图片预览
        self.list_widget = QListWidget()
        self.label = QLabel()

        hbox = QHBoxLayout()
        hbox.addWidget(self.list_widget)
        hbox.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(hbox)

        self.setCentralWidget(widget)

    def init_list(self):
        # 初始时不显示任何内容
        self.list_widget.clear()
        self.label.clear()

    def init_combobox(self):
        self.combobox = QComboBox()
        self.combobox.activated[str].connect(self.handle_combobox)
        self.toolbar = self.addToolBar("打开文件夹")
        self.toolbar.addWidget(self.combobox)
        self.addToolBarBreak()

    def handle_combobox(self, text):
        # 获取所选文件夹内所有图片的路径
        img_dir = os.path.abspath(text)
        img_paths = [os.path.join(img_dir, x) for x in os.listdir(img_dir) if x.endswith(".jpg") or x.endswith(".png")]

        # 显示到列表中
        self.list_widget.clear()
        self.list_widget.addItems(img_paths)

    def handle_list(self, item):
        # 获取所选图片路径
        img_path = item.text()

        # 显示到标签中
        pixmap = QPixmap(img_path)
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec_()