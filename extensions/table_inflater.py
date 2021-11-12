import PyQt5.QtWidgets
from PyQt5 import QtWidgets


def populate_table_from_gen(table: PyQt5.QtWidgets.QTableWidget, gen, col_count: int):
    lst = None

    for i in gen:
        lst = i.fetchall()
    if not len(lst) == 0:
        table.setRowCount(len(lst))

        row = 0
        while row < len(lst):
            sql_row = lst[row]
            for col in range(0, col_count):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(str(sql_row[col])))
            row += 1