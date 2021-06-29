import tkinter as tk

# Tutorial en español: https://python-para-impacientes.blogspot.com/p/tutorial-de-tkinter.html
# https://www.adictosaltrabajo.com/2020/06/30/interfaces-graficas-en-python-con-tkinter/
# https://docs.python.org/es/3/library/tk.html


numeros = []

# Creación de objeto ventana
window = tk.Tk()

"""
TIPOS DE OBJETO (WIDGET) EN TKINTER:

Label: para mostrar texto.
Button: Para colocar botones.
Entry: Para colocar entradas de usuario.
Text: Para colocar entradas de usuario multilinea.
Frame: Una región de la imagen.

"""

frame1 = tk.Frame(master =window, width = 200, height = 50, bg = "white")
frame1.pack(fill=tk.X, side = tk.TOP)
frame2 = tk.Frame(master =window, width = 200, height = 25, bg = "gray")
frame2.pack(fill=tk.X, side = tk.BOTTOM)



# Foreground: color de texto, Background: fondo del texto
label = tk.Label(master = frame1, text="Curso de Programación", foreground="red", background="#000000")
label2 = tk.Label(master = frame1,
    text="Horario: Sábado 8-11 AM",
    width=20,
    height=5,
)

label3 = tk.Label(master = frame2,
    text="",
    width=20,
    height=5,
)

button1 = tk.Button(master = frame2,
    text="Clic aquí",
    width=10,
    pady = 5,
    height=3,
    activeforeground="red",
    background="gray",
    foreground="white",
)

entry1 = tk.Entry(master = frame1, width = 20, text = "Numero: ")

def handle_click_button1(event):
    numero = int(entry1.get())
    numeros.append(numero)
    label3["text"] = str(numeros)


button1.bind("<Button-1>", handle_click_button1)

# .pack nos permite añadir elementos a nuestra ventana


# Formas de organizar la información en tkinter:
# https://www.activestate.com/resources/quick-reads/how-to-position-widgets-in-tkinter/
label.pack()
label2.pack()
label3.pack()
button1.pack(side=tk.BOTTOM)
entry1.pack()

# Ciclo principal
window.mainloop()
