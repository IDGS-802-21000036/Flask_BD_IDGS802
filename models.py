from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apaterno = db.Column(db.String(50))
    amaterno = db.Column(db.String(50))
    email = db.Column(db.String(50))
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    
    def __repr__(self):
        return '<Alumno %r>' % self.nombre