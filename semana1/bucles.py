#Tabla de multiplicar
numUsuario = int(input("Coloque un numero a multiplicar : "))
print("Tabla de multiplicar")
for contador in range(1,5):
    valor = numUsuario * contador
    #print(str(numUsuario) + " X " + str(contador) + " = " + str(valor))
    print(numUsuario, 'x', contador, ' = ',valor)

#bucle for
nombre = input("ingresa tu nombre : ")
for n in nombre:
    print(n)
    
#while
numUsuario2 = int(input("Coloque un numero a multiplicar : "))
c = 1
while(c <= 12):
    print(c)
    c += 1