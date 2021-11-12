from PyQt5.QtWidgets import QMainWindow

import extensions.input_sanitizer as incheck
import models.user_manager as umanager
import windows.startup_window as startw
from windows.generated.ui_authentication_window import Ui_AuthenticationWindow


class RegistrationWindow(QMainWindow, Ui_AuthenticationWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.window = None
        self.back_button.clicked.connect(self.back_clicked)
        self.submit_button.clicked.connect(self.submit_clicked)

    def submit_clicked(self):
        uname = self.username_input.text()
        pword = self.password_input.text()

        if incheck.check_username(uname) and incheck.check_password(pword):
            manager = umanager.UserManager()
            hashed_password = manager.get_hashed_string(pword)
            manager.create_user(uname, hashed_password)

            self.window = startw.StartupWindow()
            self.window.show()
            self.close()
        else:
            self.username_input.setText('Input error')

    def back_clicked(self):
        self.window = startw.StartupWindow()
        self.window.show()
        self.close()
