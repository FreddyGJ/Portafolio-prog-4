import sqlite3
import hashlib
#db = sqlite3.connet(':memory:') # Base de datos en memoria

#//////////////////////////CIFRAR EL PASSWORD//////////////////////////
# def cifrar_password(password):
#     cifrado = hashlib.sha512(password.encode('utf-8')).hexdigest()
#     return cifrado

db = sqlite3.connect('data/prueba') # Base de datos en un archivo
# db.create_function('cifrar', 1, cifrar_password)
cursor = db.cursor()
# cursor.execute('''CREATE TABLE clave(id INTEGER PRIMARY KEY,
#                   email TEXT, password TEXT)''')
# usuario = input("Correo: ")
# password = input("Password: ")
# cursor.execute('''INSERT INTO clave(email, password)
#                   VALUES(?,cifrar(?))''', (usuario, password))
# db.commit()

#////////////////TRAE LOS USUARIOS CON SUS ID'S///////////////////////////////
cursor.execute('''SELECT nombre, telefono FROM usuario''')
resultado = cursor.fetchall()
for fila in resultado:
    print("{0} , {1}".format(fila[0], fila[1]))
# ///////////////////////ELIMINAR UN USUARIO DE LA TABLA/////////////////////////////
# id = input("ID de usuario a eliminar: ")
# for fila in resultado:
#     if int(id) == int(fila[0]):
#         cursor.execute('''DELETE FROM usuario WHERE id = ?''',
#                    (id))
#         db.commit()
#
#///////////////////////////////MODIFICAR INFORMACION EN LA TABLA////////////////////
# id = input("ID de usuario a modificar: ")
# for fila in resultado:
#     if int(id) == int(fila[0]):
#         nuevo_nombre = input("Nombre nuevo: ")
#         cursor.execute('''UPDATE usuario SET nombre = ? WHERE id = ?''',
#                    (nuevo_nombre, id))
#         db.commit()
#///////////////////SE CREA UNA TABLA/////////////////////////////
# cursor.execute('''CREATE TABLE usuario(id INTEGER PRIMARY KEY, nombre TEXT,
#                     telefono TEXT, email TEXT UNIQUE, password TEXT)''')
# db.commit()

# cursor.execute('''DROP TABLE usuario''')
# db.commit()
#
# nombre = input("Nombre: ")
# telefono = input("Telefono: ")
# email = input("Email: ")
# password = input("Password: ")
#
# //////////////UNA FORMA DE INGRESAR DATA///////////////////////////////
# cursor.execute('''INSERT INTO usuario(nombre, telefono, email, password)
#                   VALUES(?,?,?,?)''', (nombre, telefono, email, password))
#
# //////////////OTRA FORMA DE INGRESAR DATA/////////////////////////////
# cursor.execute('''INSERT INTO usuario(nombre, telefono, email, password)
#                   VALUES(:nombre, :telefono, :email, :password)''',
#                {'nombre':nombre, 'telefono':telefono, 'email':email, 'password':password})
# db.commit()
#/////////////SE QUEMA DATA DENTRO DE LA TABLA//////////////////////////
# usuarios = [("Juan","23235656","juan@juan.org","12345"),
#             ("Maria","45789563","maria@maria.com","maria1223"),
#             ("Pedro","78985213","pedro@pedro.org","p3dr0"),]
# cursor.executemany('''INSERT INTO usuario(nombre, telefono, email, password)
#                       VALUES (?,?,?,?)''', usuarios)
# db.commit()

db.close()