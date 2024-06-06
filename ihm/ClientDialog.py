from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
import controller.client as client_controller
from entities.client import Client


class ClientDialog(QDialog):
    def __init__(self):
        super().__init__()  # appel du constructeur de la classe parent
        self.setWindowTitle("Ajouter un client")  # titre de la fenêtre

        self.nom_label = QLabel("Nom: ")  # création d'un label pour le nom
        self.nom_line_edit = QLineEdit()  # création d'un champ de texte pour le nom

        self.prenom_label = QLabel("Prénom: ")  # création d'un label pour le nom
        self.prenom_line_edit = QLineEdit()  # création d'un champ de texte pour le nom

        self.telephone_label = QLabel("Télephone: ")  # création d'un label pour le nom
        self.telephone_line_edit = (
            QLineEdit()
        )  # création d'un champ de texte pour le nom

        self.add_button = QPushButton(
            "Ajouter"
        )  # création d'un bouton pour ajouter un client
        self.add_button.clicked.connect(
            self.add_client
        )  # lorsque l'on clique sur le bouton, on ajoute un client

        layout = QVBoxLayout()  # création d'un layout vertical
        layout.addWidget(self.nom_label)
        layout.addWidget(self.nom_line_edit)

        layout.addWidget(self.prenom_label)
        layout.addWidget(self.prenom_line_edit)

        layout.addWidget(self.telephone_label)
        layout.addWidget(self.telephone_line_edit)

        layout.addWidget(self.add_button)
        self.setLayout(layout)  # on applique le layout à la fenêtre


    def add_client(self):
        nom = self.nom_line_edit.text()  # on récupère le nom
        prenom = self.prenom_line_edit.text()  # on récupère le prénom
        telephone = self.telephone_line_edit.text()  # on récupère le téléphone
        client : Client = Client(nom=nom, prenom=prenom, telephone=telephone)
        client_controller.create_client(client)  # on ajoute le client
        self.accept() # on ferme la fenêtre et on renvoie le client
