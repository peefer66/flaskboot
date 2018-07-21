from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def list():
    puppy_names = ['Ted', 'Spike', 'Bella']

    return render_template('mylist.html', puppy_names=puppy_names)

if __name__ == '__main__':
    app.run(debug=True)