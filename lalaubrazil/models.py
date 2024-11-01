from database import db

class Usuario(db.Model):

    __tablename__ = "tb_usuario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(200))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return F"Usuario {self.nome}"
    
class Chocotone(db.Model):
    __tablename__ = "tb_chocotone"
    id = db.Column(db.Integer, primary_key=True)
    sabor = db.Column(db.String(100))
    ingredientes = db.Column(db.String(100))
    preco = db.Column(db.Float(2, 10))

    def __init__(self, sabor, ingredientes, preco):
        self.sabor = sabor
        self.ingredientes = ingredientes
        self.preco = preco
        
    def __repr__(self):
        return f"Chocotone {self.sabor}"
        

class Pedido(db.Model):
    __tablename__ = "tb_pedido"
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey("tb_usuario.id"))
    chocoID = db.Column(db.Integer, db.ForeignKey("tb_chocotone.id"))
    data = db.Column(db.Date)
    
    usuario = db.relationship("Usuario", foreign_keys = userID)
    chocotone = db.relationship("Chocotone", foreign_keys = chocoID)

    def __init__(self, userID, chocoID, data):
        self.userID = userID
        self.chocoID = chocoID
        self.data = data

    def __repr__(self):
        return f"Pedido | {self.usuario.nome} | {self.chocotone.sabor} | {self.data}"