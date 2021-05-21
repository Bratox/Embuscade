import re
from model.dao.embuscade_dao import EmbuscadeDAO
from exceptions import Error, InvalidData


class EmbuscadeController:

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frame = []

    def list_embuscades(self):
        with self._database_engine.new_session() as session:
            embuscades = EmbuscadeDAO(session).get_all()
            embuscade_data = [embuscade.to_dict() for embuscade in embuscades]
        return embuscade_data

    def get_embuscade(self,embuscade_id):
        with self._database_engine.new_session() as session:
            embuscades = EmbuscadeDAO(session).get(embuscade_id)
            embuscade_data = [embuscade.to_dict() for embuscade in embuscades]
        return embuscade_data
    def create_embuscade(self,data):

        try:
            with self._database_engine.new_session() as session:
                embuscade = EmbuscadeDAO(session).create(data)
                embuscade_data = embuscade.to_dict()
                return embuscade_data
        except Error as e:
            return None

    def update_embuscade(self,embuscade_id,embuscade_data):

        with self._database_engine.new_session() as session:
            embuscadeDAO = EmbuscadeDAO(session)
            embuscade = embuscadeDAO.get(embuscade_id)
            embuscade = embuscadeDAO.update(embuscade,embuscade_data)
            return embuscade

    def delete_embuscade(self, embuscade_id):
        with self._database_engine.new_session() as session:
            embuscadeDAO = EmbuscadeDAO(session)
            embuscade = embuscadeDAO.get(embuscade_id)
            embuscadeDAO.delete(embuscade)