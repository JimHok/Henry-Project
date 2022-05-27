from operator import index
import sys
from tkinter import dialog
from PySide6 import QtWidgets
from PySide6.QtWidgets import *  # must need 3 of these lines ***
from PySide6.QtCore import *
from PySide6.QtGui import *
import shop_page_win
import basket_page_win


class ShopPage(QDialog):

    def __init__(self, item_name, item_price):

        QDialog.__init__(self, None)
        self.ui = shop_page_win.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Terbal Shop Page")

        # items name and price
        self.item_name = item_name
        self.item_price = item_price

        # Basket button
        self.item_num = 0
        self.item_txt = "Item"
        self.net_price = 0

        self.ui.basketButton.setText("  Basket • " + str(self.item_num) + " " + self.item_txt +
                                     "                              " + "฿" + str(self.net_price))

        # middle layout
        layout_middle = QVBoxLayout()

        self.amount_of_item = len(self.item_name)
        self.item_quantity = []
        self.orderButton = []

        self.item_quantity_label = []
        item_name_label = []
        item_price_label = []
        min_layout = []

        # declare each item (in this case, I use .append because I use list)
        for i in range(self.amount_of_item):
            self.item_quantity.append(0)
            self.orderButton.append(QPushButton("order", self))
            self.item_quantity_label.append(QLabel())  # quantity
            item_name_label.append(QLabel())  # name
            item_price_label.append(QLabel())  # price
            min_layout.append(QHBoxLayout())  # line by line

        for i in range(self.amount_of_item):

            item_name_label[i].setText(self.item_name[i])
            item_price_label[i].setText(str(self.item_price[i]) + "฿")
            self.item_quantity_label[i].setText(
                "x" + str(self.item_quantity[i]))

            # self.orderButton should be here(the middle), but not in for loop. I write it at almost last line
            min_layout[i].addWidget(item_name_label[i])
            min_layout[i].addWidget(item_price_label[i])
            min_layout[i].addWidget(self.item_quantity_label[i])
            min_layout[i].addWidget(self.orderButton[i])
            layout_middle.addLayout(min_layout[i])

        # order button (MUST!! not in for loop), you can design whatever other code is
        self.orderButton[0].clicked.connect(lambda: self.gotoSelectItem(0))
        self.orderButton[1].clicked.connect(lambda: self.gotoSelectItem(1))
        self.orderButton[2].clicked.connect(lambda: self.gotoSelectItem(2))
        self.orderButton[3].clicked.connect(lambda: self.gotoSelectItem(3))

        print("Program running!!")
        # basket button
        self.ui.basketButton.clicked.connect(self.gotoBasketPage)

        # scrollAreaWidgetContents is in scrollArea (they are created together)
        self.ui.scrollAreaWidgetContents.setLayout(layout_middle)

    def displayInShopPage(self, i, text):
        if text == "add":
            self.item_quantity[i] += 1
            self.item_num += 1  # for all items at basket button
            self.net_price += self.item_price[i]
        elif text == "minus":
            if self.item_quantity[i] >= 1:
                self.item_quantity[i] -= 1
                self.item_num -= 1  # for all items at basket button
                self.net_price -= self.item_price[i]

        print("Quantity: ", self.item_quantity[i], ", i: ", i)
        self.item_quantity_label[i].setText("x" + str(self.item_quantity[i]))

        if(self.item_num > 0):
            self.item_txt = "Items"

        self.ui.basketButton.setText("  Basket • " + str(self.item_num) + " " + self.item_txt +
                                     "                              " + "฿" + str(self.net_price))

    def gotoSelectItem(self, index):  # go to another screen **

        self.popup = []
        self.s_item_name = []
        self.noteToShop = []
        self.noteLineEdit = []
        layout_control = []
        plus_button = []
        minus_button = []
        self.addToBasketButton = []
        self.item_amount_label = []
        self.item_amount = []
        layout_big = []
        self.item_pic = []

        pic_name = ["pic/Fa_talaijord.jpeg",
                    "pic/poi_sian.jpeg",
                    "pic/propoliz.jpeg",
                    "pic/yan_hee.jpeg"]

        for i in range(self.amount_of_item):
            diag = QDialog(self)
            diag.setFixedSize(375, 600)
            diag.setWindowTitle("Select amount of items")

            self.popup.append(diag)
            layout_big.append(QVBoxLayout())
            self.s_item_name.append(QLabel(self))
            self.noteToShop.append(QLabel(self))
            self.noteLineEdit.append(QLineEdit(self))
            layout_control.append(QHBoxLayout())
            plus_button.append(QPushButton("+", self))
            minus_button.append(QPushButton("-", self))
            self.item_pic.append(QLabel(self))

            # ori 0, can use index or i are the same o/p
            self.item_amount.append(self.item_quantity[index])

            self.item_amount_label.append(QLabel(self))
            addBasketButton = QPushButton(self)
            self.addToBasketButton.append(addBasketButton)

        for i in range(self.amount_of_item):
            # # customize button
            # plus_button[i].setGeometry(QRect(210, 550, 51, 51))
            # minus_button[i].setGeometry(QRect(100, 550, 51, 51))
            fontB = QFont()
            fontB.setPointSize(28)
            plus_button[i].setFont(fontB)
            minus_button[i].setFont(fontB)
            # self.item_pic[i].setGeometry(QRect(20, 20, 331, 171)) # 331 171
            self.item_pic[i].setPixmap(QPixmap(pic_name[i]))
            self.item_pic[i].setAlignment(Qt.AlignCenter)
            layout_big[i].addWidget(self.item_pic[i])

            self.s_item_name[i].setText(
                self.item_name[i] + "  \n" + str(self.item_price[i]) + "฿")  # item name
            font1 = QFont()
            font1.setPointSize(24)
            self.s_item_name[i].setFont(font1)
            layout_big[i].addWidget(self.s_item_name[i])

            self.noteToShop[i].setText("Note to shop")
            font2 = QFont()
            font2.setPointSize(18)
            self.noteToShop[i].setFont(font2)
            layout_big[i].addWidget(self.noteToShop[i])

            self.noteLineEdit[i].setPlaceholderText("Add your request")
            self.noteLineEdit[i].setFont(font2)
            layout_big[i].addWidget(self.noteLineEdit[i])

            font3 = QFont()
            font3.setPointSize(26)
            self.item_amount_label[i].setFont(font3)
            self.item_amount_label[i].setAlignment(Qt.AlignCenter)
            # if self.item_amount[i] == 0:
            #     self.item_amount[i] = 1 # if u want to start with 1
            self.item_amount_label[i].setText(str(self.item_amount[i]))
            layout_control[i].addWidget(minus_button[i])
            layout_control[i].addWidget(self.item_amount_label[i])
            layout_control[i].addWidget(plus_button[i])
            layout_big[i].addLayout(layout_control[i])

            # may be cutomize self.addToBasketButton
            font4 = QFont()
            font4.setPointSize(24)
            self.addToBasketButton[i].setLayoutDirection(Qt.LeftToRight)
            self.addToBasketButton[i].setStyleSheet(u"text-align: left;")
            self.addToBasketButton[i].setFont(font4)
            self.addToBasketButton[i].setText(
                "Add to Basket                    ฿" + str(self.item_price[i] * self.item_amount[i]))

            layout_big[i].addWidget(self.addToBasketButton[i])

            self.popup[i].setLayout(layout_big[i])

        plus_button[0].clicked.connect(lambda: self.addAmount(0))
        plus_button[1].clicked.connect(lambda: self.addAmount(1))
        plus_button[2].clicked.connect(lambda: self.addAmount(2))
        plus_button[3].clicked.connect(lambda: self.addAmount(3))

        minus_button[0].clicked.connect(lambda: self.minusAmount(0))
        minus_button[1].clicked.connect(lambda: self.minusAmount(1))
        minus_button[2].clicked.connect(lambda: self.minusAmount(2))
        minus_button[3].clicked.connect(lambda: self.minusAmount(3))

        self.addToBasketButton[0].clicked.connect(self.popup[0].close)
        self.addToBasketButton[1].clicked.connect(self.popup[1].close)
        self.addToBasketButton[2].clicked.connect(self.popup[2].close)
        self.addToBasketButton[3].clicked.connect(self.popup[3].close)

        self.popup[index].show()

    def addAmount(self, i):
        self.item_amount[i] += 1
        if self.item_amount[i] > 0:
            self.orderButton[i].setText("change")

        self.displayInPopUp(i)
        self.displayInShopPage(i, "add")

    def minusAmount(self, i):
        self.item_amount[i] -= 1
        if self.item_amount[i] == 0:
            self.orderButton[i].setText("order")
        elif self.item_amount[i] < 0:
            self.item_amount[i] = 0

        self.displayInPopUp(i)
        self.displayInShopPage(i, "minus")

    def displayInPopUp(self, i):
        self.item_amount_label[i].setText(str(self.item_amount[i]))
        self.addToBasketButton[i].setText(
            "Add to Basket                    ฿" + str(self.item_price[i] * self.item_amount[i]))
        print("Amount: ", self.item_amount[i], ", i: ", i)

    def gotoBasketPage(self):
        print("Basket button is clicked!!")

        basketPage = BasketPage(
            self.item_name, self.item_price, self.item_quantity, self.net_price)

        widget.addWidget(basketPage)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class BasketPage(QDialog):

    def __init__(self, item_name, item_price, item_quantity, all_food_price):

        QDialog.__init__(self, None)
        self.ui = basket_page_win.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Basket Page")
        self.ui.basketBackButton.clicked.connect(self.goBackToShopPage)

        # set value
        self.item_quantity = item_quantity  # list
        self.item_name = item_name  # list
        self.item_price = item_price  # list
        self.all_food_price = all_food_price

        print("Name: ", self.item_name)
        print("Price: ", self.item_price)
        print("Quantity: ", self.item_quantity)
        print("All food price: ", self.all_food_price)

        layout_middle = QVBoxLayout()
        self.amount_of_item = len(self.item_name)

        item_quantity_label = []
        item_name_label = []
        item_price_label = []
        min_layout = []

        for i in range(self.amount_of_item):
            item_quantity_label.append(QLabel())  # quantity
            item_name_label.append(QLabel())  # name
            item_price_label.append(QLabel())  # price
            min_layout.append(QHBoxLayout())  # line by line

        for i in range(self.amount_of_item):
            item_quantity_label[i].setText("x" + str(self.item_quantity[i]))
            item_name_label[i].setText(self.item_name[i])
            item_price_label[i].setText(
                str(self.item_price[i] * self.item_quantity[i]) + "฿")

            min_layout[i].addWidget(item_quantity_label[i])
            min_layout[i].addWidget(item_name_label[i])
            min_layout[i].addWidget(item_price_label[i])
            layout_middle.addLayout(min_layout[i])

        self.ui.basketScrollAreaWidgetContents.setLayout(layout_middle)

        # set the value in UI window
        self.deliveryFee = 20
        self.ui.all_food_price_label.setText("฿" + str(self.all_food_price))
        self.ui.delivery_fee_label.setText("฿" + str(self.deliveryFee))

        self.total_price = self.all_food_price + self.deliveryFee
        self.ui.total_price_label.setText("฿" + str(self.total_price))

        self.ui.placeOrderButton.clicked.connect(self.confirmOrder)

    # set when ผ่านหน้าเลือกร้านมา เพื่อทำให้รู้ว่าคือร้านไหน ชื่ออะไร จากการใช้ i

    def setIndexOfShop(self, i):  # ใช้ obj แล้ว call เลย
        pass

    # def getIndexOfShop(self):
    #     return int(self.deliveryFee)

    def confirmOrder(self):

        print("Order Confirm:")
        print("Item name: ", self.item_name)
        print("Item price: ", self.item_price)
        print("Item quantity: ", self.item_quantity)
        print("Payment method: ", self.ui.paymentMethodComboBox.currentText())

    def goBackToShopPage(self):
        basketPage = BasketPage(
            self.item_name, self.item_price, self.item_quantity, self.all_food_price)

        widget.removeWidget(basketPage)
        widget.addWidget(shopPage)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# main func
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # items name and price
    item_name = ["อ้วยอันโอสถ \nยาแคปซูลฟ้าทะลายโจรสกัด",
                 "ยันฮี ยาฟาร์แท็บ ฟ้าทะลายโจร", "Ya Dom Poi-Sian", "Propoliz mouth spray"]
    item_price = [120, 80, 20, 90]

    shopPage = ShopPage(item_name, item_price)
    shopPage.show()

    # just add *
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(shopPage)
    widget.setFixedSize(375, 730)
    widget.setWindowTitle("Shop Page")
    widget.show()

    app.exec()
