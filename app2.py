from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SubmitField
import sqlite3
import json
from functions import add_exercise_details,add_exercise_history,dategetter
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change 'your_secret_key' to a secure, secret key

DB_NAME = 'exercise_databasev2.db'

class ExerciseForm(FlaskForm):
    date = StringField('Date (YYYY-MM-DD)')
    exercised = BooleanField('Exercised Today?')
    weight = FloatField('Weight')
    protein_intake = BooleanField('Took Protein Today?')
    water_consumed = FloatField('Water Consumed (in liters)')
    exercise_name = StringField('Exercise Name')
    exercise_data = StringField('Exercise Data (format: [(weight, reps),...])')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ExerciseForm()
    if form.validate_on_submit():
        date = form.date.data
        exercised = form.exercised.data
        weight = form.weight.data
        protein_intake = form.protein_intake.data
        water_consumed = form.water_consumed.data
        exercise_name = form.exercise_name.data
        # Parsing exercise_data from string to list of tuples
        exercise_data = json.loads(form.exercise_data.data)
        dates = dategetter()
        
        if date not in dates:
            add_exercise_history(date, exercised, weight, protein_intake, water_consumed)
        add_exercise_details(date, exercise_name, exercise_data)

        flash('Data added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
