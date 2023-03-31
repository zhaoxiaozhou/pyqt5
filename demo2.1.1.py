# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
#
#
# class Demo(QWidget):
#
#     def __init__(self):
#         super(Demo, self).__init__()
#         self.user_label = QLabel('Username:', self)
#         self.pwd_label = QLabel('Password:', self)
#
#         self.v_layout = QVBoxLayout()  # 1
#         self.v_layout.addWidget(self.user_label)  # 2
#         self.v_layout.addWidget(self.pwd_label)  # 3
#
#         self.setLayout(self.v_layout)  # 4
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout
#
#
# class Demo(QWidget):
#
#     def __init__(self):
#         super(Demo, self).__init__()
#         self.user_label = QLabel('Username:', self)
#         self.user_line = QLineEdit(self)                # 1
#
#         self.h_layout = QHBoxLayout()                   # 2
#         self.h_layout.addWidget(self.user_label)        # 3
#         self.h_layout.addWidget(self.user_line)         # 4
#
#         self.setLayout(self.h_layout)                   # 5
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
#     QHBoxLayout, QVBoxLayout
#
#
# class Demo(QWidget):
#
#     def __init__(self):
#         super(Demo, self).__init__()
#
#         self.user_label = QLabel('Username:', self)
#         self.pwd_label = QLabel('Password:', self)
#         self.user_line = QLineEdit(self)
#         self.pwd_line = QLineEdit(self)
#         self.login_button = QPushButton('Log in', self)
#         self.signin_button = QPushButton('Sign in', self)
#
#         self.label_v_layout = QVBoxLayout()                      # 1
#         self.line_v_layout = QVBoxLayout()                       # 2
#         self.button_h_layout = QHBoxLayout()                     # 3
#         self.label_line_h_layout = QHBoxLayout()                 # 4
#         self.all_v_layout = QVBoxLayout()                        # 5
#
#         self.label_v_layout.addWidget(self.user_label)           # 6
#         self.label_v_layout.addWidget(self.pwd_label)
#         self.line_v_layout.addWidget(self.user_line)
#         self.line_v_layout.addWidget(self.pwd_line)
#         self.button_h_layout.addWidget(self.login_button)
#         self.button_h_layout.addWidget(self.signin_button)
#         self.label_line_h_layout.addLayout(self.label_v_layout)  # 7
#         self.label_line_h_layout.addLayout(self.line_v_layout)
#         self.all_v_layout.addLayout(self.label_line_h_layout)
#         self.all_v_layout.addLayout(self.button_h_layout)
#
#         self.setLayout(self.all_v_layout)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())



# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
#     QHBoxLayout, QVBoxLayout, QFormLayout
#
#
# class Demo(QWidget):
#
#     def __init__(self):
#         super(Demo, self).__init__()
#
#         self.user_label = QLabel('Username:', self)
#         self.pwd_label = QLabel('Password:', self)
#         self.user_line = QLineEdit(self)
#         self.pwd_line = QLineEdit(self)
#         self.login_button = QPushButton('Log in', self)
#         self.signin_button = QPushButton('Sign in', self)
#
#         self.f_layout = QFormLayout()                           # 1
#         self.button_h_layout = QHBoxLayout()
#         self.all_v_layout = QVBoxLayout()
#
#         self.f_layout.addRow(self.user_label, self.user_line)   # 2
#         self.f_layout.addRow(self.pwd_label, self.pwd_line)
#         self.button_h_layout.addWidget(self.login_button)
#         self.button_h_layout.addWidget(self.signin_button)
#         self.all_v_layout.addLayout(self.f_layout)              # 3
#         self.all_v_layout.addLayout(self.button_h_layout)
#
#         self.setLayout(self.all_v_layout)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout


class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.grid_layout = QGridLayout()                                # 1
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)         # 2
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.h_layout.addWidget(self.login_button)
        self.h_layout.addWidget(self.signin_button)
        self.v_layout.addLayout(self.grid_layout)                       # 3
        self.v_layout.addLayout(self.h_layout)                          # 4

        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())