# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/authentication.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthenticationWindow(object):
    def setupUi(self, AuthenticationWindow):
        AuthenticationWindow.setObjectName("AuthenticationWindow")
        AuthenticationWindow.resize(450, 201)
        self.centralwidget = QtWidgets.QWidget(AuthenticationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(10, 20, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(10, 80, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(160, 30, 281, 29))
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(160, 90, 281, 29))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 150, 110, 30))
        self.back_button.setObjectName("back_button")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(330, 150, 110, 30))
        self.submit_button.setObjectName("submit_button")
        AuthenticationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AuthenticationWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthenticationWindow)

    def retranslateUi(self, AuthenticationWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthenticationWindow.setWindowTitle(_translate("AuthenticationWindow", "Authentication"))
        self.username_label.setText(_translate("AuthenticationWindow", "Username:"))
        self.password_label.setText(_translate("AuthenticationWindow", "Password:"))
        self.back_button.setText(_translate("AuthenticationWindow", "Back"))
        self.submit_button.setText(_translate("AuthenticationWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AuthenticationWindow = QtWidgets.QMainWindow()
    ui = Ui_AuthenticationWindow()
    ui.setupUi(AuthenticationWindow)
    AuthenticationWindow.show()
    sys.exit(app.exec_())
