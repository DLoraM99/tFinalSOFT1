# -*- coding: utf-8 -*-
import tkinter
import randomPaises
import random
from PIL import Image,ImageTk 

#FUNCIONES Y PROCESOS
def generarPaises(cant) :
    paisesParticipantes = randomPaises.rand(cant)
    print( paisesParticipantes)
    
#RANDOM PARA GENERAR LOS PAISES
def paisesRan():
    generarPaises(ran)

ran = random.randint(9,21)
paisesTest = paisesRan

listad = []


#INTERFAZ GRAFICA
ventana=tkinter.Tk()
ventana.title("")

# CONFIGURACION DE LA VENTANA
ventana.geometry("500x500")
ventana.configure(background="white")
ventana.resizable(0,0)


# CANTIDAD DE PAISES A GENERAR

image=Image.open("imagen.jpg")
foto=ImageTk.PhotoImage(image)
lab=tkinter.Label(image=foto)
lab.pack()

# POR BORRARLO HASTA ...
"""
etiqueta1=tkinter.Label(ventana,text="Países:",bg="white",fg="black",font=("Verdana",13))
etiqueta1.place(x=25,y=250)

paises = tkinter.IntVar()

entrada=tkinter.Entry(ventana, textvar = paises)
string_en = entrada.get()
int_en = int(string_en)

entrada.place(x=100,y=257)
"""
# ...ACA



# BOTON GENERAR PAISES PARTICIPANTES
generar= tkinter.Button(text = "Generar", command = paisesTest)
generar.pack()
generar.place(bordermode = tkinter.OUTSIDE, x = 50, y = 300)


# BOTON SIMULAR RESULTADOS
simular= tkinter.Button(text = "Simular", command = "")
simular.pack()
simular.place(bordermode = tkinter.OUTSIDE, x = 120, y = 300)


# BOTON ACERCA DEL PROGRAMA
AcercaDe= tkinter.Button(text = "Acerca De", command = "")
AcercaDe.pack()
AcercaDe.place(bordermode = tkinter.OUTSIDE, x = 80, y = 340)


# GENERACION DE VENTANA
lista=tkinter.Listbox(ventana)
lista.insert(1, paisesTest)
lista.pack()
lista.place(x=300,y=257)

ventana.mainloop()
