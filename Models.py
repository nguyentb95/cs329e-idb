'''
This file defines the models for a book
'''
# for manipulating diff parts of Python's run-time environment
import sys
import os
# for writing mapper code
from sqlalchemy import Column, ForeignKey, Integer, String, Table

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
                               Column('publisher_id', String(250), ForeignKey('publisher.Name')),
                               Column('author_id', String(250), ForeignKey('author.Name'))
                               )


# Book table
class Book(Base):
    __tablename__ = "book"
    ISBN = Column(Integer, primary_key=True)
    Title = Column(String(250))
    Google_id = Column(String(100))
    Pages = Column(Integer)
    YearPublished = Column(Integer)
    Description = Column(String(1000))
    Image = Column(String(1000))

    author = Column(String(250), ForeignKey('author.Name'))
    publisher = Column(String(250), ForeignKey('publisher.Name'))


# Author table
class Author(Base):
    __tablename__ = "author"
    Name = Column(String(250), primary_key=True)
    BirthDate = Column(DateTime)
    Education = Column(String(80))
    Nationality = Column(String(80))
    Alma_mater = Column(String(80))
    Wikipedia = Column(String(1000))
    Image = Column(String(1000))

    books = relationship("Book", backref='author')
    publishers = relationship("Publisher",
                              secondary=publisher_author_table,
                              backref='authors'
                              )


# Publisher table
class Publisher(Base):
    __tablename__ = "publisher"
    Name = Column(String(250), primary_key=True)
    ParentCompany = Column(String(250))
    ParentCountry = Column(String(100))
    Location = Column(String(100))
    YearFounded = Column(Integer)
    Image = Column(String(1000))
    Website = Column(String(250))
    Description = Column(String(1000))

    books = relationship("Book", backref='publisher')


SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:localhost/digitalbinding')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
