import sys

from controller.player_controller import PlayerController
from model.database import DatabaseEngine
from PyQt5.QtWidgets import QApplication, QMainWindow
from vue.embuscade import Ui_MainWindow as MainWindow

from exceptions import Error

def run():
    database_engine = DatabaseEngine(url='sqlite:///embuscade.db')
    database_engine.create_database()
    admin_controller = PlayerController(database_engine)

    app = QApplication(sys.argv)

    MWind = QMainWindow()
    ui = MainWindow(admin_controller, MWind)
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()

    """print("Name : ")
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
        print(t)"""


