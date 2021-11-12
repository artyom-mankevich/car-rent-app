from PyQt5.QtWidgets import QMainWindow, QMessageBox

from extensions.input_sanitizer import check_count
from extensions.table_inflater import populate_table_from_gen
from models.database import Database
from models.user_manager import UserManager
from windows.generated.ui_cars_window import Ui_CarsWindow


class CarsWindow(QMainWindow, Ui_CarsWindow):
    def __init__(self, name_query=None):
        super().__init__()
        self.setupUi(self)
        self.window = None
        self.user = UserManager().user

        self.cars_table.setColumnCount(10)
        self.header_names = ['', 'Manufacturer', 'Model', 'Year', 'Body', 'Gearbox', 'Engine', 'Price', 'Count',
                             'Dealer']
        self.cars_table.setHorizontalHeaderLabels(self.header_names)

        self.submit_button.clicked.connect(self.submit_clicked)

        if name_query is not None:
            cars_gen = Database().get_cars_by_name(name_query)
            populate_table_from_gen(self.cars_table, cars_gen, col_count=10)
        else:
            cars_gen = Database().get_all_cars()
            populate_table_from_gen(self.cars_table, cars_gen, col_count=10)

        self.cars_id_list = []
        for row in range(0, self.cars_table.rowCount()):
            self.cars_id_list.append(self.cars_table.item(row, 0).text())
        self.cars_table.setColumnHidden(0, True)

    def submit_clicked(self):
        cars_count = self.count_edit.text()
        days_count = self.days_edit.text()
        selected_row = self.cars_table.currentRow()
        available_cars_count = int(self.cars_table.item(selected_row, 8).text())
        print(available_cars_count)

        if check_count(cars_count, available_cars_count) and check_count(days_count, 30):
            car_id = self.cars_id_list[selected_row]

            Database().add_order(self.days_edit.text(), self.count_edit.text(), self.user.id, car_id)
            self.success_msgbox()
        else:
            self.error_msgbox()

    def success_msgbox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Successfully ordered")
        msg.setWindowTitle("Success")
        msg.exec_()

    def error_msgbox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText('Input error')
        msg.setWindowTitle('Input error')
        msg.exec_()
