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
import re,rstr
import smtplib
import datetime
import db
from quizAdminPage import Ui_MainWindow
from quizTakerPage import Ui_QuizPlatform
class MainSpace(QMainWindow):
    def closeEvent(self,event):
        res = db.logOut(self.usr,False)
        if(res):
            QMessageBox.information(self,"Info","Logged out Successfully.")
        event.accept()
    def __init__(self, username):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow(username)
        self.usr = username
        self.ui.setupUi(self)
class MainSpace2(QMainWindow):
    def __init__(self, name,session,pcode):
        QMainWindow.__init__(self)
        self.ui = Ui_QuizPlatform(name,session,pcode)
        self.ui.setupUi(self)
class Ui_loginSection(QWidget):
    
    def exit(self):
        self.loginSec.close()

    def switchQuizAdminLogin(self):
        self.loginCred1.clear()
        self.loginCred2.clear()
        self.signUpCred0.clear()
        self.signUpCred1.clear()
        self.signUpCred2.clear()
        self.signUpCred3.clear()
        self.signUpCred4.clear()
        self.takerNameEdit.clear()
        self.quizCodeEdit.clear()
        self.quizAdminLoginSection.setVisible(True)
        self.quizAdminRegisterSection.setVisible(False)
        self.quizTakerEntrySection.setVisible(False)

    def switchQuizAdminRegister(self):
        self.loginCred1.clear()
        self.loginCred2.clear()
        self.signUpCred0.clear()
        self.signUpCred1.clear()
        self.signUpCred2.clear()
        self.signUpCred3.clear()
        self.signUpCred4.clear()
        self.takerNameEdit.clear()
        self.quizCodeEdit.clear()
        self.quizAdminLoginSection.setVisible(False)
        self.quizAdminRegisterSection.setVisible(True)
        self.quizTakerEntrySection.setVisible(False)
        
    def switchQuizTakerEntry(self):
        self.loginCred1.clear()
        self.loginCred2.clear()
        self.signUpCred0.clear()
        self.signUpCred1.clear()
        self.signUpCred2.clear()
        self.signUpCred3.clear()
        self.signUpCred4.clear()
        self.takerNameEdit.clear()
        self.quizCodeEdit.clear()
        self.quizAdminLoginSection.setVisible(False)
        self.quizAdminRegisterSection.setVisible(False)
        self.quizTakerEntrySection.setVisible(True)
    def validateUsername(self,username):
        err = ""
        if(username==""):
            err = "Username Should not be blank.\n"
        if(len(username)<3):
            err+="Username Should be of minimum of length 3.\n"
        if(" " in username):
            err+="Username should not contain spaces.\n"
        x = re.search("[a-zA-Z]",username)
        if(x==None):
            err+="Username must contain atleast one alphabet.\n"
        if(err!=""):
            return [False,err]
        else:
            return [True,err]
    def getSignUpCreds(self):
        name = self.signUpCred0.text().strip()
        username = self.signUpCred1.text().strip()
        email = self.signUpCred2.text().strip()
        password = self.signUpCred3.text()
        cnfPassword = self.signUpCred4.text()
        err = ""
        if(name==""):
            self.signUpCred0.clear()
            err+="Name field must not blank.\n"
        usrVal = self.validateUsername(username)
        if(not usrVal[0]):
            self.signUpCred1.clear()
            err+=usrVal[1]
        passVal = self.validatePassword(password)
        if(not usrVal[0]):
            self.signUpCred3.clear()
            err+=passVal[1]
        if(email=="" or " " in email):
            self.signUpCred2.clear()
            err+="Invalid Format for Email.\n"
        if(err!=""):
            QMessageBox.critical(self,"Invalid Input Format Error",err)
            return
        if(cnfPassword!=password):
            QMessageBox.critical(self,"Password Mismatch","Entered Password does not match with above password.")
            self.signUpCred4.clear()
            return
        if(db.verifyUsername(username)[0]):
            QMessageBox.critical(self,"Error","Username already exists.")
            self.loginCred1.clear()
            self.loginCred2.clear()
            return
        res = self.validateEmail(email,name)
        if(res==True):
            if(db.addQuizAdmin([name,username,password,email])):
                QMessageBox.information(self,"Success",f"{name}, you are all set to create and manage Quizes. Login as Quiz Admin to get started.")
                self.switchQuizTakerEntry()
                return
            else:
                QMessageBox.critical(self,"Failure","Something went wrong. Failed to register.")
                self.signUpCred0.clear()
                self.signUpCred1.clear()
                self.signUpCred2.clear()
                self.signUpCred3.clear()
                self.signUpCred4.clear()
                return     
        elif(res==None):
            return
        else:
            QMessageBox.critical(self,"Verifcation Failure","Email Verification Failed. Try Again Later.")
            self.signUpCred0.clear()
            self.signUpCred1.clear()
            self.signUpCred2.clear()
            self.signUpCred3.clear()
            self.signUpCred4.clear()
            return
    def sendEmail(self,to_email,OTP,name):
        try: 
            smtp = smtplib.SMTP('smtp.gmail.com', 587) 
            smtp.starttls() 
            smtp.login("nildark2020@gmail.com","npewknmqghmnkett")
            message = f"Hello {name},\n    Your OTP for email verification is "+OTP+"\nFrom Team DarkDevs" 
            message = 'Subject: {}\n\n{}'.format("Verification Code", message)
            smtp.sendmail("nildark2020@gmail.com", to_email,message) 
            smtp.quit() 
            print ("Email sent successfully!") 
            return True
        except Exception as ex: 
            print(ex)
            return False
    def validateEmail(self,email,name):
        email_aval = db.checkEmailAvaibility(email)
        if(email_aval==None):
            QMessageBox.critical(self,"Connection Error","Something went wrong. Please check internet connection and try later.")
            return None
        elif(email_aval==False):
            QMessageBox.critical(self,"Database Error","Email Already in use. Try Using another email or login with username associated with it.")
            self.signUpCred2.clear()
            return None
        sent_vercode = rstr.xeger(r'[0-9]{6}')
        print(sent_vercode)
        if(self.sendEmail(email,sent_vercode,name)):
            recv_vercode, done = QInputDialog.getText(self, 'Email Verification', f'Enter Verification Code sent to your email: {email}')
            if(done):
                if(recv_vercode==sent_vercode):
                    QMessageBox.information(self,"Verification Success","Email Verified Successfully.")
                    return True
                else:
                    QMessageBox.critical(self,"Verification Failure","Verification code mismatch. Try again.")
                    return None
            else:
                return False
        else:
            return False
    def validatePassword(self,password):
        err = ""
        if(password==""):
            err = "Password Should not be blank.\n"
        if(len(password)<8):
            err+="Password Should be of minimum length 8.\n"
        if(" " in password):
            err+="Password should not contain spaces.\n"
        x = re.search("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",password)
        if(x==None):
            err+="Password should contain atleast one alphabet and one digit.\n"
        if(err!=""):
            return [False,err]
        else:
            return [True,err]
    def getLoginCreds(self):
        username = self.loginCred1.text().strip()
        password = self.loginCred2.text().strip()
        err = False
        err1,err2="",""
        if(username==""):
            err = True
            self.loginCred1.clear()
            err1 = "Username should not be blank."
        if(password==""):
            err = True
            self.loginCred2.clear()
            err2 = "Password should not be blank."
        if(err):        
            QMessageBox.critical(self,"Invalid Input Error",(err1+"\n"+err2).strip())
            return
        res = self.adminLogin(username,password)
        if(res):
            # res2 = db.login(username)
            # if(res2):
            #     QMessageBox.information(self,"Active Session Alert","Seems like you are already logged in on another device. Please try logging out there.")
            #     return
            self.main = MainSpace(username)
            self.exit()
            self.main.show()
        return
    def adminLogin(self,username,password):
        res = db.verifyUsername(username)
        if(res[0]):
            if(res[1]==password):
                return True
            else:
                QMessageBox.critical(self,"Error","Incorrect Password.")
                self.loginCred2.clear()    
                return False
        else:
            QMessageBox.critical(self,"Error","Username not found")
            self.loginCred1.clear()
            self.loginCred2.clear()
            return False
    def getTakerCreds(self):
        name = self.takerNameEdit.text().strip()
        quizcode = self.quizCodeEdit.text().strip()
        err = ""
        if(name==""):
            self.takerNameEdit.clear()
            err+="Name field must not blank.\n"
        if(quizcode==""):
            self.quizCodeEdit.clear()
            err+="Quiz Code field must not blank.\n"
        else:
            x = re.search("[A-Z]\d[A-Z]\d-[A-Z]\d[A-Z]\d",quizcode)
            y = re.search("[A-Z]\d[A-Z]\d-[A-Z]\d[A-Z]\d/[A-Z,0-9]{6}",quizcode)
            if(x==None and y==None):
                self.quizCodeEdit.clear()
                err+="Session Code is invalid"
        if(err!=""):
            QMessageBox.critical(self,"Error",err)
            return
        res = db.verifySessionCode(quizcode)
        if(res[0]==None):
            QMessageBox.critical(self,"Connection Error","Please Check Internet Connection and try later.")
            return
        elif(res[0]==False):
            QMessageBox.critical(self,"Database Error","Session Code is invalid.")
            return
        else:
            session = res[1]
            start = session["session_start"]
            end = session["session_end"]
            if(start!=None):
                curtime = datetime.datetime.now()
                print(curtime,end,curtime>end)
                if(curtime<start):
                    QMessageBox.information(self,"Info","Quiz session is not started yet. You may attempt from "+str(start)+" to "+str(end-datetime.timedelta(minutes = int(session["duration"]))))
                    return
                elif(curtime>end):
                    QMessageBox.information(self,"Info","Quiz session expired.")
                    return
                elif((curtime)>(end-datetime.timedelta(minutes = int(session["duration"])))):
                    QMessageBox.information(self,"Info","You can not attempt the quiz as you cannot complete the quiz by the session end.")
                    return
            res = db.addParticipant(session["session_code"],name,False,None)
            if(res==None):
                QMessageBox.critical(self,"Connection Error","Please Check Internet Connection and try later.")
                return
            
            self.main = MainSpace2(name,session,res)
            self.exit()
            self.main.show()
            # print(session)    
                    
                    
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
        self.loginCred2.returnPressed.connect(self.getLoginCreds)

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
        self.loginButton.clicked.connect(self.getLoginCreds)

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
        self.registerButton.clicked.connect(self.getSignUpCreds)

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
        self.quizCodeEdit.returnPressed.connect(self.getTakerCreds)
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
        self.switchQuizButton.clicked.connect(self.getTakerCreds)

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
        self.loginCred1.setToolTip(QCoreApplication.translate("loginSection", u"Enter Valid Username", None))
#endif // QT_CONFIG(tooltip)
        self.loginCred1.setPlaceholderText(QCoreApplication.translate("loginSection", u"Enter Username", None))
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
        self.signUpCred1.setToolTip(QCoreApplication.translate("loginSection", u"<html><head/><body><p>Username should satisfy:</p><p>1. Min Length 3</p><p>2. Contain atleast one alphabet</p><p>3. Contain no spaces</p></body></html>", None))
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
        self.quizCodeEdit.setPlaceholderText(QCoreApplication.translate("loginSection", u"Quiz Code (V1F0-B2P4)", None))
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
