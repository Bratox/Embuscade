from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey, Integer


class Game(Base):
    __tablename__ = "games"
    __table_args__ = (UniqueConstraint('id'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    creator_id = Column(String, ForeignKey('player.id'))
    nbround = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nickname": self.nickname,
            "name": self.name,
            "surname": self.surname,
            "birthday": self.birthday,
            "password": self.password
        }
