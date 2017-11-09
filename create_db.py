import json, logging
# using SQLAlchmey, creating a new DB is as easy
# as creating a new object in Python.

# import the following dependencies from SQLAlchmey
# and the empty database we created into our environment
from sqlalchemy.orm import sessionmaker
from models import Base, Book, Author, Publisher, engine

# bind the engine to the base class. This makes the connection
# between our class definitions and the corresponding tables
# within our database
Base.metadata.bind = engine

# create session maker object to establish a link
# of communication between our code execution and
# the engine we just created
DBSession = sessionmaker(bind=engine)

# in order to create, read, update or delete information
# on our database, SQLAlchmey executes database operations
# via an interface called a session.
# A session allows us to write down all the commands
# we want to execute but not send them to the DB
# until we call "commit"
# create an instance of DBSession
session = DBSession()

def addAuthor(authorName, authorBirthDate, authorEducation, authorNationality, authorAlmaMater, authorWiki, authorImage, authorDesc, newBook ):
    auth= session.query(Author).filter(Author.name == authorName).all()

    if len(auth) == 0:
        auth = Author(name=authorName,
                        birthDate=authorBirthDate,
                        education=authorEducation,
                        nationality=authorNationality,
                        alma_mater=authorAlmaMater,
                        wikipedia=authorWiki,
                        image=authorImage,
                        description=authorDesc
                        )
        auth.books = [newBook]
        return auth
    else:
        auth = auth[0]
        auth.books.append(newBook)
        return auth

def addPublisher(publisherName, publisherParCom, publisherOwner, publisherLoc, publisherYear, publisherImage, publisherWebpage, publisherWiki, publisherDesc,newBook):
    pub = session.query(Publisher).filter(Publisher.name == publisherName).all()

    if len(pub) == 0:
        pub = Publisher(name=publisherName,
                        parentCompany=publisherParCom,
                        owner=publisherOwner,
                        location=publisherLoc,
                        yearFounded=publisherYear,
                        image=publisherImage,
                        website=publisherWebpage,
                        wikipedia=publisherWiki,
                        description=publisherDesc
                        )
        pub.books = [newBook]
        session.add(pub)
        return pub
    else:
        pub = pub[0]
        pub.books.append(newBook)
        session.add(pub)
        return pub

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn


def create_books():
    book = load_json('books.json')

    for oneBook in book['Books']:
        #Extract book data
        title = oneBook['title']
        isbn = oneBook['isbn']
        googleid = oneBook['google_id']
        datePub = oneBook['publication_date']
        description = oneBook['description']
        image = oneBook['image_url']

        #Extract author data
        authorDict = oneBook['authors']
        authorName = authorDict['name']
        authorBirthDate = authorDict['born']
        authorEducation = authorDict['education']
        authorNationality = authorDict['nationality']
        authorAlmaMater = authorDict['alma_mater']
        authorWiki = authorDict['wikipedia_url']
        authorImage = authorDict['image_url']
        authorDesc = authorDict['description']

        #Extract publisher data
        publisherDict = oneBook['publishers']
        publisherName = publisherDict['name']
        publisherParCom = publisherDict['parent company']
        publisherOwner = publisherDict['owner']
        publisherLoc = publisherDict['location']
        publisherYear = publisherDict['founded']
        publisherImage = publisherDict['image_url']
        publisherWebpage = publisherDict['website']
        publisherWiki = publisherDict['wikipedia_url']
        publisherDesc = publisherDict['description']

        newBook = Book(title=title,
                       isbn=isbn,
                       google_id=googleid,
                       datePublished=datePub,
                       description=description,
                       image=image
                       )

        session.add(newBook)


        author = addAuthor(authorName,
                  authorBirthDate,
                  authorEducation,
                  authorNationality,
                  authorAlmaMater,
                  authorWiki,
                  authorImage,
                  authorDesc,
                  newBook
                  )

        publisher = addPublisher(publisherName,
                     publisherParCom,
                     publisherOwner,
                     publisherLoc,
                     publisherYear,
                     publisherImage,
                     publisherWebpage,
                     publisherWiki,
                     publisherDesc,
                     newBook
                     )

        author.publishers.append(publisher)
        session.add(author)
        # commit the session to my DB.
        session.commit()


create_books()
