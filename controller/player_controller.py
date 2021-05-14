from model.dao.player_dao import PlayerDAO
from exceptions import Error, InvalidData


class PlayerController:

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frame = []

    def list_player(self):
        with self._database_engine.new_session() as session:
            players = PlayerDAO(session).get_all()
            players_data = [player.to_dict() for player in players]

        return players_data

    def get_player(self, player_id):
        with self._database_engine.new_session as session:
            player = PlayerDAO(session).get(player_id)
            player_data = player.to_dict()
        return player_data

    def create_player(self, data):

        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                player = PlayerDAO(session).create(data)
                player_data = player.to_dict()
                return player_data
        except Error as e:
            # log error
            raise e
