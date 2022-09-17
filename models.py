from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(120), nullable=False)
    birthday = Column('birthday', String(100), nullable=True)
    email = Column('email', String(100), nullable=True)
    address = Column('address', String(100), nullable=True)
    phones = relationship('PhoneToContact', back_populates='contact')


class Notate(Base):
    __tablename__ = 'notates'
    id = Column(Integer, primary_key=True)
    notate = Column('notate', String(1000), nullable=False)
    tag = Column('tag', String(100), nullable=True)


class PhoneToContact(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True, nullable=False)
    phone = Column('phone', String(100))
    contact_id = Column('contact_id', ForeignKey('contacts.id', ondelete='CASCADE'), nullable=False)
    contact = relationship('Contact', back_populates='phones')
