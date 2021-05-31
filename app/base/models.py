# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import os
import csv
from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String


from app import db, login_manager

from app.base.util import hash_pass

class User(db.Model, UserMixin):

    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(Binary)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass( value ) # we need bytes here (not plain str)
                
            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)

class House(db.Model):

    __tablename__ = 'House'

    id = db.Column(db.Integer(), primary_key=True)
    neighbourhood_group = db.Column(db.String(), nullable=False)
    neighbourhood = db.Column(db.String(), nullable=False)
    room_type = db.Column(db.String(), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    minimum_nights = db.Column(db.Integer())

    def __repr__(self):
        return f"""
        id : {self.id},
        neighbourhood_group : {self.neighbourhood_group},
        neighbourhood = {self.neighbourhood},
        room_type = {self.room_type},
        price = {self.price},
        minimum_nights = {self.minimum_nights}
        """

def add_house_data():
    CSV_FILEPATH = os.path.join(os.getcwd(), 'app', 'airbnb_listing.csv')

    with open(CSV_FILEPATH) as File:
        # create user list to store user dict
        user_list = []
        # read csv file and pass 1st line(columns name)
        reader = csv.reader(File, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        next(reader) 

        for i in reader:
            record = House(**{
                'id' : i[0],
                'neighbourhood_group' : i[1],
                'neighbourhood' : i[2],
                'room_type' : i[3],
                'price' : i[4],
                'minimum_nights' : i[5],
            })
            breakpoint()
            db.session.add(record)
            db.session.commit()



@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None

