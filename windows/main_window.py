from PyQt5.QtWidgets import QMainWindow

import windows.cars_window as carw
import windows.dealers_window as dealerw
import windows.orders_window as orderw
import windows.startup_window as startw
from extensions.input_sanitizer import check_search
from models.user_manager import UserManager
from windows.generated.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.window = None
        self.user_manager = UserManager()

        self.logout_button.clicked.connect(self.logout_clicked)
        self.cars_button.clicked.connect(self.cars_clicked)
        self.search_button.clicked.connect(self.search_clicked)
        self.dealerships_button.clicked.connect(self.dealers_clicked)
        self.myorders_button.clicked.connect(self.myorders_clicked)

        if self.user_manager.user.is_staff:
            pass

    def logout_clicked(self):
        self.user_manager.logout()

        self.window = startw.StartupWindow()
        self.window.show()
        self.close()

    def cars_clicked(self):
        self.window = carw.CarsWindow()
        self.window.show()

    def search_clicked(self):
        search_text = self.search_edit.text()
        if check_search(search_text):
            self.window = carw.CarsWindow(self.search_edit.text())
            self.window.show()
            self.search_edit.clear()
        else:
            self.search_edit.setText("Input error")

    def dealers_clicked(self):
        self.window = dealerw.DealersWindow()
        self.window.show()

    def myorders_clicked(self):
        self.window = orderw.OrdersWindow()
        self.window.show()
