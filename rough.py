# import rstr
# import re
# import datetime
# a = rstr.xeger(r'[A-Z]\d[A-Z]\d-[A-Z]\d[A-Z]\d/[A-Z,0-9]{6}')
# print(a)
# x = datetime.datetime(year=2022, month=7, day=15,hour=23,minute=14)
# print(x)
# print(datetime.datetime.now())
# print(datetime.datetime.now()+datetime.timedelta(minutes = 120))
# b = "9a123456789"
# x = re.search("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",b)
# # y = re.search("[0-9]",b)
# print(x)
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *

# import sys
# Z6H9-A1W2
# A1A8-W4B6
# C8A7-R6K8
# L5M3-T9J4
# I0V7-V4V9
# class Widget(QWidget):

#     def __init__(self, parent= None):
#         super(Widget, self).__init__()

#         btn_new = QPushButton("Append new label")
#         btn_new.clicked.connect(self.add_new_label)

#         #Container Widget
#         self.widget = QWidget()
#         #Layout of Container Widget
#         layout = QVBoxLayout(self)
#         for _ in range(20):
#             label = QLabel("test")
#             layout.addWidget(label)
#         self.widget.setLayout(layout)

#         #Scroll Area Properties
#         scroll = QScrollArea()
#         scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         scroll.setWidgetResizable(True)
#         scroll.setWidget(self.widget)

#         #Scroll Area Layer add
#         vLayout = QVBoxLayout(self)
#         vLayout.addWidget(btn_new)
#         vLayout.addWidget(scroll)
#         self.setLayout(vLayout)

#     def add_new_label(self):
#         wid = QWidget()
#         lay = QHBoxLayout(wid)
#         # wid.setLayout(lay)
#         questionLabel = QLabel()
#         questionLabel.setWordWrap(True)
#         horizonSpacer  = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
#         questionLabel.setPlainText("Question")
#         but = QToolButton()
#         wid.layout().addWidget(questionLabel)
#         wid.layout().addItem(horizonSpacer)
#         wid.layout().addWidget(but)
#         self.widget.layout().addWidget(wid)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     dialog = Widget()
#     dialog.show()

#     app.exec_()
import socket


def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False
print(is_connected())