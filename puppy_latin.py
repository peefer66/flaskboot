from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Go to /puppy_name/name/ and see the result!</h1>'

@app.route('/puppy_name/<name>')
def puppylatin(name):
    pupname = ''
    if name[-1] == 'y': # last letter
        pupname = name[:-1] + 'iful' # replace last letter of name with iful
    else:
        pupname = name + 'y' # Add y onto name
    return '<h1> Your puppy latin name is {}</h1>'.format(pupname)


if __name__ == '__main__':
    app.run(debug=True)