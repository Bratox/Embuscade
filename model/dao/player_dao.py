from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.player import Player
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class PlayerDAO(DAO):

    def __init__(self, database_session):
        super().__init__(database_session)

    def connexion(self, nickname, password):
        try:
            return self._database_session.query(Player).filter_by(nickname=nickname, password=password).order_by(Player.nickname).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get(self, id):
        try:
            return self._database_session.query(Player).filter_by(id=id).order_by(Player.nickname).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Player).order_by(Player.nickname).all()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            player = Player(nickname=data.get('nickname'), name=data.get('name'), surname=data.get('surname'),
                            password=data.get('password'))
            self._database_session.add(player)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Le joueur existe deja")

        return player

    def update(self, player, data: dict):
        if 'name' in data:
            player.name = data['name']
        if 'surname' in data:
            player.surname = data['surname']
        if 'nickname' in data:
            player.nickname = data['nickname']

        try:
            self._database_session.merge(player)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Data may be malformed")

        return player

    def delete(self, player):
        try:
            self._database_session.delete(player)
        except SQLAlchemyError as e:
            raise Error(str(e))
