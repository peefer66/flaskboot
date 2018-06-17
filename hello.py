from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello World </h1>'

@app.route('/info')
def info():
    return '<h1> The world is round </h1>'

@app.route('/puppy/<name>')
def puppy(name):
    return '<h1> This page is for {} </h1>'.format(name.upper()) # format to uppercase

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    name_len = len(name)
    return 'Name length = {}'.format(name_len)


if __name__ == '__main__':
    app.run(debug=True)