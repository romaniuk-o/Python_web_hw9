from sqlalchemy import Column, Integer, String


from db import Base


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(120), nullable=False)
    phone = Column('phone', String(100), nullable=False)
    birthday = Column('birthday', String(100), nullable=True)
    email = Column('email', String(100), nullable=True)
    address = Column('address', String(100), nullable=True)
    #phones = relationship('Phones', back_populates='phone')


class Notate(Base):
    __tablename__ = 'notates'
    id = Column(Integer, primary_key=True)
    notate = Column('notate', String(1000), nullable=False)
    tag = Column('tag', String(100), nullable=True)
    #tag = Column(String(100), nullable=True)


# class Phone(Base):
#     __tablename__ = 'phones'
#     id = Column(Integer, primary_key=True)
#     phone = Column('phone', String(100), nullable=False)
#     contact_id = Column('contact_id', ForeignKey('contacts.id', ondelete='CASCADE'), nullable=False)
#     contact = relationship('Contact', back_populates='phones')
#
#
# class Tag(Base):
#     __tablename__ = 'Tags'
#     id = Column(Integer, primary_key=True)
#     tag = Column('tag', String(100), nullable=False)
#     notate_id = Column('notate_id', ForeignKey('notates.id', ondelete='CASCADE'), nullable=False)
#     notate = relationship('Notate', back_populates='tags')