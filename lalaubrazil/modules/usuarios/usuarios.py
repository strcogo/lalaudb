from flask import Blueprint, render_template, request, redirect, flash
from models import Usuario
from database import db

bp_usuario = Blueprint("usuarios", __name__, template_folder="templates")

@bp_usuario.route("/")
def index():
    u = Usuario.query.all()
    return render_template('usuario.html', dados = u)

@bp_usuario.route("/add")
def add():
    return render_template('usuario_add.html')

@bp_usuario.route("/save", methods=["POST"])
def save():
    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")
    if nome and senha and email:
        lalau_db = Usuario(nome, email, senha)
        db.session.add(lalau_db)
        db.session.commit()
        flash("Usuario salvo!")
        return redirect("/usuarios")
    else:
        flash("Preencha todos os campos!")
        return redirect("/usuarios/add") 