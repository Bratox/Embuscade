from model.mapping import Base
import uuid

from sqlalchemy import Column, Text, UniqueConstraint, String


class Virus(Base):
    __tablename__ = "virus"
    __table_args__ = (UniqueConstraint('id'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    exp = Column(Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "exp": self.exp,
        }