from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/book/<bookname>')
def book(bookname):
    return render_template(bookname.lower()+'.html')

if __name__ == '__main__':
    app.run('127.0.0.1', port = 8080, debug=True)