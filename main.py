import sqlite3
import sys

from PyQt6.QtWidgets import QApplication, QWidget

from config.database import Base, engine, session
from entities.restaurant import Restaurant
from entities.creneau import Creneau
from entities.restaurant_creneau import Restaurant_creneau
from entities.client import Client
from entities.carte_plat import Carte_plat
from entities.carte import Carte
from entities.plat import Plat
from entities.categorie import Categorie
from entities.reserver import Reserver

from ihm.MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Création de l'application

    main_window = MainWindow()  # Création de la fenêtre principale
    main_window.show()  # Affichage de la fenêtre

    sys.exit(app.exec())  # Exécution de l'application

    # main_window = MainWindow()
    # main_window.show()
    # sys.exit(app.exec())
    # Base.metadata.create_all(engine)
    # nouveau_restaurant = Restaurant(
    #     capacite_max_midi=15,
    #     capacite_max_soir=50,
    #     hoarire_midi="8h-12h",
    #     horaire_soir="18h-22h"
    #     )
    # session.add(nouveau_restaurant)
    # session.commit()
