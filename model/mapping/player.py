from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint


class Player(Base):
    __tablename__ = "players"
    __table_args__ = (UniqueConstraint('id', 'nickname'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    nickname = Column(String(36), nullable=False)
    name = Column(String(36), nullable=False)
    surname = Column(String(36), nullabel=False)
    password = Column(String(36), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nickname": self.nickname,
            "name": self.name,
            "surname": self.surname,
            "password": self.password
        }
