#descargar el mysql.conector ###pip install mysql-connector-python
import mysql.connector
from mysql.connector.errors import Error

def conectar():
  conn = None
  try:  
                              #nombre del host  #nombre del usuario,  #password #database name
    conn = mysql.connector.connect(host = 'localhost',user = 'root' , password = 'Teamoanayeli1.',database = 'empresa')
  except Error as e:
    print ("Error de conexion:  " + e)
  
  return conn
  
def getListado(conexion):
  cursor = conexion.cursor()
  cursor.execute("SELECT * FROM empleados")
  filas = cursor.fetchall()
  return filas



def esValido(conexion, correo, password):
    valido = False
    cursor = conexion.cursor()
    sql = "SELECT * FROM empleados WHERE email = %s and contrasenia = sha1(%s)"
    parametros = (correo, password)
    cursor.execute(sql, parametros)
    
    for elemento in cursor:
        valido = True
        print(elemento)
        break
    
    cursor.close()
    conexion.close()
    return valido

def retornarUsuario(conexion, correo, password):
    cursor = conexion.cursor()
    sql = "SELECT * FROM empleados WHERE email = %s and contrasenia = sha1(%s)"
    parametros = (correo, password)
    cursor.execute(sql, parametros)
    for elemento in cursor:
        usuario = elemento
        break
    
    cursor.close()
    conexion.close()
    return usuario

def registrarUsuario(conexion, nombre, apellido, correo, password, genero, rol, cedula):

  
    print("hola")
    print(nombre)
    print(apellido)
    print(correo)
    print(password)
    print(genero)
    print(rol)
    print(cedula)
    try:  
    
      cursor = conexion.cursor()
      sql = "INSERT INTO empleados (nombre, apellido, email, genero, contrasenia, rol, cedula) VALUES (%s, %s, %s, %s, sha1(%s), %s, %s)"
      parametros = (nombre, apellido, correo, genero, password, rol, cedula)
      cursor.execute(sql, parametros)
      
      cursor.close()
      conexion.close()
    except Error as e:
      print ("Error de conexion:  " + e)
    
    
    return True

