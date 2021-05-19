from model.mapping import Base
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey, Integer


class Game(Base):
    __tablename__ = "games"
    __table_args__ = (UniqueConstraint('id'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    creator_id = Column(String, ForeignKey('players.id'))
    nbround = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "creator_id": self.creator_id,
            "nbround": self.nbround
        }
