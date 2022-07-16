# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quizTakerPage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import enum
import random
import db
from functools import partial
class TimerStatus(enum.Enum):
    init, counting, paused = 1, 2, 3
class Ui_QuizPlatform(QMainWindow):
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
        if(self.curQues-1<0):
            self.curQues=self.totalQues-1
        self.showQuestion()
    def submitQuiz(self,fsub=False):
        if(fsub):
            self.forceFullSubmit = True
        self._left_seconds = 0
        self.score = self.evaluateQuiz()
        self.completionStatus = True
        res = db.updateParticipant(self.session["session_code"],self.pcode,self.completionStatus,self.score[0])
        if(res):
            QMessageBox.information(self,"Info",f"Hey, {self.participantName}, You scored {self.score[0]} out of {self.score[1]}. And you attempted {len(self.response)} questions out of {self.totalQues}.")
            self.exit()
            return
        else:
            QMessageBox.critical(self,"Error","Sorry, didn't able to submit your responses, may be due to internet connectivity issue.")
            self.exit()
            return
        
    def evaluateQuiz(self):
        totalScore = 0
        score = 0
        for i in range(self.totalQues):
            question = self.questions[self.queDisplayArr[i]]
            totalScore+=int(question["score"])
        for q,resp in self.response.items():
            question = self.questions[q]
            cor = question["answer"][0]
            if(resp==cor):
                score+=int(question["score"])
        return [score,totalScore]
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
        if(total_seconds<0.05*self.session["duration"]*60):
            self.timerLabel.setStyleSheet("color:red;")
        else:
            self.timerLabel.setStyleSheet("color:#000080;")
            
        self.timerLabel.setText("{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds)))
        self.timerLabel.setAlignment(Qt.AlignHCenter)
    def exit(self):
        self.mwin.close()
    def confToStart(self):
        x = self.startConf.text()
        if(x=="start"):
            self.startQuizButton.setEnabled(True)
        else:
            self.startQuizButton.setEnabled(False)
    def startQuiz(self):
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
    # retranslateUi

