# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shop_page_win.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QToolButton, QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(375, 730)
        Dialog.setStyleSheet(u"font: 14pt \"Times New Roman\";")
        self.shop_name = QLabel(Dialog)
        self.shop_name.setObjectName(u"shop_name")
        self.shop_name.setGeometry(QRect(20, 20, 31, 61))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.shop_name.setFont(font)
        self.shop_km = QLabel(Dialog)
        self.shop_km.setObjectName(u"shop_km")
        self.shop_km.setGeometry(QRect(20, 70, 61, 41))
        self.shop_km.setFont(font)
        self.shop_mins = QLabel(Dialog)
        self.shop_mins.setObjectName(u"shop_mins")
        self.shop_mins.setGeometry(QRect(90, 70, 71, 41))
        self.shop_mins.setFont(font)
        self.label_fixed_deliveryfee = QLabel(Dialog)
        self.label_fixed_deliveryfee.setObjectName(u"label_fixed_deliveryfee")
        self.label_fixed_deliveryfee.setGeometry(QRect(160, 70, 191, 41))
        self.label_fixed_deliveryfee.setFont(font)
        self.shop_delivery_fee = QLabel(Dialog)
        self.shop_delivery_fee.setObjectName(u"shop_delivery_fee")
        self.shop_delivery_fee.setGeometry(QRect(310, 70, 31, 41))
        self.shop_delivery_fee.setFont(font)
        self.basketButton = QPushButton(Dialog)
        self.basketButton.setObjectName(u"basketButton")
        self.basketButton.setGeometry(QRect(10, 650, 351, 51))
        self.basketButton.setFont(font)
        self.basketButton.setStyleSheet(u"text-align: left;")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 120, 351, 511))
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 351, 511))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 349, 509))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.toolButton = QToolButton(Dialog)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(20, 10, 31, 31))
        self.toolButton.setStyleSheet(u"image: url(:/icons/icons8-back-24.png);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.shop_name.setText(QCoreApplication.translate("Dialog", u"R1", None))
        self.shop_km.setText(QCoreApplication.translate("Dialog", u"1.5 km", None))
        self.shop_mins.setText(QCoreApplication.translate("Dialog", u"20 min", None))
        self.label_fixed_deliveryfee.setText(QCoreApplication.translate("Dialog", u"|  Delivery fee \u0e3f", None))
        self.shop_delivery_fee.setText(QCoreApplication.translate("Dialog", u"20", None))
        self.basketButton.setText(QCoreApplication.translate("Dialog", u"text", None))
        self.toolButton.setText("")
    # retranslateUi

