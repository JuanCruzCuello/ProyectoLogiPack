from flask import Flask, render_template, request,session,redirect,url_for,flash
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
    
@app.route('/seleccionar_sucursal', methods=['POST'])
def seleccionar_sucursal():
    id = request.form['id']
    if id and id != "0":
        return redirect(url_for('funcionalidadesucu', id=id))
    return redirect(url_for('Despachante'))    
        
    
    
    
    

@app.route('/funcionalidadesucu/<int:id>', methods=['GET'])
def funcionalidadesucu(id):
    sucursal= Sucursal.query.get(id)
    
    return render_template('template/funcionalidadesucu.html',sucursal=sucursal)

@app.route('/registrar_recepcion/<int:sucursal_id>', methods=['GET', 'POST'])
def registrar_recepcion(sucursal_id):
    sucursal= Sucursal.query.get(sucursal_id)
    print(sucursal)
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        peso = float(request.form['peso'])
        id_sucursal = sucursal.id
       

        if sucursal is None:
            flash('Error: No se seleccionó ninguna sucursal.')
            return redirect(url_for('despachante'))
        #el bloque try se usa para manejar errores en la base de datos
        numero_envio=Paquete.query.count()+1
        try:
            nuevo_paquete = Paquete(
            numeroEnvio=numero_envio,
            peso=peso,
            nomdestinatario=nombre,
            dirdestinatario=direccion,
            entregado=False, # El campo entregado está en falso
            observaciones='', 
            idsucursal=id_sucursal,
            idrepartidor=None, 
            idtransporte=None
        )

            db.session.add(nuevo_paquete)#agrega el paquete a la base de datos
            db.session.commit()#confirma la transacción guardando los cambios en la base de datos
            flash('Paquete registrado exitosamente.')#si se cumple
        except Exception as error : # si hay error en el try
            db.session.rollback()#cancela la transacción 
            flash(f'Error al registrar el paquete: {error}')#si se produce un error
            return redirect(url_for('registrar_recepcion'))#redirecciona al formulario de registro de paquete

    
    return render_template('template/registrar_recepcion.html',sucursal=sucursal)




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