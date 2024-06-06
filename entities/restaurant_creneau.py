from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from config.database import Base


class Restaurant_creneau(Base):
    __tablename__ = "restaurant_creneaux"
    id_creneau = Column(Integer, ForeignKey("creneaux.id_creneau"), nullable=False)
    id_restaurant = Column(
        Integer, ForeignKey("restaurants.id_restaurant"), nullable=False
    )
    __table_args__ = (
        PrimaryKeyConstraint("id_creneau", "id_restaurant"),
    )  # sert à faire une clé primaire composite pour lier les créneaux à un restaurant
