from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.models import db
from models.models import Paquete, Repartidor, Sucursal, Transporte


app = Flask(__name__)
app.config.from_pyfile('config.py')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    