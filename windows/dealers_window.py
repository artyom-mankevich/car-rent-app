from PyQt5.QtWidgets import QMainWindow

from extensions.table_inflater import populate_table_from_gen
from models.database import Database
from windows.generated.ui_dealers_window import Ui_DealersWindow


class DealersWindow(QMainWindow, Ui_DealersWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.window = None
        self.dealers_table.setColumnCount(5)
        self.header_names = ['Name', 'House', 'Street', 'City', 'Region']
        self.dealers_table.setHorizontalHeaderLabels(self.header_names)
        dealers_gen = Database().get_all_dealerships()
        populate_table_from_gen(self.dealers_table, dealers_gen, col_count=5)
