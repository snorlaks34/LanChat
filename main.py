import os
import sys
from idlelib.iomenu import encoding
from pickle import GLOBAL
from time import sleep

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget, \
    QVBoxLayout, QHBoxLayout, QScrollArea, QSizePolicy, QSpacerItem;

#logowanie robimy tak ze trzeba bedzie podać nick#id oraz haslo.
def creator():
    if not os.path.exists("pliki"):
        os.makedirs("pliki")
    if not os.path.exists("pliki/konta.txt"):
        with open("pliki/konta.txt", "x") as f:
            pass
    if not os.path.exists("pliki/wiadomosci_prywatne"):
        os.makedirs("pliki/wiadomosci_prywatne")

class Uzytkownik():
    sciezka_konta = "pliki/konta.txt"

    def __init__(self,nazwa,haslo):
        self.nazwa=nazwa
        self.haslo=haslo
        self.id=self.generuj_id()
        self.rejestracja() #write to file an user
    def generuj_id(self):
        """Generuje unikalne ID na podstawie pliku konta.txt."""
        with open(self.sciezka_konta, "r", encoding="utf-8") as plik:
            linie = plik.readlines()
            return len(linie) + 1
    @staticmethod
    def utworz_plik(Adresat,Odbiorca):
        if Adresat!=None or Odbiorca!=None:

            #sortuje nazwy żeby zawsze była jednakowa
            nazwy = sorted([str(Adresat), str(Odbiorca)])
            sciezka = f"{nazwy[0]}-{nazwy[1]}.txt"
            sciezka_do_folderu = os.path.join("pliki/wiadomosci_prywatne", sciezka)

            #tworzy plik ,który pozwoli wysylac wiadomości do użytkowników

            if not os.path.exists(sciezka_do_folderu):
                with open(sciezka_do_folderu, "x") as f:
                    pass
            else:
                return sciezka_do_folderu

    def rejestracja(self):
        """Zapisuje użytkownika do pliku konta.txt."""
        with open(self.sciezka_konta, "a", encoding="utf-8") as plik:
            plik.write(f"{self.id},{self.nazwa},{self.haslo}\n")
                    

class loginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.setWindowTitle("Ryszczat")
        self.setGeometry(300,150,800,600)
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
                font-size:25px
            }
            QLabel#name_label, QLabel#password_label
            {
                font-size:20px
            }
            
            
        """
        app.setStyleSheet(stylesheet)

    def MainWindow(self):

        login_label = QLabel("Zaloguj się! ", self)
        login_label.setGeometry(0, 20, 800, 60)
        login_label.setObjectName("login_label")
        login_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        name_label=QLabel("podaj swój nick:",self)
        name_label.setGeometry(250,200,800,30)
        name_label.setObjectName("name_label")

        self.nick=QLineEdit(self)
        self.nick.setPlaceholderText("nick:")
        self.nick.setGeometry(400,200,200,30)
        self.nick.setMaxLength(10)

        password_label = QLabel("podaj swoje haslo:", self)
        password_label.setGeometry(230, 250, 800, 30)
        password_label.setObjectName("password_label")

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setPlaceholderText("Hasło:")
        self.password.setGeometry(400, 250, 200, 30)
        self.password.setMaxLength(10)

        self.submit_button=QPushButton("Zaloguj się",self)
        self.submit_button.setGeometry(350, 300, 100, 30)
        self.submit_button.clicked.connect(self.login)


        reg_label = QLabel("Nie masz konta?-->", self)
        reg_label.setGeometry(260, 400, 800, 30)


        self.reg_button = QPushButton("Zarejestruj się", self)
        self.reg_button.setGeometry(430, 400, 100, 30)
        self.reg_button.clicked.connect(self.reg)

    # loging process
    def login(self):
        self.yourid=1 #your own account id
        with open(Uzytkownik.sciezka_konta, "r", encoding="utf-8") as plik:
            for linia in plik:
                try:
                    id_u, nick_u, password_u = linia.strip().split(",")
                    if self.password.text() == password_u and self.nick.text() == nick_u:
                        QMessageBox.information(self, "Informacja", "Pomyślnie zalogowano! Zapraszam do chatu")
                        self.yourid=id_u
                        self.yournick=nick_u
                        self.main()
                        break  # Przerywamy pętlę po udanym logowaniu
                except ValueError:
                    QMessageBox.warning(self, "Ostrzeżenie", "Problemy techniczne!")
            else:
                QMessageBox.warning(self, "Ostrzeżenie", "Błedny login lub hasło!")

    def reg(self):
        #change a window view
        self.Window = registrationWidnow()
        self.Window.show()
        self.close()

    def main(self):
        # change a window view
        self.Window = mainWindow(self.yourid,self.yournick)
        self.Window.show()
        self.close()

class registrationWidnow(QWidget):
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


           """
        app.setStyleSheet(stylesheet)

    def MainWindow(self):
        registration_label = QLabel("Zarejestruj się! ", self)
        registration_label.setGeometry(0, 20, 800, 60)
        registration_label.setObjectName("registration_label")
        registration_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        name_label = QLabel("podaj swój nick:", self)
        name_label.setGeometry(250, 200, 800, 30)
        name_label.setObjectName("name_label")

        self.rnick = QLineEdit(self)
        self.rnick.setPlaceholderText("nick:")
        self.rnick.setGeometry(400, 200, 200, 30)
        self.rnick.setMaxLength(10)

        password_label = QLabel("podaj swoje haslo:", self)
        password_label.setGeometry(230, 250, 800, 30)
        password_label.setObjectName("password_label")

        self.rpassword = QLineEdit(self)
        self.rpassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.rpassword.setPlaceholderText("Hasło:")
        self.rpassword.setGeometry(400, 250, 200, 30)
        self.rpassword.setMaxLength(10)

        self.submit_button = QPushButton("Zarejestruj się", self)
        self.submit_button.setGeometry(350, 300, 100, 30)
        self.submit_button.clicked.connect(self.registration)


        log_label = QLabel("masz konta już konto?-->", self)
        log_label.setGeometry(230, 400, 800, 30)


        self.log_button = QPushButton("Zaloguj się", self)
        self.log_button.setGeometry(430, 400, 100, 30)
        self.log_button.clicked.connect(self.log)


    def log(self):
        #change a window view
        self.Window = loginWindow()
        self.Window.show()
        self.close()

    def registration(self):
        if self.rpassword.text()!='' and self.rnick.text()!='':
            Uzytkownik(self.rnick.text(),self.rpassword.text()) #by class is creating a new account
            QMessageBox.information(self, "Informacja", "Pomyślnie zarejestrowano! Zapraszam sie zalogować")
            self.log()
        else:
            QMessageBox.warning(self,"Ostrzeżenie","musisz podać wszystkie dane!")

class mainWindow(QWidget):

    def __init__(self,yourid,yournick):
        self.yourid=yourid
        self.yournick = yournick
        self.speaker_id = None
        self.speaker_nick = None
        super().__init__()
        self.initializeUI()


    def initializeUI(self):
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
                     """
        app.setStyleSheet(stylesheet)

    def MainWindow(self):
        Vlayout = QVBoxLayout()
        Hlayout = QHBoxLayout()

        self.chat_widget  = QListWidget()
        self.chat_widget.setFixedWidth(120)
        #method to write user in list
        self.write_users()
        self.chat_widget.itemClicked.connect(self.create_cd)

        self.message_enter=QLineEdit(self)
        self.message_enter.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Fixed)
        self.message_enter.returnPressed.connect(self.send_message)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.scroll_area.setWidget(self.content_widget)
        self.scroll_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        Hlayout.addWidget(self.chat_widget)
        Hlayout.addWidget(self.scroll_area)

        Vlayout.addLayout(Hlayout)
        Vlayout.addWidget(self.message_enter)

        self.setLayout(Vlayout)



    # add items to list
    def write_users(self):

        try:
            with open("pliki/konta.txt"):
                file = open("pliki/konta.txt")
                for line in file:
                    id, nick, _ = line.strip().split(",")

                    if id!=str(self.yourid):
                        self.chat_widget.addItem(f"{id}. {nick}")
        except FileNotFoundError as e:
            QMessageBox.warning(self, "Ostrzeżenie", f"nie znaleziono Pliku {e}")
    #create a file to conversation and serves QList
    def create_cd(self,item):
        id,nick = item.text().strip().split(".")
        self.speaker_id=id
        self.speaker_nick= nick
        self.create_chat_view()
        Uzytkownik.utworz_plik(self.yourid,id)
        self.message_enter.setPlaceholderText(f"Wyślij wiadomość do: {self.speaker_nick}")
    # allows to send message
    def send_message(self):
        if self.yourid!= None or self.speaker_id != None:
            path = Uzytkownik.utworz_plik(self.yourid,self.speaker_id)
            try:
                with open(path, "a+",encoding="UTF-8") as file:
                    if self.message_enter.text()!="" or self.message_enter.text().strip()!="":
                        file.write(f"{self.yourid},{self.yournick},{self.message_enter.text()}\n")
                        file.close()
                        self.message_enter.clear()
                        self.create_chat_view()
            except FileNotFoundError as error:
                QMessageBox.warning(self, "Bład krytyczny", f"nie znaleziono chatu! {error}")
    #writes messages on screen
    def create_chat_view(self):
        for i in reversed(range(self.content_layout.count())):
            widget = self.content_layout.itemAt(i).widget()
            widget.deleteLater()
        path = Uzytkownik.utworz_plik(self.yourid, self.speaker_id)
        try:
            with open(path, "r", encoding="UTF-8") as file:
                for line in file:
                    id, nick, message = line.split(",")
                    your_message = QLabel(f"{nick}: {message}", self)
                    your_message.setWordWrap(True)
                    your_message.setAlignment(Qt.AlignmentFlag.AlignTop)

                    self.content_layout.addWidget(your_message,0)
                    self.scroll_area.repaint()

        except FileNotFoundError as error:
            QMessageBox.warning(self, "Błąd krytyczny", f"Nie znaleziono chatu! {error}")






if __name__=="__main__":
    creator()
    app=QApplication(sys.argv)
    Window=loginWindow()
    sys.exit(app.exec())
