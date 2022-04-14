#?archivo de escritura
f = open('alumnos.txt','w')
f.write('mario, mario?@gmail.com,1234151\n')
f.write('mario, mario?@gmail.com,1234152\n')

#?archivo de lectura
f = open('alumnos.txt','r')
alumnos = f.read()
# print(alumnos)

listaAlumnos = alumnos.splitlines()
print(listaAlumnos)

listResultado = []

for dicAlumno in listaAlumnos:
    lisDicAlumnos = dicAlumno.split(",")
    # print(lisDicAlumnos)
    dictAlumno = {
        'nombre': lisDicAlumnos[0],
        'email': lisDicAlumnos[1],
        'celular': lisDicAlumnos[2],
    }
    listResultado.append(dicAlumno)

print(listResultado)    
f.close