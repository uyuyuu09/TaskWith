from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    # name = Column(String, unique=False)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    admin = Column(Boolean, unique=False, default=False)

    # tickets = relationship("Ticket", back_populates="user")
