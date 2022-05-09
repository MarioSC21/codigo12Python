class Usuario:
    
    def __init__(self, nom, pwd):
        self.nombre = nom
        self.password = pwd
    
    def iniciarSesion(self):
        if(self.nombre == 'admin' and self.password == '123456'):
            print("Bienvenido"+ self.nombre)
        else:
            print("Datos denegados")
    

#?usando clase usuario            
usuario1 = Usuario("mario","1234")
usuario1.iniciarSesion()

usuario2 = Usuario("admin","123456")
usuario2.iniciarSesion()