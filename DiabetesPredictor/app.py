import os
from flask import Flask, render_template, redirect, url_for
from forms import DiabetesForm
from diabetes_predict import min_max
import pickle

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = DiabetesForm()
    if form.validate_on_submit():
        pregnancies = form.pregnancies.data
        glucose = form.glucose.data
        bp = form.bp.data
        skin_thickness = form.skin_thickness.data
        insulin = form.insulin.data
        bmi = form.bmi.data
        pedigree = form.pedigree.data
        age = form.age.data
        output = model.predict(
            min_max.transform([[pregnancies, glucose, bp, skin_thickness, insulin, bmi, pedigree, age]]))
        predict_percent = round(model.predict_proba(
            min_max.transform([[pregnancies, glucose, bp, skin_thickness, insulin, bmi, pedigree, age]]))[0, 1], 5)
        return redirect(url_for('prediction', output=output, predict_percent=predict_percent))
    return render_template('home.html', title='Home Page', form=form)


@app.route('/about')
def about():
    return render_template('about.html', title='About Page')


@app.route('/prediction/<int:output>/<float:predict_percent>')
def prediction(output, predict_percent):
    return render_template('output.html', output=output, predict_percent=predict_percent)


if __name__ == '__main__':
    app.run(debug=True)
