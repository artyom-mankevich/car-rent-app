import sys

from PyQt5 import QtWidgets

from windows.startup_window import StartupWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = StartupWindow()
    win.show()
    sys.exit(app.exec_())
