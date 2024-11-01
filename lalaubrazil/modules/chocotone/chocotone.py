from flask import Blueprint, render_template, request, redirect, flash
from models import Chocotone
from database import db

bp_chocotone = Blueprint("chocotones", __name__, template_folder="templates")

@bp_chocotone.route("/")
def index():
    u = Chocotone.query.all()
    return render_template('chocotone.html', dados = u)

@bp_chocotone.route("/add")
def add():
    return render_template('chocotone_add.html')

@bp_chocotone.route("/save", methods=["POST"])
def save():
    sabor = request.form.get("sabor")
    ingredientes = request.form.get("ingredientes")
    preco = request.form.get("preco")
    if sabor and preco and ingredientes:
        lalau_db = Chocotone(sabor, ingredientes, preco)
        db.session.add(lalau_db)
        db.session.commit()
        flash("Chocotone salvo!")
        return redirect("/chocotones")
    else:
        flash("Preencha todos os campos!")
        return redirect("/chocotones/add") 