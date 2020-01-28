# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RussianProject.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(404, 286)
        font = QtGui.QFont()
        font.setPointSize(2)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        MainWindow.setStyleSheet("background-color: rgb(219, 215, 210);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setStyleSheet("color: rgb(76, 47, 39);")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.start_training_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_training_btn.setGeometry(QtCore.QRect(10, 110, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.start_training_btn.setFont(font)
        self.start_training_btn.setStyleSheet("color: rgb(76, 47, 39);\n"
"background-color: rgb(220, 220, 220);")
        self.start_training_btn.setInputMethodHints(QtCore.Qt.ImhNone)
        self.start_training_btn.setObjectName("start_training_btn")
        self.game_mode_btn = QtWidgets.QPushButton(self.centralwidget)
        self.game_mode_btn.setGeometry(QtCore.QRect(220, 110, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.game_mode_btn.setFont(font)
        self.game_mode_btn.setStyleSheet("color: rgb(76, 47, 39);\n"
"background-color: rgb(220, 220, 220);")
        self.game_mode_btn.setInputMethodHints(QtCore.Qt.ImhNone)
        self.game_mode_btn.setObjectName("game_mode_btn")
        self.record_table_btn = QtWidgets.QPushButton(self.centralwidget)
        self.record_table_btn.setGeometry(QtCore.QRect(220, 180, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.record_table_btn.setFont(font)
        self.record_table_btn.setStyleSheet("color: rgb(76, 47, 39);\n"
"background-color: rgb(220, 220, 220);")
        self.record_table_btn.setInputMethodHints(QtCore.Qt.ImhNone)
        self.record_table_btn.setAutoDefault(False)
        self.record_table_btn.setObjectName("record_table_btn")
        self.work_on_mistakes_btn = QtWidgets.QPushButton(self.centralwidget)
        self.work_on_mistakes_btn.setGeometry(QtCore.QRect(10, 180, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.work_on_mistakes_btn.setFont(font)
        self.work_on_mistakes_btn.setStyleSheet("color: rgb(76, 47, 39);\n"
"background-color: rgb(220, 220, 220);")
        self.work_on_mistakes_btn.setInputMethodHints(QtCore.Qt.ImhNone)
        self.work_on_mistakes_btn.setObjectName("work_on_mistakes_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 404, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тренажер"))
        self.label.setText(_translate("MainWindow", "Тренажер ударений\n"
"\"АпострОф\""))
        self.start_training_btn.setText(_translate("MainWindow", "Начать тренировку"))
        self.game_mode_btn.setText(_translate("MainWindow", "Игровой режим"))
        self.record_table_btn.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.record_table_btn.setText(_translate("MainWindow", "Результаты\n"
"игрового режима"))
        self.work_on_mistakes_btn.setText(_translate("MainWindow", "Работа над\n"
"ошибками"))
