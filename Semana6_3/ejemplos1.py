import tkinter as tk

# Tutorial en español: https://python-para-impacientes.blogspot.com/p/tutorial-de-tkinter.html
# https://www.adictosaltrabajo.com/2020/06/30/interfaces-graficas-en-python-con-tkinter/
# https://docs.python.org/es/3/library/tk.html

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

frame1 = tk.Frame(master = )


# Foreground: color de texto, Background: fondo del texto
label = tk.Label(text="Curso de Programación", foreground="red", background="#000000")
label2 = tk.Label(
    text="Horario: Sábado 8-11 AM",
    width=20,
    height=5,
)

button1 = tk.Button(
    text="Clic aquí",
    width=10,
    pady = 5,
    height=3,
    activeforeground="red",
    background="gray",
    foreground="white",
)

entry1 = tk.Entry(width = 40)



# .pack nos permite añadir elementos a nuestra ventana


# Formas de organizar la información en tkinter:
# https://www.activestate.com/resources/quick-reads/how-to-position-widgets-in-tkinter/
label.pack()
label2.pack()
button1.pack(side=tk.BOTTOM)
entry1.pack()
# Ciclo principal
window.mainloop()
