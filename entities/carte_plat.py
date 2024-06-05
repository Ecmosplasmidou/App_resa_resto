from sqlalchemy import Column, Integer, ForeignKey, String, ForeignKeyConstraint
from config.database import Base
from sqlalchemy.orm import relationship


class Carte_plat(Base):
    __tablenamme__ = "carte_plats"
    id_plat = Column(Integer, ForeignKey("plats.id_plat"), nullable=False)
    id_carte = Column(Integer, ForeignKey("cartes.id_carte"), nullable=False)
    __table_args__ = (
        ForeignKeyConstraint(
            [id_plat, id_carte], ["plats.id_plats", "cartes.id_carte"]
        ),
    ) # sert à faire une clé primaire composite pour lier les plats à une carte
