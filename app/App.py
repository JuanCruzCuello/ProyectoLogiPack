from flask import Flask, render_template, request,session,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
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
    global sucursaldespachante
    if request.method == 'POST':
        sucursaldespachante=request.form.get('sucursal.id')
        return redirect('template/funcionalidadesucu.html')
    else:
        sucursales=Sucursal.query.order_by(Sucursal.numero).all()
        return render_template('template/Despachante.html', sucursales = sucursales)
        
    
    
    
    
   
     
   

@app.route('/funcionalidadesucu')
def funcionalidadesucu(sucursales):
    sucursales = Sucursal.query.get_or_404(Sucursal.numero)
    return render_template('template/funcionalidadesucu.html', sucursales = sucursales)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
     