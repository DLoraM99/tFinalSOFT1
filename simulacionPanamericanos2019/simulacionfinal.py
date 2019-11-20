# -*- coding: utf-8 -*-
import tkinter
import randomPaises
import random
from PIL import Image,ImageTk 

#FUNCIONES Y PROCESOS
def generarPaises(ran) :
    paisesParticipantes = randomPaises.rand(ran)
    return paisesParticipantes
    
def MostrarPaises():
    lista=tkinter.Listbox(ventana)
    lista.insert(0)
    lista2=generarPaises(ran)
    num=len(lista2)
    for i in range(num):
        a=(lista2[i])
        lista.insert(tkinter.END,a)    
    lista.pack()
    lista.place(x=300,y=257)

def MostrarMedallero():
    lista=tkinter.Listbox(ventana)
    lista.insert(0)
    lista2=generarPaises(ran)
    num=len(lista2)
    for i in range(num):
        a=(lista2[i])
        lista.insert(tkinter.END,a)    
    lista.pack()
    lista.place(x=400,y=257)
    
#RANDOM PARA GENERAR LOS PAISES
ran = random.randint(9,21)

#INTERFAZ GRAFICA
ventana=tkinter.Tk()
ventana.title("")

# CONFIGURACION DE LA VENTANA
ventana.geometry("1000x500")
ventana.configure(background="white")
ventana.resizable(0,0)

# CANTIDAD DE PAISES A GENERAR
image=Image.open("imagen.jpg")
foto=ImageTk.PhotoImage(image)
lab=tkinter.Label(image=foto)
lab.pack()

# BOTON GENERAR PAISES PARTICIPANTES
generar= tkinter.Button(text = "Generar", command = MostrarPaises)
generar.pack()
generar.place(bordermode = tkinter.OUTSIDE, x = 50, y = 300)

# BOTON SIMULAR RESULTADOS
simular= tkinter.Button(text = "Simular", command = MostrarMedallero)
simular.pack()
simular.place(bordermode = tkinter.OUTSIDE, x = 120, y = 300)

# BOTON ACERCA DEL PROGRAMA
AcercaDe= tkinter.Button(text = "Acerca De", command = "")
AcercaDe.pack()
AcercaDe.place(bordermode = tkinter.OUTSIDE, x = 80, y = 340)

# GENERACION DE VENTANA
ventana.mainloop()
