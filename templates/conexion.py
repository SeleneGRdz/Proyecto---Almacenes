#descargar el mysql.conector ###pip install mysql-connector-python
import mysql.connector
from mysql.connector.errors import Error

def conectar():
  conn = None
  try:  
                              ,#nombre del host  #nombre del usuario,  #password #database name
    conn = mysql.connector.connect(host = 'localhost',user = 'root' , password = '1234',database = 'nuevo')
    except Error as e:
      print ("Error de conexion:  "+ e)
     return conn
  
  def getListado(conexion):
    cursor = conexion.cursor()
    cursor.execute("Select * from empleados")
    filas = cursor.fetchall()
    return filas
