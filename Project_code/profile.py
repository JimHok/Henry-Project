# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QToolButton,
    QWidget)
import logo

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(375, 730)
        Dialog.setStyleSheet(u"*{\n"
"	font-family: century gothic;\n"
"}\n"
"\n"
"")
        self.profilepic = QLabel(Dialog)
        self.profilepic.setObjectName(u"profilepic")
        self.profilepic.setGeometry(QRect(107, 12, 161, 151))
        self.profilepic.setStyleSheet(u"*{\n"
"font-size:34px;\n"
"border-radius: 50%;\n"
"}")
        self.profilepic.setFrameShape(QFrame.NoFrame)
        self.profilepic.setAlignment(Qt.AlignCenter)
        self.browsepic = QPushButton(Dialog)
        self.browsepic.setObjectName(u"browsepic")
        self.browsepic.setGeometry(QRect(101, 170, 175, 41))
        self.browsepic.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(111, 218, 156);\n"
"font-size: 24px;\n"
"border-width: 4px;\n"
"border-radius: 15px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-color: black;\n"
"	background-color: rgb(90, 190, 130);\n"
"}")
        self.label_e = QLabel(Dialog)
        self.label_e.setObjectName(u"label_e")
        self.label_e.setGeometry(QRect(40, 230, 81, 41))
        self.label_e.setStyleSheet(u"font: 18pt \"century gothic\";\n"
"border: none;\n"
"")
        self.label_a = QLabel(Dialog)
        self.label_a.setObjectName(u"label_a")
        self.label_a.setGeometry(QRect(40, 410, 121, 41))
        self.label_a.setStyleSheet(u"font: 18pt \"century gothic\";\n"
"border: none;\n"
"")
        self.label_m = QLabel(Dialog)
        self.label_m.setObjectName(u"label_m")
        self.label_m.setGeometry(QRect(40, 500, 211, 41))
        self.label_m.setStyleSheet(u"font: 16pt \"century gothic\";\n"
"border: none;\n"
"")
        self.label_n = QLabel(Dialog)
        self.label_n.setObjectName(u"label_n")
        self.label_n.setGeometry(QRect(40, 320, 91, 41))
        self.label_n.setStyleSheet(u"font: 18pt \"century gothic\";\n"
"border: none;\n"
"")
        self.save = QPushButton(Dialog)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(101, 600, 171, 41))
        self.save.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(111, 218, 156);\n"
"	font-size: 24px;\n"
"	border-width: 4px;\n"
"	border-radius: 15px;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-color: black;\n"
"	background-color: rgb(90, 190, 130);\n"
"}")
        self.logout = QPushButton(Dialog)
        self.logout.setObjectName(u"logout")
        self.logout.setGeometry(QRect(101, 660, 171, 41))
        self.logout.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(57, 68, 84);\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"color: white;\n"
"border-width: 4px;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-color:  rgb(111, 218, 156);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-color: black;\n"
"	background-color: rgb(80, 110, 125);\n"
"}")
        self.name = QLineEdit(Dialog)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(40, 360, 295, 41))
        self.name.setStyleSheet(u"font: 14pt \"century gothic\";\n"
"border: 2px solid;\n"
"border-color: red;\n"
"border-color:  rgb(111, 218, 156);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.address = QLineEdit(Dialog)
        self.address.setObjectName(u"address")
        self.address.setGeometry(QRect(40, 450, 295, 41))
        self.address.setStyleSheet(u"font: 14pt \"century gothic\";\n"
"border: 2px solid;\n"
"border-color: red;\n"
"border-color:  rgb(111, 218, 156);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.mobile = QLineEdit(Dialog)
        self.mobile.setObjectName(u"mobile")
        self.mobile.setGeometry(QRect(40, 540, 295, 41))
        self.mobile.setStyleSheet(u"font: 14pt \"century gothic\";\n"
"border: 2px solid;\n"
"border-color: red;\n"
"border-color:  rgb(111, 218, 156);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.email = QLabel(Dialog)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(40, 270, 295, 51))
        self.email.setStyleSheet(u"font: 14pt \"century gothic\";\n"
"border: 2px solid;\n"
"border-color: red;\n"
"border-color:  rgb(111, 218, 156);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.home = QToolButton(Dialog)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(10, 10, 41, 41))
        self.home.setStyleSheet(u"QToolButton{\n"
"	image: url(:/logo/icons8-home-24.png);\n"
"	background-color: rgb(111, 218, 156);\n"
"	border-width: 4px;\n"
"	border-radius: 15px;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"	border-color: black;\n"
"	background-color: rgb(140, 238, 179)\n"
"}\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.profilepic.setText("")
        self.browsepic.setText(QCoreApplication.translate("Dialog", u"Browse Photo", None))
        self.label_e.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_a.setText(QCoreApplication.translate("Dialog", u"Address", None))
        self.label_m.setText(QCoreApplication.translate("Dialog", u"Mobile Number", None))
        self.label_n.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.save.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.logout.setText(QCoreApplication.translate("Dialog", u"Log Out", None))
        self.email.setText("")
        self.home.setText("")
    # retranslateUi

