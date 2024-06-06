from sqlalchemy import Column, Integer, ForeignKey, String, PrimaryKeyConstraint
from config.database import Base


class Reserver(Base):
    __tablename__ = "reservations"
    id_creneau = Column(Integer, ForeignKey("creneaux.id_creneau"), nullable=False)
    id_client = Column(Integer, ForeignKey("clients.id_client"), nullable=False)
    allergene = Column(String(50), nullable=False)
    nb_personne = Column(Integer, nullable=False)
    __table_args__ = (
        PrimaryKeyConstraint("id_creneau", "id_client"),
    )  # sert à faire une clé primaire composite pour lier les réservations à un client et un créneau
