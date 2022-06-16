import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

import main

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()
    # sys.exit(app.exit())