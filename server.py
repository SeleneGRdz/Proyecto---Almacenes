from flask import Flask, render_template, request, redirect, url_for
from flask.globals import request 
<<<<<<< HEAD
from conexion import guardarDatos, conectar, esValido
=======
from conexion import conectar, getListado, esValido, registrarUsuario, retornarUsuario
>>>>>>> 1483038546527953c9cc7ee01fb1f6ac3080f568

# python .\server.py

app = Flask(__name__)
# Objeto

<<<<<<< HEAD
=======

identificador = -1


>>>>>>> 1483038546527953c9cc7ee01fb1f6ac3080f568
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
<<<<<<< HEAD

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


    
=======
    
    conn = conectar()
    if(conn != None):
        nombre      = request.form['nombre']
        apellidos   = request.form['apellidos']
        correo      = request.form['correoElectronico']
        contra      = request.form['contrasena']
        genero      = request.form['genero']
        rol         = request.form['rol']
        cedula      = request.form['cedula']

    registrarUsuario(conn, nombre, apellidos, correo, contra, genero, rol, cedula)
>>>>>>> 1483038546527953c9cc7ee01fb1f6ac3080f568

    
    #return count + " " + nombre + " " + apellidos + " " +correoElectronico+ " "+ genero+ " " +rol +" la información ha sido registrada"
    return redirect(url_for('index'))


@app.route('/inicio/')
<<<<<<< HEAD
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
=======
def inicio():
    conn = conectar()
    if(conn != None):
        correo = request.form['correoElectronico']
        contra = request.form['contrasena']
        per = retornarUsuario(conn, correo, contra)

    return render_template('inicio.html', nombreP=per.get_nombre(), apellidoP=per.get_apellidos(), correoP=per.get_correoElectronico(), generoP=per.get_genero(), 
                           rolP=per.get_rol(), cedulaP = per.get_cedula() )

@app.route('/ing-procesa', methods=['POST'])
def ingProcesa():
    global personas
    global identificador

    bandera = False

    # Correo y contraseña coincidan

    conn = conectar()
    if(conn != None):
        correo = request.form['correoElectronico']
        contra = request.form['contrasena']
        bandera = esValido(conn, correo, contra)
            
>>>>>>> 1483038546527953c9cc7ee01fb1f6ac3080f568


    #return count + " " + nombre + " " + apellidos + " " +correoElectronico+ " "+ genero+ " " +rol +" la información ha sido registrada"




if __name__ == '__main__':
    app.run() # Ejecutar la app en modo de servidor
