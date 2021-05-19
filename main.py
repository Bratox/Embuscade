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

    for t in question_controller.list_question():
        print(t)
    for question in question_file.readlines():
        print(question)
        if(question.split(" ")[0] == "Qui"):
            question_controller.create_question({'exp':question+ " \n\n l'heureux.se élu.e se gratifié.e de "+ str(secrets.randbelow(3)+2)+" gorgées."})
        else :
            question_controller.create_question({ 'exp':question + "\n\n Si la réponse n'est pas bonne, l'inculte prendra "+ str(secrets.randbelow(3)+2)+" gorgées."})
    for virus in virus_file.readlines():
        virus_controller.create_virus({'exp' :virus + "\n\n Tout manquement à ce virus sera puni de "+ str(secrets.randbelow(4)+3)+"\n\n Ce virus dure " + str(secrets.randbelow(2)+1) + " tours"})
    for question in question_file.readlines():
        question_controller.create_question(question)
    for virus in virus_file.readlines():
        virus_controller.create_virus(virus)
    for act_ver in act_ver_file.readlines():
        act_ver_controller.create_act_ver(act_ver)
    for embuscade in embuscade_file.readlines():
        embuscade_controller.create_embuscade(embuscade)
    for jeu in jeu_file.readlines():
        jeu_controller.create_jeu(jeu)

    app = QApplication(sys.argv)

    MWind = QMainWindow()
    ui = MainWindow(player_controller, database_engine, MWind)
    sys.exit(app.exec_())"""


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


