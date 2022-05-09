from tkinter import *
from tkinter import messagebox

def saludar():
    messagebox.showinfo("title","hola " + txtNombre.get())

app = Tk()
app.title('Mi primera interfaz grafica')
app.geometry('300x300')
frame = LabelFrame(app,text='Ventana')
frame.grid(row=0,column=0,columnspan=5,pady=15,padx=20)
#etiqueta
lbNombre = Label(frame,text= 'Nombre : ')
lbNombre.grid(row=1,column=0)
#caja de texto
txtNombre = Entry(frame)
txtNombre.grid(row=1,column=1)
#boton
btnSaludo = Button(frame,text='saludar',command=saludar)
btnSaludo.grid(row=1,column=2)

app.mainloop()