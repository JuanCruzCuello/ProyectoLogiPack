from flask_sqlalchemy import SQLAlchemy, ForeignKey
from __main__ import App
from sqlalchemy.orm import relationship

db = SQLAlchemy(App)


class Paquete(db.Model):
    __tablename__ = 'Paquetes'
    __idpac=db.Column(db.Integer, primary_key=True)
    __numenvio=db.Column(db.Integer)
    __peso=db.Column(db.Float)
    __nombredestino=db.Column(db.String(50))
    __direcciondestino=db.Column(db.String(50))
    __entregado=db.Column(db.Boolean)
    __observaciones=db.Column(db.String(50))
    __idsucursal=db.Column(db.Integer,ForeignKey('sucursales.idsucursal'))
    sucursal = relationship("Sucursal", backref="Paquetes")
    __idtransporte=db.Column(db.Integer,ForeignKey('transportes.idtransporte'))
    transporte = relationship("Transporte", backref="Paquetes")
    __idrepartidor=db.Column(db.Integer,ForeignKey('repartidores.idrepartidor'))
    repartidor = relationship("Repartidor", backref="Paquetes")
    def __repr__(self):
        return  "<User(ID='%d', Numero de envio='%d', Peso='%f', Nombre de destino='%s', Direccion de destino='%s', Entregado='%s', Observaciones='%s', ID de sucursal='%d', ID de transporte='%d', ID de repartidor='%d')>" % (self.__idpac, self.__numenvio, self.__peso, self.__nombredestino, self.__direcciondestino, self.__entregado, self.__observaciones, self.__idsucursal, self.__idtransporte, self.__idrepartidor)


class Repartidor(db.Model):
    __tablename__ = 'Repartidores'
    __idrepartidor=db.Column(db.Integer, primary_key=True)
    __nombre=db.Column(db.String(50))
    __dni=db.Column(db.String(50))
    __idsucursal=db.Column(db.Integer,ForeignKey('sucursales.idsucursal'))
    sucursal = relationship("Sucursal", backref="Repartidores")
    
    def __repr__(self) -> str:
        return "<Repartidor(ID='%d', Nombre='%s', DNI='%s', ID de sucursal='%d')>" % (self.__idrepartidor, self.__nombre, self.__dni, self.__idsucursal)


class Sucursal(db.Model):
    __tablename__ = 'sucursales'
    __idsucursal=db.Column(db.Integer, primary_key=True)
    __nombre=db.Column(db.String(50))
    __provincia=db.Column(db.String(50))
    __direccion=db.Column(db.String(50))
    __localidad=db.Column(db.String(50))
    
    def __repr__(self):
        return "<Sucursal(ID='%d', Nombre='%s', Provincia='%s', Direccion='%s', Localidad='%s')>" % (self.__idsucursal, self.__nombre, self.__provincia, self.__direccion, self.__localidad)



class Transporte(db.Model):
    __tablename__ = 'transportes'
    __idtransporte=db.Column(db.Integer, primary_key=True)
    __numtrans=db.Column(db.Integer)
    __fechahorasalida=db.Column(db.String(50))
    __fechahorallegada=db.Column(db.String(50))
    __idsucursal=db.Column(db.Integer)
    __idsucursal=db.Column(db.Integer,ForeignKey('sucursales.idsucursal'))
    sucursal = relationship("Sucursal", backref="Repartidores")

    
    def __repr__(self):
        return "<Transporte(ID='%d', Numero de transporte='%d', Fecha de salida='%s', Fecha de llegada='%s', ID de sucursal='%d')>" % (self.__idtransporte, self.__numtrans, self.__fechahorasalida, self.__fechahorallegada, self.__idsucursal)




