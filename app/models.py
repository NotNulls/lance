from app import db
from flask_login import UserMixin

# Create User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    type_of_snow_activity = db.Column(db.String(50))
    password_hash = db.Column(db.String(64))
    token = db.Column(db.String(64))
    token_expiration = db.Column(db.DateTime)
    resorts = db.relationship('Resort', secondary='visits', backref='user')
    instructors = db.relationship('Instructor', secondary='lessons', backref='users')

    def __repr__(self):
        return '<User {}>'.format(self.username)

# Create Instructor model
class Instructor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password_hash = db.Column(db.String(64))
    email = db.Column(db.String(50))
    sport = db.Column(db.String(50))
    license_type = db.Column(db.String(50))
    resorts = db.relationship('Resort', secondary='lessons', backref='instructors')
    dates_available = db.Column(db.String(50))
    price = db.Column(db.Float)

    def __repr__(self):
        return '<Instructor {}>'.format(self.username)

# Create Resort model
class Resort(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    country = db.Column(db.String(50))
    type_of_snow_activity_supported = db.Column(db.String(50))

    def __repr__(self):
        return '<Resort {}>'.format(self.username)

# Create Visits model
class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    resort_id = db.Column(db.Integer, db.ForeignKey('resort.id'))

# Create Lessons model
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    resort_id = db.Column(db.Integer, db.ForeignKey('resort.id'))