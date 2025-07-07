from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QWidget,QLabel, QLineEdit, QPushButton, QMessageBox,\
    QVBoxLayout, QHBoxLayout,QFormLayout

from UserClass import UserClass

from MainWindow import MainWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setWindowTitle("Ryszczat")
        self.setGeometry(300, 150, 800, 600)
        self.MainWindow()
        self.style()
        self.show()

    def style(self):
        stylesheet = """
            QWidget {
                background-color: #2E3440;
                color: white;
                font-size: 16px;
            }
            QLabel#login_label 
            {
                font-size:25px;
            }
            QLabel#name_label, QLabel#password_label
            {
                font-size:20px;
            }
            QLineEdit
            {
                max-width: 250px;
                margin-top:10px;
            }
            QPushButton#submit_button
            {
                width:200px;
            }

        """
        self.setStyleSheet(stylesheet)

    def MainWindow(self):
        main_Vlayout = QVBoxLayout()
        main_Hlayout = QHBoxLayout()
        form_layout = QFormLayout()

        login_label = QLabel("Zaloguj się! ", self)
        login_label.setObjectName("login_label")

        name_label = QLabel("podaj swój nick:", self)
        name_label.setObjectName("name_label")

        self.nick = QLineEdit(self)
        self.nick.setPlaceholderText("nick:")
        self.nick.setMaxLength(10)

        password_label = QLabel("podaj swoje haslo:", self)
        password_label.setObjectName("password_label")

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setPlaceholderText("Hasło:")
        self.password.setMaxLength(10)

        self.submit_button = QPushButton("Zaloguj się", self)
        self.submit_button.clicked.connect(self.login)
        self.submit_button.setObjectName("submit_button")

        reg_label = QLabel("Nie masz konta?-->", self)

        self.reg_button = QPushButton("Zarejestruj się", self)
        self.reg_button.clicked.connect(self.reg)

        form_layout.addRow(name_label, self.nick)
        form_layout.addRow(password_label, self.password)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter)

        main_Vlayout.addWidget(login_label, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        main_Hlayout.addStretch()
        main_Hlayout.addWidget(reg_label)
        main_Hlayout.addWidget(self.reg_button)
        main_Hlayout.addStretch()

        main_Vlayout.addStretch(5)
        main_Vlayout.addLayout(form_layout)
        main_Vlayout.addStretch(1)
        main_Vlayout.addWidget(self.submit_button, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        main_Vlayout.addLayout(main_Hlayout)
        main_Vlayout.addStretch(10)
        self.setLayout(main_Vlayout)

    # loging process
    def login(self):
        self.yourid = 1  # your own account id
        with open(UserClass.account_path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    id_u, nick_u, password_u = line.strip().split(",")
                    if self.password.text() == password_u and self.nick.text() == nick_u:
                        QMessageBox.information(self, "Informacja", "Pomyślnie zalogowano! Zapraszam do chatu")
                        self.yourid = id_u
                        self.yournick = nick_u
                        self.main()
                        break  # Break the loop if the login is successful
                except ValueError:
                    QMessageBox.warning(self, "Ostrzeżenie", "Problemy techniczne!")
            else:
                QMessageBox.warning(self, "Ostrzeżenie", "Błedny login lub hasło!")

    def reg(self):
        # Change a window view
        from RegistrationWindow import RegistrationWindow
        self.Window = RegistrationWindow()
        self.Window.show()
        self.close()

    def main(self):
        # Change a window view
        self.Window = MainWindow(self.yourid, self.yournick)
        self.Window.show()
        self.close()