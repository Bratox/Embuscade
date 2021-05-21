import re
from model.dao.game_dao import GameDAO
from exceptions import Error, InvalidData


class GameController:

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_game(self):
        with self._database_engine.new_session() as session:
            games = GameDAO(session).get_all()
            game_data = [games.to_dict() for game in games]
        return game_data

    def create_game(self,data):

        try:
            with self._database_engine.new_session() as session:
                game = GameDAO(session).create(data)
                game_data = game.to_dict()
                return game_data
        except Error as e:
            return None

    def update_game(self,game_id,game_data):

        with self._database_engine.new_session() as session:
            gameDAO = GameDAO(session)
            game = gameDAO.get(game_id)
            game = gameDAO.update(game,game_data)
            return game

    def delete_game(self, game_id):
        with self._database_engine.new_session() as session:
            gameDAO = GameDAO(session)
            game = gameDAO.get(game_id)
            gameDAO.delete(game_id)