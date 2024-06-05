from config.database import Base
from sqlalchemy import Column, Integer, String


class Categorie(Base):
    __tablename__ = "categories"
    id_categorie = Column(Integer, primary_key=True, autoincrement=True)
    libelle = Column(String(50), nullable=False)
