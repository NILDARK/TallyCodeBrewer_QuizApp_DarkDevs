# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys

class Ui_loginSection(QWidget):
    
    def exit(self):
        self.loginSec.close()

    def switchQuizAdminLogin(self):
        self.quizAdminLoginSection.setVisible(True)
        self.quizAdminRegisterSection.setVisible(False)
        self.quizTakerEntrySection.setVisible(False)

    def switchQuizAdminRegister(self):
        self.quizAdminLoginSection.setVisible(False)
        self.quizAdminRegisterSection.setVisible(True)
        self.quizTakerEntrySection.setVisible(False)
        
    def switchQuizTakerEntry(self):
        self.quizAdminLoginSection.setVisible(False)
        self.quizAdminRegisterSection.setVisible(False)
        self.quizTakerEntrySection.setVisible(True)
        
    def setupUi(self, loginSection):
        if not loginSection.objectName():
            loginSection.setObjectName(u"loginSection")
        loginSection.setWindowModality(Qt.WindowModal)
        loginSection.resize(518, 640)
        loginSection.setMaximumSize(1280, 640)
        loginSection.setMinimumSize(1280, 640)
        loginSection.setWindowFlags(Qt.FramelessWindowHint)
        self.loginSec = loginSection
        self.horizontalLayout_17 = QHBoxLayout(loginSection)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.widget = QWidget(loginSection)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_16 = QHBoxLayout(self.widget)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.quizAdminLoginSection = QGroupBox(self.widget)
        self.quizAdminLoginSection.setObjectName(u"quizAdminLoginSection")
        self.horizontalLayout_4 = QHBoxLayout(self.quizAdminLoginSection)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.widget_2 = QWidget(self.quizAdminLoginSection)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loginCred1 = QLineEdit(self.widget_3)
        self.loginCred1.setObjectName(u"loginCred1")

        self.horizontalLayout.addWidget(self.loginCred1)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.loginCred2 = QLineEdit(self.widget_4)
        self.loginCred2.setObjectName(u"loginCred2")
        self.loginCred2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.loginCred2)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.cancelLoginButton = QPushButton(self.widget_5)
        self.cancelLoginButton.setObjectName(u"cancelLoginButton")
        self.cancelLoginButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"Images/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelLoginButton.setIcon(icon)
        self.cancelLoginButton.clicked.connect(self.switchQuizTakerEntry)

        self.horizontalLayout_3.addWidget(self.cancelLoginButton)

        self.switchSignUpButton = QPushButton(self.widget_5)
        self.switchSignUpButton.setObjectName(u"switchSignUpButton")
        self.switchSignUpButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"Images/sign-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.switchSignUpButton.setIcon(icon1)
        self.switchSignUpButton.clicked.connect(self.switchQuizAdminRegister)

        self.horizontalLayout_3.addWidget(self.switchSignUpButton)

        self.loginButton = QPushButton(self.widget_5)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"Images/login_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loginButton.setIcon(icon2)
        # self.loginButton.clicked.connect(self.switchQuizAdminLogin)

        self.horizontalLayout_3.addWidget(self.loginButton)


        self.verticalLayout.addWidget(self.widget_5)

        self.verticalSpacer_2 = QSpacerItem(20, 67, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addWidget(self.widget_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_16.addWidget(self.quizAdminLoginSection)

        self.quizAdminRegisterSection = QGroupBox(self.widget)
        self.quizAdminRegisterSection.setObjectName(u"quizAdminRegisterSection")
        self.quizAdminRegisterSection.setEnabled(True)
        self.horizontalLayout_11 = QHBoxLayout(self.quizAdminRegisterSection)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.widget_6 = QWidget(self.quizAdminRegisterSection)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_2 = QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.widget_11 = QWidget(self.widget_6)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.signUpCred0 = QLineEdit(self.widget_11)
        self.signUpCred0.setObjectName(u"signUpCred0")

        self.horizontalLayout_9.addWidget(self.signUpCred0)


        self.verticalLayout_2.addWidget(self.widget_11)

        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.signUpCred1 = QLineEdit(self.widget_7)
        self.signUpCred1.setObjectName(u"signUpCred1")

        self.horizontalLayout_5.addWidget(self.signUpCred1)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.signUpCred2 = QLineEdit(self.widget_8)
        self.signUpCred2.setObjectName(u"signUpCred2")
        self.signUpCred2.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.horizontalLayout_6.addWidget(self.signUpCred2)


        self.verticalLayout_2.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.signUpCred3 = QLineEdit(self.widget_9)
        self.signUpCred3.setObjectName(u"signUpCred3")
        self.signUpCred3.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.signUpCred3)


        self.verticalLayout_2.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.signUpCred4 = QLineEdit(self.widget_10)
        self.signUpCred4.setObjectName(u"signUpCred4")
        self.signUpCred4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.signUpCred4.setAcceptDrops(False)
        self.signUpCred4.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.signUpCred4.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.signUpCred4)


        self.verticalLayout_2.addWidget(self.widget_10)

        self.widget_12 = QWidget(self.widget_6)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_6 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.cancelRegisterButton = QPushButton(self.widget_12)
        self.cancelRegisterButton.setObjectName(u"cancelRegisterButton")
        self.cancelRegisterButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelRegisterButton.setIcon(icon)
        self.cancelRegisterButton.clicked.connect(self.switchQuizTakerEntry)

        self.horizontalLayout_10.addWidget(self.cancelRegisterButton)

        self.registerButton = QPushButton(self.widget_12)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"Images/register.png", QSize(), QIcon.Normal, QIcon.Off)
        self.registerButton.setIcon(icon3)

        self.horizontalLayout_10.addWidget(self.registerButton)


        self.verticalLayout_2.addWidget(self.widget_12)

        self.verticalSpacer_4 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.horizontalLayout_11.addWidget(self.widget_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_16.addWidget(self.quizAdminRegisterSection)

        self.quizTakerEntrySection = QGroupBox(self.widget)
        self.quizTakerEntrySection.setObjectName(u"quizTakerEntrySection")
        self.horizontalLayout_15 = QHBoxLayout(self.quizTakerEntrySection)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)

        self.widget_13 = QWidget(self.quizTakerEntrySection)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_3 = QVBoxLayout(self.widget_13)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_5 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.takerNameEdit = QLineEdit(self.widget_14)
        self.takerNameEdit.setObjectName(u"takerNameEdit")

        self.horizontalLayout_12.addWidget(self.takerNameEdit)


        self.verticalLayout_3.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_13)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.quizCodeEdit = QLineEdit(self.widget_15)
        self.quizCodeEdit.setObjectName(u"quizCodeEdit")
        self.quizCodeEdit.setClearButtonEnabled(False)

        self.horizontalLayout_13.addWidget(self.quizCodeEdit)


        self.verticalLayout_3.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.widget_13)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_9)

        self.exitButton = QPushButton(self.widget_16)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"Images/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon4)
        self.exitButton.clicked.connect(self.exit)

        self.horizontalLayout_14.addWidget(self.exitButton)

        self.swicthSignUpButton_2 = QPushButton(self.widget_16)
        self.swicthSignUpButton_2.setObjectName(u"swicthSignUpButton_2")
        self.swicthSignUpButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.swicthSignUpButton_2.setIcon(icon1)
        self.swicthSignUpButton_2.clicked.connect(self.switchQuizAdminRegister)

        self.horizontalLayout_14.addWidget(self.swicthSignUpButton_2)

        self.switchLoginButton = QPushButton(self.widget_16)
        self.switchLoginButton.setObjectName(u"switchLoginButton")
        self.switchLoginButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.switchLoginButton.setIcon(icon2)
        self.switchLoginButton.clicked.connect(self.switchQuizAdminLogin)

        self.horizontalLayout_14.addWidget(self.switchLoginButton)

        self.switchQuizButton = QPushButton(self.widget_16)
        self.switchQuizButton.setObjectName(u"switchQuizButton")
        self.switchQuizButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"Images/right_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.switchQuizButton.setIcon(icon5)

        self.horizontalLayout_14.addWidget(self.switchQuizButton)


        self.verticalLayout_3.addWidget(self.widget_16)

        self.verticalSpacer_6 = QSpacerItem(20, 67, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)


        self.horizontalLayout_15.addWidget(self.widget_13)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_8)


        self.horizontalLayout_16.addWidget(self.quizTakerEntrySection)


        self.horizontalLayout_17.addWidget(self.widget)

        self.quizAdminRegisterSection.setVisible(False)
        self.quizAdminLoginSection.setVisible(False)
        self.retranslateUi(loginSection)

        QMetaObject.connectSlotsByName(loginSection)
    # setupUi

    def retranslateUi(self, loginSection):
        loginSection.setWindowTitle(QCoreApplication.translate("loginSection", u"Dialog", None))
        self.quizAdminLoginSection.setTitle(QCoreApplication.translate("loginSection", u"Quiz Admin Login", None))
#if QT_CONFIG(tooltip)
        self.loginCred1.setToolTip(QCoreApplication.translate("loginSection", u"Enter Valid Email/Username", None))
#endif // QT_CONFIG(tooltip)
        self.loginCred1.setPlaceholderText(QCoreApplication.translate("loginSection", u"Enter Email/Username", None))
#if QT_CONFIG(tooltip)
        self.loginCred2.setToolTip(QCoreApplication.translate("loginSection", u"Enter Password", None))
#endif // QT_CONFIG(tooltip)
        self.loginCred2.setPlaceholderText(QCoreApplication.translate("loginSection", u"Enter Password", None))
#if QT_CONFIG(tooltip)
        self.cancelLoginButton.setToolTip(QCoreApplication.translate("loginSection", u"Cancel Login", None))
#endif // QT_CONFIG(tooltip)
        self.cancelLoginButton.setText(QCoreApplication.translate("loginSection", u"Cancel", None))
#if QT_CONFIG(tooltip)
        self.switchSignUpButton.setToolTip(QCoreApplication.translate("loginSection", u"Register Admin", None))
#endif // QT_CONFIG(tooltip)
        self.switchSignUpButton.setText(QCoreApplication.translate("loginSection", u"Sign Up", None))
#if QT_CONFIG(tooltip)
        self.loginButton.setToolTip(QCoreApplication.translate("loginSection", u"Login", None))
#endif // QT_CONFIG(tooltip)
        self.loginButton.setText(QCoreApplication.translate("loginSection", u"Login", None))
        self.quizAdminRegisterSection.setTitle(QCoreApplication.translate("loginSection", u"Quiz Admin Register", None))
#if QT_CONFIG(tooltip)
        self.signUpCred0.setToolTip(QCoreApplication.translate("loginSection", u"Only Alphabets and Spaces are allowed", None))
#endif // QT_CONFIG(tooltip)
        self.signUpCred0.setPlaceholderText(QCoreApplication.translate("loginSection", u"Name", None))
#if QT_CONFIG(tooltip)
        self.signUpCred1.setToolTip(QCoreApplication.translate("loginSection", u"<html><head/><body><p>Username should satisfy:</p><p>1. Min Length 3</p><p>2. Contain atleast one alphabet and one digit</p><p>3. Contain no spaces</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.signUpCred1.setPlaceholderText(QCoreApplication.translate("loginSection", u"Username", None))
#if QT_CONFIG(tooltip)
        self.signUpCred2.setToolTip(QCoreApplication.translate("loginSection", u"Enter Valid Email", None))
#endif // QT_CONFIG(tooltip)
        self.signUpCred2.setPlaceholderText(QCoreApplication.translate("loginSection", u"Email", None))
#if QT_CONFIG(tooltip)
        self.signUpCred3.setToolTip(QCoreApplication.translate("loginSection", u"<html><head/><body><p>Password should satisfy:</p><p>1. Minimum 8 Characters</p><p>2. Contain No Spaces</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.signUpCred3.setPlaceholderText(QCoreApplication.translate("loginSection", u"Password", None))
#if QT_CONFIG(tooltip)
        self.signUpCred4.setToolTip(QCoreApplication.translate("loginSection", u"<html><head/><body><p>Should Match Above Password</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.signUpCred4.setPlaceholderText(QCoreApplication.translate("loginSection", u"Confirm Password", None))
#if QT_CONFIG(tooltip)
        self.cancelRegisterButton.setToolTip(QCoreApplication.translate("loginSection", u"Cancel Register", None))
#endif // QT_CONFIG(tooltip)
        self.cancelRegisterButton.setText(QCoreApplication.translate("loginSection", u"Cancel", None))
#if QT_CONFIG(tooltip)
        self.registerButton.setToolTip(QCoreApplication.translate("loginSection", u"Register Admin", None))
#endif // QT_CONFIG(tooltip)
        self.registerButton.setText(QCoreApplication.translate("loginSection", u"Register", None))
        self.quizTakerEntrySection.setTitle(QCoreApplication.translate("loginSection", u"Quiz Taker ", None))
#if QT_CONFIG(tooltip)
        self.takerNameEdit.setToolTip(QCoreApplication.translate("loginSection", u"Enter Your Name", None))
#endif // QT_CONFIG(tooltip)
        self.takerNameEdit.setPlaceholderText(QCoreApplication.translate("loginSection", u"Your Name", None))
#if QT_CONFIG(tooltip)
        self.quizCodeEdit.setToolTip(QCoreApplication.translate("loginSection", u"Enter Valid Quiz Code", None))
#endif // QT_CONFIG(tooltip)
        self.quizCodeEdit.setPlaceholderText(QCoreApplication.translate("loginSection", u"Quiz Code (V1F0-B2P4-N2K0)", None))
#if QT_CONFIG(tooltip)
        self.exitButton.setToolTip(QCoreApplication.translate("loginSection", u"Exit Application", None))
#endif // QT_CONFIG(tooltip)
        self.exitButton.setText(QCoreApplication.translate("loginSection", u"Exit Application", None))
#if QT_CONFIG(tooltip)
        self.swicthSignUpButton_2.setToolTip(QCoreApplication.translate("loginSection", u"To Register for Quiz Admin", None))
#endif // QT_CONFIG(tooltip)
        self.swicthSignUpButton_2.setText(QCoreApplication.translate("loginSection", u"Register As Quiz Admin", None))
#if QT_CONFIG(tooltip)
        self.switchLoginButton.setToolTip(QCoreApplication.translate("loginSection", u"To Login/Register as Quiz Admin", None))
#endif // QT_CONFIG(tooltip)
        self.switchLoginButton.setText(QCoreApplication.translate("loginSection", u"Login As Quiz Admin", None))
#if QT_CONFIG(tooltip)
        self.switchQuizButton.setToolTip(QCoreApplication.translate("loginSection", u"Enter Quiz", None))
#endif // QT_CONFIG(tooltip)
        self.switchQuizButton.setText(QCoreApplication.translate("loginSection", u"Enter Quiz", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win = QWidget()
    ui = Ui_loginSection()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())
