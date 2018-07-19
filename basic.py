from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    name = 'Peefer'
    letters = list(name)
    pup_dict = {'pup_name':'sammy'}
    return render_template('basic2.html', name=name, letters=letters, pup_dict=pup_dict)


if __name__ == '__main__':
    app.run(debug=True)