from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello World </h1>'

@app.route('/info')
def info():
    return '<h1> The world is round </h1>'

@app.route('/country/<name>')
def country(name):
    return '<h1> This page is for {} </h1>'.format(name.upper())


if __name__ == '__main__':
    app.run(debug=True)