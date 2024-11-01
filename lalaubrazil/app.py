from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config["SECRET_KEY"] = "FROMTHESCREENTOTHERINGTOTHEPENTOTHEKING"
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/lalau_db"
app.config["SQLALCHEMY_DATABASE_URI"] = conexao
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from database import db
from flask_migrate import Migrate
from models import Usuario, Chocotone, Pedido

db.init_app(app)
migrate = Migrate(app, db)

from modules.usuarios.usuarios import bp_usuario
app.register_blueprint(bp_usuario, url_prefix="/usuarios")

from modules.chocotone.chocotone import bp_chocotone
app.register_blueprint(bp_chocotone, url_prefix="/chocotones")