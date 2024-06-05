from sqlalchemy import Column, Integer, Bool, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship


class Carte(Base):
    __tablenamme__ = "cartes"
    id_carte = Column(Integer, primary_key=True, autoincrement=True)
    carte_gastronomique = Column(Bool, nullable=False)
    id_restaurant = Column(
        Integer, ForeignKey("restaurants.id_restaurant"), nullable=False
    )  # Sert à lier la carte à un restaurant
    restaurant = relationship("restaurants", back_populates="carte")
