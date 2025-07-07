import os


class UserClass:
    account_path = "../pliki/konta.txt"

    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.id=self.generate_id()
        self.register() #Write the user to a file
    def generate_id(self):
        #Generate ID by "konta.txt" file;
        with open(self.account_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return len(lines) + 1
    @staticmethod
    def create_a_file(sender,receiver):
        if sender is not None or receiver is not None:

            #sort names to keep them consistent
            names = sorted([str(sender), str(receiver)])
            path_to_file = f"{names[0]}-{names[1]}.txt"
            path_to_folder = os.path.join("../pliki/wiadomosci_prywatne", path_to_file)

            #Create a file, that allows sending messages between users

            if not os.path.exists(path_to_folder):
                with open(path_to_folder, "x"):
                    pass
            else:
                return path_to_folder

    def register(self):
        #Write a user to the "konta.txt" file
        with open(self.account_path, "a", encoding="utf-8") as file:
            file.write(f"{self.id},{self.name},{self.password}\n")