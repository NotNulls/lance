from app.models import User, Appointment, Instructor, InstructorSchedule, Service
from app import app, db

@app.shell_context_processor
def make_shell_context():
    return {'db':db,'User': User, 'Appointment':Appointment, 'Service':Service, 'Instructor':Instructor, 'InstructorSchedule': InstructorSchedule}

