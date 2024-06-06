from PyQt6.QtWidgets import QWidget, QListWidget, QPushButton, QVBoxLayout, QDialog
from ihm.ClientDialog import ClientDialog
from entities.client import Client
import controller.client as client_controller


class MainWindow(
    QWidget
):  # Qwidget est une classe de base pour tous les objets d'interface utilisateur

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reservation de restaurant")  # titre de la fenêtre
        self.setGeometry(100, 100, 400, 300)

        self.client_list = QListWidget(self)  # création d'une liste de clients
        
        self.add_button_client = QPushButton("Ajouter un client")  # création d'un bouton pour ajouter un client
        self.add_button_client.clicked.connect(self.open_dialog_create_client)  # lorsque l'on clique sur le bouton, on ouvre une fenêtre pour ajouter un client

        layout = QVBoxLayout()  # création d'un layout vertical
        layout.addWidget(self.client_list)  # ajout de la liste et du bouton au layout
        layout.addWidget(
            self.add_button_client
        )  # ajout de la liste et du bouton au layout
        self.setLayout(layout)  # on applique le layout à la fenêtre
        
        
    def open_dialog_create_client(self):
        dialog = ClientDialog()  # on crée une fenêtre pour ajouter un client
        dialog.accepted.connect(self.add_client_list)
        dialog.exec()  # on affiche la fenêtre
            
                
    # def add_client_list(self):
    #     self.client_list.clear() # on vide la liste
    #     client_lsit_db = client_controller.get_all_clients()
    #     for client in client_lsit_db:
    #         self.client_list.addItems(f"{client.nom} {client.prenom}")  # on ajoute le client à la liste
            
    def add_client_list(self):
        self.client_list.clear() # on vide la liste
        client_list_db = client_controller.get_all_clients()
        for client in client_list_db:
            self.client_list.addItem(f"{client.nom} {client.prenom} {client.telephone}")  # on ajoute le client à la liste


