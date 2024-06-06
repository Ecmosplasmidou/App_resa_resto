from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from config.database import Base


class Carte_plat(Base):
    __tablename__ = "carte_plats"
    id_plat = Column(Integer, ForeignKey("plats.id_plat"), nullable=False)
    id_carte = Column(Integer, ForeignKey("cartes.id"), nullable=False)
    __table_args__ = (
        PrimaryKeyConstraint("id_plat", "id_carte"),
    )  # sert à faire une clé primaire composite pour lier les plats à une carte
