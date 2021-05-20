from model.mapping import Base, generate_id
import uuid

from sqlalchemy import Column, Text, UniqueConstraint, String


class Jeu(Base):
    __tablename__ = "jeux"
    __table_args__ = (UniqueConstraint('id'),)

    id = Column(String(36), default=generate_id, primary_key=True)

    exp = Column(Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "exp": self.exp,
        }
