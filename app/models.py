from app import db
from flask_login import UserMixin

# Create User model
class User(db.Model, UserMixin):
    __tablename__="user"
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    phone_number = db.Column(db.String(50))
    password_hash = db.Column(db.String(64))
    token = db.Column(db.String(64))
    token_expiration = db.Column(db.DateTime)
    appointment = db.relationship('Appointment', backref="client", lazy=True)
    
    def __repr__(self):
        return '<User: {} {}>'.format(self.name,self.last_name)


# Create Instructor model
class Instructor(db.Model, UserMixin):
    __tablename__="instructor"
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password_hash = db.Column(db.String(64))
    email = db.Column(db.String(50), )
    sport = db.Column(db.String(50))
    license_type = db.Column(db.String(50))
    dates_available = db.Column(db.String(50))
    price = db.Column(db.Float)
    rating = db.Column(db.Integer)
    comments = db.Column(db.String(500))
    appointment = db.relationship('Appointment', backref="instructor", lazy=True)

    def __repr__(self):
        return '<Instructor: {} {}>'.format(self.name, self.last_name)


# Create Appointment model
class Appointment(db.Model):
    __tablename__="appointment"
    uid = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.uid'))
    from_date = db.Column(db.DateTime)
    to_date = db.Column(db.DateTime)
    price_expected = db.Column(db.Float)
    price_full = db.Column(db.Float)
    dicount = db.Column(db.Float)
    cancellation = db.Column(db.Boolean, default=False)
    rating = db.Column(db.Integer)
    comments = db.Column(db.String(500))
    
    
class InstructorSchedule(db.Model, UserMixin):
    __tablename__="instructorschedule"
    uid = db.Column(db.Integer, primary_key=True)
    from_date = db.Column(db.DateTime)
    to_date = db.Column(db.DateTime)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.uid'))


#Create Service model
class Service(db.Model):
    __tablename__="service"
    uid = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'))
    services_booked = db.relationship('ServicesBooked', backref='service', lazy=True)
    services_provided = db.relationship('ServicesProvided', backref='service', lazy=True)


#  Create ServiceProvided
class ServicesProvided(db.Model):
    __tablename__="serviceprovided"
    uid = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.uid'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.uid'))
    price = db.Column(db.Float)


#Create ServiceBooked model
class ServicesBooked(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointment.uid'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.uid'))
    price = db.Column(db.Float)
    
