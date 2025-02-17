from flask import Flask, render_template
from jinja2 import FileSystemLoader

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/films')
def films():
    return render_template('films.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/films/galactic-battles')
def galactic_battles():
    return render_template('galactic-battles.html')

@app.route('/films/charles')
def charles():
    return render_template('charles.html')

@app.route('/films/charles-renaissance')
def charles_renaissance():
    return render_template('charles-renaissance.html')

if __name__ == '__main__':
    app.run(debug=True)
