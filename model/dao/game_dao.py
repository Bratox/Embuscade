from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.game import Game
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class GameDAO(DAO):

    def __init__(self, database_session):
        super().__init__(database_session)

    def get_game_by_creator_id(self, creator_id):
        try:
            return self._database_session.query(Game).filter_by(creator_id=creator_id).all()
        except NoResultFound:
            return None

    def get(self, id):
        try:
            return self._database_session.query(Game).filter_by(id=id).one()
        except NoResultFound:
            raise None

    def get_all(self):
        try:
            return self._database_session.query(Game).order_by(Game.id).all()
        except NoResultFound:
            raise None

    def create(self, data: dict):
        try:
            game = Game(creator_id=data.get('creator_id'), nbround=data.get('nbround'))
            self._database_session.add(game)
            self._database_session.flush()
        except IntegrityError:
            raise None

        return game

    def delete(self, game):
        try:
            self._database_session.delete(game)
        except SQLAlchemyError as e:
            raise None
