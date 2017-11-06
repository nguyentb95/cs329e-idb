from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

books = [{'id': 0, \
          'pagename': 'tokillamockingbird', \
          'book': 'To Kill a Mockingbird', \
          'author' :'Harper Lee [POSSIBLE MANY TO ONE]', \
          'googleid': '-D8WBAAAQBAJ', \
          'img': 'https://books.google.com/books/content/images/frontcover/-D8WBAAAQBAJ?fife=w500', \
          'publisher' :'HarperCollins [POSSIBLE MANY TO ONE]'},\
         {'id' : 1, \
          'pagename': 'motherfuckingtemp', \
          'book': '???', \
          'author' :'in', \
          'googleid': 'the', \
          'img': 'DB',
          'publisher' :'instead of this dictionary'}]

authors = [{'id': 0, \
          'pagename': 'harperlee', \
          'book': 'To Kill a Mockingbird [POSSIBLE MANY TO ONE]', \
          'author' :'Harper Lee', \
          'img': 'http://upload.wikimedia.org/wikipedia/commons/5/5f/HarperLee_2007Nov05.jpg', \
          'publisher' :'HarperCollins [POSSIBLE MANY TO ONE]'},\
         {'id' : 1, \
          'pagename': 'motherfuckingtemp', \
          'book': 'put', \
          'author' :'???', \
          'img': 'DB',
          'publishername' :'instead of this dictionary'}]

publishers = [{'id': 0, \
          'pagename': 'harpercollins', \
          'book': 'To Kill a Mockingbird [POSSIBLE MANY TO ONE]', \
          'author' :'Harper Lee [POSSIBLE MANY TO ONE]', \
          'img': 'http://upload.wikimedia.org/wikipedia/en/thumb/0/00/Harpercollins-logo.svg/250px-Harpercollins-logo.svg.png', \
          'publisher' :'Palgrave Macmillan'}]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/<string:pagename>')
def page(pagename):
    return render_template(pagename.lower()+'.html')

@app.route('/test/') #put this into index later
def testbooks():
    return render_template('testpage.html', books=books, authors=authors, publishers=publishers)

@app.route('/book')
def genericbook():
    bid = request.args.get('bid')
    return render_template('genericbook.html', bid = books[int(bid)])

@app.route('/author')
def genericauthor(): ###For loop needs to be put in genericauthor.html to retrieve all books
    aid = request.args.get('aid')
    return render_template('genericauthor.html', aid = authors[int(aid)])

@app.route('/publisher')
def genericpublisher(): ###For loop needs to be put in genericauthor.html to retrieve all books
    pid = request.args.get('pid')
    return render_template('genericpublisher.html', pid = authors[int(pid)])

if __name__ == '__main__':
    app.run('127.0.0.1', port = 8080, debug=True)

