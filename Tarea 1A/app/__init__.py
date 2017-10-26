import sqlite3

db = sqlite3.connect('data/Tarea 1A')
cursor = db.cursor()

# cursor.execute('''CREATE TABLE Libros(Titulo TEXT, Autor TEXT, Publicacion DATE)''')
# db.commit()
while True:
    print("\n\t\tMENU DE LA TABLA LIBROS")
    print("1. Agregar")
    print("2. Quitar")
    print("3. Listar")
    print("4. Consultar")
    print("5. Salir")
    try:
        opc = int(input("\nOpcion: "))
    except ValueError:
        opc = 0

    if opc == 1:
        print("\nSe agregara un articulo a la tabla")
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        publicacion = input("Fecha de Publicacion: ")
        cursor.execute('''INSERT INTO Libros(Titulo, Autor, Publicacion)
                          VALUES(?,?,?)''', (titulo, autor, publicacion))
        db.commit()
    elif opc == 2:
        print("\nSe quitara un articulo de la tabla")
        nombre = input("Introduzca titulo del libro: ")
        cursor.execute('''DELETE FROM Libros WHERE Titulo = ?''', (nombre,))
        db.commit()
        print("\nEl libro se elimino con exito.")
    elif opc == 3:
        print("\nListado de libros en la tabla")
        cursor.execute('''SELECT Titulo, Autor, Publicacion FROM Libros''')
        for row in cursor:
            print("{0}: {1}, {2}".format(row[0], row[1], row[2]))
    elif opc == 4:
        p = input("\nIntroduzca la Fecha de Publicacion: ")
        cursor.execute('''SELECT Titulo, Autor, Publicacion FROM Libros WHERE Publicacion=?''', (p,))
        for row in cursor:
            print("{0}: {1}, {2}".format(row[0], row[1], row[2]))
    elif opc == 5:
        break
    else:
        print("\nERROR: Opcion no valida")
print("\n\t\t\tHASTA LUEGO!!")