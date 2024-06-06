from entities.client import Client
from config.database import session


# on crée un client
def create_client(client: Client):
    session.add(client)
    session.commit()


# on met à jour un client
def update_client(client: Client):
    old_client: Client = (
        session.query(Client).where(Client.id_client == client.id_client).first()
    )  # select * from clients where id_client = client.id_client
    old_client.nom = client.nom
    old_client.prenom = client.prenom
    old_client.telephone = client.telephone
    session.add(old_client)
    session.commit()


# on supprime un client
def delete_client(client: Client):
    session.delete(client)
    session.commit()


# on récupère tous les clients
def get_all_clients() -> list[Client]:
    return session.query(Client).all()  # select * from clients


# on récupère un client par son id
def get_client_by_id(id_client: int) -> Client:
    return (
        session.query(Client).where(Client.id_client == id_client).first()
    )  # select * from clients where id_client = id_client
