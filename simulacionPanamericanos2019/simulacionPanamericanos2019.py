# -*- coding: utf-8 -*-
import tkinter
from PIL import Image,ImageTk 

ventana=tkinter.Tk()
ventana.title("")


#CONFIGURACION DE LA VENTANA
ventana.geometry("500x500")
ventana.configure(background="white")
ventana.resizable(0,0)


#CANTIDAD DE PAISES A GENERAR
etiqueta1=tkinter.Label(ventana,text="Países:",bg="white",fg="black",font=("Verdana",13))
etiqueta1.place(x=25,y=250)

image=Image.open("imagen.jpg")
foto=ImageTk.PhotoImage(image)
lab=tkinter.Label(image=foto)
lab.pack()

fn=tkinter.StringVar()

entrada=tkinter.Entry(ventana,textvar=fn)
entrada.place(x=100,y=257)


#BOTON GENERAR PAISES PARTICIPANTES
generar= tkinter.Button(text = "Generar", command = "")
generar.pack()
generar.place(bordermode = tkinter.OUTSIDE, x = 50, y = 300)


#BOTON SIMULAR RESULTADOS
simular= tkinter.Button(text = "Simular", command = "")
simular.pack()
simular.place(bordermode = tkinter.OUTSIDE, x = 120, y = 300)


#BOTON ACERCA DEL PROGRAMA
AcercaDe= tkinter.Button(text = "Acerca De", command = "")
AcercaDe.pack()
AcercaDe.place(bordermode = tkinter.OUTSIDE, x = 80, y = 340)


#GENERACION DE VENTANA
lista=tkinter.Listbox(ventana)
lista.pack()
lista.place(x=300,y=257)

ventana.mainloop()
