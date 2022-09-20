import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMessageBox
# #import mysql.connector
# from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel

from PyQt5.QtCore import Qt
from PyQt5.QtSql import (
    QSqlDatabase,
    QSqlQuery
)
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem
)
from moderator_ui import Ui_MainWindow


config = {
    'user':'ko2f', 
    'password':'Ko2f2018!', 
    'host':'127.0.0.1', 
    'database':'ehaw'
}


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Load Winlink configuration
        ehawCfg = QSqlQuery("SELECT cfgId, cfgWinlinkExePath, cfgOutPath, cfgSentPath FROM ehaw.ehawconfig")
        while ehawCfg.next():
            self.ui.le_WinlinkExecPath.setText(ehawCfg.value(1))
            self.ui.le_WinlinkOutPath.setText(ehawCfg.value(2))
            self.ui.le_WinlinkSentPath.setText(ehawCfg.value(3))

        #Load Event Configuration
        self.ui.tw_EventConfig.setColumnCount(4)
        self.ui.tw_EventConfig.setHorizontalHeaderLabels(["Event Id", " Event Location / Description", "Operator Call", "Winlink Call"])
        ehawEvents = QSqlQuery("SELECT eventId, eventLocation, eventOperatorCallsign, eventWinlinkCallsign FROM ehaw.eventMetadata")
        while ehawEvents.next():
            rows = self.ui.tw_EventConfig.rowCount()
            self.ui.tw_EventConfig.setRowCount(rows + 1)
            self.ui.tw_EventConfig.setItem(rows, 0, QTableWidgetItem(str(ehawEvents.value(0))))
            self.ui.tw_EventConfig.setItem(rows, 1, QTableWidgetItem(ehawEvents.value(1)))
            self.ui.tw_EventConfig.setItem(rows, 2, QTableWidgetItem(ehawEvents.value(2)))
            self.ui.tw_EventConfig.setItem(rows, 3, QTableWidgetItem(ehawEvents.value(3)))
        self.ui.tw_EventConfig.resizeColumnsToContents()

        #Load Open Message Queue
        self.ui.tw_OpenMsgQueue.setColumnCount(4)
        self.ui.tw_OpenMsgQueue.setHorizontalHeaderLabels(["Msg Id", "From", "To", "Message", "Created"])
        openMsgs = QSqlQuery("SELECT msgId, msgFrom, msgTo, msgText, msgCreate FROM ehaw.openMsgQueue")
        rows = 0
        actMsgId = 0
        while openMsgs.next():
            rows = self.ui.tw_OpenMsgQueue.rowCount()
            self.ui.tw_OpenMsgQueue.setRowCount(rows + 1)
            self.ui.tw_OpenMsgQueue.setItem(rows, 0, QTableWidgetItem(str(openMsgs.value(0))))
            self.ui.tw_OpenMsgQueue.setItem(rows, 1, QTableWidgetItem(openMsgs.value(1)))
            self.ui.tw_OpenMsgQueue.setItem(rows, 2, QTableWidgetItem(openMsgs.value(2)))
            self.ui.tw_OpenMsgQueue.setItem(rows, 3, QTableWidgetItem(openMsgs.value(3)))
            self.ui.tw_OpenMsgQueue.setItem(rows, 4, QTableWidgetItem(openMsgs.value(4)))
            if rows == 0:
                actMsgId = openMsgs.value(0)
        #Make each cell in each row read only
        for i in range(rows):
            for j in range(5):
                cell_item = QTableWidgetItem()
                cell_item = self.ui.tw_OpenMsgQueue.item(rows, j)
                cell_item.setFlags(cell_item.flags() ^ Qt.ItemIsEditable)
        self.ui.tw_OpenMsgQueue.resizeColumnsToContents()

        #Retrieve Active Message
        if actMsgId > 0:
            qString = "SELECT msgId, msgSubject, msgTo, msgBody FROM ehaw.buildMsg WHERE msgId = " + str(actMsgId)
            actMsg = QSqlQuery(qString)
            actMsg.next()
            print(actMsg.value(0))
            print(actMsg.value(1))
            print(actMsg.value(2))
            print(actMsg.value(3))
            self.ui.le_ActMsgId.setText(str(actMsg.value(0)))
            self.ui.le_ActSubject.setText(actMsg.value(1))
            self.ui.le_ActTo.setText(actMsg.value(2))
            self.ui.tb_ActiveMessage.setText(actMsg.value(3))



        #Load Message Queue
        self.ui.tw_MsgQueue.setColumnCount(6)
        self.ui.tw_MsgQueue.setHorizontalHeaderLabels(["Msg Id", "Status", "From", "Message", "Updated", "Created"])
        msgQueue = QSqlQuery("SELECT msgId, msgStatus, msgFrom, msgText, msgUpdate, msgCreate FROM ehaw.userMsgQueue")
        rows = 0
        while msgQueue.next():
            rows = self.ui.tw_MsgQueue.rowCount()
            self.ui.tw_MsgQueue.setRowCount(rows + 1)
            self.ui.tw_MsgQueue.setItem(rows, 0, QTableWidgetItem(str(msgQueue.value(0))))
            self.ui.tw_MsgQueue.setItem(rows, 1, QTableWidgetItem(msgQueue.value(1)))
            self.ui.tw_MsgQueue.setItem(rows, 2, QTableWidgetItem(msgQueue.value(2)))
            self.ui.tw_MsgQueue.setItem(rows, 3, QTableWidgetItem(msgQueue.value(3)))
            self.ui.tw_MsgQueue.setItem(rows, 4, QTableWidgetItem(msgQueue.value(4)))
            self.ui.tw_MsgQueue.setItem(rows, 5, QTableWidgetItem(msgQueue.value(5)))
        #Make each cell in each row read only
        for i in range(rows):
            for j in range(6):
                cell_item = QTableWidgetItem()
                cell_item = self.ui.tw_MsgQueue.item(rows, j)
                cell_item.setFlags(cell_item.flags() ^ Qt.ItemIsEditable)
        self.ui.tw_MsgQueue.resizeColumnsToContents()


def createConnection():
    con = QSqlDatabase.addDatabase("QMYSQL")
    con.setHostName(config["host"])
    con.setDatabaseName(config["database"])
    if not con.open(config["user"], config["password"]):
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )
        return False
    return True

# main
app = QApplication(sys.argv)
if not createConnection():
    sys.exit(1)
if __name__ == "__main__":
    win = Window()
    win.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
