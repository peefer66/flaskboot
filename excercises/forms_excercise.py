# The exercise for assessing if password has upper, lower case letter and ends in a number
from flask import Flask, render_template, request

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    name = request.args.get('username')
    errors = []
    # Logic to determine if username contains a Capital letter, a lowercase letter and a number
    if not any(letter.isupper() for letter in name):
        errors.append('Your username needs at least 1 capital letter.')
    
    if not any(letter.islower() for letter in name):
        errors.append('Your username needs at least 1 lower case letter')
    
    if not any(letter.isnumeric() for letter in name):
        errors.append('Your username needs at least 1 number.')

    return render_template('report.html', name=name, errors=errors)

if __name__ == '__main__':
    app.run(debug=True)