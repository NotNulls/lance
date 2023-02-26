from app.models import User, Lesson, Resort, Instructor, Visit
from app import app, db

@app.shell_context_processor
def make_shell_context():
    return {'db':db,'User': User, 'Lesson':Lesson, 'Resort':Resort, 'Instructor':Instructor, 'Visits':Visit}