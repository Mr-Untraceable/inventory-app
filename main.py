import os
from PyQt5 import QtGui, uic, QtWidgets, Qt
from functools import partial
import login
import tkinter as tk
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import subprocess

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


main_path = resource_path('ui/main.ui')
Form, Base = uic.loadUiType(main_path)


class Users:
    pass


class MainWidget(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.showMaximized()

        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(0)
        self.display_msg = QtWidgets.QMessageBox()
        self.display_msg.setIcon(QtWidgets.QMessageBox.Information)

        self.homepage.suppliersButton.clicked.connect(partial(self.pageChanger, 1))  # 1
        self.homepage.ordersButton.clicked.connect(partial(self.pageChanger, 2))
        self.homepage.billingButton.clicked.connect(partial(self.pageChanger, 3))
        self.homepage.customerButton.clicked.connect(partial(self.pageChanger, 4))
        self.homepage.pricingButton.clicked.connect(partial(self.pageChanger, 5))
        self.homepage.stocksButton.clicked.connect(partial(self.pageChanger, 6))

        self.supplier.actionBack.triggered.connect(partial(self.pageChanger, 0))
        self.billing.actionBack.triggered.connect(partial(self.pageChanger, 0))
        self.contact.actionBack.triggered.connect(partial(self.pageChanger, 0))
        self.order.actionBack.triggered.connect(partial(self.pageChanger, 0))
        self.stock.actionBack.triggered.connect(partial(self.pageChanger, 0))
        self.pricing.actionBack.triggered.connect(partial(self.pageChanger, 0))

        # logout button #
        self.homepage.logoutButton.clicked.connect(self.logout)
        self.homepage.pushButton.clicked.connect(self.support)

    def pageChanger(self, i):
        self.stackedWidget.setCurrentIndex(i)



    def support(self):
        file_path = 'tkinter_dt.py'  # Replace with the actual path to the tkinter_dt.py file

        try:
            subprocess.run(['python', file_path], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to execute the file: {e}")

    def logout(self):
        self.loginpage = login.loginWindow()
        self.loginpage.show()
        self.close()

    def fetchUsername(self, name):
        self.username = name
        self.homepage.label_8.setText(name)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = MainWidget()
    w.show()
    sys.exit(app.exec_())
