from sqlalchemy import Column, Integer, ForeignKey, String, ForeignKeyConstraint
from config.database import Base
from sqlalchemy.orm import relationship


class Reserver(Base):
    __tablenamme__ = "reservations"
    id_creneau = Column(Integer, ForeignKey("creneaux.id_creneau"), nullable=False)
    id_client = Column(Integer, ForeignKey("clients.id_client"), nullable=False)
    allergene = Column(String(50), nullable=False)
    nb_personne = Column(Integer, nullable=False)
    __table_args__ = (
        ForeignKeyConstraint(
            [id_creneau, id_client], ["creneaux.id_creneau", "clients.id_client"]
        ),
    ) # sert à faire une clé primaire composite pour lier les réservations à un client et un créneau
