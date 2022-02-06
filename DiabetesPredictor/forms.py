from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SubmitField
from wtforms.validators import NumberRange, DataRequired


class DiabetesForm(FlaskForm):
    pregnancies = IntegerField('Pregnancies', validators=[NumberRange(min=0, max=20)],
                               render_kw={'placeholder': 'Number of Pregnancies'})
    glucose = IntegerField('Glucose', validators=[NumberRange(min=0, max=200)],
                           render_kw={'placeholder': 'Plasma glucose concentration '})
    bp = IntegerField('Blood Pressure', validators=[NumberRange(min=0, max=125)],
                      render_kw={'placeholder': 'Diastolic Blood pressure (mm Hg)'})
    skin_thickness = IntegerField('Skin Thickness', validators=[NumberRange(min=0, max=100)],
                                  render_kw={'placeholder': 'Triceps skin fold(mm)'})
    insulin = IntegerField('Insulin', validators=[NumberRange(min=0, max=850)],
                           render_kw={'placeholder': '2-Hour serum insulin (mu U/ml)'})
    bmi = FloatField('BMI', validators=[NumberRange(min=0, max=68)],
                     render_kw={'placeholder': 'Body mass index (weight in kg/(height in m)^2)'})
    pedigree = FloatField('Diabetes Pedigree Function', validators=[NumberRange(min=0, max=3)],
                          render_kw={'placeholder': 'Pedigree Function'})
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1, max=100)],
                       render_kw={'placeholder': 'Age (years)'})
    submit = SubmitField('Submit')
