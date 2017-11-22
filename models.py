
# -*- coding: utf-8 -*-

from mongoengine import StringField
from extensions import db
from flask_login import UserMixin


class User(UserMixin,db.Document):

    username=StringField(default="")
    password=StringField(default="")

    def get_userid(self):
        return self.id
