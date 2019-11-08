# -*- coding: utf-8 -*-
import tkinter
from PIL import Image,ImageTk 

ventana=tkinter.Tk()
ventana.title("")

#AnchoxAlto
ventana.geometry("500x500")
ventana.configure(background="white")
ventana.resizable(0,0)


etiqueta1=tkinter.Label(ventana,text="Países:",bg="white",fg="black",font=("Verdana",13))
etiqueta1.place(x=120,y=250)

image=Image.open("imagen.jpg")
foto=ImageTk.PhotoImage(image)
lab=tkinter.Label(image=foto)
lab.pack()

fn=tkinter.StringVar()

entrada=tkinter.Entry(ventana,textvar=fn)
entrada.place(x=200,y=257)



generar= tkinter.Button(text = "Generar", command = "")
generar.pack()
generar.place(bordermode = tkinter.OUTSIDE, x = 230, y = 300)


ventana.mainloop()
