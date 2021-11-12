from PyQt5.QtWidgets import QMainWindow

import windows.registration_window as regw
import windows.login_window as logw
from windows.generated.ui_startup_window import Ui_startup_window


class StartupWindow(QMainWindow, Ui_startup_window):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = None
        self.setupUi(self)
        self.login_button.clicked.connect(self.login_clicked)
        self.register_button.clicked.connect(self.register_clicked)

    def login_clicked(self):
        self.window = logw.LoginWindow()
        self.window.show()
        self.close()

    def register_clicked(self):
        self.window = regw.RegistrationWindow()
        self.window.show()
        self.close()
