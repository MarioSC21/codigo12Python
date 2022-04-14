from funcionAlumnos import buscarindices,menu,insertarAlumnos,pintarAlumnos,actaulizarAlumno,cargarAlumnos,grabarAlumnos
# PROGRAMA PARA
# CREATE - C
# READ - R
# UPDATE - U
# DELETE - D
menu()
opcion = 0
# alumnos = [{'nombre': 'cesar mayta', 'email': 'cesarmayta@gmail.com', 'celular': '232323'},
#            {'nombre': 'mario', 'email': 'cesarmayta@gmail.com', 'celular': '232323'}]
f = open('alumnos.txt', 'r')
strAlumnos = f.read()
alumnos = cargarAlumnos(strAlumnos)
f.close

while(opcion != 5):
    opcion = int(input("\nINGRESE OPCIÓN DEL MENU : "))
    if(opcion == 1):
        print("NUEVO ALUMNO ")
        insertarAlumnos(alumnos)
        print("ALUMNO REGISTRADO CON EXITO!!!")
    elif(opcion == 2):
        print("RELACIÓN DE ALUMNOS")
        pintarAlumnos(alumnos)

    elif(opcion == 3):
        print("Actualizar alumno")
        nombreActualizar = input("NOMBRE  : ")
        indice = buscarindices(nombreActualizar,alumnos)
        if(indice == -1):
            print("no se encontro el alumno")
        else:
            actaulizarAlumno(alumnos,indice)
            print("Alumno actualizado")
            
    elif(opcion == 4):
        print("Coloque el nombre del alumno a eliminar")
        nombreEliminar = input("NOMBRE  : ")
        indice2 = buscarindices(nombreEliminar,alumnos)
        if(indice2 == -1):
            print("No se encontro el alumno a eliminar")
        else:
            alumnos.pop(indice2)
            print("Alumno eliminado")

    elif(opcion == 5):
        strAlumnos = grabarAlumnos(alumnos)
        fw = open('alumnos.txt','w')
        fw.write(strAlumnos)
        fw.close()
        print("FINALIZANDO PROGRAMA")
    else:
        print("OPCION INCORRECTA")
