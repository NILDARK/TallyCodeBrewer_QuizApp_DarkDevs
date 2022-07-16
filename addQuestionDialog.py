# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addQuestion.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import re


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 327)
        self.horizontalLayout_8 = QHBoxLayout(Form)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.questionEdit = QPlainTextEdit(self.widget_2)
        self.questionEdit.setObjectName(u"questionEdit")

        self.horizontalLayout.addWidget(self.questionEdit)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.scoreEdit = QLineEdit(self.widget_3)
        self.scoreEdit.setObjectName(u"scoreEdit")

        self.horizontalLayout_2.addWidget(self.scoreEdit)

        self.horizontalSpacer = QSpacerItem(137, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout = QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.opt1 = QRadioButton(self.widget_5)
        self.opt1.setObjectName(u"opt1")

        self.horizontalLayout_3.addWidget(self.opt1)

        self.horizontalSpacer_2 = QSpacerItem(191, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.toolButton = QToolButton(self.widget_5)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_3.addWidget(self.toolButton)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.opt_2 = QRadioButton(self.widget_6)
        self.opt_2.setObjectName(u"opt_2")

        self.horizontalLayout_4.addWidget(self.opt_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.toolButton_2 = QToolButton(self.widget_6)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_4.addWidget(self.toolButton_2)


        self.verticalLayout.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.opt_3 = QRadioButton(self.widget_7)
        self.opt_3.setObjectName(u"opt_3")

        self.horizontalLayout_5.addWidget(self.opt_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.toolButton_3 = QToolButton(self.widget_7)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_5.addWidget(self.toolButton_3)


        self.verticalLayout.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.opt_4 = QRadioButton(self.widget_8)
        self.opt_4.setObjectName(u"opt_4")

        self.horizontalLayout_6.addWidget(self.opt_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.toolButton_4 = QToolButton(self.widget_8)
        self.toolButton_4.setObjectName(u"toolButton_4")

        self.horizontalLayout_6.addWidget(self.toolButton_4)


        self.verticalLayout.addWidget(self.widget_8)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_6 = QSpacerItem(161, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.pushButton_2 = QPushButton(self.widget_9)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget_9)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_7.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.widget_9)


        self.horizontalLayout_8.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.questionEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Question", None))
        self.scoreEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Score (Default 1)", None))
        self.opt1.setText(QCoreApplication.translate("Form", u"Option 1", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.opt_2.setText(QCoreApplication.translate("Form", u"Option 2", None))
        self.toolButton_2.setText(QCoreApplication.translate("Form", u"...", None))
        self.opt_3.setText(QCoreApplication.translate("Form", u"Option 3", None))
        self.toolButton_3.setText(QCoreApplication.translate("Form", u"...", None))
        self.opt_4.setText(QCoreApplication.translate("Form", u"Option 4", None))
        self.toolButton_4.setText(QCoreApplication.translate("Form", u"...", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Back", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Done", None))
    # retranslateUi

    def validateQuestion(self, question):
        err = ""
        if(question == ""):
            err = "Question cannot be blank \n" 
        if(len(question) > 500):
            err += "Question cannot have more than 500 characters \n"
        if(err!=""):
            return [False,err]
        else:
            return [True,err] 

    def validateOption(self, option):
        err = ""
        if(option == ""):
            err = "Option cannot be blank \n" 
        if(len(option) > 100):
            err += "Option cannot have more than 100 characters \n"
        if(err!=""):
            return [False,err]
        else:
            return [True,err] 

    def validateScore(self, score):
        err = ""
        if(score < 0):
            err = "Score cannot be negative"
        x = re.search("[a-zA-Z]",score)
        if(x != None):
            err += "Score cannot contain alphabets"
        if(err!=""):
            return [False,err]
        else:
            return [True,err] 