from google.appengine.ext import ndb
from datetime import datetime


class Account(ndb.Model):
    username = ndb.StringProperty(required=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def get_by_username(cls, username):
        return cls.query(cls.username == username).get()
