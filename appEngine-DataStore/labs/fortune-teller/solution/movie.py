from google.appengine.ext import ndb

class Movie(ndb.Model):

    title = ndb.StringProperty(required = True)
    media_type = ndb.StringProperty(required = True, default='Movie')
    runtime_mins = ndb.IntegerProperty(required = False)
    rating = ndb.FloatProperty(required = False)

class Person(ndb.Model):
    fname = ndb.StringProperty(required=True)
    lname = ndb.StringProperty(required=False)
    occupation = ndb.StringProperty(required=False)
    age = ndb.IntegerProperty(required=True, default=15)

class Company(ndb.Model):
    company_name = ndb.StringProperty(required=True)
    location = ndb.StringProperty(required=False)
    description = ndb.StringProperty(required=True)

class College(ndb.Model):
    college_name = ndb.StringProperty(required=True)
    class_size = ndb.IntegerProperty(required=True)
    location = ndb.StringProperty(required=True)
