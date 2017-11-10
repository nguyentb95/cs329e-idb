from flask import Flask
from flask import request
from flask import render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book, Author, Publisher, engine
from create_db import create_books, session

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/<string:pagename>')
def page(pagename):
    return render_template(pagename.lower()+'.html')

@app.route('/bookmodel')
def book():
    return render_template('bookmodel.html',
                           bookRows = session.query(Book).all()
                           )

@app.route('/test/') #put this into index later
def testbooks():
    return render_template('testpage.html')



if __name__ == '__main__':
    app.run('127.0.0.1', port = 8080, debug=True)

