# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createacc.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import logo

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(375, 730)
        Dialog.setStyleSheet(u"*{\n"
"	background-color: rgb(57, 68, 84);\n"
"	font-family: century gothic;\n"
"}\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 20, 231, 211))
        self.label.setStyleSheet(u"image: url(:/logo/Terbal (1).png);")
        self.email = QLineEdit(Dialog)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(60, 350, 301, 41))
        self.email.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"border: none;\n"
"border-bottom: 1px solid #717072")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 330, 30, 71))
        self.label_2.setStyleSheet(u"image: url(:/logo/email-5-512.png);")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 450, 30, 71))
        self.label_3.setStyleSheet(u"image: url(:/logo/padlock-3-512.png);")
        self.createaccbutton = QPushButton(Dialog)
        self.createaccbutton.setObjectName(u"createaccbutton")
        self.createaccbutton.setGeometry(QRect(77, 660, 200, 61))
        font = QFont()
        font.setFamilies([u"century gothic"])
        font.setBold(True)
        self.createaccbutton.setFont(font)
        self.createaccbutton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(57, 68, 84);\n"
"font-size: 23px;\n"
"font-weight: bold;\n"
"color: white;\n"
"border-radius: 15px;\n"
"border-width: 4px;\n"
"border-style: solid;\n"
"border-color:  rgb(111, 218, 156);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-color: black;\n"
"	background-color: rgb(80, 110, 125);\n"
"}")
        self.password = QLineEdit(Dialog)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(60, 460, 301, 41))
        self.password.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"border: none;\n"
"border-bottom: 1px solid #717072")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(15, 300, 81, 41))
        self.label_4.setStyleSheet(u"font: 18pt \"century gothic\";\n"
"color: white;\n"
"border: none;\n"
"")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(15, 410, 141, 31))
        self.label_5.setStyleSheet(u"font: 18pt \"century gothic\";\n"
"color: white;\n"
"border: none;\n"
"")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(107, 230, 151, 56))
        self.label_6.setStyleSheet(u"font: 26pt \"century gothic\";\n"
"color: white;\n"
"border: none;\n"
"")
        self.confirmpass = QLineEdit(Dialog)
        self.confirmpass.setObjectName(u"confirmpass")
        self.confirmpass.setGeometry(QRect(60, 580, 301, 41))
        self.confirmpass.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"border: none;\n"
"border-bottom: 1px solid #717072")
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 570, 30, 71))
        self.label_7.setStyleSheet(u"image: url(:/logo/padlock-3-512.png);")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(15, 530, 261, 31))
        self.label_8.setStyleSheet(u"font: 18pt \"century gothic\";\n"
"color: white;\n"
"border: none;\n"
"")
        self.invalid = QLabel(Dialog)
        self.invalid.setObjectName(u"invalid")
        self.invalid.setGeometry(QRect(280, 630, 91, 17))
        self.invalid.setStyleSheet(u"font: 9pt \"century gothic\";\n"
"color: red;\n"
"border: none;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.email.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.createaccbutton.setText(QCoreApplication.translate("Dialog", u"Create Account", None))
        self.password.setInputMask("")
        self.password.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Sign Up", None))
        self.confirmpass.setText("")
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Confirm Password", None))
        self.invalid.setText(QCoreApplication.translate("Dialog", u"Invalid Email", None))
    # retranslateUi

