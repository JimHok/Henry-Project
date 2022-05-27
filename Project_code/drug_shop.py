# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'drug_shop.ui'
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
    QPushButton, QSizePolicy, QToolButton, QWidget)
import search

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(375, 730)
        Dialog.setLayoutDirection(Qt.LeftToRight)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: #DAE5D0;\n"
"}")
        self.search_icon = QLabel(Dialog)
        self.search_icon.setObjectName(u"search_icon")
        self.search_icon.setGeometry(QRect(310, 10, 31, 31))
        self.search_icon.setStyleSheet(u"")
        self.search_icon.setPixmap(QPixmap(u":/searchicon/icons8-search-24.png"))
        self.SearchBar = QLineEdit(Dialog)
        self.SearchBar.setObjectName(u"SearchBar")
        self.SearchBar.setEnabled(True)
        self.SearchBar.setGeometry(QRect(30, 10, 311, 31))
        self.SearchBar.setStyleSheet(u"QLineEdit {\n"
"	background-color: white;\n"
"	font: 11pt \"Segoe UI\";\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #00FFAB;\n"
"	background-color: #EEEEEE;\n"
"}")
        self.SearchBar.setFrame(False)
        self.SearchBar.setAlignment(Qt.AlignCenter)
        self.SearchBar.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.shop_r1 = QWidget(Dialog)
        self.shop_r1.setObjectName(u"shop_r1")
        self.shop_r1.setGeometry(QRect(30, 80, 121, 141))
        self.shop_r1.setStyleSheet(u"QWidget{\n"
"	background-color: #C2DED1;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border: 2px solid #14C38E;\n"
"}")
        self.shop_r1_pic = QLabel(self.shop_r1)
        self.shop_r1_pic.setObjectName(u"shop_r1_pic")
        self.shop_r1_pic.setGeometry(QRect(40, 10, 51, 51))
        self.shop_r1_pic.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_r1_pic.setPixmap(QPixmap(u":/searchicon/icons8-drug-50.png"))
        self.shop_time_r1 = QLabel(self.shop_r1)
        self.shop_time_r1.setObjectName(u"shop_time_r1")
        self.shop_time_r1.setGeometry(QRect(10, 90, 41, 16))
        self.shop_time_r1.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_distance_r1 = QLabel(self.shop_r1)
        self.shop_distance_r1.setObjectName(u"shop_distance_r1")
        self.shop_distance_r1.setGeometry(QRect(80, 90, 31, 16))
        self.shop_distance_r1.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.pushButton = QPushButton(self.shop_r1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 110, 75, 24))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: #15133C;\n"
"	border: 1px solid rgb(111,218,156);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: #EFEAD8;\n"
"	background: #6D8B74;\n"
"	border: 1px solid #D0C9C0;\n"
"}")
        self.shop_name_r1 = QLabel(self.shop_r1)
        self.shop_name_r1.setObjectName(u"shop_name_r1")
        self.shop_name_r1.setGeometry(QRect(20, 70, 81, 16))
        self.shop_name_r1.setStyleSheet(u"QLabel{\n"
"	border-radius: 0px;\n"
"	border: none;\n"
"}")
        self.shop_name_r1.setAlignment(Qt.AlignCenter)
        self.shop_r2 = QWidget(Dialog)
        self.shop_r2.setObjectName(u"shop_r2")
        self.shop_r2.setGeometry(QRect(220, 80, 121, 141))
        self.shop_r2.setStyleSheet(u"QWidget{\n"
"	background-color: #C2DED1;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border: 2px solid #14C38E;\n"
"}")
        self.shop_r2_pic = QLabel(self.shop_r2)
        self.shop_r2_pic.setObjectName(u"shop_r2_pic")
        self.shop_r2_pic.setGeometry(QRect(40, 10, 51, 61))
        self.shop_r2_pic.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_r2_pic.setPixmap(QPixmap(u":/searchicon/icons8-drug-50 (1).png"))
        self.shop_name_r1_2 = QLabel(self.shop_r2)
        self.shop_name_r1_2.setObjectName(u"shop_name_r1_2")
        self.shop_name_r1_2.setGeometry(QRect(20, 70, 71, 16))
        self.shop_name_r1_2.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_name_r1_2.setAlignment(Qt.AlignCenter)
        self.shop_time_r1_2 = QLabel(self.shop_r2)
        self.shop_time_r1_2.setObjectName(u"shop_time_r1_2")
        self.shop_time_r1_2.setGeometry(QRect(10, 90, 41, 16))
        self.shop_time_r1_2.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_distance_r1_2 = QLabel(self.shop_r2)
        self.shop_distance_r1_2.setObjectName(u"shop_distance_r1_2")
        self.shop_distance_r1_2.setGeometry(QRect(80, 90, 31, 16))
        self.shop_distance_r1_2.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.pushButton_2 = QPushButton(self.shop_r2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 110, 75, 24))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: #15133C;\n"
"	border: 1px solid rgb(111,218,156);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: #EFEAD8;\n"
"	background: #6D8B74;\n"
"	border: 1px solid #D0C9C0;\n"
"}")
        self.shop_r3 = QWidget(Dialog)
        self.shop_r3.setObjectName(u"shop_r3")
        self.shop_r3.setGeometry(QRect(30, 280, 121, 141))
        self.shop_r3.setStyleSheet(u"QWidget{\n"
"	background-color: #C2DED1;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border: 2px solid #14C38E;\n"
"}")
        self.shop_r3_pic = QLabel(self.shop_r3)
        self.shop_r3_pic.setObjectName(u"shop_r3_pic")
        self.shop_r3_pic.setGeometry(QRect(40, 10, 51, 61))
        self.shop_r3_pic.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_r3_pic.setPixmap(QPixmap(u":/searchicon/icons8-drug-50 (2).png"))
        self.shop_name_r1_3 = QLabel(self.shop_r3)
        self.shop_name_r1_3.setObjectName(u"shop_name_r1_3")
        self.shop_name_r1_3.setGeometry(QRect(20, 70, 81, 20))
        self.shop_name_r1_3.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_name_r1_3.setAlignment(Qt.AlignCenter)
        self.shop_time_r1_3 = QLabel(self.shop_r3)
        self.shop_time_r1_3.setObjectName(u"shop_time_r1_3")
        self.shop_time_r1_3.setGeometry(QRect(10, 90, 41, 16))
        self.shop_time_r1_3.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_distance_r1_3 = QLabel(self.shop_r3)
        self.shop_distance_r1_3.setObjectName(u"shop_distance_r1_3")
        self.shop_distance_r1_3.setGeometry(QRect(80, 90, 31, 16))
        self.shop_distance_r1_3.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.pushButton_3 = QPushButton(self.shop_r3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 110, 75, 24))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: #15133C;\n"
"	border: 1px solid rgb(111,218,156);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: #EFEAD8;\n"
"	background: #6D8B74;\n"
"	border: 1px solid #D0C9C0;\n"
"}")
        self.shop_r4 = QWidget(Dialog)
        self.shop_r4.setObjectName(u"shop_r4")
        self.shop_r4.setGeometry(QRect(220, 280, 121, 141))
        self.shop_r4.setStyleSheet(u"QWidget{\n"
"	background-color: #C2DED1;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border: 2px solid #14C38E;\n"
"}")
        self.shop_r4_pic = QLabel(self.shop_r4)
        self.shop_r4_pic.setObjectName(u"shop_r4_pic")
        self.shop_r4_pic.setGeometry(QRect(30, 10, 61, 61))
        self.shop_r4_pic.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_r4_pic.setPixmap(QPixmap(u":/searchicon/icons8-herbal-64.png"))
        self.shop_name_r1_4 = QLabel(self.shop_r4)
        self.shop_name_r1_4.setObjectName(u"shop_name_r1_4")
        self.shop_name_r1_4.setGeometry(QRect(20, 70, 71, 20))
        self.shop_name_r1_4.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_name_r1_4.setAlignment(Qt.AlignCenter)
        self.shop_time_r1_4 = QLabel(self.shop_r4)
        self.shop_time_r1_4.setObjectName(u"shop_time_r1_4")
        self.shop_time_r1_4.setGeometry(QRect(10, 90, 41, 16))
        self.shop_time_r1_4.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_distance_r1_4 = QLabel(self.shop_r4)
        self.shop_distance_r1_4.setObjectName(u"shop_distance_r1_4")
        self.shop_distance_r1_4.setGeometry(QRect(80, 90, 31, 16))
        self.shop_distance_r1_4.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.pushButton_4 = QPushButton(self.shop_r4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 110, 75, 24))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: #15133C;\n"
"	border: 1px solid rgb(111,218,156);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: #EFEAD8;\n"
"	background: #6D8B74;\n"
"	border: 1px solid #D0C9C0;\n"
"}")
        self.shop_r5 = QWidget(Dialog)
        self.shop_r5.setObjectName(u"shop_r5")
        self.shop_r5.setGeometry(QRect(30, 480, 121, 141))
        self.shop_r5.setStyleSheet(u"QWidget{\n"
"	background-color: #C2DED1;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border: 2px solid #14C38E;\n"
"}")
        self.shop_r5_pic = QLabel(self.shop_r5)
        self.shop_r5_pic.setObjectName(u"shop_r5_pic")
        self.shop_r5_pic.setGeometry(QRect(40, 10, 51, 61))
        self.shop_r5_pic.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_r5_pic.setPixmap(QPixmap(u":/searchicon/icons8-healthy-food-50.png"))
        self.shop_name_r1_5 = QLabel(self.shop_r5)
        self.shop_name_r1_5.setObjectName(u"shop_name_r1_5")
        self.shop_name_r1_5.setGeometry(QRect(30, 70, 61, 20))
        self.shop_name_r1_5.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_name_r1_5.setAlignment(Qt.AlignCenter)
        self.shop_time_r1_5 = QLabel(self.shop_r5)
        self.shop_time_r1_5.setObjectName(u"shop_time_r1_5")
        self.shop_time_r1_5.setGeometry(QRect(10, 90, 41, 16))
        self.shop_time_r1_5.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_distance_r1_5 = QLabel(self.shop_r5)
        self.shop_distance_r1_5.setObjectName(u"shop_distance_r1_5")
        self.shop_distance_r1_5.setGeometry(QRect(70, 90, 41, 16))
        self.shop_distance_r1_5.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.pushButton_5 = QPushButton(self.shop_r5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 110, 75, 24))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: #15133C;\n"
"	border: 1px solid rgb(111,218,156);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: #EFEAD8;\n"
"	background: #6D8B74;\n"
"	border: 1px solid #D0C9C0;\n"
"}")
        self.shop_r6 = QWidget(Dialog)
        self.shop_r6.setObjectName(u"shop_r6")
        self.shop_r6.setGeometry(QRect(220, 480, 121, 141))
        self.shop_r6.setStyleSheet(u"QWidget{\n"
"	background-color: #C2DED1;\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"	border: 2px solid #14C38E;\n"
"}")
        self.shop_r6_pic = QLabel(self.shop_r6)
        self.shop_r6_pic.setObjectName(u"shop_r6_pic")
        self.shop_r6_pic.setGeometry(QRect(30, 10, 61, 61))
        self.shop_r6_pic.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_r6_pic.setPixmap(QPixmap(u":/searchicon/icons8-natural-food-64.png"))
        self.shop_name_r1_6 = QLabel(self.shop_r6)
        self.shop_name_r1_6.setObjectName(u"shop_name_r1_6")
        self.shop_name_r1_6.setGeometry(QRect(20, 70, 81, 16))
        self.shop_name_r1_6.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_name_r1_6.setAlignment(Qt.AlignCenter)
        self.shop_time_r1_6 = QLabel(self.shop_r6)
        self.shop_time_r1_6.setObjectName(u"shop_time_r1_6")
        self.shop_time_r1_6.setGeometry(QRect(10, 90, 41, 16))
        self.shop_time_r1_6.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.shop_distance_r1_6 = QLabel(self.shop_r6)
        self.shop_distance_r1_6.setObjectName(u"shop_distance_r1_6")
        self.shop_distance_r1_6.setGeometry(QRect(70, 90, 41, 16))
        self.shop_distance_r1_6.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"}")
        self.pushButton_6 = QPushButton(self.shop_r6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 110, 75, 24))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	background-color: white;\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: #15133C;\n"
"	border: 1px solid rgb(111,218,156);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: #EFEAD8;\n"
"	background: #6D8B74;\n"
"	border: 1px solid #D0C9C0;\n"
"}")
        self.profile_icon = QToolButton(Dialog)
        self.profile_icon.setObjectName(u"profile_icon")
        self.profile_icon.setGeometry(QRect(20, 690, 141, 31))
        self.profile_icon.setStyleSheet(u"QToolButton{\n"
"	background-color: white;\n"
"	font: 11pt \"Segoe UI\";\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	image: url(:/searchicon/icons8-male-user-48.png);\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"	color: #00FFAB;\n"
"	border-color: #00FFAB;\n"
"	background-color: #EEEEEE;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"	image: url(:/searchicon/icons8-male-user-48 (1).png);\n"
"	background: #6D8B74;\n"
"	border: 1px solid #D0C9C0;\n"
"}")
        self.profile_icon.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.home_icon = QToolButton(Dialog)
        self.home_icon.setObjectName(u"home_icon")
        self.home_icon.setGeometry(QRect(210, 690, 141, 31))
        self.home_icon.setStyleSheet(u"QToolButton{\n"
"	\n"
"	image: url(:/searchicon/icons8-home-48 1.png);\n"
"	background-color: white;\n"
"	font: 11pt \"Segoe UI\";\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"	color: #00FFAB;\n"
"	border-color: #00FFAB;\n"
"	background-color: #EEEEEE;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"	image: url(:/searchicon/icons8-home-48.png);\n"
"	background: #6D8B74;\n"
"	border: 1px solid #D0C9C0;\n"
"}")
        self.home_icon.setIconSize(QSize(12, 12))
        self.SearchBar.raise_()
        self.search_icon.raise_()
        self.shop_r1.raise_()
        self.shop_r2.raise_()
        self.shop_r3.raise_()
        self.shop_r4.raise_()
        self.shop_r5.raise_()
        self.shop_r6.raise_()
        self.profile_icon.raise_()
        self.home_icon.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.search_icon.setText("")
        self.SearchBar.setPlaceholderText(QCoreApplication.translate("Dialog", u"Search", None))
        self.shop_r1_pic.setText("")
        self.shop_time_r1.setText(QCoreApplication.translate("Dialog", u"20 min", None))
        self.shop_distance_r1.setText(QCoreApplication.translate("Dialog", u"1.5km", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Order", None))
        self.shop_name_r1.setText(QCoreApplication.translate("Dialog", u"ArinCare", None))
        self.shop_r2_pic.setText("")
        self.shop_name_r1_2.setText(QCoreApplication.translate("Dialog", u"BeeCare", None))
        self.shop_time_r1_2.setText(QCoreApplication.translate("Dialog", u"25 min", None))
        self.shop_distance_r1_2.setText(QCoreApplication.translate("Dialog", u"3km", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Order", None))
        self.shop_r3_pic.setText("")
        self.shop_name_r1_3.setText(QCoreApplication.translate("Dialog", u"Terbal Offical", None))
        self.shop_time_r1_3.setText(QCoreApplication.translate("Dialog", u"30 min", None))
        self.shop_distance_r1_3.setText(QCoreApplication.translate("Dialog", u"4km", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Order", None))
        self.shop_r4_pic.setText("")
        self.shop_name_r1_4.setText(QCoreApplication.translate("Dialog", u"PrukSa", None))
        self.shop_time_r1_4.setText(QCoreApplication.translate("Dialog", u"10 min", None))
        self.shop_distance_r1_4.setText(QCoreApplication.translate("Dialog", u"1 km", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Order", None))
        self.shop_r5_pic.setText("")
        self.shop_name_r1_5.setText(QCoreApplication.translate("Dialog", u"Tumrub tai", None))
        self.shop_time_r1_5.setText(QCoreApplication.translate("Dialog", u"30 min", None))
        self.shop_distance_r1_5.setText(QCoreApplication.translate("Dialog", u"4.5 km", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Order", None))
        self.shop_r6_pic.setText("")
        self.shop_name_r1_6.setText(QCoreApplication.translate("Dialog", u"Ginjai", None))
        self.shop_time_r1_6.setText(QCoreApplication.translate("Dialog", u"15 min", None))
        self.shop_distance_r1_6.setText(QCoreApplication.translate("Dialog", u"1.5 km", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Order", None))
        self.profile_icon.setText("")
        self.home_icon.setText("")
    # retranslateUi

