from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.embuscade import Embuscade
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class EmbuscadeDAO(DAO):

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Embuscade).filter_by(id=id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Embuscade).order_by(Embuscade.id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            embuscade = Embuscade(exp=data.get('exp'))
            self._database_session.add(embuscade)
            self._database_session.flush()
        except IntegrityError:
            raise Error("L'embuscade existe deja")

        return embuscade

    def update(self, embuscade, data: dict):
        if 'exp' in data:
            embuscade.exp = data['exp']

        try:
            self._database_session.merge(embuscade)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Data may be malformed")

        return embuscade

    def delete(self, embuscade):
        try:
            self._database_session.delete(embuscade)
        except SQLAlchemyError as e:
            raise Error(str(e))
