# -*- coding: utf-8 -*-
import tkinter
import randomPaises
import medallas
import random
from PIL import Image,ImageTk 


#FUNCIONES Y PROCESOS
def genPaises(ran) :
    paisesParticipantes = randomPaises.generarPaises(ran)
    return paisesParticipantes

def genParticipantes(paisesParticip) :
    numParticip = randomPaises.generarCantParticip(paisesParticip)
    return numParticip

def genMedallas():
    medals = medallas.generarMedallas(lista2, lista3)
    return medals
  
def MostrarPaises():
    lista=tkinter.Listbox(ventana)
    lista.insert(0)
    num=len(lista2)
    for i in range(num):
        a=(lista2[i])
        lista.insert(tkinter.END,a)    
    lista.pack()
    lista.place(x=300,y=257)

def MostrarMarticipantes():
    lista=tkinter.Listbox(ventana)
    lista.insert(0)
    num=len(lista3)
    for i in range(num):
        a=(lista3[i])
        lista.insert(tkinter.END,a)    
    lista.pack()
    lista.place(x=500,y=257)

def MostrarMedallas():
    lista=tkinter.Listbox(ventana)
    lista.insert(0)
    lista3=genParticipantes(lista2)
    num=len(lista3)
    for i in range(num):
        a=(lista3[i])
        lista.insert(tkinter.END,a)    
    lista.pack()
    lista.place(x=700,y=257)

#RANDOM PARA GENERAR LOS PAISES
ran = random.randint(10,40)
lista2 = genPaises(ran) 
lista3=genParticipantes(lista2)

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
simular= tkinter.Button(text = "Participantes", command = MostrarMarticipantes)
simular.pack()
simular.place(bordermode = tkinter.OUTSIDE, x = 120, y = 300)

simular= tkinter.Button(text = "Medallas", command = MostrarMedallas)
simular.pack()
simular.place(bordermode = tkinter.OUTSIDE, x = 80, y = 340)

# BOTON ACERCA DEL PROGRAMA
AcercaDe= tkinter.Button(text = "Acerca De", command = "")
AcercaDe.pack()
AcercaDe.place(bordermode = tkinter.OUTSIDE, x = 80, y = 380)

# GENERACION DE VENTANA
ventana.mainloop()
