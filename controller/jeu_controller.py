import re
from model.dao.jeu_dao import JeuDAO
from exceptions import Error, InvalidData


class JeuController:

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frame = []

    def list_jeux(self):
        with self._database_engine.new_session() as session:
            jeux = JeuDAO(session).get_all()
            jeu_data = [jeux.to_dict() for jeu in jeux]
        return jeu_data

    def get_jeu(self,jeu_id):
        with self._database_engine.new_session() as session:
            jeux = JeuDAO(session).get(jeu_id)
            jeu_data = [jeux.to_dict() for jeu in jeux]
        return jeu_data
    def create_jeu(self,data):

        try:
            with self._database_engine.new_session as session:
                jeu = JeuDAO(session).create(data)
                jeu_data = jeu.to_dict()
                return jeu_data
        except Error as e:
            return None

    def update_jeu(self,jeu_id,jeu_data):

        with self._database_engine.new_session as session:
            jeuDAO = JeuDAO(session)
            jeu = jeuDAO.get(jeu_id)
            jeu = jeuDAO.update(jeu,jeu_data)
            return jeu

    def delete_jeu(self, jeu_id):
        with self._database_engine.new_session as session:
            jeuDAO = JeuDAO(session)
            jeu = jeuDAO.get(jeu_id)
            jeuDAO.delete(jeu_id)