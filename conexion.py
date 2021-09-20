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
    cursor.close()
    conexion.close()
    return valido

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
    
