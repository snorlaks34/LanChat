
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QWidget,QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget, \
    QVBoxLayout, QHBoxLayout, QScrollArea, QSizePolicy

from UserClass import UserClass

class MainWindow(QWidget):

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
        self.setStyleSheet(stylesheet)

    def MainWindow(self):
        Vlayout = QVBoxLayout()
        Hlayout = QHBoxLayout()
        bottom_Hlayout=QHBoxLayout()

        self.chat_widget  = QListWidget()
        self.chat_widget.setFixedWidth(120)
        #That method writes users to the  list
        self.write_users()
        self.chat_widget.itemClicked.connect(self.create_cd)

        self.message_enter=QLineEdit(self)
        self.message_enter.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Fixed)
        self.message_enter.returnPressed.connect(self.send_message)

        refresh_button=QPushButton("⟲")
        refresh_button.clicked.connect(self.create_chat_view)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)


        self.scroll_area.setWidget(self.content_widget)
        self.scroll_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        Hlayout.addWidget(self.chat_widget)
        Hlayout.addWidget(self.scroll_area)

        Vlayout.addLayout(Hlayout)

        bottom_Hlayout.addWidget(self.message_enter)
        bottom_Hlayout.addWidget(refresh_button)

        Vlayout.addLayout(bottom_Hlayout)

        self.setLayout(Vlayout)



    # Adds items to the list
    def write_users(self):
        try:
            with open("../pliki/konta.txt"):
                file = open("../pliki/konta.txt")
                for line in file:
                    id, nick, _ = line.strip().split(",")

                    if id!=str(self.yourid):
                        self.chat_widget.addItem(f"{id}. {nick}")
        except FileNotFoundError as e:
            QMessageBox.warning(self, "Ostrzeżenie", f"nie znaleziono Pliku {e}")
    #Create a file for the conversation and serve QList
    def create_cd(self,item):
        id, nick = item.text().strip().split(".")
        self.speaker_id = id
        self.speaker_nick = nick
        self.create_chat_view()
        UserClass.create_a_file(self.yourid, id)
        self.message_enter.setPlaceholderText(f"Wyślij wiadomość do: {self.speaker_nick}")
    # Allows sending messages
    def send_message(self):
        if self.speaker_id != None and self.speaker_nick != None:
            if self.yourid != None or self.speaker_id != None or self.message_enter.text().strip() != "":
                path = UserClass.create_a_file(self.yourid, self.speaker_id)
                try:
                    with open(path, "a+", encoding="UTF-8") as file:
                        if self.message_enter.text() != "" or self.message_enter.text().strip() != "" or self:
                            file.write(f"{self.yourid},{self.yournick},{self.message_enter.text()}\n")
                            file.close()
                            self.message_enter.clear()
                            self.create_chat_view()
                except FileNotFoundError as error:
                    QMessageBox.warning(self, "Bład krytyczny", f"nie znaleziono chatu! {error}")
    #Writes messages on screen
    def create_chat_view(self):
        #deletes all widget in scrollArea
        for i in reversed(range(self.content_layout.count())):
            item = self.content_layout.itemAt(i)
            widget = item.widget()
            if widget:
                widget.setParent(None)
            else:
                self.content_layout.removeItem(item)
        path = UserClass.create_a_file(self.yourid, self.speaker_id)
        try:
            with open(path, "r", encoding="UTF-8") as file:
                for line in file:
                    id, nick, message = line.split(",")
                    your_message = QLabel(f"{nick}: {message}", self)
                    your_message.setWordWrap(True)
                    your_message.setAlignment(Qt.AlignmentFlag.AlignTop)
                    self.content_layout.addWidget(your_message, 0)
                    self.scroll_area.repaint()
            self.content_layout.addStretch()
        except FileNotFoundError as error:
            QMessageBox.warning(self, "Błąd krytyczny", f"Nie znaleziono chatu! {error}")
