from flask_sqlalchemy import SQLAlchemy 
from __main__ import app
from sqlalchemy.orm import relationship
db = SQLAlchemy(app)

class Sucursal(db.Model):
    __tablename__ = 'sucursal'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    provincia = db.Column(db.String(100), nullable=False)
    localidad = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    repartidores = db.relationship('Repartidor', backref='sucursal', lazy=True)
    paquetes = db.relationship('Paquete', backref='sucursal', lazy=True)
    transportes = db.relationship('Transporte', backref='sucursal', lazy=True)

class Repartidor(db.Model):
    __tablename__ = 'repartidor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.Integer, nullable=False)
    id_sucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    paquetes = db.relationship('Paquete', backref='repartidor', lazy=True)

class Paquete(db.Model):
    __tablename__ = 'paquete'
    id = db.Column(db.Integer, primary_key=True , autoincrement=True)
    numeroEnvio = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    nomdestinatario = db.Column(db.String(100), nullable=False)
    dirdestinatario = db.Column(db.String(100), nullable=False)
    entregado = db.Column(db.Boolean, nullable=False)
    observaciones = db.Column(db.String(100), nullable=False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'), nullable=False)
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'), nullable=False)

class Transporte(db.Model):
    __tablename__ = 'transporte'
    id = db.Column(db.Integer, primary_key=True)
    numeroTransporte = db.Column(db.Integer, nullable=False)
    fechahorasalida = db.Column(db.DateTime, nullable=False)
    fechahorallegada = db.Column(db.DateTime, nullable=False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    paquetes = db.relationship('Paquete', backref='transporte', lazy=True)  # Relación con Paquete