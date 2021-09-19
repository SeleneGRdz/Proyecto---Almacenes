from flask import Flask, render_template, request, redirect, url_for
from flask.globals import request 
from conexion import conectar, getListado, esValido, registrarUsuario, retornarUsuario

# python .\server.py

app = Flask(__name__)
# Objeto


identificador = -1


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

    
    #return count + " " + nombre + " " + apellidos + " " +correoElectronico+ " "+ genero+ " " +rol +" la información ha sido registrada"
    return redirect(url_for('index'))


@app.route('/inicio/')
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
            

    if bandera == False :
        return redirect(url_for('index'))
    elif bandera == True :
        return redirect(url_for('inicio'))

    #return count + " " + nombre + " " + apellidos + " " +correoElectronico+ " "+ genero+ " " +rol +" la información ha sido registrada"




if __name__ == '__main__':
    app.run() # Ejecutar la app en modo de servidor
