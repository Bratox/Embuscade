import re
from model.dao import jeu_dao
from exceptions import Error, InvalidData


class jeuController:

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frame = []

    def list_jeux(self):
        with self._database_engine.new_session() as session:
            jeux = jeu_dao(session).get_all()
            jeu_data = [jeux.to_dict() for jeu in jeux]
        return jeu_data

    def get_jeu(self,jeu_id):
        with self._database_engine.new_session() as session:
            jeux = jeu_dao(session).get(jeu_id)
            jeu_data = [jeux.to_dict() for jeu in jeux]
        return jeu_data
    def create_jeu(self,data):

        try:
            with self._database_engine.new_session as session:
                jeu = jeu_dao(session).create(data)
                jeu_data = jeu.to_dict()
                return jeu_data
        except Error as e:
            raise e

    def update_jeu(self,jeu_id,jeu_data):

        with self._database_engine.new_session as session:
            jeuDAO = jeu_dao(session)
            jeu = jeuDAO.get(jeu_id)
            jeu = jeuDAO.update(jeu,jeu_data)
            return jeu

    def delete_jeu(self, jeu_id):
        with self._database_engine.new_session as session:
            jeuDAO = jeu_dao(session)
            jeu = jeuDAO.get(jeu_id)
            jeuDAO.delete(jeu_id)