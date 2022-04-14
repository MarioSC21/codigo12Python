import tabulate
# ?Funciones


def menu():
    print("-" * 50)
    print("|" + " " * 9 + "MATRICULA DE ALUMNOS EN CODIGO " + " " * 8 + "|")
    print("-" * 50)
    print("|" + " " * 9 + "MENU DE OPCIONES     " + " " * 18 + "|")
    print("|" + " " * 9 + "[1] REGISTRAR ALUMNO " + " " * 18 + "|")
    print("|" + " " * 9 + "[2] MOSTRAR ALUMNOS  " + " " * 18 + "|")
    print("|" + " " * 9 + "[3] ACTUALIZAR ALUMNO" + " " * 18 + "|")
    print("|" + " " * 9 + "[4] ELIMINAR ALUMNO  " + " " * 18 + "|")
    print("|" + " " * 9 + "[5] SALIR            " + " " * 18 + "|")
    print("-" * 50)


def insertarAlumnos(alumnos):
    nombre = input("NOMBRE  : ")
    email = input("EMAIL   : ")
    celular = input("CELULAR : ")
    dictAlumno = {
        'nombre': nombre,
        'email': email,
        'celular': celular
    }
    alumnos.append(dictAlumno)


def pintarAlumnos(alumnos):
    cabeceras = alumnos[0].keys()
    values = [x.values() for x in alumnos]
    print(tabulate.tabulate(values, cabeceras))


def actaulizarAlumno(alumnos, indice):
    print("Coloque los datos para actualizar")
    nombre = input("NOMBRE  : ")
    email = input("EMAIL   : ")
    celular = input("CELULAR : ")
    dictAlumno = {
        'nombre': nombre,
        'email': email,
        'celular': celular
    }
    alumnos[indice].update(dictAlumno)


def buscarindices(nombre, alumnos):
    indice = -1
    for na in range(len(alumnos)):
        if(alumnos[na]['nombre'] == nombre):
            indice = na
            break
    return indice


def cargarAlumnos(strAlumnos):
    alumnos = []
    listaAlumnos = strAlumnos.splitlines()
    for l in listaAlumnos:
        alumnoData = l.split(",")
        dictAlumno = {
            'nombre': alumnoData[0],
            'email': alumnoData[1],
            'celular': alumnoData[2],
        }
        alumnos.append(dictAlumno)
    return alumnos

def grabarAlumnos(alumnos):
    strAlumnos = ""
    c = 1
    for l in alumnos:
        for clave,valor in l.items():
            strAlumnos += valor
            if(clave != 'celular'):
                strAlumnos += ','
            else:
                strAlumnos += '\n'
    return strAlumnos            