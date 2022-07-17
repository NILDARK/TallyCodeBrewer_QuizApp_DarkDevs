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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(768, 477)
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
        self.usernameLabel.setScaledContents(True)
        self.usernameLabel.setWordWrap(True)

        self.horizontalLayout.addWidget(self.usernameLabel)

        self.horizontalSpacer = QSpacerItem(604, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.logOutButton = QPushButton(self.widget)
        self.logOutButton.setObjectName(u"logOutButton")
        icon = QIcon()
        icon.addFile(u"../Images/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logOutButton.setIcon(icon)

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

        self.horizontalLayout_11.addWidget(self.nickNameRadio)

        self.activeCheck = QCheckBox(self.widget_16)
        self.activeCheck.setObjectName(u"activeCheck")

        self.horizontalLayout_11.addWidget(self.activeCheck)


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
        self.searchButton.setEnabled(False)
        self.searchButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"../../../python projects/Challan Generator/Uis/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon1)

        self.horizontalLayout_14.addWidget(self.searchButton)

        self.horizontalSpacer_8 = QSpacerItem(214, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)


        self.verticalLayout_5.addWidget(self.widget_19)


        self.verticalLayout_9.addWidget(self.widget_15)

        self.sessionList = QListWidget(self.widget_11)
        self.sessionList.setObjectName(u"sessionList")
        self.sessionList.setFrameShape(QFrame.NoFrame)
        self.sessionList.setFrameShadow(QFrame.Plain)

        self.verticalLayout_9.addWidget(self.sessionList)


        self.horizontalLayout_18.addWidget(self.widget_11)

        self.sessionDisplayWidget = QWidget(self.widget_14)
        self.sessionDisplayWidget.setObjectName(u"sessionDisplayWidget")
        self.verticalLayout_6 = QVBoxLayout(self.sessionDisplayWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.sessionDetailsBox = QGroupBox(self.sessionDisplayWidget)
        self.sessionDetailsBox.setObjectName(u"sessionDetailsBox")
        self.verticalLayout_4 = QVBoxLayout(self.sessionDetailsBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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

        self.horizontalLayout_3.addWidget(self.sessionStart)

        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.sessionEnd = QDateTimeEdit(self.widget_6)
        self.sessionEnd.setObjectName(u"sessionEnd")

        self.horizontalLayout_3.addWidget(self.sessionEnd)


        self.horizontalLayout_4.addWidget(self.widget_6)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.duration = QLineEdit(self.widget_7)
        self.duration.setObjectName(u"duration")

        self.horizontalLayout_5.addWidget(self.duration)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.widget_7)

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

        self.horizontalLayout_6.addWidget(self.addQuestionButton)

        self.publishButton = QPushButton(self.widget_8)
        self.publishButton.setObjectName(u"publishButton")

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 299, 332))
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

        self.horizontalLayout_7.addWidget(self.backToQuizSettings)

        self.resetAllQuestions = QPushButton(self.widget_10)
        self.resetAllQuestions.setObjectName(u"resetAllQuestions")

        self.horizontalLayout_7.addWidget(self.resetAllQuestions)

        self.doneAddingButton = QPushButton(self.widget_10)
        self.doneAddingButton.setObjectName(u"doneAddingButton")

        self.horizontalLayout_7.addWidget(self.doneAddingButton)


        self.verticalLayout.addWidget(self.widget_10)


        self.horizontalLayout_8.addWidget(self.widget_9)

        self.tabWidget.addTab(self.createQuizTab, "")

        self.horizontalLayout_9.addWidget(self.tabWidget)


        self.verticalLayout_3.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Welcome, Username", None))
#if QT_CONFIG(tooltip)
        self.logOutButton.setToolTip(QCoreApplication.translate("MainWindow", u"Log Out of the Session", None))
#endif // QT_CONFIG(tooltip)
        self.logOutButton.setText(QCoreApplication.translate("MainWindow", u"LogOut", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Search by ", None))
        self.sessionCodeRadio.setText(QCoreApplication.translate("MainWindow", u"Session Code", None))
        self.nickNameRadio.setText(QCoreApplication.translate("MainWindow", u"Session Nick Name", None))
        self.activeCheck.setText(QCoreApplication.translate("MainWindow", u"Active Session", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Session Code", None))
#if QT_CONFIG(tooltip)
        self.searchButton.setToolTip(QCoreApplication.translate("MainWindow", u"Search Challan", None))
#endif // QT_CONFIG(tooltip)
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.sessionDetailsBox.setTitle(QCoreApplication.translate("MainWindow", u"Session Details", None))
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
        self.duration.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Duration in Minutes", None))
        self.addQuestionButton.setText(QCoreApplication.translate("MainWindow", u"Add Questions", None))
        self.publishButton.setText(QCoreApplication.translate("MainWindow", u"Publish Quiz", None))
        self.backToQuizSettings.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.resetAllQuestions.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.doneAddingButton.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.createQuizTab), QCoreApplication.translate("MainWindow", u"Create Quiz", None))
    # retranslateUi

