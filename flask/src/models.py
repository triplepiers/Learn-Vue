from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# metadata = Base.metadata


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))
    nick_name = Column(String(255))
    age = Column(Integer)
    sex = Column(String(255))
    address = Column(String(255))

    # def __setattr__(self, key, value):
    #     self.key = value

    # def __init__(self):
    #
    #
    # def __init__(self, uname, pwd, nname, age, sex, address):
    #     self.uname = uname
    #     self.pwd = pwd
    #     self.nick_name = nname
    #     self.age = age
    #     self.sex = sex
    #     self.address = address