from flask import Flask, render_template, request,session,redirect
from flask_sqlalchemy import SQLAlchemy
import os 
app = Flask(__name__)
app.secret_key = os.urandom(24) 
app.config.from_pyfile('config.py')


from models.models import db
from models.models import Paquete, Repartidor, Sucursal, Transporte
@app.route('/')
def index():
    return render_template('template/inicio.html')






@app.route('/login_Repartidor', methods=['GET', 'POST'])
def login_Repartidor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        dni = request.form['dni']
        repartidor = Repartidor.query.filter_by(nombre=nombre, dni=dni).first()
        if repartidor:
            
            session['user_nombre'] = repartidor.nombre
            session['user_dni'] = repartidor.dni
            session['user_type'] = 'repartidor'  
            return redirect('/')
        else:
            return render_template('message.html', message="Nombre o DNI incorrecto.", tipo="login")

    return render_template('template/login_Repartidor.html')
    

@app.route('/Despachante', methods=['GET', 'POST'])
def despachante():
        sucursales=Sucursal.query.order_by(Sucursal.id).all()
        return render_template('template/Despachante.html', sucursales = sucursales)
        
    
    
    
    

@app.route('/funcionalidadesucu', methods=['GET', 'POST'])
def funcionalidadesucu():
    sucursal_id= request.form.get('sucursal.id')
    session['sucursal_id']= sucursal_id
    return render_template('template/funcionalidadesucu.html')

@app.route('/registrar_recepcion')
def registrar_recepcion():
    return render_template('template/registrar_recepcion.html')

@app.route('/registrar_salida_trans')
def registrar_salida_trans():
    return render_template('template/registrar_salida_trans.html')

@app.route('/registrar_llegada_trans')
def Registrar_llegada_trans():
    return render_template('template/registrar_llegada_trans.html')

@app.route('/asignar_paquete')
def Asignar_paquete():
    return render_template('template/asignar_paquete.html')
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)