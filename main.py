from flask import Flask, request, render_template, Response
from flask_wtf.csrf import CSRFProtect
from flask import flash
from models import db
from config import DevelopmentConfig
import forms
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(error):
    return "{}".format(error), 404



@app.route("/")
def index():
    return render_template("index.html")

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

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()