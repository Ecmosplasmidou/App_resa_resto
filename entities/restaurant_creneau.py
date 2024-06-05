from sqlalchemy import Column, Integer, ForeignKey, String, ForeignKeyConstraint
from config.database import Base
from sqlalchemy.orm import relationship


class Restaurant_creneau(Base):
    __tablenamme__ = "restaurant_creneaux"
    id_creneau = Column(Integer, ForeignKey("creneaux.id_creneau"), nullable=False)
    id_restaurant = Column(Integer, ForeignKey("restauatnts.id_restaurant"), nullable=False)
    __table_args__ = (
        ForeignKeyConstraint(
            [id_creneau, id_restaurant], ["creneaux.id_creneau", "restaurants.id_restaurant"]
        ),
    ) # sert à faire une clé primaire composite pour lier les créneaux à un restaurant
