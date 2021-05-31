# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField
from wtforms.validators import InputRequired, Email, DataRequired

## login and registration

class LoginForm(FlaskForm):
    username = TextField    ('Username', id='username_login'   , validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login'        , validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username = TextField('Username'     , id='username_create' , validators=[DataRequired()])
    email    = TextField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
    password = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])

class PredictForm(FlaskForm):
    neighbourhood_group = SelectField('Neighbourhood_group',
                                      choices=[(1,'Brooklyn'), (2, 'Manhattan'), (3, 'Queens'), (4, 'Staten Island'), (5, 'Bronx')],
                                      coerce=int
    )
    roomtype = SelectField('Roomtype', 
                      choices=[(1,"Private room"),(2,"Entire home/apt"),(3,"Shared room")],
                      coerce=int)
    minimum_nights = TextField('Minimum_nights', id='night_create' , validators=[DataRequired()])
