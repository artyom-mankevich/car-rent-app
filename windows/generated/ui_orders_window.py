# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/orders.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyOrders(object):
    def setupUi(self, MyOrders):
        MyOrders.setObjectName("MyOrders")
        MyOrders.resize(724, 465)
        self.centralwidget = QtWidgets.QWidget(MyOrders)
        self.centralwidget.setObjectName("centralwidget")
        self.orders_table = QtWidgets.QTableWidget(self.centralwidget)
        self.orders_table.setGeometry(QtCore.QRect(10, 50, 701, 401))
        self.orders_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.orders_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.orders_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.orders_table.setObjectName("orders_table")
        self.orders_table.setColumnCount(0)
        self.orders_table.setRowCount(0)
        self.orders_table.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MyOrders.setCentralWidget(self.centralwidget)

        self.retranslateUi(MyOrders)
        QtCore.QMetaObject.connectSlotsByName(MyOrders)

    def retranslateUi(self, MyOrders):
        _translate = QtCore.QCoreApplication.translate
        MyOrders.setWindowTitle(_translate("MyOrders", "My Orders"))
        self.label.setText(_translate("MyOrders", "My orders:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyOrders = QtWidgets.QMainWindow()
    ui = Ui_MyOrders()
    ui.setupUi(MyOrders)
    MyOrders.show()
    sys.exit(app.exec_())
