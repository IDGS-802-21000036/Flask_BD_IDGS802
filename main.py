from flask import Flask, request, render_template, Response, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask import flash
from models import db
from models import Alumnos
from config import DevelopmentConfig
import forms
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(error):
    return "{}".format(error), 404



@app.route("/index", methods=['GET', 'POST'])
def index():
    alumn_form = forms.UsersForm2(request.form)
    
    if request.method == "POST" and alumn_form.validate():
        alumno = Alumnos(nombre = alumn_form.nombre.data, 
                      apaterno = alumn_form.apaterno.data, 
                      email = alumn_form.email.data)
        #insert into alumnos values()
        db.session.add(alumno)
        db.session.commit()
    return render_template("index.html", form = alumn_form)

@app.route('/ABC_Completo', methods=['GET', 'POST'])
def ABCompleto():
    alumn_form = forms.UsersForm2(request.form)
    alumnos = Alumnos.query.all()
    
    return render_template("ABC_Completo.html", form = alumn_form, alumnos = alumnos)

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    print("Dentro 2")
    alumn_form = forms.UserForm(request.form)
    if request.method == "POST" and alumn_form.validate():
        print("Dentro del IF")
        nom = alumn_form.nombre.data
        apaterno = alumn_form.apaterno.data
        amaterno = alumn_form.amaterno.data
        edad = alumn_form.edad.data
        correo = alumn_form.correo.data
        mensaje = "Bienvenido: {}".format(nom)
        print(mensaje)
        flash(mensaje)
        print("Nombre:{}".format(nom))
        print("Email:{}".format(correo))
        print("Apellido paterno:{}".format(apaterno))
        return render_template("alumnos.html", form = alumn_form, nombre = nom, correo = correo, apaterno = apaterno, amaterno = amaterno, edad = edad)
    else:
        return render_template("alumnos.html", form = alumn_form)

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    alumno_form = forms.UsersForm2(request.form)
    if request.method == "GET":
        id = request.args.get('id')
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alumno_form.id.data = request.args.get('id')
        alumno_form.nombre.data = alumno.nombre
        alumno_form.apaterno.data = alumno.apaterno
        alumno_form.email.data = alumno.email
    if request.method == "POST":
        id = alumno_form.id.data
        alumno=Alumnos.query.get(id)
        db.session.delete(alumno)
        db.session.commit()
        #alumno = Alumnos.query.filter_by(id = alumno_form.id.data).delete()
        return redirect(url_for('ABCompleto'))
    return render_template("eliminar.html", form = alumno_form)

@app.route('/modificar', methods=['GET', 'POST'])
def modificar():
    alumno_form = forms.UsersForm2(request.form)
    if request.method == "GET":
        id = request.args.get('id')
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alumno_form.id.data = request.args.get('id')
        alumno_form.nombre.data = alumno.nombre
        alumno_form.apaterno.data = alumno.apaterno
        alumno_form.email.data = alumno.email
    if request.method == "POST":
        id = alumno_form.id.data
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alumno.nombre = alumno_form.nombre.data
        alumno.apaterno = alumno_form.apaterno.data
        alumno.email = alumno_form.email.data
        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template("modificar.html", form = alumno_form)

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()