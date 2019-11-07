import tkinter

window = tkinter.Tk()

#CABECERA
window.title("Acerca de")
window.resizable(0, 0)
window.geometry('300x300')

#TITULO DE CONTENIDO
titulo1 = tkinter.Label(window, text = "Simulación de Resultados", height = 2, width = 100)
titulo2 = tkinter.Label(window, text = "Juegos Panamericanos Lima 2019", height = 0, width = 100)
titulo1.pack()
titulo2.pack()


#CUERPO DE CONTENIDO
texto1 = tkinter.Label(window, text = "Desarrolladores:", height = 5, width = 100)
texto2 = tkinter.Label(window, text = "- ESTRELLA YAURI, Kelly", height = 0, width = 100)
texto3 = tkinter.Label(window, text = "- HURTADO CONDORI, Jorge", height = 0, width = 100)
texto4 = tkinter.Label(window, text = "- LORA MOLINA, Diego", height = 0, width = 100)
texto5 = tkinter.Label(window, text = "- PRADO MIRANDA, Kevin", height = 0, width = 100)

texto1.pack()
texto2.pack()
texto3.pack()
texto4.pack()
texto5.pack()


#APERTURA DE VENTANA
window.mainloop()
