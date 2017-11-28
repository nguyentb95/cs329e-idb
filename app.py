from flask import Flask
from flask import request
from flask import render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book, Author, Publisher, engine
from create_db import create_books, session
import subprocess
import json
import test

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html',
                           results = False)

@app.route('/search', methods=['GET','POST'])
def searchResults():
    searchterm = request.form['text']
    print(searchterm)
    return render_template('search.html',
                            results = True,
                            searchResultsBooks = session.query(Book).filter(Book.title.ilike('%' + searchterm + '%')).all(),
                            searchResultsAuthors = session.query(Author).filter(Author.name.ilike('%'+ searchterm + '%')).all(),
                            searchResultsPublishers = session.query(Publisher).filter(Publisher.name.ilike('%' + searchterm +'%'))
                            )


@app.route('/<string:pagename>')
def page(pagename):
    return render_template(pagename.lower()+'.html')

@app.route('/bookmodel')
def book():
    return render_template('bookmodel.html',
                           bookRows = session.query(Book).order_by(Book.title).all()
                           )
@app.route('/authormodel')
def author():
    return render_template('authormodel.html',
                           authorRows = session.query(Author).order_by(Author.name).all()
                           )
@app.route('/publishermodel')
def publisher():
    return render_template('publishermodel.html',
                           publisherRows = session.query(Publisher).order_by(Publisher.name).all()
                           )

@app.route('/bookpage/<string:bookisbn>')
def bookpage(bookisbn):
    return render_template('genericbook.html',
                           book = session.query(Book).filter(Book.isbn == bookisbn).one()
                           )

@app.route('/authorpage/<string:authorname>')
def authorpage(authorname):
    print(authorname)
    return render_template('genericauthor.html',
                           author = session.query(Author).filter(Author.name == authorname).one()
                           )

@app.route('/publisherpage/<string:publishername>')
def publisherpage(publishername):
    return render_template('genericpublisher.html',
                           publisher = session.query(Publisher).filter(Publisher.name == publishername).one()
                           )


@app.route('/unittests')
def unittests():
    output = subprocess.getoutput("python test.py")
    return render_template('unittests.html',
                           output = output.split("\n"))

if __name__ == '__main__':
    app.run('127.0.0.1', port = 8080, debug=True)

