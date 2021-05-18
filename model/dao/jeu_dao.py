from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.jeu import Jeu
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class JeuDAO(DAO):

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Jeu).filter_by(id=id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Jeu).order_by(Jeu.id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            jeu = Jeu(exp=data.get('exp'))
            self._database_session.add(jeu)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Le jeu existe deja")

        return jeu

    def update(self, jeu, data: dict):
        if 'exp' in data:
            jeu.exp = data['exp']

        try:
            self._database_session.merge(jeu)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Data may be malformed")

        return jeu

    def delete(self, jeu):
        try:
            self._database_session.delete(jeu)
        except SQLAlchemyError as e:
            raise Error(str(e))
