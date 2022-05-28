# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'shop_page_win.ui'
##
# Created by: Qt User Interface Compiler version 6.2.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
                               QScrollArea, QSizePolicy, QToolButton, QWidget)
import search


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(375, 728)
        Dialog.setStyleSheet(u"*{\n"
                             "	font: 14pt \"Times New Roman\";\n"
                             "}\n"
                             "\n"
                             "QDialog{\n"
                             "	background-color: #DAE5D0;\n"
                             "}")
        self.shop_name = QLabel(Dialog)
        self.shop_name.setObjectName(u"shop_name")
        self.shop_name.setGeometry(QRect(90, 20, 181, 51))
        font = QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        self.shop_name.setFont(font)
        self.shop_name.setStyleSheet(u"QLabel{\n"
                                     "	font: 25pt \"Calibri\";\n"
                                     "	background-color: #C2DED1;\n"
                                     "	border: 2px solid #14C38E;\n"
                                     "	border-top-left-radius: 15px;\n"
                                     "	border-bottom-right-radius: 15px;\n"
                                     "}\n"
                                     "\n"
                                     "")
        self.shop_km = QLabel(Dialog)
        self.shop_km.setObjectName(u"shop_km")
        self.shop_km.setGeometry(QRect(30, 70, 51, 41))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.shop_km.setFont(font1)
        self.shop_mins = QLabel(Dialog)
        self.shop_mins.setObjectName(u"shop_mins")
        self.shop_mins.setGeometry(QRect(90, 70, 61, 41))
        self.shop_mins.setFont(font1)
        self.shop_delivery_fee = QLabel(Dialog)
        self.shop_delivery_fee.setObjectName(u"shop_delivery_fee")
        self.shop_delivery_fee.setGeometry(QRect(300, 70, 31, 41))
        self.shop_delivery_fee.setFont(font1)
        self.basketButton = QPushButton(Dialog)
        self.basketButton.setObjectName(u"basketButton")
        self.basketButton.setGeometry(QRect(10, 650, 351, 51))
        self.basketButton.setFont(font1)
        self.basketButton.setStyleSheet(u"QPushButton{\n"
                                        "	text-align: left;\n"
                                        "	border-radius: 10px;\n"
                                        "	background-color: rgb(57, 68, 84);\n"
                                        "	color: white;\n"
                                        "	border: 5px solid rgb(111, 218, 156);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "	border: 4px solid green;\n"
                                        "	background-color: rgb(80, 110, 125);\n"
                                        "}")
        self.basketButton.setAutoExclusive(False)
        self.basketButton.setAutoDefault(True)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 120, 351, 511))
        self.widget.setStyleSheet(u"QWidget{\n"
                                  "	background-color: #DAE5D0;\n"
                                  "	border-top-left-radius: 15px;\n"
                                  "	border-bottom-right-radius: 15px;\n"
                                  "}")
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 351, 511))
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
                                      "	border: 6px inset #14C38E\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 339, 499))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_fixed_deliveryfee = QLabel(Dialog)
        self.label_fixed_deliveryfee.setObjectName(u"label_fixed_deliveryfee")
        self.label_fixed_deliveryfee.setGeometry(QRect(170, 70, 121, 41))
        self.label_fixed_deliveryfee.setFont(font1)
        self.toolButton = QToolButton(Dialog)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(20, 20, 41, 41))
        self.toolButton.setStyleSheet(u"QToolButton{\n"
                                      "	\n"
                                      "	image: url(:/searchicon/icons8-left-arrow-26.png);\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton{\n"
                                      "	background-color: rgb(111, 218, 156);\n"
                                      "	border-radius: 15px;\n"
                                      "}\n"
                                      "\n"
                                      "QToolButton:hover{\n"
                                      "	border:1px solid black;\n"
                                      "	background-color: rgb(140, 238, 179)\n"
                                      "}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.shop_name.setText(QCoreApplication.translate(
            "Dialog", u"Shop name", None))
        self.shop_km.setText(
            QCoreApplication.translate("Dialog", u"10 km", None))
        self.shop_mins.setText(
            QCoreApplication.translate("Dialog", u"50 mins", None))
        self.shop_delivery_fee.setText(
            QCoreApplication.translate("Dialog", u"20", None))
        self.basketButton.setText(
            QCoreApplication.translate("Dialog", u" Text", None))
        self.label_fixed_deliveryfee.setText(
            QCoreApplication.translate("Dialog", u"| Delivery fee", None))
        self.toolButton.setText("")
    # retranslateUi
