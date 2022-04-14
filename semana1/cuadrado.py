ladoCuadrado = int(input("ingrese el lado del cuadarado : "))
dibujoCuadrado = "* "
espacioCuadrados = "  "
restaLados = ladoCuadrado-2
for lados in range(ladoCuadrado):
    if(lados == 0 or lados == ladoCuadrado -1):
        print(dibujoCuadrado * ladoCuadrado)
    else:
        print(dibujoCuadrado + espacioCuadrados *  (restaLados)+ dibujoCuadrado)       