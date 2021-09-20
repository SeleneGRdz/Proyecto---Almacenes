from flask import Flask, render_template, request, redirect, url_for
from flask.globals import request 
from conexion import guardarDatos, conectar, esValido

# python .\server.py

app = Flask(__name__)
# Objeto

# Indicar que irá a la página de inicio
@app.route('/')
def index():

    return render_template('home.html') # Cuando le dará la dirección, mostrará este texto

    

# Visualizar el formulario
@app.route('/registro/')
def registro():
    return render_template('registro.html')
    
        

@app.route('/reg-procesa', methods=['POST'])
def procesa():

    # ID de registro junto al campo que referencia 
    nombre = request.form['nombre']
    apellidos=request.form['apellidos']
    genero=request.form['genero']
    rol=request.form['rol']
    cedula= request.form['cedula']
    correo=request.form['correoElectronico']
    contrasenia=request.form['contrasena']
    conn = conectar()

    if conn != None: #None significa que no se pudo instanciar correctamente
       # return nombre + " " + apellidos + " "+genero+ " "+rol+ " "+ cedula+ " "+correo+ " "+contrasenia
        guardarDatos(conn, nombre, apellidos,genero, correo, contrasenia,rol, cedula)
    else:
        return "<p>Error de conexion a la base de datos</p>"


    

    
    #return count + " " + nombre + " " + apellidos + " " +correoElectronico+ " "+ genero+ " " +rol +" la información ha sido registrada"
    return redirect(url_for('index'))


@app.route('/inicio/')
def inicio(datos):


    return render_template('inicio.html', data=datos)

@app.route('/ing-procesa', methods=['POST'])
def ingProcesa():
    conn = conectar()
    if conn != None:
        correo =  request.form['correo']
        contra = request.form['contrasena']
        elemento =esValido(conn, correo, contra)
        if elemento != False:
            return render_template('inicio.html', data=elemento)
        else:
            return redirect(url_for('index'))


    #return count + " " + nombre + " " + apellidos + " " +correoElectronico+ " "+ genero+ " " +rol +" la información ha sido registrada"




if __name__ == '__main__':
    app.run() # Ejecutar la app en modo de servidor
