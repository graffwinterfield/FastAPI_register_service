from database import Base
from sqlalchemy import Numeric, Column, String, Boolean, INT, JSON


class Note(Base):
    __tablename__ = 'note'
    id = Column(INT, primary_key=True)
    timestamp = Column(Numeric, nullable=False)
    is_new = Column(Boolean, nullable=False)
    user_id = Column(String, nullable=False)
    key = Column(String, nullable=False)
    target_id = Column(String, nullable=False)
    data = Column(JSON, nullable=True)
