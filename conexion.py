<<<<<<< HEAD
import mysql.connector
from mysql.connector.errors import Error
def conectar():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='empresa1')
    except Error as e:
        print("Error de conexion: ", e)
    return conn

def getListado(conexion):
    cursor = conexion.cursor() # se pone simepre el cursos cuando se quiere hacer una consulta, es la conexion a la DB
    cursor.execute("SELECT * from empleados")
    filas =  cursor.fetchall() # todos los valores de la consulta los asiana a la variable filas
    cursor.close()
    conexion.close()
    return filas

def esValido(conexion, correo, password):
    valido = False
    cursor =  conexion.cursor()
    sql = "SELECT * from usuarios where correo = %s and passwd = sha1(%s)"
    parametros = (correo, password)
    cursor.execute(sql,parametros)
    for elemento in cursor:
        valido = True
        break
=======
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
    
>>>>>>> 1483038546527953c9cc7ee01fb1f6ac3080f568
    cursor.close()
    conexion.close()
    return valido

<<<<<<< HEAD
def guardarDatos(conexion, nombre, apellidos,genero,correo,contrasenia, rol,cedula):    
    cursor = conexion.cursor() # se pone simepre el cursos cuando se quiere hacer una consulta, es la conexion a la DB
    cursor.execute("INSERT INTO empleados values(null,'"+nombre+"','"+apellidos+"','"+genero+"','"+correo+"',sha1('"+contrasenia+"'),'"+rol+"','"+cedula+"')")    
    cursor.close()
    conexion.close()
    

def esValido(conexion, correo, password):
    valido = False
    cursor =  conexion.cursor()
    sql = "SELECT * from empleados where correo = %s and contrasenia = sha1(%s)"
    parametros = (correo, password)
    cursor.execute(sql,parametros)
    for elemento in cursor:
        return elemento                
    cursor.close()
    conexion.close()
    return False
    
=======
def retornarUsuario(conexion, correo, password):
    cursor = conexion.cursor()
    sql = "SELECT * FROM empleados WHERE email = %s and contrasenia = sha1(%s)"
    #en parametros creo que es contrasena en vez de password
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

>>>>>>> 1483038546527953c9cc7ee01fb1f6ac3080f568
