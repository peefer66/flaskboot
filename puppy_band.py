from flask import Flask, render_template, request

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    
    return render_template('index.html')
@app.route('/signup_form')
def signup_form():
    return render_template('sign_up_puppy_band.html')

@app.route('/thankyou_puppy_band')
def thankyou_puppy_band():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankyou_puppy_band.html', first=first, last=last)

if __name__ == '__main__':
    app.run(debug=True)