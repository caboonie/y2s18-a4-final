from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    name = Column(String)
    location = Column(String)



    def __repr__(self):
        return ("username: {}, password:{}, email:{}, name:{}, location:{}".format(self.username, self.password, self.email, self.name, self.location))