# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eHawconfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 356)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("KO2FClientIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gb_WinlinkPaths = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_WinlinkPaths.setGeometry(QtCore.QRect(300, 150, 401, 180))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gb_WinlinkPaths.setFont(font)
        self.gb_WinlinkPaths.setObjectName("gb_WinlinkPaths")
        self.le_WinlinkExePath = QtWidgets.QLineEdit(self.gb_WinlinkPaths)
        self.le_WinlinkExePath.setGeometry(QtCore.QRect(10, 50, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.le_WinlinkExePath.setFont(font)
        self.le_WinlinkExePath.setToolTip("")
        self.le_WinlinkExePath.setObjectName("le_WinlinkExePath")
        self.label_2 = QtWidgets.QLabel(self.gb_WinlinkPaths)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 160, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.le_WinlinkOutPath = QtWidgets.QLineEdit(self.gb_WinlinkPaths)
        self.le_WinlinkOutPath.setGeometry(QtCore.QRect(10, 100, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.le_WinlinkOutPath.setFont(font)
        self.le_WinlinkOutPath.setObjectName("le_WinlinkOutPath")
        self.le_WinlinkSentPath = QtWidgets.QLineEdit(self.gb_WinlinkPaths)
        self.le_WinlinkSentPath.setGeometry(QtCore.QRect(10, 150, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.le_WinlinkSentPath.setFont(font)
        self.le_WinlinkSentPath.setObjectName("le_WinlinkSentPath")
        self.label_3 = QtWidgets.QLabel(self.gb_WinlinkPaths)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 160, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.gb_WinlinkPaths)
        self.label.setGeometry(QtCore.QRect(20, 30, 160, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gb_UserAccounts = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_UserAccounts.setGeometry(QtCore.QRect(10, 10, 271, 181))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gb_UserAccounts.setFont(font)
        self.gb_UserAccounts.setObjectName("gb_UserAccounts")
        self.label_9 = QtWidgets.QLabel(self.gb_UserAccounts)
        self.label_9.setGeometry(QtCore.QRect(30, 28, 100, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.le_UserName = QtWidgets.QLineEdit(self.gb_UserAccounts)
        self.le_UserName.setGeometry(QtCore.QRect(20, 99, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.le_UserName.setFont(font)
        self.le_UserName.setAlignment(QtCore.Qt.AlignCenter)
        self.le_UserName.setObjectName("le_UserName")
        self.le_AdminPwd = QtWidgets.QLineEdit(self.gb_UserAccounts)
        self.le_AdminPwd.setGeometry(QtCore.QRect(146, 49, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.le_AdminPwd.setFont(font)
        self.le_AdminPwd.setAlignment(QtCore.Qt.AlignCenter)
        self.le_AdminPwd.setObjectName("le_AdminPwd")
        self.label_5 = QtWidgets.QLabel(self.gb_UserAccounts)
        self.label_5.setGeometry(QtCore.QRect(30, 78, 90, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.gb_UserAccounts)
        self.label_10.setGeometry(QtCore.QRect(156, 28, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.le_UserPwd = QtWidgets.QLineEdit(self.gb_UserAccounts)
        self.le_UserPwd.setGeometry(QtCore.QRect(146, 99, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.le_UserPwd.setFont(font)
        self.le_UserPwd.setAlignment(QtCore.Qt.AlignCenter)
        self.le_UserPwd.setObjectName("le_UserPwd")
        self.label_6 = QtWidgets.QLabel(self.gb_UserAccounts)
        self.label_6.setGeometry(QtCore.QRect(156, 78, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.le_AdminName = QtWidgets.QLineEdit(self.gb_UserAccounts)
        self.le_AdminName.setGeometry(QtCore.QRect(20, 49, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.le_AdminName.setFont(font)
        self.le_AdminName.setAlignment(QtCore.Qt.AlignCenter)
        self.le_AdminName.setObjectName("le_AdminName")
        self.label_8 = QtWidgets.QLabel(self.gb_UserAccounts)
        self.label_8.setGeometry(QtCore.QRect(156, 129, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.gb_UserAccounts)
        self.label_7.setGeometry(QtCore.QRect(30, 129, 90, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.le_ModeratorPwd = QtWidgets.QLineEdit(self.gb_UserAccounts)
        self.le_ModeratorPwd.setGeometry(QtCore.QRect(146, 150, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.le_ModeratorPwd.setFont(font)
        self.le_ModeratorPwd.setAlignment(QtCore.Qt.AlignCenter)
        self.le_ModeratorPwd.setObjectName("le_ModeratorPwd")
        self.le_ModeratorName = QtWidgets.QLineEdit(self.gb_UserAccounts)
        self.le_ModeratorName.setGeometry(QtCore.QRect(20, 150, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.le_ModeratorName.setFont(font)
        self.le_ModeratorName.setAlignment(QtCore.Qt.AlignCenter)
        self.le_ModeratorName.setObjectName("le_ModeratorName")
        self.pb_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pb_Cancel.setGeometry(QtCore.QRect(160, 300, 75, 23))
        self.pb_Cancel.setObjectName("pb_Cancel")
        self.tb_Info = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_Info.setGeometry(QtCore.QRect(20, 200, 256, 90))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tb_Info.setFont(font)
        self.tb_Info.setObjectName("tb_Info")
        self.pb_Save = QtWidgets.QPushButton(self.centralwidget)
        self.pb_Save.setGeometry(QtCore.QRect(60, 300, 75, 23))
        self.pb_Save.setObjectName("pb_Save")
        self.bg_EventDetails = QtWidgets.QGroupBox(self.centralwidget)
        self.bg_EventDetails.setGeometry(QtCore.QRect(300, 13, 401, 130))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bg_EventDetails.setFont(font)
        self.bg_EventDetails.setObjectName("bg_EventDetails")
        self.le_OperatorCall = QtWidgets.QLineEdit(self.bg_EventDetails)
        self.le_OperatorCall.setGeometry(QtCore.QRect(146, 50, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.le_OperatorCall.setFont(font)
        self.le_OperatorCall.setAlignment(QtCore.Qt.AlignCenter)
        self.le_OperatorCall.setObjectName("le_OperatorCall")
        self.label_11 = QtWidgets.QLabel(self.bg_EventDetails)
        self.label_11.setGeometry(QtCore.QRect(156, 29, 90, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.bg_EventDetails)
        self.label_12.setGeometry(QtCore.QRect(30, 29, 90, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.le_EventLocation = QtWidgets.QLineEdit(self.bg_EventDetails)
        self.le_EventLocation.setGeometry(QtCore.QRect(19, 99, 370, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.le_EventLocation.setFont(font)
        self.le_EventLocation.setObjectName("le_EventLocation")
        self.label_4 = QtWidgets.QLabel(self.bg_EventDetails)
        self.label_4.setGeometry(QtCore.QRect(29, 79, 110, 13))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.le_WinlinkCall = QtWidgets.QLineEdit(self.bg_EventDetails)
        self.le_WinlinkCall.setGeometry(QtCore.QRect(20, 50, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.le_WinlinkCall.setFont(font)
        self.le_WinlinkCall.setAlignment(QtCore.Qt.AlignCenter)
        self.le_WinlinkCall.setObjectName("le_WinlinkCall")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.le_AdminName.returnPressed.connect(self.pb_Save.click) # type: ignore
        self.le_AdminPwd.returnPressed.connect(self.pb_Save.click) # type: ignore
        self.le_UserName.returnPressed.connect(self.pb_Save.click) # type: ignore
        self.le_UserPwd.returnPressed.connect(self.pb_Save.click) # type: ignore
        self.le_ModeratorName.returnPressed.connect(self.pb_Save.click) # type: ignore
        self.le_ModeratorPwd.returnPressed.connect(self.pb_Save.click) # type: ignore
        self.le_WinlinkCall.returnPressed.connect(self.pb_Save.click) # type: ignore
        self.le_OperatorCall.returnPressed.connect(self.pb_Save.click) # type: ignore
        self.le_EventLocation.returnPressed.connect(self.pb_Save.click) # type: ignore
        self.le_WinlinkExePath.returnPressed.connect(self.pb_Save.click) # type: ignore
        self.le_WinlinkOutPath.returnPressed.connect(self.pb_Save.click) # type: ignore
        self.le_WinlinkSentPath.returnPressed.connect(self.pb_Save.click) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pb_Save, self.le_AdminName)
        MainWindow.setTabOrder(self.le_AdminName, self.le_AdminPwd)
        MainWindow.setTabOrder(self.le_AdminPwd, self.le_UserName)
        MainWindow.setTabOrder(self.le_UserName, self.le_UserPwd)
        MainWindow.setTabOrder(self.le_UserPwd, self.le_ModeratorName)
        MainWindow.setTabOrder(self.le_ModeratorName, self.le_ModeratorPwd)
        MainWindow.setTabOrder(self.le_ModeratorPwd, self.le_WinlinkCall)
        MainWindow.setTabOrder(self.le_WinlinkCall, self.le_OperatorCall)
        MainWindow.setTabOrder(self.le_OperatorCall, self.le_EventLocation)
        MainWindow.setTabOrder(self.le_EventLocation, self.le_WinlinkExePath)
        MainWindow.setTabOrder(self.le_WinlinkExePath, self.le_WinlinkOutPath)
        MainWindow.setTabOrder(self.le_WinlinkOutPath, self.le_WinlinkSentPath)
        MainWindow.setTabOrder(self.le_WinlinkSentPath, self.pb_Cancel)
        MainWindow.setTabOrder(self.pb_Cancel, self.tb_Info)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "eHaW Config"))
        self.gb_WinlinkPaths.setTitle(_translate("MainWindow", "Winlink File Paths"))
        self.le_WinlinkExePath.setPlaceholderText(_translate("MainWindow", "If Pat is in your system or user path, leave this blank"))
        self.label_2.setText(_translate("MainWindow", "Winlink Out Folder Path"))
        self.le_WinlinkOutPath.setPlaceholderText(_translate("MainWindow", "C:\\Users\\login\\AppData\\Local\\pat\\mailbox\\callsign\\out"))
        self.le_WinlinkSentPath.setPlaceholderText(_translate("MainWindow", "C:\\Users\\login\\AppData\\Local\\pat\\mailbox\\callsign\\sent"))
        self.label_3.setText(_translate("MainWindow", "Winlink Sent Folder Path"))
        self.label.setText(_translate("MainWindow", "Winlink Executable Path"))
        self.gb_UserAccounts.setTitle(_translate("MainWindow", "User Account Details"))
        self.label_9.setText(_translate("MainWindow", "eHaW Admin User"))
        self.le_UserName.setPlaceholderText(_translate("MainWindow", "eHaWuser"))
        self.le_AdminPwd.setPlaceholderText(_translate("MainWindow", "*********"))
        self.label_5.setText(_translate("MainWindow", "eHaW User"))
        self.label_10.setText(_translate("MainWindow", "Password"))
        self.le_UserPwd.setPlaceholderText(_translate("MainWindow", "*********"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.le_AdminName.setPlaceholderText(_translate("MainWindow", "ko2f"))
        self.label_8.setText(_translate("MainWindow", "Password"))
        self.label_7.setText(_translate("MainWindow", "Moderator User"))
        self.le_ModeratorPwd.setPlaceholderText(_translate("MainWindow", "*********"))
        self.le_ModeratorName.setPlaceholderText(_translate("MainWindow", "eHaWmoderator"))
        self.pb_Cancel.setText(_translate("MainWindow", "Cancel"))
        self.tb_Info.setPlaceholderText(_translate("MainWindow", "Fill in the fields and click Save to continue.  Or.. just click Save and we will walk you through it."))
        self.pb_Save.setText(_translate("MainWindow", "Save"))
        self.bg_EventDetails.setTitle(_translate("MainWindow", "Initial Event Details"))
        self.le_OperatorCall.setPlaceholderText(_translate("MainWindow", "Your Callsign"))
        self.label_11.setText(_translate("MainWindow", "Operator Callsign"))
        self.label_12.setText(_translate("MainWindow", "Winlink Callsign"))
        self.le_EventLocation.setPlaceholderText(_translate("MainWindow", "Short (20-60 char) string to identify the Event/Location of messages"))
        self.label_4.setText(_translate("MainWindow", "Initial Event Location"))
        self.le_WinlinkCall.setPlaceholderText(_translate("MainWindow", "Your Winlink  Callsign"))
