import os
import sys

from PyQt6.QtWidgets import  QApplication,QStyleFactory

from MainWindow import MainWindow
from Windows.LoginWindow import LoginWindow

def creator():
    if not os.path.exists("../pliki"):
        os.makedirs("../pliki")
    if not os.path.exists("../pliki/konta.txt"):
        with open("../pliki/konta.txt", "x") as f:
            pass
    if not os.path.exists("../pliki/wiadomosci_prywatne"):
        os.makedirs("../pliki/wiadomosci_prywatne")



if __name__=="__main__":
    creator()
    app=QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("windows"))
    Window=LoginWindow()
    sys.exit(app.exec())
