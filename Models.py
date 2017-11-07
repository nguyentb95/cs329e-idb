from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

#Book table
class Book(db.Model):\
	id = db.Column(db.Integer, primary_key=True)
	ISBN = db.Column(db.Integer)
	Title = db.Column(db.String(250))
	Google_id = db.Column(db.String(100))
	Pages = db.Column(Integer)
	YearPublished = db.Column(Integer)
	Description = db.Column(db.String(1000))
	Image = db.Column(db.String(1000))

	def __repr__(self):
		return '<Book %r>' % self.ISBN

#Author table
class Author(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(80))
	BirthDate = db.Column(db.DateTime)
	Education = db.Column(db.String(80))
	Nationality = db.Column(db.String(80))
	Alma_mater = db.Column(db.String(80))
	Wikipedia = db.Coumn(String(1000))
	Image = db.Column(db.String(1000))

	def __repr__(self):
		return '<Author %r>' % self.Name

#Publisher table
class Publisher(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(250))
	ParentCompany = db.Column(db.String(250))
	ParentCountry = db.Column(db.String(100))
	Location = db.Column(db.String(100))
	YearFounded = db.Column(db.Integer)
	Image = db.Column(db.String(1000))
	Website = db.Column(db.String(250))
	Description = db.Column(db.String(1000))

	def __repr__(self):
		return '<Publisher %r>' % self.Name

#Junction Tables
class BookAuthor(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	Author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
	author = db.relationship('Author', backref=db.backref('books', lazy = True))

	Book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
	book = db.relationship('Book', backref=db.backref('books', lazy = True))

class BookPublisher(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	Publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))
	publisher = db.relationship('Publisher', backref=db.backref('books', lazy = True))

	Book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
	book = db.relationship('Book', backref=db.backref('books', lazy = True))

