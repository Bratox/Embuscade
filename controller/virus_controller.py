from model.dao.virus_dao import VirusDAO
from exceptions import Error, InvalidData


class VirusController:

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frame = []

    def list_virus(self):
        with self._database_engine.new_session() as session:
            viruss = VirusDAO(session).get_all()
            virus_data = [virus.to_dict() for virus in viruss]

        return virus_data

    def get_virus(self, virus_id):
        with self._database_engine.new_session as session:
            virus = VirusDAO(session).get(virus_id)
            virus_data = virus.to_dict()
        return virus_data

    def create_virus(self, data):

        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                virus = VirusDAO(session).create(data)
                virus_data = virus.to_dict()
                return virus_data
        except Error as e:
            # log error
            raise e

    def update_virus(self, virus_id, virus_data):
        with self._database_engine.new_session() as session:
            virus_dao = VirusDAO(session)
            virus = virus_dao.get(virus_id)
            virus = virus_dao.update(virus, virus_data)
            return virus

    def delete_virus(self, virus_id):
        with self._database_engine.new_session() as session:
            virus_dao = VirusDAO(session)
            virus = virus_dao.get(virus_id)
            virus_dao.delete(virus)
