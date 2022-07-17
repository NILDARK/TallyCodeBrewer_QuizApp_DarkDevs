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
import sys,socket
import re,rstr
import smtplib
import datetime
import db
from dateutil import parser
import random,enum
from functools import partial
from creds import *
class MainSpace(QMainWindow):
    def isConnected(self):
        try:
            socket.create_connection(("1.1.1.1", 53))
            # QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
            return True
        except OSError:
            pass
        return False
    def closeEvent(self,event):
        if(self.isConnected()==False):
            QMessageBox.critical(self,"Connection Error","No Internet Connection. Unsuccessful logout. Exiting Application")
            event.accept()
            return
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

    def isConnected(self):
        try:
            socket.create_connection(("1.1.1.1", 53))
            # QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
            return True
        except OSError:
            pass
        return False
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
        if(self.isConnected()==False):
            QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
            return
        if(db.verifyUsername(username)[0]):
            QMessageBox.critical(self,"Error","Username already exists.")
            self.loginCred1.clear()
            self.loginCred2.clear()
            return
        if(self.isConnected()==False):
            QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
            return
        res = self.validateEmail(email,name)
        if(res==True):
            if(self.isConnected()==False):
                QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
                return
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
            smtp.login(sndemail,emailpass)
            message = f"Hello {name},\n    Your OTP for email verification is "+OTP+"\nFrom Team DarkDevs" 
            message = 'Subject: {}\n\n{}'.format("Verification Code", message)
            smtp.sendmail("sndemail", to_email,message) 
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
        if(self.isConnected()==False):
            QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
            return False
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
        if(self.isConnected()==False):
            QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
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
            if(self.isConnected()==False):
                QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
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
class Login(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_loginSection()
        self.ui.setupUi(self)
class Ui_MainWindow(QMainWindow):
    def isConnected(self):
        try:
            socket.create_connection(("1.1.1.1", 53))
            # QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
            return True
        except OSError:
            pass
        return False
    def __init__(self,username):
        QMainWindow.__init__(self)
        self.username = username
        self.qid = 0
        self.questions = {}
        self.sessions = {}
    def addQuestion(self):
        self.qid+=1
        wid = QWidget()
        wid.setObjectName(f"wid#{self.qid}")
        horizontalLayout_8 = QHBoxLayout(wid)
        horizontalLayout_8.setObjectName(f"horizontalLayout_8#{self.qid}")
        widget = QWidget(wid)
        widget.setObjectName(f"widget#{self.qid}")
        verticalLayout_2 = QVBoxLayout(widget)
        verticalLayout_2.setObjectName(f"verticalLayout_2#{self.qid}")
        widget_2 = QWidget(widget)
        widget_2.setObjectName(f"widget_2#{self.qid}")
        horizontalLayout = QHBoxLayout(widget_2)
        horizontalLayout.setObjectName(f"horizontalLayout#{self.qid}")
        questionEdit = QPlainTextEdit(widget_2)
        questionEdit.setObjectName(f"questionEdit#{self.qid}")
        horizontalLayout.addWidget(questionEdit)
        verticalLayout_2.addWidget(widget_2)
        widget_3 = QWidget(widget)
        widget_3.setObjectName(f"widget_3#{self.qid}")
        horizontalLayout_2 = QHBoxLayout(widget_3)
        horizontalLayout_2.setObjectName(f"horizontalLayout_2#{self.qid}")
        scoreEdit = QLineEdit(widget_3)
        scoreEdit.setObjectName(f"scoreEdit#{self.qid}")
        horizontalLayout_2.addWidget(scoreEdit)
        horizontalSpacer = QSpacerItem(137, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLayout_2.addItem(horizontalSpacer)
        verticalLayout_2.addWidget(widget_3)
        widget_4 = QWidget(widget)
        widget_4.setObjectName(f"widget_4#{self.qid}")
        verticalLayout = QVBoxLayout(widget_4)
        verticalLayout.setObjectName(f"verticalLayout#{self.qid}")
        widget_5 = QWidget(widget_4)
        widget_5.setObjectName(f"widget_5#{self.qid}")
        horizontalLayout_3 = QHBoxLayout(widget_5)
        horizontalLayout_3.setObjectName(f"horizontalLayout_3#{self.qid}")
        optionGroup = QButtonGroup(widget_4)
        optionGroup.setObjectName(f"optionGroup#{self.qid}")
        opt_1 = QRadioButton(widget_5)
        opt_1.setObjectName(f"opt_1#{self.qid}")
        optionGroup.addButton(opt_1,0)
        horizontalLayout_3.addWidget(opt_1)
        horizontalSpacer_2 = QSpacerItem(191, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLayout_3.addItem(horizontalSpacer_2)
        toolButton_1 = QToolButton(widget_5)
        toolButton_1.setObjectName(f"toolButton_1#{self.qid}")
        toolButton_1.clicked.connect(partial(self.editOption,toolButton_1.objectName()))
        horizontalLayout_3.addWidget(toolButton_1)
        verticalLayout.addWidget(widget_5)
        widget_6 = QWidget(widget_4)
        widget_6.setObjectName(f"widget_6#{self.qid}")
        horizontalLayout_4 = QHBoxLayout(widget_6)
        horizontalLayout_4.setObjectName(f"horizontalLayout_4#{self.qid}")
        opt_2 = QRadioButton(widget_6)
        opt_2.setObjectName(f"opt_2#{self.qid}")
        optionGroup.addButton(opt_2,1)
        horizontalLayout_4.addWidget(opt_2)
        horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLayout_4.addItem(horizontalSpacer_3)
        toolButton_2 = QToolButton(widget_6)
        toolButton_2.setObjectName(f"toolButton_2#{self.qid}")
        toolButton_2.clicked.connect(partial(self.editOption,toolButton_2.objectName()))
        horizontalLayout_4.addWidget(toolButton_2)
        verticalLayout.addWidget(widget_6)
        widget_7 = QWidget(widget_4)
        widget_7.setObjectName(f"widget_7#{self.qid}")
        horizontalLayout_5 = QHBoxLayout(widget_7)
        horizontalLayout_5.setObjectName(f"horizontalLayout_5#{self.qid}")
        opt_3 = QRadioButton(widget_7)
        opt_3.setObjectName(f"opt_3#{self.qid}")
        optionGroup.addButton(opt_3,2)
        horizontalLayout_5.addWidget(opt_3)
        horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLayout_5.addItem(horizontalSpacer_4)
        toolButton_3 = QToolButton(widget_7)
        toolButton_3.setObjectName(f"toolButton_3#{self.qid}")
        toolButton_3.clicked.connect(partial(self.editOption,toolButton_3.objectName()))
        horizontalLayout_5.addWidget(toolButton_3)
        verticalLayout.addWidget(widget_7)
        widget_8 = QWidget(widget_4)
        widget_8.setObjectName(f"widget_8#{self.qid}")
        horizontalLayout_6 = QHBoxLayout(widget_8)
        horizontalLayout_6.setObjectName(f"horizontalLayout_6#{self.qid}")
        opt_4 = QRadioButton(widget_8)
        opt_4.setObjectName(f"opt_4#{self.qid}")
        optionGroup.addButton(opt_4,3)
        horizontalLayout_6.addWidget(opt_4)
        horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLayout_6.addItem(horizontalSpacer_5)
        toolButton_4 = QToolButton(widget_8)
        toolButton_4.setObjectName(f"toolButton_4#{self.qid}")
        toolButton_4.clicked.connect(partial(self.editOption,toolButton_4.objectName()))
        horizontalLayout_6.addWidget(toolButton_4)
        verticalLayout.addWidget(widget_8)
        verticalLayout_2.addWidget(widget_4)
        widget_9 = QWidget(widget)
        widget_9.setObjectName(f"widget_9#{self.qid}")
        horizontalLayout_7 = QHBoxLayout(widget_9)
        horizontalLayout_7.setObjectName(f"horizontalLayout_7#{self.qid}")
        horizontalSpacer_6 = QSpacerItem(161, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        horizontalLayout_7.addItem(horizontalSpacer_6)
        widget_2.setEnabled(False)
        widget_3.setEnabled(False)
        widget_4.setEnabled(False)
        pushButton_2 = QPushButton(widget_9)
        pushButton_2.setObjectName(f"pushButton_2#{self.qid}")
        horizontalLayout_7.addWidget(pushButton_2)
        pushButton_3 = QPushButton(widget_9)
        pushButton_3.setObjectName(f"pushButton_3#{self.qid}")
        horizontalLayout_7.addWidget(pushButton_3)
        pushButton_4 = QPushButton(widget_9)
        pushButton_4.setObjectName(f"pushButton_4#{self.qid}")
        horizontalLayout_7.addWidget(pushButton_4)
        pushButton = QPushButton(widget_9)
        pushButton.setObjectName(f"pushButton#{self.qid}")
        horizontalLayout_7.addWidget(pushButton)
        verticalLayout_2.addWidget(widget_9)
        horizontalLayout_8.addWidget(widget)
        self.scrollAreaWidgetContents.layout().addWidget(wid)
        questionEdit.setPlaceholderText(u"Question (Max. 500 characters)")
        scoreEdit.setPlaceholderText(u"Score (1 by default)", )
        opt_1.setText(u"Option 1")
        toolButton_1.setText(u"...")
        opt_2.setText(u"Option 2")
        toolButton_2.setText(u"...")
        opt_3.setText(u"Option 3")
        toolButton_3.setText(u"...")
        opt_4.setText(u"Option 4")
        toolButton_4.setText(u"...")
        pushButton_2.setText(u"Delete")
        icon = QIcon()
        icon.addFile(u"Images/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton_2.setIcon(icon)
        pushButton_3.setText(u"Edit")
        icon1 = QIcon()
        icon1.addFile(u"Images/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton_3.setIcon(icon1)
        pushButton_4.setText(u"Cancel Edit")
        icon2 = QIcon()
        icon2.addFile(u"Images/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton_4.setIcon(icon2)
        pushButton.setText(u"Save Question")
        icon3 = QIcon()
        icon3.addFile(u"Images/done.png", QSize(), QIcon.Normal, QIcon.Off)
        pushButton.setIcon(icon3)
        doneObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton#{self.qid}")
        doneObj.setVisible(False)
        cancelEditObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton_4#{self.qid}")
        cancelEditObj.setVisible(False)
        pushButton.clicked.connect(partial(self.add,pushButton.objectName()))
        pushButton_2.clicked.connect(partial(self.deleteQue,pushButton.objectName()))
        pushButton_3.clicked.connect(partial(self.edit,pushButton.objectName()))
        pushButton_4.clicked.connect(partial(self.cancelEdit,pushButton.objectName()))
    def reset(self):
        layout = self.scrollAreaWidgetContents.layout()
        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().setParent(None)
    def add(self,objname):
        x = objname.find('#')
        id = int(objname[x+1:])
        err = ""
        queEdit = self.scrollAreaWidgetContents.findChild(QPlainTextEdit,f"questionEdit#{id}")
        scoreEdit = self.scrollAreaWidgetContents.findChild(QLineEdit,f"scoreEdit#{id}")
        que = queEdit.toPlainText().strip()
        score = scoreEdit.text().strip()
        opt1 = self.scrollAreaWidgetContents.findChild(QRadioButton,f"opt_1#{id}")
        opt2 = self.scrollAreaWidgetContents.findChild(QRadioButton,f"opt_2#{id}")
        opt3 = self.scrollAreaWidgetContents.findChild(QRadioButton,f"opt_3#{id}")
        opt4 = self.scrollAreaWidgetContents.findChild(QRadioButton,f"opt_4#{id}")
        options = {0:opt1.text().strip(),1:opt2.text().strip(),2:opt3.text().strip(),3:opt4.text().strip()}
        optionGroup = self.scrollAreaWidgetContents.findChild(QButtonGroup,f"optionGroup#{id}")
        answer = []
        resp = optionGroup.checkedId()
        if(resp==-1):
            err+="Must select correct option.\n"
        else:
            answer.append(resp)
        if(score==""):
            score = "1"
        elif(score.isnumeric()==False):
            err+="Score must be a number > 0.\n"
        if(que==""):
            err+="Question must not be blank."
        if(err!=""):
            QMessageBox.critical(self,"Error",err)
            return
        self.questions[id] = {"question":que,"options":options,"score":int(score),"answer":answer}
        wid_2 = self.scrollAreaWidgetContents.findChild(QWidget,f"widget_2#{id}")
        wid_3 = self.scrollAreaWidgetContents.findChild(QWidget,f"widget_3#{id}")
        wid_4 = self.scrollAreaWidgetContents.findChild(QWidget,f"widget_4#{id}")
        wid_2.setEnabled(False)
        wid_3.setEnabled(False)
        wid_4.setEnabled(False)
        doneObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton#{id}")
        doneObj.setVisible(False)
        cancelEditObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton_4#{id}")
        cancelEditObj.setVisible(False)
        editObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton_3#{id}")
        editObj.setVisible(True)
        deleteObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton_2#{id}")
        deleteObj.setVisible(True)
    def deleteQue(self,objname):
        x = objname.find('#')
        id = int(objname[x+1:])
        obj = self.scrollAreaWidgetContents.findChild(QWidget,f"wid#{id}")
        obj.setParent(None)
    def edit(self,objname):
        x = objname.find('#')
        id = int(objname[x+1:])
        wid_2 = self.scrollAreaWidgetContents.findChild(QWidget,f"widget_2#{id}")
        wid_3 = self.scrollAreaWidgetContents.findChild(QWidget,f"widget_3#{id}")
        wid_4 = self.scrollAreaWidgetContents.findChild(QWidget,f"widget_4#{id}")
        wid_2.setEnabled(True)
        wid_3.setEnabled(True)
        wid_4.setEnabled(True)
        doneObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton#{id}")
        doneObj.setVisible(True)
        cancelEditObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton_4#{id}")
        cancelEditObj.setVisible(True)
        editObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton_3#{id}")
        editObj.setVisible(False)
        deleteObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton_2#{id}")
        deleteObj.setVisible(False)
    def cancelEdit(self,objname):
        x = objname.find('#')
        id = int(objname[x+1:])
        wid_2 = self.scrollAreaWidgetContents.findChild(QWidget,f"widget_2#{id}")
        wid_3 = self.scrollAreaWidgetContents.findChild(QWidget,f"widget_3#{id}")
        wid_4 = self.scrollAreaWidgetContents.findChild(QWidget,f"widget_4#{id}")
        wid_2.setEnabled(False)
        wid_3.setEnabled(False)
        wid_4.setEnabled(False)
        doneObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton#{id}")
        doneObj.setVisible(False)
        cancelEditObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton_4#{id}")
        cancelEditObj.setVisible(False)
        editObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton_3#{id}")
        editObj.setVisible(True)
        deleteObj = self.scrollAreaWidgetContents.findChild(QPushButton,f"pushButton_2#{id}")
        deleteObj.setVisible(True)
    def editOption(self,objname):
        x = objname.find('_')
        id1 = (objname[x+1:])
        optno = int(objname[x+1])
        x = objname.find('#')
        id = int(objname[x+1:])
        obj = self.scrollAreaWidgetContents.findChild(QRadioButton,f"opt_{id1}")
        opt, done = QInputDialog.getText(self, 'Edit Option', 'Enter Option Text')
        if(done and opt.strip()!=""):
            obj.setText(opt)
        return
        
    def switchQuestionAdding(self):
        self.widget_3.setVisible(False)
        self.widget_9.setVisible(True)
    def switchQuizSettings(self):
        self.widget_3.setVisible(True)
        self.widget_9.setVisible(False)
    def timeConstrain(self):
        if(self.isTimeConstrained.isChecked()):
            self.widget_6.setVisible(True)
        else:
            self.widget_6.setVisible(False)
    def sessionStartChanged(self):
        duration = self.duration.value()
        try:
            self.sessionEnd.setMinimumDateTime(self.sessionStart.dateTime().addSecs(int(duration)*60))
        except:
            self.sessionEnd.setMinimumDateTime(self.sessionStart.dateTime().addSecs(10*60))
    def durationChanged(self):
        duration = self.duration.value()
        try:
            self.sessionEnd.setMinimumDateTime(self.sessionStart.dateTime().addSecs(int(duration)*60))
        except:
            self.sessionEnd.setMinimumDateTime(self.sessionStart.dateTime().addSecs(10*60))
        
    def publishQuiz(self):
        quizNickName = self.sessionNickName.text().strip()
        err = ""
        if(quizNickName==""):
            err+="Nick Name must not be blank.\n"
        duration = self.duration.value()
        
        if(self.isTimeConstrained.isChecked()):
            if(self.sessionStart.dateTime().addSecs(int(duration)*60)>self.sessionEnd.dateTime()):
                err+="Time constraint invalid.\n"
                self.sessionStart.setMinimumDateTime(QDateTime.currentDateTime())
                self.sessionEnd.setMinimumDateTime(self.sessionStart.dateTime().addSecs(10*60))
            start = self.sessionStart.dateTime().toString()
            end = self.sessionEnd.dateTime().toString()
            start = parser.parse(start)
            end = parser.parse(end)
            print(start,end)
        else:
            start=datetime.datetime.now()
            end = datetime.datetime(year=2100,day=1,month=1,hour=0,minute=0,second=0)
        if(len(self.questions)==0):
            err+="You have not added questions or may not have valid inputs. Try Adding or editing added questions.\n"
        if(err!=""):
            QMessageBox.critical(self,"Error",err)
            return
        if(duration==""):
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Warning)
            alert.setInformativeText("You have not set duration for quiz, by default it is set to 10 minutes. Do You want to continue?")
            alert.setWindowTitle("Error")
            alert.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            cancel_button = alert.button(QMessageBox.Cancel)
            cancel_button.setText("No")
            ok_button = alert.button(QMessageBox.Ok)
            ok_button.setText("Yes")
            res = alert.exec_()
            if(res==4194304):
                return
        if(self.isConnected()==False):
            QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
            return
        res = db.publishQuiz(self.questions,quizNickName,duration,self.username,start=start,end=end)
        if(res[0]):
            self.reload()
            QMessageBox.information(self,"Success",f"Quiz is Live Now. You may share the common code provided below:\n {res[1]}")
            self.resetAll()
            return
        else:
            QMessageBox.information(self,"Failure",f"Unable to publish quiz. Try again later.")
            return
    def logOut(self):
        self.mwin.close()
        self.mwin = Login()
        self.mwin.show()
    def resetAll(self):
        self.reset()
        self.sessionNickName.clear()
        self.duration.setValue(10)
        self.isTimeConstrained.setChecked(False)
    def sessionCodeRadioToggled(self):
        self.searchBar.clear()
        self.activeCheck.setEnabled(False)
        self.activeCheck.setChecked(False)
        self.searchBar.setPlaceholderText("Enter Quiz Code")

    def nickNameRadioToggled(self):
        self.searchBar.clear()
        self.activeCheck.setEnabled(True)
        self.searchBar.setPlaceholderText("Enter Quiz Name")
        
    def addAllSessionsToList(self):
        if(self.isConnected()==False):
            QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
            return
        self.allSessionDetails = db.getAllSessions(self.username)
        self.allSessionDetails = {k: v for k, v in sorted(self.allSessionDetails.items(), key=lambda item: item[1]["session_start"],reverse=True)}
        self.sessionList.clearContents()
        self.sessionList.setRowCount(0)
        self.sessionList.setRowCount(len(self.allSessionDetails))
        row = 0
        for session_code,session in self.allSessionDetails.items():
            item1 = QTableWidgetItem(session_code)
            item1.setTextAlignment(Qt.AlignCenter)
            item2 = QTableWidgetItem(session["session_nickname"])
            item2.setTextAlignment(Qt.AlignCenter)
            item3 = QTableWidgetItem(str(session["duration"]))
            item3.setTextAlignment(Qt.AlignCenter)
            self.sessionList.setItem(row, 0, item1)
            self.sessionList.setItem(row, 1, item2)
            self.sessionList.setItem(row, 2, item3)
            row+=1
    def showSessionDetails(self):
        self.sessionDisplayWidget.setVisible(True)
        cur = self.sessionList.currentRow()
        session_code = self.sessionList.item(cur,0).text().strip()
        duration = self.sessionList.item(cur,2).text().strip()
        nickName = self.sessionList.item(cur,1).text().strip()
        res = self.allSessionDetails[session_code]
        start = res["session_start"]
        end = res["session_end"]
        participants = res["participants"]
        participants = {k:v for k,v in sorted(participants.items(),key=lambda x:x[1]["score"],reverse=True)}
        total = res["total_score"]
        self.nickNameDisplay.setText(nickName)
        self.durationDisplay.setText(duration)
        self.quizCodeDisplay.setText(session_code)
        if(start==None or end==None):
            self.timeConstraintDisplay.setVisible(False)
        else:
            self.timeConstraintDisplay.setVisible(True)
            self.sessionStartDisplay.setDateTime(start)
            self.sessionEndDisplay.setDateTime(end)
        self.participantsList.clearContents()
        self.participantsList.setRowCount(0)
        self.participantsList.setRowCount(len(participants))
        row = 0
        for participant in participants.values():
            item1 = QTableWidgetItem(participant["participantName"])
            item1.setTextAlignment(Qt.AlignCenter)
            if(participant["completionStatus"]):
                x = "Successfully Attempted"
                score = str(participant["score"])+" out of "+str(total)
            else:
                x = "Not Attempted/Unsuccessfull Attempt"
                score = "Not Available"
            item2 = QTableWidgetItem(x)
            item2.setTextAlignment(Qt.AlignCenter)
            item3 = QTableWidgetItem(score)
            item3.setTextAlignment(Qt.AlignCenter)
            self.participantsList.setItem(row, 0, item1)
            self.participantsList.setItem(row, 1, item2)
            self.participantsList.setItem(row, 2, item3)
            row+=1
    def reload(self):
        if(self.isConnected()==False):
            QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
            return
        res = db.getAllSessions(self.username)
        if(res!=None):
            self.sessions = res
            self.addAllSessionsToList()
            self.searchBar.clear()
            self.activeCheck.setEnabled(False)
            self.activeCheck.setChecked(False)
            self.sessionCodeRadio.setChecked(True)
            self.sessionDisplayWidget.setVisible(False)
        else:
            QMessageBox.critical(self,"Connection Error","Unable to fetch database, please check internet connection and try again.")
            return
    def search(self):
        txt = self.searchBar.text().strip()
        if(self.sessionCodeRadio.isChecked()):
            x = re.search("[A-Z]\d[A-Z]\d-[A-Z]\d[A-Z]\d",txt)
            if(x==None):
                QMessageBox.critical(self,"Error","Invalid Code Format")
                self.searchBar.clear()
                return
            self.addSessionsToList(session_code=txt)
        else:
            if(txt==""):
                self.searchBar.clear()
                self.addAllSessionsToList()
                return
            self.addSessionsToList(nick_name=txt,active=self.activeCheck.isChecked())
    def getMatch(self, txt, dic,active=False):
        txt = txt.strip()
        txt = txt.upper()
        res = {}
        l = len(txt)
        for k,v in dic.items():
            word = v["session_nickname"]
            start = v["session_start"]
            end = v["session_end"]
            isactive = False
            if(active==False):
                isactive = True
            curtime = datetime.datetime.now()
            if(curtime<end):
                isactive = True
            if(txt == (word.upper())[:l] and isactive):
                res[k]=v
        res = {k: v for k, v in sorted(res.items(), key=lambda item: item[1]["session_start"],reverse=True)}
        return res
    def addSessionsToList(self,session_code=None,nick_name=None,active=False):
        if(session_code!=None):
            self.sessionDetails ={session_code:self.sessions[session_code]}
        else:
            self.sessionDetails = self.getMatch(nick_name,self.sessions,active)
        self.sessionList.clearContents()
        self.sessionList.setRowCount(0)
        self.sessionList.setRowCount(len(self.sessionDetails))
        row = 0
        for sessioncode,session in self.sessionDetails.items():
            item1 = QTableWidgetItem(sessioncode)
            item1.setTextAlignment(Qt.AlignCenter)
            item2 = QTableWidgetItem(session["session_nickname"])
            item2.setTextAlignment(Qt.AlignCenter)
            item3 = QTableWidgetItem(str(session["duration"]))
            item3.setTextAlignment(Qt.AlignCenter)
            self.sessionList.setItem(row, 0, item1)
            self.sessionList.setItem(row, 1, item2)
            self.sessionList.setItem(row, 2, item3)
            row+=1
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(768, 406)
        self.mwin = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.usernameLabel = QLabel(self.widget)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setText(f"Welcome, {self.username}")
        self.horizontalLayout.addWidget(self.usernameLabel)

        self.horizontalSpacer = QSpacerItem(604, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.logOutButton = QPushButton(self.widget)
        self.logOutButton.setObjectName(u"logOutButton")
        icon = QIcon()
        icon.addFile(u"Images/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logOutButton.setIcon(icon)
        self.logOutButton.clicked.connect(self.logOut)

        self.horizontalLayout.addWidget(self.logOutButton)


        self.verticalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tabWidget = QTabWidget(self.widget_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.manageQuizTab = QWidget()
        self.manageQuizTab.setObjectName(u"manageQuizTab")
        
        self.verticalLayout_7 = QVBoxLayout(self.manageQuizTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_13 = QWidget(self.manageQuizTab)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_7 = QSpacerItem(651, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.pushButton = QPushButton(self.widget_13)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.reload)
        self.horizontalLayout_10.addWidget(self.pushButton)


        self.verticalLayout_7.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.manageQuizTab)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.widget_11 = QWidget(self.widget_14)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_9 = QVBoxLayout(self.widget_11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_15 = QWidget(self.widget_11)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_5 = QVBoxLayout(self.widget_15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.widget_16)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_11.addWidget(self.label_4)

        self.sessionCodeRadio = QRadioButton(self.widget_16)
        self.sessionCodeRadio.setObjectName(u"sessionCodeRadio")

        self.horizontalLayout_11.addWidget(self.sessionCodeRadio)

        self.nickNameRadio = QRadioButton(self.widget_16)
        self.nickNameRadio.setObjectName(u"nickNameRadio")
        self.sessionCodeRadio.setChecked(True)
        self.horizontalLayout_11.addWidget(self.nickNameRadio)
        self.sessionCodeRadio.toggled.connect(self.sessionCodeRadioToggled)
        self.nickNameRadio.toggled.connect(self.nickNameRadioToggled)
        self.activeCheck = QCheckBox(self.widget_16)
        self.activeCheck.setObjectName(u"activeCheck")

        self.horizontalLayout_11.addWidget(self.activeCheck)
        if(self.isConnected()==False):
            QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
            self.mwin.close()
        self.sessions = db.getAllSessions(self.username,active=False)

        self.verticalLayout_5.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.widget_15)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.searchBar = QLineEdit(self.widget_17)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.searchBar.setInputMethodHints(Qt.ImhUppercaseOnly)

        self.horizontalLayout_12.addWidget(self.searchBar)


        self.verticalLayout_5.addWidget(self.widget_17)

        self.widget_19 = QWidget(self.widget_15)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.searchButton = QPushButton(self.widget_19)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setEnabled(True)
        self.searchButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"Images/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon1)
        self.searchButton.clicked.connect(self.search)
        self.horizontalLayout_14.addWidget(self.searchButton)

        self.horizontalSpacer_8 = QSpacerItem(214, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)


        self.verticalLayout_5.addWidget(self.widget_19)


        self.verticalLayout_9.addWidget(self.widget_15)

        # self.sessionList = QListWidget(self.widget_11)
        # self.sessionList.setObjectName(u"sessionList")
        self.activeCheck.setEnabled(False)

        self.sessionList = QTableWidget(self.widget_11)
        self.sessionList.setObjectName(u"sessionList")
        self.sessionList.setFrameShape(QFrame.NoFrame)
        self.sessionList.setFrameShadow(QFrame.Plain)
        self.sessionList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sessionList.verticalHeader().setVisible(False)
        self.sessionList.setColumnCount(3)
        self.sessionList.setRowCount(0)
        self.sessionList.setDragDropOverwriteMode(False)
        self.sessionList.itemClicked.connect(self.showSessionDetails)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        item.setBackground(QColor(135, 155, 161))
        item.setText("Quiz Code")
        self.sessionList.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        item.setBackground(QColor(135, 155, 161))
        item.setText("Quiz Nick Name")
        self.sessionList.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        item.setBackground(QColor(135, 155, 161))
        item.setText("Quiz Duration (in Minutes)")
        self.sessionList.setHorizontalHeaderItem(2, item)
        self.sessionList.horizontalHeader().setDefaultSectionSize(600)

        self.verticalLayout_9.addWidget(self.sessionList)
        self.addAllSessionsToList()

        self.horizontalLayout_18.addWidget(self.widget_11)

        self.sessionDisplayWidget = QWidget(self.widget_14)
        self.sessionDisplayWidget.setObjectName(u"sessionDisplayWidget")
        self.sessionDisplayWidget.setVisible(False)
        self.verticalLayout_6 = QVBoxLayout(self.sessionDisplayWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.sessionDetailsBox = QGroupBox(self.sessionDisplayWidget)
        self.sessionDetailsBox.setObjectName(u"sessionDetailsBox")
        self.verticalLayout_4 = QVBoxLayout(self.sessionDetailsBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_181 = QWidget(self.sessionDetailsBox)
        self.widget_181.setObjectName(u"widget_181")
        self.horizontalLayout_131 = QHBoxLayout(self.widget_181)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.quizCodeDisplay = QLineEdit(self.widget_181)
        self.quizCodeDisplay.setObjectName(u"quizCodeDisplay")
        self.quizCodeDisplay.setReadOnly(True)
        self.quizCodeDisplay.setPlaceholderText("Quiz Code")
        self.horizontalLayout_131.addWidget(self.quizCodeDisplay)

        self.horizontalSpacer_91 = QSpacerItem(189, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_131.addItem(self.horizontalSpacer_91)


        self.verticalLayout_4.addWidget(self.widget_181)
        self.widget_18 = QWidget(self.sessionDetailsBox)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.nickNameDisplay = QLineEdit(self.widget_18)
        self.nickNameDisplay.setObjectName(u"nickNameDisplay")
        self.nickNameDisplay.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.nickNameDisplay)

        self.horizontalSpacer_9 = QSpacerItem(189, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)


        self.verticalLayout_4.addWidget(self.widget_18)

        self.widget_20 = QWidget(self.sessionDetailsBox)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.durationDisplay = QLineEdit(self.widget_20)
        self.durationDisplay.setObjectName(u"durationDisplay")
        self.durationDisplay.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.durationDisplay)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_10)


        self.verticalLayout_4.addWidget(self.widget_20)

        self.timeConstraintDisplay = QWidget(self.sessionDetailsBox)
        self.timeConstraintDisplay.setObjectName(u"timeConstraintDisplay")
        self.horizontalLayout_16 = QHBoxLayout(self.timeConstraintDisplay)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_3 = QLabel(self.timeConstraintDisplay)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_16.addWidget(self.label_3)

        self.sessionStartDisplay = QDateTimeEdit(self.timeConstraintDisplay)
        self.sessionStartDisplay.setObjectName(u"sessionStartDisplay")
        self.sessionStartDisplay.setReadOnly(True)
        self.sessionStartDisplay.setCalendarPopup(True)

        self.horizontalLayout_16.addWidget(self.sessionStartDisplay)

        self.label_5 = QLabel(self.timeConstraintDisplay)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_16.addWidget(self.label_5)

        self.sessionEndDisplay = QDateTimeEdit(self.timeConstraintDisplay)
        self.sessionEndDisplay.setObjectName(u"sessionEndDisplay")
        self.sessionEndDisplay.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.sessionEndDisplay)


        self.verticalLayout_4.addWidget(self.timeConstraintDisplay)


        self.verticalLayout_6.addWidget(self.sessionDetailsBox)

        self.participantsBox = QGroupBox(self.sessionDisplayWidget)
        self.participantsBox.setObjectName(u"participantsBox")
        self.horizontalLayout_17 = QHBoxLayout(self.participantsBox)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.participantsList = QTableWidget(self.participantsBox)
        self.participantsList.setObjectName(u"participantsList")
        self.participantsList.setFrameShape(QFrame.NoFrame)
        self.participantsList.setFrameShadow(QFrame.Plain)
        self.participantsList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.participantsList.verticalHeader().setVisible(False)
        self.participantsList.setColumnCount(3)
        self.participantsList.setRowCount(0)
        self.participantsList.setDragDropOverwriteMode(False)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        item.setBackground(QColor(135, 155, 161))
        item.setText("Participant Name")
        self.participantsList.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        item.setBackground(QColor(135, 155, 161))
        item.setText("Completion Status")
        self.participantsList.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignCenter)
        item.setBackground(QColor(135, 155, 161))
        item.setText("Score")
        self.participantsList.setHorizontalHeaderItem(2, item)
        self.participantsList.horizontalHeader().setDefaultSectionSize(380)
        self.horizontalLayout_17.addWidget(self.participantsList)


        self.verticalLayout_6.addWidget(self.participantsBox)

        self.horizontalLayout_18.addWidget(self.sessionDisplayWidget)


        self.verticalLayout_7.addWidget(self.widget_14)
        
        self.tabWidget.addTab(self.manageQuizTab, "")
        self.createQuizTab = QWidget()
        self.createQuizTab.setObjectName(u"createQuizTab")
        self.horizontalLayout_8 = QHBoxLayout(self.createQuizTab)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_3 = QWidget(self.createQuizTab)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sessionNickName = QLineEdit(self.widget_4)
        self.sessionNickName.setObjectName(u"sessionNickName")

        self.horizontalLayout_2.addWidget(self.sessionNickName)

        self.horizontalSpacer_3 = QSpacerItem(189, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        # self.duration = QLineEdit(self.widget_7)
        self.xLabel = QLabel(self.widget_7)
        self.xLabel.setText("Duration in Minutes")
        self.horizontalLayout_5.addWidget(self.xLabel)
        
        self.duration = QSpinBox(self.widget_7)
        self.duration.setObjectName(u"duration")
        self.horizontalLayout_5.addWidget(self.duration)
        self.duration.setMinimum(1)
        self.duration.setMaximum(359940)
        self.duration.setValue(10)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.isTimeConstrained = QCheckBox(self.widget_5)
        self.isTimeConstrained.setObjectName(u"isTimeConstrained")

        self.horizontalLayout_4.addWidget(self.isTimeConstrained)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget_6)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.sessionStart = QDateTimeEdit(self.widget_6)
        self.sessionStart.setObjectName(u"sessionStart")
        self.sessionStart.setCalendarPopup(True)
        self.sessionStart.setCalendarWidget(QCalendarWidget())
        self.sessionStart.setDisplayFormat("dd-MM-yyyy hh:mm:ss")
        self.sessionStart.setMinimumDateTime(QDateTime.currentDateTime())
        self.sessionStart.dateTimeChanged.connect(self.sessionStartChanged)
        self.horizontalLayout_3.addWidget(self.sessionStart)

        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.sessionEnd = QDateTimeEdit(self.widget_6)
        self.sessionEnd.setObjectName(u"sessionEnd")
        self.sessionEnd.setCalendarPopup(True)
        self.sessionEnd.setCalendarWidget(QCalendarWidget())
        self.sessionEnd.setDisplayFormat("dd-MM-yyyy hh:mm:ss")
        self.sessionEnd.setMinimumDateTime(self.sessionStart.dateTime().addSecs(10*60))
        self.horizontalLayout_3.addWidget(self.sessionEnd)

        self.duration.valueChanged.connect(self.durationChanged)

        self.horizontalLayout_4.addWidget(self.widget_6)


        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_6.setVisible(False)
        self.isTimeConstrained.stateChanged.connect(self.timeConstrain)

        self.verticalSpacer = QSpacerItem(20, 132, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(264, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.addQuestionButton = QPushButton(self.widget_8)
        self.addQuestionButton.setObjectName(u"addQuestionButton")
        self.addQuestionButton.clicked.connect(self.switchQuestionAdding)
        icon10 = QIcon()
        icon10.addFile(u"Images/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addQuestionButton.setIcon(icon10)
        
        self.horizontalLayout_6.addWidget(self.addQuestionButton)

        self.publishButton = QPushButton(self.widget_8)
        self.publishButton.setObjectName(u"publishButton")
        self.publishButton.clicked.connect(self.publishQuiz)
        icon11 = QIcon()
        icon11.addFile(u"Images/publishing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.publishButton.setIcon(icon11)

        self.horizontalLayout_6.addWidget(self.publishButton)


        self.verticalLayout_2.addWidget(self.widget_8)


        self.horizontalLayout_8.addWidget(self.widget_3)

        self.widget_9 = QWidget(self.createQuizTab)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout = QVBoxLayout(self.widget_9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.questionListArea = QScrollArea(self.widget_9)
        self.questionListArea.setObjectName(u"questionListArea")
        self.questionListArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 296, 255))
        self.questionLayout = QVBoxLayout(self.widget_9)
        self.scrollAreaWidgetContents.setLayout(self.questionLayout)
        self.questionListArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.questionListArea)

        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_6 = QSpacerItem(103, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.backToQuizSettings = QPushButton(self.widget_10)
        self.backToQuizSettings.setObjectName(u"backToQuizSettings")
        self.backToQuizSettings.clicked.connect(self.switchQuizSettings)
        icon12 = QIcon()
        icon12.addFile(u"Images/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backToQuizSettings.setIcon(icon12)

        self.horizontalLayout_7.addWidget(self.backToQuizSettings)
        self.addQueButton = QPushButton(self.widget_10)
        self.addQueButton.setText("Add Question")
        self.addQueButton.clicked.connect(self.addQuestion)
        self.addQueButton.setObjectName(u"addQueButton")
        icon13 = QIcon()
        icon13.addFile(u"Images/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addQueButton.setIcon(icon13)

        self.horizontalLayout_7.addWidget(self.addQueButton)

        self.resetAllQuestions = QPushButton(self.widget_10)
        self.resetAllQuestions.setObjectName(u"resetAllQuestions")
        self.resetAllQuestions.clicked.connect(self.reset)
        icon14 = QIcon()
        icon14.addFile(u"Images/reset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resetAllQuestions.setIcon(icon14)

        self.horizontalLayout_7.addWidget(self.resetAllQuestions)

        self.doneAddingButton = QPushButton(self.widget_10)
        self.doneAddingButton.setObjectName(u"doneAddingButton")
        self.doneAddingButton.clicked.connect(self.switchQuizSettings)
        icon15 = QIcon()
        icon15.addFile(u"Images/done.png", QSize(), QIcon.Normal, QIcon.Off)
        self.doneAddingButton.setIcon(icon15)

        self.horizontalLayout_7.addWidget(self.doneAddingButton)


        self.verticalLayout.addWidget(self.widget_10)


        self.horizontalLayout_8.addWidget(self.widget_9)

        self.tabWidget.addTab(self.createQuizTab, "")

        self.horizontalLayout_9.addWidget(self.tabWidget)


        self.verticalLayout_3.addWidget(self.widget_2)
        self.widget_9.setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Quiz Manager", None))
        # self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Welcome, Username", None))
#if QT_CONFIG(tooltip)
        self.logOutButton.setToolTip(QCoreApplication.translate("MainWindow", u"Log Out of the Session", None))
#endif // QT_CONFIG(tooltip)
        self.logOutButton.setText(QCoreApplication.translate("MainWindow", u"LogOut", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Search by ", None))
        self.sessionCodeRadio.setText(QCoreApplication.translate("MainWindow", u"Quiz Code", None))
        self.nickNameRadio.setText(QCoreApplication.translate("MainWindow", u"Quiz Nick Name", None))
        self.activeCheck.setText(QCoreApplication.translate("MainWindow", u"Active Quiz", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Quiz Code", None))
#if QT_CONFIG(tooltip)
        self.searchButton.setToolTip(QCoreApplication.translate("MainWindow", u"Search Challan", None))
#endif // QT_CONFIG(tooltip)
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.sessionDetailsBox.setTitle(QCoreApplication.translate("MainWindow", u"Quiz Details", None))
        self.nickNameDisplay.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quiz Nick Name", None))
        self.durationDisplay.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Duration in Minutes", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.sessionStartDisplay.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yyyy hh:mm:ss", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.sessionEndDisplay.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yyyy hh:mm:ss", None))
        self.participantsBox.setTitle(QCoreApplication.translate("MainWindow", u"Participants", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manageQuizTab), QCoreApplication.translate("MainWindow", u"Manage Quiz", None))
        self.sessionNickName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quiz Nick Name", None))
        self.isTimeConstrained.setText(QCoreApplication.translate("MainWindow", u"Time Constrained", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.duration.setToolTip(QCoreApplication.translate("MainWindow", u"Duration in Minutes (10 by default)", None))
        self.addQuestionButton.setText(QCoreApplication.translate("MainWindow", u"Add Questions", None))
        self.publishButton.setText(QCoreApplication.translate("MainWindow", u"Publish Quiz", None))
        self.backToQuizSettings.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.resetAllQuestions.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.doneAddingButton.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.createQuizTab), QCoreApplication.translate("MainWindow", u"Create Quiz", None))

class TimerStatus(enum.Enum):
    init, counting, paused = 1, 2, 3
class Ui_QuizPlatform(QMainWindow):
    def isConnected(self):
        try:
            socket.create_connection(("1.1.1.1", 53))
            # QMessageBox.critical(self,"Connection Error","No Internet Connection. Please after reconnecting.")
            return True
        except OSError:
            pass
        return False
    def __init__(self,name,session,pcode):
        QMainWindow.__init__(self)
        self.participantName = name
        self.session = session
        self.response = {}
        self.score = None
        self.completionStatus = False
        self.pcode = pcode
        self.questions = self.session["questions"]
        self.queDisplayArr = list(self.questions.keys())
        random.shuffle(self.queDisplayArr)
        self.curQues = 0
        self.totalQues = len(self.questions)
        self.curOptionBasket = {}
        self.instructionsButClicked = False
        self.forceFullSubmit = False
    def showQuestion(self):
        question = self.questions[self.queDisplayArr[self.curQues]]
        self.questionEdit.setPlainText(question["question"])
        optionsList =list(question["options"].keys())
        random.shuffle(optionsList)
        self.opt_1.setText(question["options"][optionsList[0]]) 
        self.opt_2.setText(question["options"][optionsList[1]]) 
        self.opt_3.setText(question["options"][optionsList[2]]) 
        self.opt_4.setText(question["options"][optionsList[3]])
        self.curOptionBasket[0]= optionsList[0]
        self.curOptionBasket[1]= optionsList[1]
        self.curOptionBasket[2]= optionsList[2]
        self.curOptionBasket[3]= optionsList[3]
        try:
            resp = self.response[self.queDisplayArr[self.curQues]]
            for i in range(4):
                if(resp==self.curOptionBasket[i]):
                    if(i==0):
                        self.opt_1.setChecked(True)
                    elif(i==1):
                        self.opt_2.setChecked(True)
                    elif(i==2):
                        self.opt_3.setChecked(True)
                    elif(i==3):
                        self.opt_4.setChecked(True)
                    break
        except:
            pass
        self.maxScoreLabel.setText(f"Max Score: {int(question['score'])}")
        self.questionCountLabel.setText(f"{self.curQues+1}/{self.totalQues}")
    def nextQue(self):
        resp = self.optionsGroup.checkedId()
        if(resp!=-1 and resp!=4):
            self.response[self.queDisplayArr[self.curQues]]=self.curOptionBasket[resp]
            self.opt_5.setChecked(True)

        self.curQues = (self.curQues+1)%self.totalQues
        self.showQuestion()
    def prevQue(self):
        resp = self.optionsGroup.checkedId()
        if(resp!=-1 and resp!=4):
            self.response[self.queDisplayArr[self.curQues]]=self.curOptionBasket[resp]
            self.opt_5.setChecked(True)
        self.curQues = self.curQues-1
        if(self.curQues<0):
            self.curQues=self.totalQues-1
        self.showQuestion()
    def submitQuiz(self,fsub=False):
        if(fsub):
            self.forceFullSubmit = True
        self._left_seconds = 0
        self.score = self.evaluateQuiz()
        self.completionStatus = True
        if(self.isConnected()==False):
            QMessageBox.critical(self,"Connection Error","No Internet Connection. Unable to submit responses. Exiting Application")
            sys.exit(0)
            return
        res = db.updateParticipant(self.session["session_code"],self.pcode,self.completionStatus,self.score[0])
        if(res):
            QMessageBox.information(self,"Info",f"Hey, {self.participantName}, You scored {self.score[0]} out of {self.score[1]}. \n You attempted {self.score[2]} questions out of {self.totalQues}.")
            self.exit()
            return
        else:
            QMessageBox.critical(self,"Error","Sorry, didn't able to submit your responses, may be due to internet connectivity issue.")
            self.exit()
            return
        
    def evaluateQuiz(self):
        totalScore = 0
        score = 0
        attempted = 0
        for i in range(self.totalQues):
            question = self.questions[self.queDisplayArr[i]]
            totalScore+=int(question["score"])
        for q,resp in self.response.items():
            question = self.questions[q]
            cor = question["answer"][0]
            if(resp==cor):
                score+=int(question["score"])
            if(resp!=-1):
                attempted+=1
        return [score,totalScore,attempted]
    def resetSelection(self):
        resp = self.optionsGroup.checkedId()
        self.response[self.queDisplayArr[self.curQues]]=-1
        self.opt_5.setChecked(True)
    def _countdown_and_show(self):
        if self._left_seconds > 0:
            self._left_seconds -= 1
            self.showTime()
        else:
            self.timer.stop()
            self.showTime()
            self._status = TimerStatus.init
            self._left_seconds = self.session["duration"] * 60
            if(self.forceFullSubmit==False):
                QMessageBox.information(self,"Info","Out of Time. Submitting your responses.")
                self.submitQuiz()
            
    def _start_event(self):
        if (self._status == TimerStatus.init or self._status == TimerStatus.paused) and self._left_seconds > 0:
            self._left_seconds -= 1
            self._status = TimerStatus.counting
            self.showTime()
            self.timer.start(1000)
        elif self._status == TimerStatus.counting:
            self.timer.stop()
            self._status = TimerStatus.paused
    def _reset_event(self):
        self._status = TimerStatus.init
        self._left_seconds = self.session["duration"] * 60
        self.timer.stop()
        self.showTime()
    def showTime(self):
        total_seconds = min(self._left_seconds, 359940)
        hours = total_seconds // 3600
        total_seconds = total_seconds - (hours * 3600)
        minutes = total_seconds // 60
        seconds = total_seconds - (minutes * 60)
        if(total_seconds<0.1*self.session["duration"]*60):
            self.timerLabel.setStyleSheet("color:red;")
        else:
            self.timerLabel.setStyleSheet("color:#000080;")
            
        self.timerLabel.setText("{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds)))
        self.timerLabel.setAlignment(Qt.AlignHCenter)
    def exit(self):
        self.mwin.close()
        self.mwin = Login()
        self.mwin.show()
    def confToStart(self):
        x = self.startConf.text()
        if(x=="start"):
            self.startQuizButton.setEnabled(True)
        else:
            self.startQuizButton.setEnabled(False)
    def startQuiz(self):
        curtime = datetime.datetime.now()
        if(self.session["session_end"]!=None and (curtime)>(self.session["session_end"]-datetime.timedelta(minutes = int(self.session["duration"])))):
            QMessageBox.information(self,"Info","You can not attempt the quiz as you cannot complete the quiz by the session end.")
            self.exit()
            return
        self.timerWidget.setVisible(True)
        self.quizWidget.setVisible(True)
        self.instructionsWidget.setVisible(False)
        self._start_event()
        self.showQuestion()
        self.submitQuizButton.setVisible(True)
        self.exitSessionButton.setVisible(False)
        self.instructionsIcon.setVisible(True)
    def showInstructions(self):
        self.quizStartWidget.setVisible(False)
        if(self.instructionsButClicked):
            self.instructionsWidget.setVisible(False)
            self.instructionsButClicked=False
            icon = QIcon()
            icon.addFile(u"Images/info_icon.png", QSize(), QIcon.Normal, QIcon.Off)
            self.instructionsIcon.setIcon(icon)
        else:
            self.instructionsWidget.setVisible(True)
            self.instructionsButClicked=True
            icon = QIcon()
            icon.addFile(u"Images/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
            self.instructionsIcon.setIcon(icon)    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 481)
        self.mwin = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_15 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.participantNameLabel = QLabel(self.widget_2)
        self.participantNameLabel.setObjectName(u"participantNameLabel")
        self.participantNameLabel.setText(f"Welcome, {self.participantName}")
        self.horizontalLayout_3.addWidget(self.participantNameLabel)

        self.horizontalSpacer = QSpacerItem(227, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.timerWidget = QWidget(self.widget_2)
        self.timerWidget.setObjectName(u"timerWidget")
        self.timerWidget.setVisible(False)
        self.horizontalLayout_2 = QHBoxLayout(self.timerWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.timerLabel = QLabel(self.timerWidget)
        self.timerLabel.setObjectName(u"timerLabel")
        self.timerLabel.setStyleSheet("color:#000080;")
        self.timerLabel.setFont(QFont("Arial",38))

        self.horizontalLayout_2.addWidget(self.timerLabel)
        self.extraLabel = QLabel(self.timerWidget)
        self.extraLabel.setText("Remaining Time To Finish")
        self.horizontalLayout_2.addWidget(self.extraLabel)

        self.horizontalLayout_3.addWidget(self.timerWidget)

        self.horizontalSpacer_2 = QSpacerItem(227, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout = QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exitSessionButton = QPushButton(self.widget_5)
        self.exitSessionButton.setObjectName(u"exitSessionButton")
        self.exitSessionButton.clicked.connect(self.exit)
        
        self.horizontalLayout.addWidget(self.exitSessionButton)

        self.submitQuizButton = QPushButton(self.widget_5)
        self.submitQuizButton.setObjectName(u"submitQuizButton")
        self.submitQuizButton.setVisible(False)
        self.submitQuizButton.clicked.connect(partial(self.submitQuiz,True))
        self.horizontalLayout.addWidget(self.submitQuizButton)

        self.instructionsIcon = QPushButton(self.widget_5)
        self.instructionsIcon.setObjectName(u"instructionsIcon")
        self.instructionsIcon.setVisible(False)
        self.instructionsIcon.clicked.connect(self.showInstructions)
        icon = QIcon()
        icon.addFile(u"Images/info_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.instructionsIcon.setIcon(icon)
        self.horizontalLayout.addWidget(self.instructionsIcon)


        self.horizontalLayout_3.addWidget(self.widget_5)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.instructionsWidget = QWidget(self.widget_6)
        self.instructionsWidget.setObjectName(u"instructionsWidget")
        self.verticalLayout = QVBoxLayout(self.instructionsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_9 = QWidget(self.instructionsWidget)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.textBrowser = QTextBrowser(self.widget_9)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_5.addWidget(self.textBrowser)


        self.verticalLayout.addWidget(self.widget_9)

        self.quizStartWidget = QWidget(self.instructionsWidget)
        self.quizStartWidget.setObjectName(u"quizStartWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.quizStartWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(137, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.startConf = QLineEdit(self.quizStartWidget)
        self.startConf.returnPressed.connect(self.startQuiz)
        self.startConf.setObjectName(u"startConf")
        self.startConf.textChanged.connect(self.confToStart)
        self.horizontalLayout_4.addWidget(self.startConf)

        self.startQuizButton = QPushButton(self.quizStartWidget)
        self.startQuizButton.setObjectName(u"startQuizButton")
        self.startQuizButton.setEnabled(False)
        self.startQuizButton.clicked.connect(self.startQuiz)
        self.horizontalLayout_4.addWidget(self.startQuizButton)


        self.verticalLayout.addWidget(self.quizStartWidget)


        self.horizontalLayout_14.addWidget(self.instructionsWidget)

        self.quizWidget = QWidget(self.widget_6)
        self.quizWidget.setObjectName(u"quizWidget")
        self.quizWidget.setVisible(False)
        self.verticalLayout_4 = QVBoxLayout(self.quizWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.questionWidget = QWidget(self.quizWidget)
        self.questionWidget.setObjectName(u"questionWidget")
        self.verticalLayout_2 = QVBoxLayout(self.questionWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_14 = QWidget(self.questionWidget)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.questionEdit = QPlainTextEdit(self.widget_14)
        self.questionEdit.setObjectName(u"questionEdit")
        self.questionEdit.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.questionEdit)


        self.verticalLayout_2.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.questionWidget)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.maxScoreLabel = QLabel(self.widget_15)
        self.maxScoreLabel.setObjectName(u"maxScoreLabel")

        self.horizontalLayout_9.addWidget(self.maxScoreLabel)

        self.horizontalSpacer_6 = QSpacerItem(137, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.resetButton = QPushButton(self.widget_15)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.clicked.connect(self.resetSelection)
        self.horizontalLayout_9.addWidget(self.resetButton)


        self.verticalLayout_2.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.questionWidget)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_3 = QVBoxLayout(self.widget_16)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.optionsGroup = QButtonGroup(self.widget_16)
        self.opt_1 = QRadioButton(self.widget_17)
        self.opt_1.setObjectName(u"opt_1")
        self.optionsGroup.addButton(self.opt_1,0)
        self.horizontalLayout_10.addWidget(self.opt_1)

        self.horizontalSpacer_7 = QSpacerItem(191, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.opt_2 = QRadioButton(self.widget_18)
        self.opt_2.setObjectName(u"opt_2")
        self.optionsGroup.addButton(self.opt_2,1)

        self.horizontalLayout_11.addWidget(self.opt_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.widget_16)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.opt_3 = QRadioButton(self.widget_19)
        self.opt_3.setObjectName(u"opt_3")
        self.optionsGroup.addButton(self.opt_3,2)
        self.horizontalLayout_12.addWidget(self.opt_3)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)


        self.verticalLayout_3.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.widget_16)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.opt_4 = QRadioButton(self.widget_20)
        self.opt_4.setObjectName(u"opt_4")
        self.optionsGroup.addButton(self.opt_4,3)
        self.opt_5 = QRadioButton(self.widget_20)
        self.opt_5.setObjectName(u"opt_4")
        self.opt_5.setVisible(False)
        self.optionsGroup.addButton(self.opt_5,4)
        self.horizontalLayout_13.addWidget(self.opt_4)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)


        self.verticalLayout_3.addWidget(self.widget_20)


        self.verticalLayout_2.addWidget(self.widget_16)


        self.verticalLayout_4.addWidget(self.questionWidget)

        self.widget_12 = QWidget(self.quizWidget)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.previousButton = QPushButton(self.widget_12)
        self.previousButton.setObjectName(u"previousButton")
        self.previousButton.clicked.connect(self.prevQue)
        self.horizontalLayout_7.addWidget(self.previousButton)

        self.horizontalSpacer_4 = QSpacerItem(61, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.questionCountLabel = QLabel(self.widget_12)
        self.questionCountLabel.setObjectName(u"questionCountLabel")

        self.horizontalLayout_7.addWidget(self.questionCountLabel)

        self.horizontalSpacer_5 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.nextButton = QPushButton(self.widget_13)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.clicked.connect(self.nextQue)

        self.horizontalLayout_6.addWidget(self.nextButton)

        # self.submitButton = QPushButton(self.widget_13)
        # self.submitButton.setObjectName(u"submitButton")

        # self.horizontalLayout_6.addWidget(self.submitButton)


        self.horizontalLayout_7.addWidget(self.widget_13)


        self.verticalLayout_4.addWidget(self.widget_12)


        self.horizontalLayout_14.addWidget(self.quizWidget)


        self.verticalLayout_5.addWidget(self.widget_6)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")

        self.verticalLayout_5.addWidget(self.widget_3)


        self.horizontalLayout_15.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self._status = TimerStatus.init
        self._left_seconds = self.session["duration"]*60
        self.timer = QTimer()
        self.timer.timeout.connect(self._countdown_and_show)
        self.showTime()
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Quiz Platform", None))
        # self.participantNameLabel.setText(QCoreApplication.translate("MainWindow", u"Taker Name", None))
        # self.timerLabel.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.exitSessionButton.setText(QCoreApplication.translate("MainWindow", u"Exit Session", None))
        self.submitQuizButton.setText(QCoreApplication.translate("MainWindow", u"Submit Quiz", None))
        # self.instructionsIcon.setText(QCoreApplication.translate("MainWindow", u"instructions", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Instructions</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. You can attempt the quiz only once.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. All the questions in this quiz are single choice questions. Each question has exactly one correct answer.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. Read each question carefully and choose the best answer to each one.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4. Score for every question might be different.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">5. After responding to a question, click on the 'Next' button at the bottom to save and go to the next question.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">6. You may toggle between questions using below given toggle buttons.</span>"
                        "</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">7. Make sure you have a stable internet connection before attempting the quiz. In case of any internet issues, the quiz will be terminated immediately.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">8. The total score for the quiz is based on your responses to all the questions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; ma"
                        "rgin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">9. Your quiz will not be graded if you exit before end time without submitting quiz.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ALL THE BEST</span></p></body></html>", None))
        self.startConf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type \"start\" to start quiz", None))
        self.startQuizButton.setText(QCoreApplication.translate("MainWindow", u"Start Quiz", None))
        self.questionEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Question", None))
        self.maxScoreLabel.setText(QCoreApplication.translate("MainWindow", u"Max Score", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.opt_1.setText(QCoreApplication.translate("MainWindow", u"Option 1", None))
        self.opt_2.setText(QCoreApplication.translate("MainWindow", u"Option 2", None))
        self.opt_3.setText(QCoreApplication.translate("MainWindow", u"Option 3", None))
        self.opt_4.setText(QCoreApplication.translate("MainWindow", u"Option 4", None))
        self.previousButton.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.questionCountLabel.setText(QCoreApplication.translate("MainWindow", u"1/10", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        # self.submitButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win = QWidget()
    ui = Ui_loginSection()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())
