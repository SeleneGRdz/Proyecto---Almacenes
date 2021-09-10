from flask import Flask, render_template, request, redirect, url_for
from flask.globals import request 

# python .\server.py

app = Flask(__name__)
# Objeto



personas = []



# Indicar que irá a la página de inicio
@app.route('/')
def index():
    return render_template('home.html') # Cuando le dará la dirección, mostrará este texto

# Visualizar el formulario
@app.route('/registro/')
def registro():
    return render_template('registro.html')
    
class persona:
    def __init__(self, nombre, apellidos, genero, correoElectronico, contrasena, rol):

        self.nombre = nombre
        self.apellidos = apellidos
        self.genero = genero
        self.correoElectronico = correoElectronico
        self.contrasena = contrasena
        self.rol = rol
        

@app.route('/reg-procesa', methods=['POST'])
def procesa():
    global personas
    global persona

    # ID de registro junto al campo que referencia 
    persona(request.form['nombre'],
            request.form['apellidos'],
            request.form['genero'], 
            request.form['correoElectronico'], 
            request.form['contrasena'], 
            request.form['rol'])

    personas.append(persona)

    
    #return count + " " + nombre + " " + apellidos + " " +correoElectronico+ " "+ genero+ " " +rol +" la información ha sido registrada"
    return redirect(url_for('index'))


@app.route('/inicio/')
def inicio():
    return render_template('inicio.html')

@app.route('/ing-procesa', methods=['POST'])
def ingProcesa():
    global personas

    print(personas[0].nombre)
    return 'hola'
    # Correo y contraseña coincidan
    # for i in count:
    #     if(request.form['correoElectronico'] == personas[i].correoElectronico and request.form['contrasena'] == contrasena[i]):
    #         return 'hola paso!'
    #         # identificador = i
    #         # bandera = True
    #         # break
    # return 'hola noo'
    # if bandera == False :
    #     return redirect(url_for('index'))
    # elif bandera == True :
    #     return redirect(url_for('inicio'))

    #return count + " " + nombre + " " + apellidos + " " +correoElectronico+ " "+ genero+ " " +rol +" la información ha sido registrada"

if __name__ == '__main__':
    app.run() # Ejecutar la app en modo de servidor