from model.dao.question_dao import QuestionDAO
from exceptions import Error, InvalidData


class QuestionController:

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frame = []

    def list_question(self):
        with self._database_engine.new_session() as session:
            questions = QuestionDAO(session).get_all()
            questions_data = [question.to_dict() for question in questions]

        return questions_data

    def get_question(self, question_id):
        with self._database_engine.new_session() as session:
            question = QuestionDAO(session).get(question_id)
            question_data = question.to_dict()
        return question_data

    def create_question(self, data):

        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                question = QuestionDAO(session).create(data)
                question_data = question.to_dict()
                return question_data
        except Error as e:
            # log error
            return None

    def update_question(self, question_id, question_data):
        with self._database_engine.new_session() as session:
            question_dao = QuestionDAO(session)
            question = question_dao.get(question_id)
            question = question_dao.update(question, question_data)
            return question

    def delete_question(self, question_id):
        with self._database_engine.new_session() as session:
            question_dao = QuestionDAO(session)
            question = question_dao.get(question_id)
            question_dao.delete(question)
