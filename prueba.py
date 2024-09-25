import mysql.connector

def conexion():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="prueba_78"
    )
    return mydb

mydb = conexion()

class Profesor:

    def __init__(self, id_profesor=None, nombre=None, apellido=None, email=None):
        self.id_profesor = id_profesor
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def consultar_profesor(self):
        cur = mydb.cursor()
        cur.execute("SELECT * FROM profesor")
        resultado = cur.fetchall()
        print("Los profesores registrados son los siguientes: ")
        for i in resultado:
            print(f"{i[0]} {i[1]} {i[2]} {i[3]} ")

    def agregar_profesor(self):
        nombre= input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        email = input("Ingrese email: ")
        curIn = mydb.cursor()
        curIn.execute(f"INSERT INTO profesor(nombre, apellido, email) values ('{nombre}', '{apellido}', '{email}')")
        print("Profesor agregado correctamente")
        mydb.commit()
    
    def actualizar_profesor(self):
        id = int(input("Ingrese id de profesor para actualizar: "))
        nombre= input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        email = input("Ingrese email: ")
        curAc = mydb.cursor()
        curAc.execute(f"UDPATE profesor SET nombre = '{nombre}', apellido = '{apellido}', email = '{email}'\
                        WHERE id_profesor = '{id}'")
        print("Profesor actualizado correctamente")
        mydb.commit()

    def eliminar_profesor(self):
        id = int(input("Ingrese id de profesor para eliminar: "))
        curEl = mydb.cursor()
        curEl.execute(f"DELETE FROM profesor WHERE id_profesor = '{id}'")
        print("Profesor actualizado correctamente")
        mydb.commit()

class Alumno:

    def __init__(self, id_alumno=None, rut_alumno=None, nombre=None, apellido=None, email=None):
        self.id_alumno = id_alumno
        self.rut_alumno = rut_alumno
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def consultar_alumno(self):
        cur = mydb.cursor()
        cur.execute("SELECT * FROM alumno")
        resultado = cur.fetchall()
        print("Los alumnos registrados son los siguientes: ")
        for i in resultado:
            print(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} ")

    def agregar_alumno(self):
        rut_alumno = input("Ingrese Rut: ")
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        email = input("Ingrese email: ")
        curIn = mydb.cursor()
        curIn.execute(f"INSERT INTO alumno(rut_alumno, nombre, apellido, email) values ('{rut_alumno}', '{nombre}', '{apellido}', '{email}')")
        print("Profesor agregado correctamente")
        mydb.commit()

    def actualizar_alumno(self):
        id = int(input("Ingrese id del alumno para actualizar: "))
        rut_alumno = input("Ingrese el rut del alumno: ")
        nombre= input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        email = input("Ingrese email: ")
        curAc = mydb.cursor()
        curAc.execute(f"UDPATE alumno SET rut_alumno = '{rut_alumno}', nombre = '{nombre}', apellido = '{apellido}', email = '{email}'\
                        WHERE id_alumno = '{id}'")
        print("Alumno actualizado correctamente")
        mydb.commit()

    def eliminar_alumno(self):
        id = int(input("Ingrese id de alumno para eliminar: "))
        curEl = mydb.cursor()
        curEl.execute(f"DELETE FROM alumno WHERE id_alumno = '{id}'")
        print("Alumno actualizado correctamente")
        mydb.commit()

    def calcular_promedio(self):
        id = int(input("Ingrese el id del alumno a promediar: "))
        curBuscar = mydb.cursor()
        curBuscar.execute(f"SELECT nota FROM nota WHERE id_alumno = '{id}'")
        resultado = curBuscar.fetchall()
        notas = []
        for i in resultado:
            notas.append(i[0])
        
        if len(notas) > 0:
            promedio = sum(notas) / len(notas)
            print(f"El promedio del alumno es {promedio:.2f}")
        else:
            print(f"No se encontraron notas para el alumno con id {id}")
    
    def obtener_notas(self):
        id = int(input("Ingrese el id del alumno para obtener sus notas: "))
        curBuscar = mydb.cursor()
        curBuscar.execute(f"SELECT nota FROM nota WHERE id_alumno = '{id}'")
        resultado = curBuscar.fetchall()

        if resultado:
            print(f"Notas del alumno con id {id}:")
            for i in resultado:
                print(f"Nota: {i[0]}")
        else:
            print(f"No se encontraron notas para el alumno con id {id}")

class Nota:

    def __init__(self, id_nota=None, id_alumno=None, id_asignatura=None, nota=None, fecha=None):
        self.id_nota = id_nota
        self.id_alumno = id_alumno
        self.id_asignatura = id_asignatura
        self.nota = nota
        self.fecha = fecha
    
    def consultar_nota(self):
        cur = mydb.cursor()
        cur.execute("SELECT * FROM nota")
        resultado = cur.fetchall()
        print("Las notas registradas son las siguientes")
        for i in resultado:
            print(f"{i[0]} {i[1]} {i[2]} {i[3]} {i[4]}")

    def agregar_nota(self):
        id_alumno = int(input("Ingrese el id del alumno que corresponde la nota: "))
        id_asignatura = int(input("Ingrese id de la asignatura: "))
        nota = float(input("Ingrese la nota: "))
        fecha = input("Ingrese la fecha formato YYYY-MM-DD: ")
        curIn = mydb.cursor()
        curIn.execute(f"INSERT INTO nota(id_alumno, id_asignatura, nota, fecha) values ('{id_alumno}', '{id_asignatura}', '{nota}', '{fecha}')")
        print("Nota agregada correctamente")
        mydb.commit()

    def actualizar_nota(self):
        id = int(input("Ingrese id de la nota para actualizar: "))
        nota = float(input("Ingrese la nueva nota: "))
        curAc = mydb.cursor()
        curAc.execute(f"UDPATE nota SET nota = '{nota}' WHERE id_nota = '{id}'")
        print("Nota actualizada correctamente")
        mydb.commit()

    def eliminar_nota(self):
        id = int(input("Ingrese id de la nota para eliminar: "))
        curEl = mydb.cursor()
        curEl.execute(f"DELETE FROM nota WHERE id_nota = '{id}'")
        print("Nota actualizada correctamente")
        mydb.commit()

class Asignatura:
    def __init__(self, id_asignatura=None, id_profesor=None, nombre_asignatura=None):
        self.id_asignatura = id_asignatura
        self.nombre_asignatura = nombre_asignatura
        self.id_profesor = id_profesor

    def consultar_asignatura(self):
        cur = mydb.cursor()
        cur.execute("SELECT * FROM asignatura")
        resultado = cur.fetchall()
        print("Las asignaturas registradas son las siguientes: ")
        for i in resultado:
            print(f"{i[0]} {i[1]} {i[2]} ")
        
    def agregar_asignatura(self):
        nombre_asignatura = input("Ingrese el nombre de la asignatura a agregar: ")
        id_profesor = int(input("Ingrese el id del profesor a cargo: "))
        curIn = mydb.cursor()
        curIn.execute(f"INSERT INTO asignatura(nombre_asignatura, id_profesor) values ('{nombre_asignatura}', '{id_profesor}')")
        print("asignatura agregada correctamente")
        mydb.commit()

    def actualizar_asignatura(self):
        id = int(input("Ingrese id de la asignatura para actualizar: "))
        nombre_asignatura = input("Ingrese el nuevo nombre de la asignatura: ")
        curAc = mydb.cursor()
        curAc.execute(f"UDPATE asignatura SET nombre_asignatura = '{nombre_asignatura}' WHERE id_asignatura = '{id}'")
        print("Nota actualizada correctamente")
        mydb.commit()

    def eliminar_asignatura(self):
        id = int(input("Ingrese id de la asignatura para eliminar: "))
        curEl = mydb.cursor()
        curEl.execute(f"DELETE FROM asignatura WHERE id_asignatura = '{id}'")
        print("Asignatura eliminada correctamente")
        mydb.commit()

obj_Profesor1 = Profesor("Juan", "Munoz", "asd@gmail.com")
obj_Alumno1 = Alumno("111-1", "Juan", "Pérez","dsa@gmail.com")
obj_Alumno2 = Alumno("222-2", "Liliana", "Huaquillan", "frs@gmail.com")
obj_Nota1 = Nota("")
