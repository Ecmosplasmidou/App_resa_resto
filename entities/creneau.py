from sqlalchemy import Column, Integer, Date
from config.database import Base


class Creaneu(Base):
    __tablenamme__ = "creneaux"
    id_creneau = Column(Integer, primary_key=True, autoincrement=True)
    heure = Column(Integer, nullable=False)
    capacite_max = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
