import sys

from controller.player_controller import PlayerController
from model.database import DatabaseEngine
from PySide6.QtWidgets import QApplication



from exceptions import Error
from model.dao.player_dao import PlayerDAO

if __name__ == '__main__':
    database_engine = DatabaseEngine(url='sqlite:///embuscade.db')
    database_engine.create_database()
    admin_controller = PlayerController(database_engine)

    print("Name : ")
    prenom = input()

    print("Surname : ")
    nom = input()

    print("Nickname : ")
    pseudo = input()

    print("Pass : ")
    mdp = input()

    data = {'name': prenom, 'surname': nom, 'nickname': pseudo, 'password': mdp}

    test = admin_controller.create_player(data)

    for t in admin_controller.list_player():
        print(t)
