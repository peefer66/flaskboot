from flask import Flask, render_template, url_for, session, redirect
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, TextField, DateTimeField,
                     RadioField, TextAreaField, BooleanField, SelectField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you', validators=[DataRequired()])
    neutered = BooleanField('have you been neutered?')
    mood = RadioField('What is your mood?',
                         choices=[('mood_one', 'Sad'), ('mood_two','Happy')])
    food =SelectField(u'What is you favorite meal',
                        choices=[('c','Chicken'), ('b','Beef'),('f','Fish')])
    comments = TextAreaField()
    submit = SubmitField('submit')

@app.route('/', methods=['GET', 'POST'])
def index():

    # Create instance of the form.
    form = InfoForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.

        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food.data
        session['comments'] = form.comments.data

        return redirect(url_for("thankyou"))


    return render_template('fields_index.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('fields_thankyou.html')







if __name__ == '__main__':
    app.run(debug=True)