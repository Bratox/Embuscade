from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.virus import Virus
from model.dao.dao import DAO


class VirusDAO(DAO):

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Virus).filter_by(id=id).one()
        except NoResultFound:
            raise print('Aucun resultat')

    def get_all(self):
        try:
            return self._database_session.query(Virus).order_by(Virus.id).all()
        except NoResultFound:
            raise print("Aucun resultat")

    def create(self, data: dict):
        try:
            virus = Virus(title=data.get('title'), exp=data.get('exp'))
            self._database_session.add(virus)
            self._database_session.flush()
        except IntegrityError:
            raise ValueError("Le virus existe deja")

        return virus

    def update(self, virus, data: dict):
        if 'title' in data:
            virus.title = data['title']
        if 'exp' in data:
            virus.exp = data['exp']

        try:
            self._database_session.merge(virus)
            self._database_session.flush()
        except IntegrityError:
            raise ValueError("Data may be malformed")

        return virus

    def delete(self, virus):
        try:
            self._database_session.delete(virus)
        except SQLAlchemyError as e:
            raise print(str(e))
