##Base de datos de alumnos

alumno1 = {
    'Nombre': 'mario',
    'edad': 12,
    'nota' : 10,
    'aprobado': True,
    'cursos': ['java', 'c#']
}

alumno2 = {
    'Nombre': 'mario2',
    'edad': 15,
    'nota' : 13,
    'aprobado': True,
    'cursos': ['java', 'c++']
}

alumnos = [alumno1, alumno2]
print("Nombre - edad - nota - aprobado - cursos")
for alumnno in alumno1:
    print(alumnno,end = '       | ')
print()
print("*" * 100)
for alu in alumnos:
    for clave,valor in alu.items():
        print(valor,end = '     |    ')
    print()    