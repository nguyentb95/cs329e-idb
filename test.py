import os
import unittest
from models import Base, Book, Author, Publisher, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class DBTestCases(unittest.TestCase):
    def test_book_1(self):
        s = Book(isbn='20', title = 'C++', google_id = "45", datePublished = "2015-12-08", description = "It is a impressive book.", image="http://upload.wikimedia.org/wikipedia/en/thumb/6/6f/Pottermore.png/225px-Pottermore.png")
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(isbn = '20').one()
        self.assertEqual(str(r.isbn), '20')

        session.query(Book).filter_by(isbn = '20').delete()
        session.commit()

    def test_book_2(self):
        s = Book(isbn='33', title = 'How to be Awesome', google_id = "11", datePublished = "2017-11-11", description = "Best book of all time.", image="https://cdn.business2community.com/wp-content/uploads/2016/03/Vd3MJo.jpg")
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(isbn = '33').one()
        self.assertEqual(str(r.isbn), '33')

        session.query(Book).filter_by(isbn = '33').delete()
        session.commit()

    def test_book_3(self):
        s = Book(isbn='37', title = 'How to be bad', google_id = "22", datePublished = "2017-11-12", description = "Wrost book of all time.", image="https://cdn.business2community.com/wp-content/uploads/2016/03/Vd3MJo.jpg")
        session.add(s)
        session.commit()


        r = session.query(Book).filter_by(isbn = '37').one()
        self.assertEqual(str(r.isbn), '37')

        session.query(Book).filter_by(isbn = '37').delete()
        session.commit()
        
    def test_author_1(self):
        s = Author(name='harperlee', birthDate = '1965-07-31', education = "Bachelor of Arts", nationality = "British", alma_mater = "University of Exeter", wikipedia="https://en.wikipedia.org/wiki/J._K._Rowling", image="http://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/J._K._Rowling_2010.jpg/220px-J._K._Rowling_2010.jpg", description="oanne \"Jo\" Rowling, OBE, FRSL, pen names J. K. Rowling and Robert Galbraith, is a British novelist, screenwriter and film producer best known as the author of the Harry Potter fantasy series.")
        session.add(s)
        session.commit()


        r = session.query(Author).filter_by(name = 'harperlee').one()
        self.assertEqual(str(r.name), 'harperlee')

        session.query(Author).filter_by(name= 'harperlee').delete()
        session.commit()

    def test_author_2(self):
        s = Author(name='cslewis', birthDate = '1898-11-29', education = "Bachelor of Arts", nationality = "Irish", alma_mater = "University of Oxford", wikipedia="https://en.wikipedia.org/wiki/C._S._Lewis", image="https://upload.wikimedia.org/wikipedia/en/1/1e/C.s.lewis3.JPG", description="Clive Staples Lewis was a British novelist, poet, academic, medievalist, literary critic, essayist, lay theologian, broadcaster, lecturer, and Christian apologist. He held academic positions at both Oxford University and Cambridge University.")
        session.add(s)
        session.commit()


        r = session.query(Author).filter_by(name = 'cslewis').one()
        self.assertEqual(str(r.name), 'cslewis')

        session.query(Author).filter_by(name= 'cslewis').delete()
        session.commit()

    def test_author_3(self):
        s = Author(name='chuck', birthDate = '1898-12-29', education = "nothing", nationality = "welsh", alma_mater = "University of nowhere", wikipedia="https://en.wikipedia.org/wiki/C._S._Lewis", image="https://upload.wikimedia.org/wikipedia/en/1/1e/C.s.lewis3.JPG", description="Clive Staples Lewis was a British novelist, poet, academic, medievalist, literary critic, essayist, lay theologian, broadcaster, lecturer, and Christian apologist. He held academic positions at both Oxford University and Cambridge University.")
        session.add(s)
        session.commit()


        r = session.query(Author).filter_by(name = 'chuck').one()
        self.assertEqual(str(r.name), 'chuck')

        session.query(Author).filter_by(name= 'chuck').delete()
        session.commit()

    def test_publisher_1(self):
        s = Publisher(name='Pottermore', parentCompany = 'C++', owner = "Yuto", location = "England", yearFounded = "1965-07-31", image="http://upload.wikimedia.org/wikipedia/en/thumb/6/6f/Pottermore.png/225px-Pottermore.png", website = "http://www.pottermore.com\nshop.pottermore.com", wikipedia= "http://www.pottermore.com\nshop.pottermore.com", description="Pottermore is the digital publishing, e-commerce, entertainment, and news company from J.K. Rowling and is the global digital publisher of Harry Potter and J.K. Rowling's Wizarding World.")
        session.add(s)
        session.commit()


        r = session.query(Publisher).filter_by(name = 'Pottermore').one()
        self.assertEqual(str(r.name), 'Pottermore')

        session.query(Publisher).filter_by(name = 'Pottermore').delete()
        session.commit()

    def test_publisher_2(self):
        s = Publisher(name='Scholastic', parentCompany = 'Scholastic', owner = "Public Company", location = "U.S.", yearFounded = "1920-10-22", image="https://www.dedicatedteacher.com/media/images/publishers/large/sch_700.jpg", website = "http://www.scholastic.com/home/", wikipedia= "https://en.wikipedia.org/wiki/Scholastic_Corporation", description="Scholastic Corporation is an American multinational publishing, education and media company known for publishing, selling, and distributing books and educational materials for schools, teachers, parents, and children. ")
        session.add(s)
        session.commit()


        r = session.query(Publisher).filter_by(name = 'Scholastic').one()
        self.assertEqual(str(r.name), 'Scholastic')

        session.query(Publisher).filter_by(name = 'Scholastic').delete()
        session.commit()

    def test_publisher_3(self):
        s = Publisher(name='fakepub', parentCompany = 'fakepub', owner = "fakepub", location = "U.S.", yearFounded = "1900-10-22", image="https://www.dedicatedteacher.com/media/images/publishers/large/sch_700.jpg", website = "http://www.scholastic.com/home/", wikipedia= "https://en.wikipedia.org/wiki/Scholastic_Corporation", description="Scholastic Corporation is an American multinational publishing, education and media company known for publishing, selling, and distributing books and educational materials for schools, teachers, parents, and children. ")
        session.add(s)
        session.commit()


        r = session.query(Publisher).filter_by(name = 'fakepub').one()
        self.assertEqual(str(r.name), 'fakepub')

        session.query(Publisher).filter_by(name = 'fakepub').delete()
        session.commit()

if __name__ == '__main__':
    unittest.main()
