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
        MainWindow.resize(391, 489)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 341, 91))
        font = QtGui.QFont()
        font.setFamily("NovemberPro-Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.start_training_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_training_btn.setGeometry(QtCore.QRect(50, 130, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.start_training_btn.setFont(font)
        self.start_training_btn.setInputMethodHints(QtCore.Qt.ImhNone)
        self.start_training_btn.setObjectName("start_training_btn")
        self.about_box_btn = QtWidgets.QPushButton(self.centralwidget)
        self.about_box_btn.setGeometry(QtCore.QRect(290, 420, 75, 23))
        self.about_box_btn.setObjectName("about_box_btn")
        self.game_mode_btn = QtWidgets.QPushButton(self.centralwidget)
        self.game_mode_btn.setGeometry(QtCore.QRect(50, 220, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.game_mode_btn.setFont(font)
        self.game_mode_btn.setInputMethodHints(QtCore.Qt.ImhNone)
        self.game_mode_btn.setObjectName("game_mode_btn")
        self.record_table_btn = QtWidgets.QPushButton(self.centralwidget)
        self.record_table_btn.setGeometry(QtCore.QRect(50, 310, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(14)
        self.record_table_btn.setFont(font)
        self.record_table_btn.setInputMethodHints(QtCore.Qt.ImhNone)
        self.record_table_btn.setObjectName("record_table_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 21))
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
        self.label.setText(_translate("MainWindow", "Тренажер по русскому языку \n"
" \"Ударения\""))
        self.start_training_btn.setText(_translate("MainWindow", "Начать тренировку"))
        self.about_box_btn.setText(_translate("MainWindow", "О программе"))
        self.game_mode_btn.setText(_translate("MainWindow", "Игровой режим"))
        self.record_table_btn.setText(_translate("MainWindow", "Таблица рекордов"))
