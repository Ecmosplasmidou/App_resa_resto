from sqlalchemy import Column, Integer, Boolean, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship


class Carte(Base):
    __tablename__ = "cartes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    carte_gastronomique = Column(Boolean, nullable=False)
    id_restaurant = Column(
        Integer, ForeignKey("restaurants.id_restaurant"), nullable=False
    )  # Sert à lier la carte à un restaurant
    restaurant = relationship("Restaurant")
