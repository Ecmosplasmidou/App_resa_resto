from config.database import Base
from sqlalchemy import Column, Integer, String


class Client(Base):
    __tablename__ = "clients"
    id_client = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    telephone = Column(String(10), nullable=False)
