'''
This file defines the models for a book
'''
# for manipulating diff parts of Python's run-time environment
import sys
import os
# for writing mapper code
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Date

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for writing mapper code (create out foreign key relationship)
from sqlalchemy.orm import relationship

# for configuring code at the end of the file
from sqlalchemy import create_engine

# for creating an instance of the declarative_base class
# (the declarative base class will let SQLAlchemy know
# that our classes are special SQLAlchemy classes that
# corresponds to tables in our DB)
Base = declarative_base()

# Relational Tables

publisher_author_table = Table('publisherAuthorRelational', Base.metadata,
                               Column('publisher_id', String(250), ForeignKey('publisher.name')),
                               Column('author_id', String(250), ForeignKey('author.name'))
                               )


# Book table
class Book(Base):
    __tablename__ = "book"
    isbn = Column(String(13), primary_key=True)
    title = Column(String(250))
    google_id = Column(String(100))
    datePublished = Column(String(10))
    description = Column(String(5000))
    image = Column(String(1000))

    author = Column(String(250), ForeignKey('author.name'))
    publisher = Column(String(250), ForeignKey('publisher.name'))


# Author table
class Author(Base):
    __tablename__ = "author"
    name = Column(String(250), primary_key=True)
    birthDate = Column(String(100))
    education = Column(String(500))
    nationality = Column(String(80))
    alma_mater = Column(String(500))
    wikipedia = Column(String(1000))
    image = Column(String(1000))
    description = Column(String(1000))

    books = relationship("Book")
    publishers = relationship("Publisher",
                              secondary=publisher_author_table,
                              backref='authors'
                              )


# Publisher table
class Publisher(Base):
    __tablename__ = "publisher"
    name = Column(String(250), primary_key=True)
    parentCompany = Column(String(250))
    owner = Column(String(250))
    location = Column(String(100))
    yearFounded = Column(String(100))
    image = Column(String(1000))
    website = Column(String(250))
    wikipedia = Column(String(250))
    description = Column(String(1000))

    books = relationship("Book")


SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:blank@localhost/digitalbinding')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
