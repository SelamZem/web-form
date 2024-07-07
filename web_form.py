from flask import Flask, render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectMultipleField, RadioField, SubmitField, TextAreaField, SelectField,PasswordField,validators
from wtforms.validators import DataRequired, Email, EqualTo, input_required, ValidationError
from email_validator import validate_email, EmailNotValidError
from wtforms.widgets import ListWidget, CheckboxInput

app = Flask(__name__)
app.config['SECRET_KEY'] = 'selam'

def validate_checkbox_selected(form, checked):
    if not checked.data:
        raise ValidationError('please awlect at least one checkbox')

class RegisterForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators= [DataRequired(), Email()])#Email ...validates the email
    password = PasswordField('Password', validators=[DataRequired()])  
    confirm_password = PasswordField('Confirm password',validators=[DataRequired(), EqualTo('password')])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')], validators=[input_required()])

    interest_choices = [('web_development', 'Website development'),('data_science', 'Data_Scinece and AI'),('game_development', 'Game development'), ('cyber_security','Cyber security')]
    interest = SelectMultipleField('Interests', choices=interest_choices,option_widget=CheckboxInput(), widget=ListWidget(prefix_label=False))
        #prefix_label= False =>the labels are the right of the check boxes

    city = SelectField('City',choices=[('addis_ababa', 'Addis Ababa'),('adama','Adama'),('hawassa','Hawassa')], validators=[DataRequired()])
    comment = TextAreaField('Comment')

    submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.password.data
        gender = form.gender.data
        checked_interests= form.interest.data
        selected_city= form.city.data
        comment = form.comment.data

        return redirect(url_for('registered'))
    return render_template('index.html', form=form)

@app.route('/registered')
def registered():
    return '<h1>Successfully Registered</h1>'
