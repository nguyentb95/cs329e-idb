import os
import unittest
from models import Base, Book, Author, Publisher, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class DBTestCases(unittest.TestCase):
    def book_1(self):
        s = Book(isbn='20', title = 'C++', google_id = "45", datePublished = "2015-12-08", description = "It is a impressive book.", image="http://upload.wikimedia.org/wikipedia/en/thumb/6/6f/Pottermore.png/225px-Pottermore.png")
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(isbn = '20').one()
        self.assertEqual(str(r.isbn), '20')

        session.query(Book).filter_by(isbn = '20').delete()
        session.commit()

    def book_1(self):
        s = Book(isbn='33', title = 'How to be Awesome', google_id = "11", datePublished = "2017-11-11", description = "Best book of all time.", image="https://cdn.business2community.com/wp-content/uploads/2016/03/Vd3MJo.jpg")
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(isbn = '33').one()
        self.assertEqual(str(r.isbn), '33')

        session.query(Book).filter_by(isbn = '33').delete()
        session.commit()


    def author_1(self):
        s = Author(name='harperlee', birthDate = '1965-07-31', education = "achelor of Arts", nationality = "British", alma_mater = "University of Exeter", wikipedia="https://en.wikipedia.org/wiki/J._K._Rowling", image="http://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/J._K._Rowling_2010.jpg/220px-J._K._Rowling_2010.jpg", description="oanne \"Jo\" Rowling, OBE, FRSL, pen names J. K. Rowling and Robert Galbraith, is a British novelist, screenwriter and film producer best known as the author of the Harry Potter fantasy series.")
        session.add(s)
        session.commit()


        r = session.query(Author).filter_by(name = 'harperlee').one()
        self.assertEqual(str(r.name), 'harperlee')

        session.query(Author).filter_by(name= 'harperlee').delete()
        session.commit()

    def publisher_1(self):
        s = Publisher(name='Pottermore', parentCompany = 'C++', owner = "Yuto", location = "England", yearFounded = "1965-07-31", image="http://upload.wikimedia.org/wikipedia/en/thumb/6/6f/Pottermore.png/225px-Pottermore.png", website = "http://www.pottermore.com\nshop.pottermore.com", wikipedia= "http://www.pottermore.com\nshop.pottermore.com", description="Pottermore is the digital publishing, e-commerce, entertainment, and news company from J.K. Rowling and is the global digital publisher of Harry Potter and J.K. Rowling's Wizarding World.")
        session.add(s)
        session.commit()


        r = session.query(Publisher).filter_by(name = 'Pottermore').one()
        self.assertEqual(str(r.name), 'Pottermore')

        session.query(Publisher).filter_by(name = 'Pottermore').delete()
        session.commit()

if __name__ == '__main__':
    unittest.main()
