from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')


from models.models import db
from models.models import Paquete, Repartidor, Sucursal, Transporte
@app.route('/')
def index():
    return render_template('template/inicio.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
     