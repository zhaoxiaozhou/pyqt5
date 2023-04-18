# import sys
# from PyQt5.QtCore import QPropertyAnimation, QSize
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
#
#
# class Demo(QWidget):
#     def __init__(self):
#         super(Demo, self).__init__()
#         self.resize(600, 600)
#
#         self.btn = QPushButton('Bigger', self)
#         self.btn.resize(100, 100)
#
#         self.animation = QPropertyAnimation(self.btn, b'size')
#         self.animation.setDuration(10000)
#         self.animation.setKeyValueAt(0.3, QSize(200, 200))
#         self.animation.setKeyValueAt(0.8, QSize(300, 300))
#         self.animation.setKeyValueAt(1, QSize(600, 600))
#         self.animation.start()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtCore import QPropertyAnimation, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.btn = QPushButton('Move', self)
        self.btn.resize(100, 100)

        self.animation = QPropertyAnimation(self.btn, b'pos')
        self.animation.setDuration(5000)
        self.animation.setStartValue(QPoint(0, 0))
        self.animation.setEndValue(QPoint(500, 500))
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())