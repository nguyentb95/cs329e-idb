from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

class Book(db.Model):
	ISBN = db.Column(db.Integer, primary_key=True)
	Title = db.Column(db.String(80), unique=True, nullable=False)
	Author_id = db.Column(db.Integer, db.ForeignKey('author.Author_id'))
	Publisher_id = db.Column(db.Integer)
	Pages = db.Column(Integer)
	YearPublished = db.Column(Integer)

	def __repr__(self):
		return '<Book %r>' % self.ISBN

class Author(db.Model):
	Author_id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(80), nullable=False)
	BirthDate = db.Column(db.DateTime)
	DeathDate = db.Column(db.DateTime)
	Country = db.Column(db.String(80))
	Male = db.Column(db.Boolean)

	def __repr__(self):
		return '<Author %r>' % self.Name

class Publisher(db.Model):
	Publisher_id = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(80), nullable=False)
	ParentCompany = db.Column(db.String(80))
	ParentCountry = db.Column(db.String(80))
	2014Revenue = db.Column(db.Integer)
	YearEstablished = db.Column(db.Integer)
	BookCount = db.Column(db.Integer)

	def __repr__(self):
		return '<Publisher %r>' % self.Name