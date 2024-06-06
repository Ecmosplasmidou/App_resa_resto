from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Plat(Base):
    __tablename__ = "plats"
    id_plat = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    allergene = Column(String(50), nullable=False)
    prix = Column(Float, nullable=False)
    archive = Column(Boolean, nullable=False)

    id_categorie = Column(
        Integer, ForeignKey("categories.id_categorie"), nullable=False
    )  # Sert à lier la carte à un restaurant
    categorie = relationship("Categorie")
