from model.mapping import Base
import uuid

from sqlalchemy import Column, Text, UniqueConstraint, String


class Question(Base):
    __tablename__ = "questions"
    __table_args__ = (UniqueConstraint('id'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    title = Column(String(36), nullable=False)
    exp = Column(Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "exp": self.exp,
        }