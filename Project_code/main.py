import profile
import sys
import os
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import login_screen_new
import createacc
import profile
from pyrebase import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests
import drug_shop
import shop_page_win
import basket_page_win


cred = credentials.Certificate(
    r'C:\Users\jimyj\Desktop\Code\Python\Practices\Firebase\Henry Project new\Project_code\TestAccountKey.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-26b5b-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('Users/')

# for authentication
firebaseConfig = {"apiKey": "AIzaSyCQq2Pz8QW8STqDu8BbehbHAOxff8boaIo",
                  "authDomain": "test-26b5b.firebaseapp.com",
                  "databaseURL": "https://test-26b5b-default-rtdb.asia-southeast1.firebasedatabase.app",
                  "projectId": "test-26b5b",
                  "storageBucket": "test-26b5b.appspot.com",
                  "messagingSenderId": "856362923148",
                  "appId": "1:856362923148:web:625e1076eda813e5d737a9",
                  "measurementId": "G-3YHK5K5JR4"}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

shop_number = [0]


class Login(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)

        self.ui = login_screen_new.Ui_Dialog()  # load the login ui
        self.ui.setupUi(self)
        self.setWindowTitle("Terbal")

        self.ui.loginbutton.clicked.connect(self.loginfunction)
        self.ui.password.setEchoMode(
            QtWidgets.QLineEdit.Password)  # make password into dots
        self.ui.signupbutton.clicked.connect(self.gotocreate)
        self.ui.invalid_login.setVisible(False)

    def loginfunction(self):
        email = self.ui.email.text()
        password = self.ui.password.text()
        try:
            auth.sign_in_with_email_and_password(email, password)
            home = Shop()
            login = Login()
            widget.removeWidget(login)
            widget.addWidget(home)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            self.ui.invalid_login.setVisible(True)

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAcc(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)

        self.ui = createacc.Ui_Dialog()  # load create acc ui
        self.ui.setupUi(self)
        self.setWindowTitle("Terbal")

        self.ui.createaccbutton.clicked.connect(self.createaccfunction)
        self.ui.password.setEchoMode(
            QtWidgets.QLineEdit.Password)  # hide password
        self.ui.confirmpass.setEchoMode(
            QtWidgets.QLineEdit.Password)  # hide confirm password
        # when register email failed will show up
        self.ui.invalid.setVisible(False)

    def createaccfunction(self):
        email = self.ui.email.text()
        if self.ui.password.text() == self.ui.confirmpass.text():
            password = self.ui.password.text()
            try:
                auth.create_user_with_email_and_password(email, password)
                user = auth.sign_in_with_email_and_password(email, password)
                ref.child(user['localId']).set(
                    {'Email': email, 'Password': password, 'Picture': '', 'Name': '', 'Address': '', 'Mobile': ''})
                login = Login()
                createacc = CreateAcc()
                widget.removeWidget(createacc)
                widget.addWidget(login)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                self.ui.invalid.setVisible(True)


class Shop(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)

        self.ui = drug_shop.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Terbal")

        self.ui.SearchBar.returnPressed.connect(self.Search)

        self.ui.pushButton.clicked.connect(lambda: self.choosen(1))
        self.ui.pushButton_2.clicked.connect(lambda: self.choosen(2))
        self.ui.pushButton_3.clicked.connect(lambda: self.choosen(3))
        self.ui.pushButton_4.clicked.connect(lambda: self.choosen(4))
        self.ui.pushButton_5.clicked.connect(lambda: self.choosen(5))
        self.ui.pushButton_6.clicked.connect(lambda: self.choosen(6))

        self.ui.profile_icon.clicked.connect(self.profile)
        self.ui.home_icon.clicked.connect(self.choosen)

        self.shop_name = [self.ui.shop_name_r1.text(), self.ui.shop_name_r1_2.text(), self.ui.shop_name_r1_3.text(
        ), self.ui.shop_name_r1_4.text(), self.ui.shop_name_r1_5.text(), self.ui.shop_name_r1_6.text()]

    def choosen(self, shop_num):
        shop_number[0] = shop_num
        try:
            shop = ShopPage()
            home = Shop()
            widget.removeWidget(home)
            widget.addWidget(shop)
            widget.setCurrentIndex(widget.currentIndex() + 1)

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(e, exc_type, fname, exc_tb.tb_lineno)

    def profile(self):
        try:
            home = Shop()
            profile = Profile()
            widget.removeWidget(home)
            widget.addWidget(profile)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

    def Search(self):
        shop_name = [self.ui.shop_name_r1.text(), self.ui.shop_name_r1_2.text(), self.ui.shop_name_r1_3.text(),
                     self.ui.shop_name_r1_4.text(), self.ui.shop_name_r1_5.text(), self.ui.shop_name_r1_6.text()]
        widgets = []
        search_text = self.ui.SearchBar.text()
        i = 0

        for i in shop_name:
            widgets.append(i)

        self.ui.shop_r1.setVisible(False)
        self.ui.shop_r2.setVisible(False)
        self.ui.shop_r3.setVisible(False)
        self.ui.shop_r4.setVisible(False)
        self.ui.shop_r5.setVisible(False)
        self.ui.shop_r6.setVisible(False)
        search_result = [
            string for string in widgets if search_text.lower() in string.lower()]
        for i in search_result:
            if i in widgets[0]:
                self.ui.shop_r1.setVisible(True)
            if i == widgets[1]:
                self.ui.shop_r2.setVisible(True)
            if i == widgets[2]:
                self.ui.shop_r3.setVisible(True)
            if i == widgets[3]:
                self.ui.shop_r4.setVisible(True)
            if i == widgets[4]:
                self.ui.shop_r5.setVisible(True)
            if i == widgets[5]:
                self.ui.shop_r6.setVisible(True)


class Profile(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)

        self.ui = profile.Ui_Dialog()  # load create acc ui
        self.ui.setupUi(self)
        self.setWindowTitle("Terbal")

        self.ui.browsepic.clicked.connect(self.imageProf)
        self.ui.save.clicked.connect(self.saveProf)
        self.ui.logout.clicked.connect(self.logoutProf)
        self.ui.home.clicked.connect(self.gotoHome)

        self.uid = auth.current_user['localId']
        self.user = db.reference(f'Users/{self.uid}').get()
        try:
            url = self.user['Picture']
            image = QImage()
            image.loadFromData(requests.get(url).content)
            pixmap = QPixmap(image)
            self.ui.profilepic.setPixmap(pixmap.scaled(161, 151))
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            pass
        self.ui.email.setText(self.user['Email'])
        self.ui.name.setText(self.user['Name'])
        self.ui.address.setText(self.user['Address'])
        self.ui.mobile.setText(self.user['Mobile'])

    def imageProf(self):
        path = "C:\\Users\\jimyj\\Downloads"
        selected_filter = "Images (*.png *.jpg *.jpeg *.gif)"
        self.image_file = QFileDialog.getOpenFileName(
            self, 'Open file', path, selected_filter)
        label = self.ui.profilepic
        pixmap = QPixmap(self.image_file[0])
        label.setPixmap(pixmap.scaled(161, 151))

    def gotoHome(self):
        profile = Profile()
        home = Shop()
        widget.removeWidget(profile)
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def saveProf(self):
        db.reference(f'Users/{self.uid}').update(
            {'Name': self.ui.name.text(), 'Address': self.ui.address.text(), 'Mobile': self.ui.mobile.text()})
        try:
            storage = firebase.storage()
            profile_pic = f"{self.image_file[0]}"
            storage.child(f'Image/{self.uid}').put(profile_pic)
            profile_pic_url = storage.child(
                f'Image/{self.uid}').get_url(auth.current_user['idToken'])
            db.reference(
                f'Users/{self.uid}').update({'Picture': profile_pic_url})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            pass

    def logoutProf(self):
        profile = Profile()
        login = Login()
        widget.removeWidget(profile)
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ShopPage(QDialog):
    def __init__(self):

        QDialog.__init__(self, None)
        self.ui = shop_page_win.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Terbal Shop Page")

        # Basket button
        self.item_num = 0
        self.item_txt = "Item"
        self.net_price = 0
        self.shop_db = db.reference(f'Shop/R{shop_number[0]}').get()
        self.ui.shop_name.setText(self.shop_db['Name'])
        self.ui.shop_km.setText(self.shop_db['Distance'])
        self.ui.shop_mins.setText(self.shop_db['Time'])
        self.ui.shop_delivery_fee.setText(f"{str(self.shop_db['Fee'])}฿")
        self.ui.basketButton.setText("  Basket • " + str(self.item_num) + " " + self.item_txt +
                                     "                              " + "฿" + str(self.net_price))
        self.ui.toolButton.clicked.connect(self.gotoHome)
        self.ui.basketButton.clicked.connect(self.gotoBasket)

        # middle layout
        layout_middle = QVBoxLayout()

        # items name and price
        self.item_name = ["อ้วยอันโอสถ \nยาแคปซูลฟ้าทะลายโจรสกัด",
                          "ยันฮี ยาฟาร์แท็บ ฟ้าทะลายโจร", "Ya Dom Poi-Sian", "Propoliz mouth spray"]
        self.item_price = [120, 80, 20, 90]

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

        # print("Program running!!")
        self.displayInShop = False
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

    def gotoHome(self):
        try:
            shop = ShopPage()
            home = Shop()
            widget.removeWidget(shop)
            widget.addWidget(home)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except Exception as e:
            print(e)

    def gotoSelectItem(self, index):  # go to another screen **

        self.popup = []
        self.s_item_name = []
        self.noteToShop = []
        self.noteLineEdit = []
        layout_control = []
        plus_button = []
        minus_button = []
        addToBasketButton = []
        self.item_amount_label = []
        self.item_amount = []
        layout_big = []
        self.item_pic = []

        pic_name = [r"C:\Users\jimyj\Desktop\Code\Python\Practices\Firebase\Henry Project new\pic\Fa_talaijord.jpeg",
                    r"C:\Users\jimyj\Desktop\Code\Python\Practices\Firebase\Henry Project new\pic\poi_sian.jpeg",
                    r"C:\Users\jimyj\Desktop\Code\Python\Practices\Firebase\Henry Project new\pic\propoliz.jpeg",
                    r"C:\Users\jimyj\Desktop\Code\Python\Practices\Firebase\Henry Project new\pic\yan_hee.jpeg"]

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
            addToBasketButton.append(addBasketButton)

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
            self.item_amount_label[i].setText(str(self.item_amount[i]))
            layout_control[i].addWidget(minus_button[i])
            layout_control[i].addWidget(self.item_amount_label[i])
            layout_control[i].addWidget(plus_button[i])
            layout_big[i].addLayout(layout_control[i])

            # may be cutomize addToBasketButton
            font4 = QFont()
            font4.setPointSize(24)
            addToBasketButton[i].setLayoutDirection(Qt.LeftToRight)
            addToBasketButton[i].setStyleSheet(u"text-align: left;")
            addToBasketButton[i].setFont(font4)
            addToBasketButton[i].setText(
                "Add to Basket                    ฿" + str(self.item_price[i]))

            layout_big[i].addWidget(addToBasketButton[i])

            self.popup[i].setLayout(layout_big[i])

        plus_button[0].clicked.connect(lambda: self.addAmount(0))
        plus_button[1].clicked.connect(lambda: self.addAmount(1))
        plus_button[2].clicked.connect(lambda: self.addAmount(2))
        plus_button[3].clicked.connect(lambda: self.addAmount(3))

        minus_button[0].clicked.connect(lambda: self.minusAmount(0))
        minus_button[1].clicked.connect(lambda: self.minusAmount(1))
        minus_button[2].clicked.connect(lambda: self.minusAmount(2))
        minus_button[3].clicked.connect(lambda: self.minusAmount(3))

        addToBasketButton[0].clicked.connect(self.popup[0].close)
        addToBasketButton[1].clicked.connect(self.popup[1].close)
        addToBasketButton[2].clicked.connect(self.popup[2].close)
        addToBasketButton[3].clicked.connect(self.popup[3].close)

        self.popup[index].show()

    def gotoBasket(self):
        try:
            shop = ShopPage()
            basket = Basket(self.item_name, self.item_price,
                            self.item_quantity, self.net_price)
            widget.removeWidget(shop)
            widget.addWidget(basket)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except Exception as e:
            print(e)

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
        print("Amount: ", self.item_amount[i], ", i: ", i)


class Basket(QDialog):
    def __init__(self, item_name, item_price, item_quantity, all_food_price):
        QDialog.__init__(self, None)
        self.ui = basket_page_win.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Basket Page")
        self.ui.basketBackButton.clicked.connect(self.gotoShopPage)

        # set value
        self.item_quantity = item_quantity  # list
        self.item_name = item_name  # list
        self.item_price = item_price  # list
        self.all_food_price = all_food_price

        # access shop db
        self.shop_db = db.reference(f'Shop/R{shop_number[0]}').get()

        # access user db
        self.uid = auth.current_user['localId']
        self.user = db.reference(f'Users/{self.uid}').get()

        # button
        self.ui.basket_shop_name.setText(self.shop_db['Name'])
        self.ui.basket_shop_km.setText(self.shop_db['Distance'])
        self.ui.basket_shop_mins.setText(self.shop_db['Time'])
        self.ui.addressLineEdit.setText(self.user['Address'])

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

    def gotoShopPage(self):
        try:
            shop = ShopPage()
            basket = Basket(self.item_name, self.item_price,
                            self.item_quantity, self.all_food_price)
            widget.removeWidget(basket)
            widget.addWidget(shop)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Login()
    window.show()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(window)
    widget.setFixedSize(375, 730)
    widget.show()

    app.exec()
