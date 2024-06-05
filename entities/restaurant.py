from sqlalchemy import Column, Integer, String
from config.database import Base


class Restaurant(Base):
    __tablenamme__ = "restaurants"
    id_restaurant = Column(Integer, primary_key=True, autoincrement=True)
    capacite_max_midi = Column(Integer, nullable=False)
    capacite_max_soir = Column(Integer, nullable=False)
    hoarire_midi = Column(String(50), nullable=False)
    hoarire_soir = Column(String(50), nullable=False)
