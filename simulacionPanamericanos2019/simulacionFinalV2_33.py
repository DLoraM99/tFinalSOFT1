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

def genMedallas(lista2, lista3):
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
    lista.place(x=250,y=257)
    
    Pa = tkinter.Label(text = "Paises", bg = "white")
    Pa.pack()
    Pa.place(x = 285, y = 235)

def MostrarMarticipantes():
    lista=tkinter.Listbox(ventana, width = 5)
    lista.insert(0)
    num=len(lista3)
    for i in range(num):
        a=(lista3[i])
        lista.insert(tkinter.END,a)    
    lista.pack()
    lista.place(x=405,y=257)
    
    P = tkinter.Label(text = "Participantes", bg = "white")
    P.pack()
    P.place(x = 385, y = 235)

def MostrarMedallas():
    lista=tkinter.Listbox(ventana, width = 100, height = 4)
    lista.insert(0)
    num=len(lista4)
    for i in range(num):
        a=(lista4[i])
        lista.insert(tkinter.END,a)    
    lista.pack()
    lista.place(x=500,y=257)
    
    # LABELS
    
    M = tkinter.Label(text = "Medallas", bg = "white")
    M.pack()
    M.place(x = 535, y = 235)
    
    o = tkinter.Label(text = "Oro", bg = "white")
    o.pack()
    o.place(x=450, y=258)
    
    p = tkinter.Label(text = "Plata", bg = "white")
    p.pack()
    p.place(x=450, y=273)
    
    b = tkinter.Label(text = "Bronce", bg = "white")
    b.pack()
    b.place(x=450, y=288)
    
    t = tkinter.Label(text = "Total", bg = "white")
    t.pack()
    t.place(x=450, y=303)
    
def newWin():
    #CABECERA
    ventana.title("Acerca de")
    ventana.geometry('500x500')
    
    #TITULO DE CONTENIDO
    titulo1 = tkinter.Label(ventana, text = "Simulación de Resultados", height = 2, width = 100)
    titulo2 = tkinter.Label(ventana, text = "Juegos Panamericanos Lima 2019", height = 0, width = 100)
    titulo1.pack()
    titulo2.pack()
    
    
    #CUERPO DE CONTENIDO
    texto1 = tkinter.Label(ventana, text = "Desarrolladores:", height = 5, width = 100)
    texto2 = tkinter.Label(ventana, text = "- ESTRELLA YAURI, Kelly", height = 0, width = 100)
    texto3 = tkinter.Label(ventana, text = "- HURTADO CONDORI, Jorge", height = 0, width = 100)
    texto4 = tkinter.Label(ventana, text = "- LORA MOLINA, Diego", height = 0, width = 100)
    texto5 = tkinter.Label(ventana, text = "- PRADO MIRANDA, Kevin", height = 0, width = 100)
    
    texto1.pack()
    texto2.pack()
    texto3.pack()
    texto4.pack()
    texto5.pack()
    
    regresar= tkinter.Button(ventana, text = "Salir", command = ventana.destroy)
    regresar.pack()
    regresar.place(bordermode = tkinter.OUTSIDE, x = 120, y = 300)

#RANDOM PARA GENERAR LOS PAISES
ran = random.randint(10,40)
lista2 = genPaises(ran) 
lista3 = genParticipantes(lista2)
lista4 = genMedallas(lista2, lista3)

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

# BOTON PARTICIPANTES
participantes= tkinter.Button(text = "Participantes", command = MostrarMarticipantes)
participantes.pack()
participantes.place(bordermode = tkinter.OUTSIDE, x = 120, y = 300)

# BOTON DE GENERAR MEDALLAS

medalls= tkinter.Button(text = "Medallas", command = MostrarMedallas)
medalls.pack()
medalls.place(bordermode = tkinter.OUTSIDE, x = 80, y = 340)

# BOTON ACERCA DEL PROGRAMA
AcercaDe= tkinter.Button(text = "Acerca De", command = newWin)
AcercaDe.pack()
AcercaDe.place(bordermode = tkinter.OUTSIDE, x = 80, y = 380)



    

# GENERACION DE VENTANA
ventana.mainloop()
