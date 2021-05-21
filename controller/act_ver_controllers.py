import re
from model.dao.act_ver_dao import ActVerDAO
from exceptions import Error, InvalidData


class Act_verController:

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frame = []

    def list_act_vers(self):
        with self._database_engine.new_session() as session:
            act_vers = ActVerDAO(session).get_all()
            act_ver_data = [act_ver.to_dict() for act_ver in act_vers]
        return act_ver_data

    def get_act_ver(self,act_ver_id):
        with self._database_engine.new_session() as session:
            act_vers = ActVerDAO(session).get(act_ver_id)
            act_ver_data = [act_ver.to_dict() for act_ver in act_vers]
        return act_ver_data

    def create_act_ver(self,data):

        try:
            with self._database_engine.new_session() as session:
                act_ver = ActVerDAO(session).create(data)
                act_ver_data = act_ver.to_dict()
                return act_ver_data
        except Error as e:
            return None

    def update_act_ver(self,act_ver_id,act_ver_data):

        with self._database_engine.new_session() as session:
            act_verDAO = ActVerDAO(session)
            act_ver = act_verDAO.get(act_ver_id)
            act_ver = act_verDAO.update(act_ver,act_ver_data)
            return act_ver

    def delete_act_ver(self, act_ver_id):
        with self._database_engine.new_session() as session:
            act_verDAO = ActVerDAO(session)
            act_ver = act_verDAO.get(act_ver_id)
            act_verDAO.delete(act_ver)