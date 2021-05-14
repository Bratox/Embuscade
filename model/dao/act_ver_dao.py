from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.act_ver import ActVer
from model.dao.dao import DAO


class ActVerDAO(DAO):

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(ActVer).filter_by(id=id).one()
        except NoResultFound:
            raise print('Aucun resultat')

    def get_all(self):
        try:
            return self._database_session.query(ActVer).order_by(ActVer.id).all()
        except NoResultFound:
            raise print("Aucun resultat")

    def create(self, data: dict):
        try:
            actver = ActVer(title=data.get('title'), exp=data.get('exp'))
            self._database_session.add(actver)
            self._database_session.flush()
        except IntegrityError:
            raise ValueError("L'action verite existe deja")

        return actver

    def update(self, actver, data: dict):
        if 'title' in data:
            actver.title = data['title']
        if 'exp' in data:
            actver.exp = data['exp']

        try:
            self._database_session.merge(actver)
            self._database_session.flush()
        except IntegrityError:
            raise ValueError("Data may be malformed")

        return actver

    def delete(self, actver):
        try:
            self._database_session.delete(actver)
        except SQLAlchemyError as e:
            raise print(str(e))
