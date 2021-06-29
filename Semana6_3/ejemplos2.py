"""
Ejercicio: Elabore un simulador de ventas de jugo natural. Para esto, simule 30 minutos y un
inventario de 20 jugos, los cuales se venden por 2000 pesos c/u.

Para simular lo que pasa en cada minuto, debe usar una variable aleatoria que tome valores entre 1 y 3.

Si el valor es 1, llega un cliente nuevo con una edad aleatoria entre 10 y 80. Pista: clase Cliente.

Si el valor es 2 y la longitud de la cola es mayor a 3, el último cliente de la cola se cansa de esperar
y se marcha.

Si el valor es 3, no pasa nada.

Además, en cada minuto que pasa se debe atender al cliente que esté en la cabeza de la cola.
Si el cliente tiene menos de 10 años, se dará cuenta de que el jugo no tiene azucar y se irá sin comprar.
De lo contrario, comprará el jugo.

En cada minuto se debe reportar lo siguiente:

Jugos restantes: {numero_jugos}
Total ganado: {dinero_obtenido}
Número de clientes en la cola: {len(cola)}
"""

import random
import tkinter as tk
from tkinter import messagebox

class Cliente:
    def __init__(self, id):
        self.id = id
        self.edad = random.randint(8, 100)

    # igual a
    def __eq__(self, other):
        son_iguales = self.id == other.id
        return son_iguales

    # mayor que
    def __gt__(self, other):
        mayor_que = self.id > other.id
        return mayor_que

    # diferente de
    def __ne__(self, other):
        diferente = self.id != other.id
        return diferente

    def __str__(self):
        return f"Cliente con id {self.id}, edad {self.edad}"


total_jugos_disponibles = 10
total_ventas = 0
n_clientes = 5
precio_jugo = 1000

cola_clientes = []

for i in range(n_clientes):
    cliente = Cliente(i)
    cola_clientes.append(cliente)

window = tk.Tk()
window.title("App venta de jugos")

frame_titulo = tk.Frame(master=window, width=200, height=10, bg="white")
frame_titulo.pack()

label_titulo = tk.Label(
    master=frame_titulo,
    text="VENTA DE JUGOS NATURALES",
    width=50,
    height=3,
    font=("Courier", 30),
)
label_titulo.pack()

frame_datos = tk.Frame(master=window, width=200, height=10, bg="white")
frame_datos.pack()


label_jugos_disp = tk.Label(
    master=frame_datos,
    width=30,
    height=1,
    text="Total de jugos disponibles: " + str(total_jugos_disponibles),
    font=("Courier", 16),
)
label_jugos_disp.pack()

label_total_ventas = tk.Label(
    master=frame_datos,
    width=30,
    height=1,
    text="Total ganado en ventas: " + str(total_ventas),
    font=("Courier", 16),
)
label_total_ventas.pack()

label_clientes_en_cola = tk.Label(
    master=frame_datos,
    width=30,
    height=1,
    text="Total clientes en cola: " + str(len(cola_clientes)),
    font=("Courier", 16),
)
label_clientes_en_cola.pack()

frame_acciones = tk.Frame(master=window, width=300, height=60)
frame_acciones.pack(pady=30, side="bottom")
# frame_acciones.pack_propagate(0)

label_entry = tk.Label(
    master=frame_acciones,
    width=50,
    height=2,
    text=f"Cliente {cola_clientes[0].id}, edad {cola_clientes[0].edad}, ¿Cuántos jugos quiere comprar?",
    font=("Courier", 16),
)
label_entry.pack(side="top")

input_jugos = tk.Entry(master=frame_acciones, width=30)
input_jugos.pack(side="top")

boton_siguiente = tk.Button(master=frame_acciones, text="Siguiente", width=25)
boton_siguiente.pack(side="bottom", pady=10)


def siguiente_cliente(event):
    global cola_clientes
    global total_jugos_disponibles
    valor_valido = verificar_cantidad_jugos(input_jugos.get())
    if valor_valido:
        cliente = actualizar_listado_clientes()
        realizar_compra(cliente)
        verificar_paciencia()

        if len(cola_clientes) == 0 or total_jugos_disponibles == 0:
            messagebox.showinfo("Atención","Se acabó la venta del día de hoy")
            window.destroy()



def actualizar_listado_clientes():
    global cola_clientes

    cliente = cola_clientes.pop(0)
    if len(cola_clientes) != 0:
        label_clientes_en_cola["text"] = "Total clientes en cola: " + str(
            len(cola_clientes)
        )
        label_entry[
            "text"
        ] = f"Cliente {cola_clientes[0].id}, edad {cola_clientes[0].edad}, ¿Cuántos jugos quiere comprar?"
    else:
        label_clientes_en_cola["text"] = "Total clientes en cola: 0"
        label_entry["text"]="Buen trabajo el día de hoy, nos vemos mañana."
    return cliente

def verificar_cantidad_jugos(value):
    if not str(value).isnumeric():
        messagebox.showinfo("Atención",f"Debe insertar un valor válido.")
        return False
    else:
        return True

def realizar_compra(cliente):
    global total_jugos_disponibles
    global total_ventas

    if cliente.edad >= 10:
        jugos_por_comprar = int(input_jugos.get())
        if jugos_por_comprar > total_jugos_disponibles:
            messagebox.showinfo("Atención",f"Hay {total_jugos_disponibles} y pidió {jugos_por_comprar}. Se le venderán {total_jugos_disponibles}.")
            jugos_por_comprar = total_jugos_disponibles
        else:
            messagebox.showinfo("Atención",f"Se vendieron {jugos_por_comprar} jugos al cliente {cliente.id}.")
        total_jugos_disponibles = total_jugos_disponibles - jugos_por_comprar
        total_ventas = total_ventas + jugos_por_comprar*precio_jugo
        label_jugos_disp["text"] = "Total de jugos disponibles: " + str(total_jugos_disponibles)
        label_total_ventas["text"]= "Total ganado en ventas: " + str(total_ventas)
        input_jugos.delete(0, tk.END)

def verificar_paciencia():
    if random.random() < 0.1 and len(cola_clientes) > 1:
        cola_clientes.pop()
        messagebox.showinfo("Atención",f"El último cliente de la cola se cansó de esperar y se fue.")
        label_clientes_en_cola["text"] = "Total clientes en cola: " + str(
            len(cola_clientes)
        )

boton_siguiente.bind("<Button-1>", siguiente_cliente)

window.mainloop()


# https://runestone.academy/runestone/books/published/thinkcspy/GUIandEventDrivenProgramming/02_standard_dialog_boxes.html <- Cómo sacar ventanas de diálogo con mensajes cortos
