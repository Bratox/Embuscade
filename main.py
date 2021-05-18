import sys

from controller.player_controller import PlayerController
from controller.question_controller import QuestionController
from controller.virus_controller import VirusController
from controller.jeu_controller import jeuController
from controller.act_ver_controllers import Act_verController
from controller.embuscade_controller import EmbuscadeController
from controller.game_controller import GameController
from model.database import DatabaseEngine
from PyQt5.QtWidgets import QApplication, QMainWindow
from vue.embuscade import Ui_MainWindow as MainWindow

from exceptions import Error

def run():
    database_engine = DatabaseEngine(url='sqlite:///embuscade.db')
    database_engine.create_database()
    player_controller = PlayerController(database_engine)

    """question_file = open("question.txt", "r")
    virus_file = open("virus.txt", "r")
    embuscade_file = open("embuscade.txt", "r")
    act_ver_file = open("act_ver.txt", "r")
    jeu_file = open("jeu.txt", "r")

    for question in question_file.readlines():
        question_controller.create_question(question)
    for virus in virus_file.readlines():
        virus_controller.create_virus(virus)
    for act_ver in act_ver_file.readlines():
        act_ver_controller.create_act_ver(act_ver)
    for embuscade in embuscade_file.readlines():
        embuscade_controller.create_embuscade(embuscade)
    for jeu in jeu_file.readlines():
        jeu_controller.create_jeu(jeu)"""

    app = QApplication(sys.argv)

    MWind = QMainWindow()
    ui = MainWindow(player_controller, database_engine, MWind)
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()

    """print("Name : "), 
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


