from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.question import Question
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class QuestionDAO(DAO):

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Question).filter_by(id=id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Question).order_by(Question.id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            question = Question(exp=data.get('exp'))
            self._database_session.add(question)
            self._database_session.flush()
        except IntegrityError:
            raise Error("La question existe deja")

        return question

    def update(self, question, data: dict):
        if 'exp' in data:
            question.exp = data['exp']

        try:
            self._database_session.merge(question)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Data may be malformed")

        return question

    def delete(self, question):
        try:
            self._database_session.delete(question)
        except SQLAlchemyError as e:
            raise Error(str(e))
