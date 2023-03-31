import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('information', self)
        self.button.clicked.connect(self.show_messagebox)

    def show_messagebox(self):
        choice = QMessageBox.information(self, 'Tile', 'Content', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if choice == QMessageBox.Yes:
            self.button.setText('Changed')
        elif choice == QMessageBox.No:
            pass
        # QMessageBox.warning(self, 'Tile', 'content')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())