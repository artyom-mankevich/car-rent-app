from PyQt5.QtWidgets import QMainWindow

from extensions.table_inflater import populate_table_from_gen
from models.database import Database
from models.user_manager import UserManager
from windows.generated.ui_orders_window import Ui_MyOrders


class OrdersWindow(QMainWindow, Ui_MyOrders):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.window = None

        self.orders_table.setColumnCount(5)
        header_names = ['Date', 'Price', 'Manufacturer', 'Model', 'Dealer']
        self.orders_table.setHorizontalHeaderLabels(header_names)

        user_id = UserManager().user.id
        orders_gen = Database().get_all_orders(user_id)
        populate_table_from_gen(self.orders_table, orders_gen, col_count=5)
