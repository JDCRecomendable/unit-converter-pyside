# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 440)
        MainWindow.setMinimumSize(QSize(580, 320))
        MainWindow.setMaximumSize(QSize(720, 440))
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionDisplay_All_Digits = QAction(MainWindow)
        self.actionDisplay_All_Digits.setObjectName(u"actionDisplay_All_Digits")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionReset = QAction(MainWindow)
        self.actionReset.setObjectName(u"actionReset")
        self.actionCopy_Input_to_Clipboard = QAction(MainWindow)
        self.actionCopy_Input_to_Clipboard.setObjectName(u"actionCopy_Input_to_Clipboard")
        self.actionCopy_Result_to_Clipboard = QAction(MainWindow)
        self.actionCopy_Result_to_Clipboard.setObjectName(u"actionCopy_Result_to_Clipboard")
        self.actionRound_off_to_whole_number = QAction(MainWindow)
        self.actionRound_off_to_whole_number.setObjectName(u"actionRound_off_to_whole_number")
        self.actionRound_off_to_1_d_p = QAction(MainWindow)
        self.actionRound_off_to_1_d_p.setObjectName(u"actionRound_off_to_1_d_p")
        self.actionRound_off_to_2_d_p = QAction(MainWindow)
        self.actionRound_off_to_2_d_p.setObjectName(u"actionRound_off_to_2_d_p")
        self.actionRound_off_to_3_d_p = QAction(MainWindow)
        self.actionRound_off_to_3_d_p.setObjectName(u"actionRound_off_to_3_d_p")
        self.actionRound_off_to_4_d_p = QAction(MainWindow)
        self.actionRound_off_to_4_d_p.setObjectName(u"actionRound_off_to_4_d_p")
        self.actionRound_off_to_5_d_p = QAction(MainWindow)
        self.actionRound_off_to_5_d_p.setObjectName(u"actionRound_off_to_5_d_p")
        self.actionRound_off_to_6_d_p = QAction(MainWindow)
        self.actionRound_off_to_6_d_p.setObjectName(u"actionRound_off_to_6_d_p")
        self.actionRound_off_to_7_d_p = QAction(MainWindow)
        self.actionRound_off_to_7_d_p.setObjectName(u"actionRound_off_to_7_d_p")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.unitCategoryListView = QListView(self.centralwidget)
        self.unitCategoryListView.setObjectName(u"unitCategoryListView")

        self.horizontalLayout.addWidget(self.unitCategoryListView)

        self.unitConversionArea = QVBoxLayout()
        self.unitConversionArea.setObjectName(u"unitConversionArea")
        self.unitPickerArea = QHBoxLayout()
        self.unitPickerArea.setObjectName(u"unitPickerArea")
        self.fromUnitArea = QVBoxLayout()
        self.fromUnitArea.setObjectName(u"fromUnitArea")
        self.fromUnitPicker = QListView(self.centralwidget)
        self.fromUnitPicker.setObjectName(u"fromUnitPicker")

        self.fromUnitArea.addWidget(self.fromUnitPicker)

        self.fromUnitInput = QLineEdit(self.centralwidget)
        self.fromUnitInput.setObjectName(u"fromUnitInput")
        font = QFont()
        font.setPointSize(16)
        self.fromUnitInput.setFont(font)
        self.fromUnitInput.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.fromUnitArea.addWidget(self.fromUnitInput)


        self.unitPickerArea.addLayout(self.fromUnitArea)

        self.toUnitArea = QVBoxLayout()
        self.toUnitArea.setObjectName(u"toUnitArea")
        self.toUnitPicker = QListView(self.centralwidget)
        self.toUnitPicker.setObjectName(u"toUnitPicker")

        self.toUnitArea.addWidget(self.toUnitPicker)

        self.toUnitOutput = QLineEdit(self.centralwidget)
        self.toUnitOutput.setObjectName(u"toUnitOutput")
        self.toUnitOutput.setEnabled(True)
        self.toUnitOutput.setFont(font)
        self.toUnitOutput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.toUnitOutput.setReadOnly(True)

        self.toUnitArea.addWidget(self.toUnitOutput)


        self.unitPickerArea.addLayout(self.toUnitArea)


        self.unitConversionArea.addLayout(self.unitPickerArea)

        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")

        self.unitConversionArea.addWidget(self.resetButton)


        self.horizontalLayout.addLayout(self.unitConversionArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionReset)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy_Input_to_Clipboard)
        self.menuEdit.addAction(self.actionCopy_Result_to_Clipboard)
        self.menuView.addAction(self.actionDisplay_All_Digits)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionRound_off_to_whole_number)
        self.menuView.addAction(self.actionRound_off_to_1_d_p)
        self.menuView.addAction(self.actionRound_off_to_2_d_p)
        self.menuView.addAction(self.actionRound_off_to_3_d_p)
        self.menuView.addAction(self.actionRound_off_to_4_d_p)
        self.menuView.addAction(self.actionRound_off_to_5_d_p)
        self.menuView.addAction(self.actionRound_off_to_6_d_p)
        self.menuView.addAction(self.actionRound_off_to_7_d_p)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Unit Converter", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionDisplay_All_Digits.setText(QCoreApplication.translate("MainWindow", u"Display All Digits", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.actionCopy_Input_to_Clipboard.setText(QCoreApplication.translate("MainWindow", u"Copy Input to Clipboard", None))
        self.actionCopy_Result_to_Clipboard.setText(QCoreApplication.translate("MainWindow", u"Copy Result to Clipboard", None))
        self.actionRound_off_to_whole_number.setText(QCoreApplication.translate("MainWindow", u"Round off to whole number", None))
        self.actionRound_off_to_1_d_p.setText(QCoreApplication.translate("MainWindow", u"Round off to 1 d.p.", None))
        self.actionRound_off_to_2_d_p.setText(QCoreApplication.translate("MainWindow", u"Round off to 2 d.p.", None))
        self.actionRound_off_to_3_d_p.setText(QCoreApplication.translate("MainWindow", u"Round off to 3 d.p.", None))
        self.actionRound_off_to_4_d_p.setText(QCoreApplication.translate("MainWindow", u"Round off to 4 d.p.", None))
        self.actionRound_off_to_5_d_p.setText(QCoreApplication.translate("MainWindow", u"Round off to 5 d.p.", None))
        self.actionRound_off_to_6_d_p.setText(QCoreApplication.translate("MainWindow", u"Round off to 6 d.p.", None))
        self.actionRound_off_to_7_d_p.setText(QCoreApplication.translate("MainWindow", u"Round off to 7 d.p.", None))
        self.fromUnitInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"From", None))
        self.toUnitOutput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"To", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

