# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quizAdminPage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from functools import partial
from dateutil import parser
import db

class Ui_MainWindow(QMainWindow):
    def __init__(self,username):
        QMainWindow.__init__(self)
        self.username = username
        self.qid = 0
        self.questions = {}
        
        
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
        opt_1 = QRadioButton(widget_5)
        opt_1.setObjectName(f"opt_1#{self.qid}")
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
        questionEdit.setPlaceholderText(u"Question")
        scoreEdit.setPlaceholderText(u"Score", )
        opt_1.setText(u"Option 1")
        toolButton_1.setText(u"...")
        opt_2.setText(u"Option 2")
        toolButton_2.setText(u"...")
        opt_3.setText(u"Option 3")
        toolButton_3.setText(u"...")
        opt_4.setText(u"Option 4")
        toolButton_4.setText(u"...")
        pushButton_2.setText(u"Delete")
        pushButton_3.setText(u"Edit")
        pushButton_4.setText(u"Cancel Edit")
        pushButton.setText(u"Done Edit")
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
        queEdit = self.scrollAreaWidgetContents.findChild(QPlainTextEdit,f"questionEdit#{id}")
        scoreEdit = self.scrollAreaWidgetContents.findChild(QLineEdit,f"scoreEdit#{id}")
        que = queEdit.toPlainText()
        score = scoreEdit.text().strip()
        opt1 = self.scrollAreaWidgetContents.findChild(QRadioButton,f"opt_1#{id}")
        opt2 = self.scrollAreaWidgetContents.findChild(QRadioButton,f"opt_2#{id}")
        opt3 = self.scrollAreaWidgetContents.findChild(QRadioButton,f"opt_3#{id}")
        opt4 = self.scrollAreaWidgetContents.findChild(QRadioButton,f"opt_4#{id}")
        options = {0:opt1.text().strip(),1:opt2.text().strip(),2:opt3.text().strip(),3:opt4.text().strip()}
        answer = []
        if(opt1.isChecked()):
            answer.append(0)
        if(opt2.isChecked()):
            answer.append(1)
        if(opt3.isChecked()):
            answer.append(2)
        if(opt4.isChecked()):
            answer.append(3)
        if(score==""):
            score = "1"
        self.questions[id] = {"question":que,"options":options,"score":int(score),"answer":answer}
        print(self.questions)
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
        duration = self.duration.text().strip()
        try:
            self.sessionEnd.setMinimumDateTime(self.sessionStart.dateTime().addSecs(int(duration)*60))
        except:
            self.sessionEnd.setMinimumDateTime(self.sessionStart.dateTime().addSecs(10*60))
    def durationChanged(self):
        duration = self.duration.text().strip()
        try:
            self.sessionEnd.setMinimumDateTime(self.sessionStart.dateTime().addSecs(int(duration)*60))
        except:
            self.sessionEnd.setMinimumDateTime(self.sessionStart.dateTime().addSecs(10*60))
        
    def publishQuiz(self):
        quizNickName = self.sessionNickName.text().strip()
        err = ""
        if(quizNickName==""):
            err+="Nick Name must not be blank.\n"
        duration = self.duration.text().strip()
        if(duration!="" and duration.isnumeric()==False):
            err+="Duration must be a number.\n"
        else:
            duration = 10
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
            start=None
            end = None
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
        
        res = db.publishQuiz(self.questions,quizNickName,duration,self.username,start=start,end=end)
        print(res)
        if(res[0]):
            print("Published Successfully",res[1])
            self.resetAll()
        else:
            print("failed")
    def logOut(self):
        self.mwin.close()
    def resetAll(self):
        self.reset()
        self.sessionNickName.clear()
        self.duration.clear()
        self.isTimeConstrained.setChecked(False)
        
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
        self.duration = QLineEdit(self.widget_7)
        self.duration.setObjectName(u"duration")
        self.duration.textChanged.connect(self.durationChanged)
        self.horizontalLayout_5.addWidget(self.duration)

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

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        # self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Welcome, Username", None))
#if QT_CONFIG(tooltip)
        self.logOutButton.setToolTip(QCoreApplication.translate("MainWindow", u"Log Out of the Session", None))
#endif // QT_CONFIG(tooltip)
        self.logOutButton.setText(QCoreApplication.translate("MainWindow", u"LogOut", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manageQuizTab), QCoreApplication.translate("MainWindow", u"Manage Quiz", None))
        self.sessionNickName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quiz Nick Name", None))
        self.isTimeConstrained.setText(QCoreApplication.translate("MainWindow", u"Time Constrained", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.duration.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Duration in Minutes", None))
        self.addQuestionButton.setText(QCoreApplication.translate("MainWindow", u"Add Questions", None))
        self.publishButton.setText(QCoreApplication.translate("MainWindow", u"Publish Quiz", None))
        self.backToQuizSettings.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.resetAllQuestions.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.doneAddingButton.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.createQuizTab), QCoreApplication.translate("MainWindow", u"Create Quiz", None))
    # retranslateUi

