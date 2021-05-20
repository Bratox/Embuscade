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
        with self._database_engine.new_session() as session:
            player = PlayerDAO(session).get(player_id)
            player_data = player.to_dict()
        return player_data

    def get_player_by_nick(self, player_name):
        with self._database_engine.new_session() as session:
            player = PlayerDAO(session).get_player_by_nickname(player_name)
            if player:
                player_data = player.to_dict()
            else:
                player_data = None
        return player_data

    def connexion(self, player_name, player_password):
        with self._database_engine.new_session() as session:
            player = PlayerDAO(session).connexion(player_name, player_password)
            if player:
                player_data = player.to_dict()
            else:
                player_data = None
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
            return None

    def update_player(self, player_id, player_data):
        with self._database_engine.new_session() as session:
            player_dao = PlayerDAO(session)
            player = player_dao.get(player_id)
            player = player_dao.update(player, player_data)
            return player

    def delete_player(self, player_id):
        with self._database_engine.new_session() as session:
            player_dao = PlayerDAO(session)
            player = player_dao.get(player_id)
            player_dao.delete(player)
