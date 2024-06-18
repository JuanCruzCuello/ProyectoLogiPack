from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')


from models.models import db
from models.models import Paquete, Repartidor, Sucursal, Transporte
@app.route('/')
def index():
    return render_template('template/inicio.html')






@app.route('/Repartidor', methods=['GET', 'POST'])
def repartidor():
    if request.method == 'GET':
        return render_template('template/repartidor.html')
    elif request.method == 'POST':
      return render_template('template/repartidor.html')
  
  
  
  

@app.route('/Despachante')
def despachante():
     sucursales = Sucursal.query.order_by(Sucursal.numero).all()
     return render_template('template/Despachante.html', sucursales = sucursales)
   

@app.route('/acciones_sucursal/<int:numero>')
def acciones_sucursal(numero):
    # Obtener la sucursal desde la base de datos por su número (ID)
    sucursal = Sucursal.query.get(numero)

    if not sucursal:
        return "Sucursal no encontrada", 404

    # Renderizar la plantilla de acciones para la sucursal seleccionada
    return render_template('acciones_sucursal.html', sucursal=sucursal)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
     