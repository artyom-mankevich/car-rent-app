from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_startup_window(object):
    def setupUi(self, startup_window):
        startup_window.setObjectName("startup_window")
        startup_window.resize(500, 400)

        self.centralwidget = QtWidgets.QWidget(startup_window)
        self.centralwidget.setObjectName("centralwidget")

        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(80, 200, 150, 80))
        self.login_button.setObjectName("login_button")

        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(270, 200, 150, 80))
        self.register_button.setObjectName("register_button")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 80, 280, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        startup_window.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(startup_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        startup_window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(startup_window)
        self.statusbar.setObjectName("statusbar")
        startup_window.setStatusBar(self.statusbar)

        self.retranslateUi(startup_window)
        QtCore.QMetaObject.connectSlotsByName(startup_window)

    def retranslateUi(self, startup_window):
        _translate = QtCore.QCoreApplication.translate
        startup_window.setWindowTitle(_translate("startup_window", "Welcome to Car Rental Service"))
        self.login_button.setText(_translate("startup_window", "Log In"))
        self.register_button.setText(_translate("startup_window", "Register"))
        self.label.setText(_translate("startup_window", "Welcome to Car Rental Service!"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    startup_window = QtWidgets.QMainWindow()
    ui = Ui_startup_window()
    ui.setupUi(startup_window)
    startup_window.show()
    sys.exit(app.exec_())
