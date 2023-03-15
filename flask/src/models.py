from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))
    nick_name = Column(String(255))
    age = Column(Integer)
    sex = Column(String(255))
    address = Column(String(255))

    @staticmethod
    def keys():
        return ['id', 'username', 'password', 'nick_name', 'age', 'sex', 'address']


    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'nick_name': self.nick_name,
            'age': self.age,
            'sex': self.sex,
            'address': self.address
        }