import re
from model.dao import embuscade_dao
from exceptions import Error, InvalidData


class EmbuscadeController:

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frame = []

    def list_embuscades(self):
        with self._database_engine.new_session() as session:
            embuscades = embuscade_dao(session).get_all()
            embuscade_data = [embuscades.to_dict() for embuscade in embuscades]
        return embuscade_data

    def get_embuscade(self,embuscade_id):
        with self._database_engine.new_session() as session:
            embuscades = embuscade_dao(session).get(embuscade_id)
            embuscade_data = [embuscades.to_dict() for embuscade in embuscades]
        return embuscade_data
    def create_embuscade(self,data):

        try:
            with self._database_engine.new_session as session:
                embuscade = embuscade_dao(session).create(data)
                embuscade_data = embuscade.to_dict()
                return embuscade_data
        except Error as e:
            raise e

    def update_embuscade(self,embuscade_id,embuscade_data):

        with self._database_engine.new_session as session:
            embuscadeDAO = embuscade_dao(session)
            embuscade = embuscadeDAO.get(embuscade_id)
            embuscade = embuscadeDAO.update(embuscade,embuscade_data)
            return embuscade

    def delete_embuscade(self, embuscade_id):
        with self._database_engine.new_session as session:
            embuscadeDAO = embuscade_dao(session)
            embuscade = embuscadeDAO.get(embuscade_id)
            embuscadeDAO.delete(embuscade_id)