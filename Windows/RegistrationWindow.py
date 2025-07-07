
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, \
    QVBoxLayout, QHBoxLayout, QFormLayout


from UserClass import UserClass

class RegistrationWindow(QWidget):
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
               QLabel#registration_label 
               {
                   font-size:25px
               }
               QLabel#name_label, QLabel#password_label
               {
                   font-size:20px
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

        registration_label = QLabel("Zarejestruj się! ", self)

        registration_label.setObjectName("registration_label")
        registration_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        name_label = QLabel("podaj swój nick:", self)
        name_label.setObjectName("name_label")

        self.rnick = QLineEdit(self)
        self.rnick.setPlaceholderText("nick:")
        self.rnick.setMaxLength(20)

        password_label = QLabel("podaj swoje haslo:", self)
        password_label.setObjectName("password_label")

        self.rpassword = QLineEdit(self)
        self.rpassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.rpassword.setPlaceholderText("Hasło:")
        self.rpassword.setMaxLength(20)

        form_layout.addRow(name_label, self.rnick)
        form_layout.addRow(password_label, self.rpassword)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.submit_button = QPushButton("Zarejestruj się", self)

        self.submit_button.clicked.connect(self.registration)


        log_label = QLabel("masz konta już konto?-->", self)



        self.log_button = QPushButton("Zaloguj się", self)

        self.log_button.clicked.connect(self.log)

        main_Vlayout.addWidget(registration_label, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        main_Hlayout.addStretch()
        main_Hlayout.addWidget(log_label)
        main_Hlayout.addWidget(self.log_button)
        main_Hlayout.addStretch()
        main_Vlayout.addStretch(5)
        main_Vlayout.addLayout(form_layout)
        main_Vlayout.addStretch(1)
        main_Vlayout.addWidget(self.submit_button, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        main_Vlayout.addLayout(main_Hlayout)
        main_Vlayout.addStretch(10)
        self.setLayout(main_Vlayout)


    def log(self):
        #Change a window view
        from LoginWindow import LoginWindow
        self.Window = LoginWindow()
        self.Window.show()
        self.close()

    def registration(self):
        if self.rpassword.text()!='' and self.rnick.text()!='':
            UserClass(self.rnick.text(),self.rpassword.text()) #by class is creating a new account
            QMessageBox.information(self, "Informacja", "Pomyślnie zarejestrowano! Zapraszam sie zalogować")
            self.log()
        else:
            QMessageBox.warning(self,"Ostrzeżenie","musisz podać wszystkie dane!")