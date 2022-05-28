# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'orderhistory.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
                               QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
                               QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(375, 730)
        self.history_order = QLabel(Dialog)
        self.history_order.setObjectName(u"history_order")
        self.history_order.setGeometry(QRect(10, 50, 241, 51))
        self.history_order.setStyleSheet(u"font: 24pt \"MS Shell Dlg 2\";")
        self.orderBackButton = QPushButton(Dialog)
        self.orderBackButton.setObjectName(u"orderBackButton")
        self.orderBackButton.setGeometry(QRect(10, 10, 41, 41))
        font = QFont()
        font.setPointSize(16)
        self.orderBackButton.setFont(font)
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 110, 351, 601))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.history_order.setText(QCoreApplication.translate(
            "Dialog", u"Order History", None))
        self.orderBackButton.setText(
            QCoreApplication.translate("Dialog", u"<", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("Dialog", u"Date", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("Dialog", u"Shop", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("Dialog", u"Item", None))
    # retranslateUi
