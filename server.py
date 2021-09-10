from flask import Flask, render_template, request, redirect, url_for
from flask.globals import request 

# python .\server.py

app = Flask(__name__)
# Objeto


class persona:
    def __init__(self, nombre, apellidos, genero, correoElectronico, contrasena, rol):

        self._nombre = nombre
        self._apellidos = apellidos
        self._genero = genero
        self._correoElectronico = correoElectronico
        self._contrasena = contrasena
        self._rol = rol

    def get_nombre(self):
        return self._nombre

    def get_apellidos(self):
        return self._apellidos

    def get_genero(self):
        return self._genero

    def get_correoElectronico(self):
        return self._correoElectronico

    def get_contrasena(self):
        return self._contrasena

    def get_rol(self):
        return self._rol


personas = []


identificador = -1


# Indicar que irá a la página de inicio
@app.route('/')
def index():
    global persona
    global personas

    person = persona('Hector',
            'Guerrero',
            'Masculino', 
            'hector_jesus_89@hotmail.com', 
            'Contra1', 
            'Medico')

    personas.append(person)

    return render_template('home.html') # Cuando le dará la dirección, mostrará este texto

    

# Visualizar el formulario
@app.route('/registro/')
def registro():
    return render_template('registro.html')
    
        

@app.route('/reg-procesa', methods=['POST'])
def procesa():
    global personas
    global persona

    # ID de registro junto al campo que referencia 
    person = persona(request.form['nombre'],
            request.form['apellidos'],
            request.form['genero'], 
            request.form['correoElectronico'], 
            request.form['contrasena'], 
            request.form['rol'])


    personas.append(person)

    
    #return count + " " + nombre + " " + apellidos + " " +correoElectronico+ " "+ genero+ " " +rol +" la información ha sido registrada"
    return redirect(url_for('index'))


@app.route('/inicio/')
def inicio():
    global personas

    per = personas[identificador]

    return render_template('inicio.html', nombreP=per.get_nombre(), apellidoP=per.get_apellidos(), correoP=per.get_correoElectronico(), generoP=per.get_genero(), rolP=per.get_rol() )

@app.route('/ing-procesa', methods=['POST'])
def ingProcesa():
    global personas
    global identificador

    bandera = False

    # hola = personas[0].get_nombre()

    # Correo y contraseña coincidan
    i = 0

    for persona in personas:
        if(request.form['correoElectronico'] == persona.get_correoElectronico() and request.form['contrasena'] == persona.get_contrasena()):
            bandera = True
            identificador = i
            break
        i = i + 1
    

    if bandera == False :
        return redirect(url_for('index'))
    elif bandera == True :
        return redirect(url_for('inicio'))

    #return count + " " + nombre + " " + apellidos + " " +correoElectronico+ " "+ genero+ " " +rol +" la información ha sido registrada"

if __name__ == '__main__':
    app.run() # Ejecutar la app en modo de servidor