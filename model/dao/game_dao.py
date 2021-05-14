from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.game import Game
from model.dao.dao import DAO


class GameDAO(DAO):

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Game).filter_by(id=id).one()
        except NoResultFound:
            raise print('Aucun resultat')

    def get_all(self):
        try:
            return self._database_session.query(Game).order_by(Game.id).all()
        except NoResultFound:
            raise print("Aucun resultat")

    def create(self, data: dict):
        try:
            game = Game(creator_id=data.get('creator_id'), nbround=data.get('nbround'))
            self._database_session.add(game)
            self._database_session.flush()
        except IntegrityError:
            raise ValueError("La game existe deja")

        return game

    def delete(self, game):
        try:
            self._database_session.delete(game)
        except SQLAlchemyError as e:
            raise print(str(e))
