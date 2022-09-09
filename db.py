from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Base = None
# session = None
#
#
# def connect_db():

url = f'sqlite:///DB_HW_9.db'
Base = declarative_base()
engine = create_engine(url)   #, echo=True)

DBSession = sessionmaker(bind=engine)
session = DBSession()


# class Contact(Base):
#     __tablename__ = 'contacts'
#     id = Column(Integer, primary_key=True)
#     user_name = Column(String(120), nullable=False)
#     phone = Column('phone', String(100), nullable=False)
#     birthday = Column('birthday', String(100), nullable=True)
#     email = Column('email', String(100), nullable=True)
#     address = Column('address', String(100), nullable=True)
#
#
# class Notate(Base):
#     __tablename__ = 'notates'
#     id = Column(Integer, primary_key=True)
#     notate = Column(String(1000), nullable=False)
#     tag = Column(String(100), nullable=True)