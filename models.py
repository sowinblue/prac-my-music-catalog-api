from sqlalchemy import Column, Integer, String
from database import Base


class Track(Base):
    __tablename__ = "tracks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    bpm = Column(Integer)
    genre = Column(String)
    soundcloud_url = Column(String)