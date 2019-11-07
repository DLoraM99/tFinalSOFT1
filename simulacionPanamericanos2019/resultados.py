import tkinter

window = tkinter.Tk()
menu = tkinter.Menu(window) 


#CABECERA
window.title("Resultados de Simulación - Juegos Panamericanos Lima 2019")
window.resizable(0, 0)
window.geometry('500x500')


#MENU
agregarM = tkinter.Menu(menu)
agregarM.add_command(label = 'Acerca de')
agregarM.add_separator()
agregarM.add_command(label = 'Salir', command = window.destroy)
menu.add_cascade(label = 'Archivo', menu = agregarM)


#TABLA
tablaPos = tkinter.LabelFrame(window, text = "Tabla de Posiciones", height = 350, width = 350)
tablaPos.pack()

tablaText = tkinter.Text(tablaPos, height = 23, width = 45)
tablaText.pack()


#BOTONES
generarR = tkinter.Button(text = "Generar Reporte", command = "")
generarR.pack()
generarR.place(bordermode = tkinter.OUTSIDE, x = 75, y = 400)

grafico = tkinter.Button(text = "Generar Gráfico", command = "")
grafico.pack()
grafico.place(bordermode = tkinter.OUTSIDE, x = 180, y = 400)

btn = tkinter.Button(text = "Ver Detalles", command = "")
btn.pack()
btn.place(bordermode = tkinter.OUTSIDE, x = 350, y = 400)

window.config(menu = menu)
window.mainloop()
