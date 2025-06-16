import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
from datetime import datetime
from openpyxl import Workbook, load_workbook
import csv
import os

# --- Base de datos ---
conn = sqlite3.connect('base.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS vehiculos (
    patente TEXT,
    sector TEXT,
    ingreso TEXT,
    egreso TEXT,
    tiempo_estimado TEXT,
    tiempo_total TEXT,
    precio_hora REAL,
    precio_total REAL,
    pago_confirmado INTEGER DEFAULT 0
)''')
conn.commit()

# --- Funciones ---
def formatear_patente(p):
    return f"{p[:3]}-{p[3:]}" if len(p) == 6 else p

def registrar():
    patente = formatear_patente(entry_patente.get().upper())
    sector = combo_sector.get()
    tiempo_est = entry_tiempo.get()
    ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not patente or not sector:
        messagebox.showerror("Error", "Patente y Sector son obligatorios.")
        return

    cursor.execute("INSERT INTO vehiculos (patente, sector, ingreso, egreso, tiempo_estimado, tiempo_total, precio_hora, precio_total, pago_confirmado) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (patente, sector, ingreso, '', tiempo_est, '', 1500.0, 0.0, 0))
    conn.commit()
    mostrar_datos()
    entry_patente.delete(0, tk.END)
    entry_tiempo.delete(0, tk.END)

def buscar_vehiculo():
    patente = formatear_patente(entry_patente.get().upper())
    for item in tree.get_children():
        if tree.item(item)['values'][0] == patente:
            tree.selection_set(item)
            tree.focus(item)
            tree.see(item)
            return
    messagebox.showinfo("Buscar", "Vehículo no encontrado.")

def cobrar():
    seleccionado = tree.focus()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Seleccione un vehículo.")
        return

    datos = tree.item(seleccionado)['values']
    if datos[-1] == "Sí":
        messagebox.showinfo("Información", "El vehículo ya ha sido pagado.")
        return

    ingreso = datetime.strptime(datos[2], "%Y-%m-%d %H:%M:%S")
    egreso = datetime.now()
    tiempo_total = (egreso - ingreso).total_seconds() / 3600
    tiempo_total = round(tiempo_total, 2)
    precio_total = round(tiempo_total * 1500, 2)

    cursor.execute("UPDATE vehiculos SET egreso=?, tiempo_total=?, precio_total=?, pago_confirmado=1 WHERE patente=? AND ingreso=?",
                   (egreso.strftime("%Y-%m-%d %H:%M:%S"), f"{tiempo_total:.2f}", precio_total, datos[0], datos[2]))
    conn.commit()
    mostrar_datos()

def mostrar_datos():
    for i in tree.get_children():
        tree.delete(i)
    cursor.execute("SELECT * FROM vehiculos")
    for row in cursor.fetchall():
        pago = "Sí" if row[-1] else "No"
        tree.insert("", tk.END, values=row[:-1] + (pago,))

def guardar_excel():
    wb = Workbook()
    ws = wb.active
    ws.append(["Patente", "Sector", "Ingreso", "Egreso", "Tiempo estimado", "Tiempo total", "Precio por Hora", "Precio Total", "Pagó"])
    cursor.execute("SELECT * FROM vehiculos")
    for row in cursor.fetchall():
        pago = "Sí" if row[-1] else "No"
        ws.append(row[:-1] + (pago,))
    wb.save("registro_estacionamiento.xlsx")

def guardar_csv():
    with open("registro_estacionamiento.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Patente", "Sector", "Ingreso", "Egreso", "Tiempo estimado", "Tiempo total", "Precio por Hora", "Precio Total", "Pagó"])
        cursor.execute("SELECT * FROM vehiculos")
        for row in cursor.fetchall():
            pago = "Sí" if row[-1] else "No"
            writer.writerow(row[:-1] + (pago,))

def actualizar_reloj():
    reloj_label.config(text=datetime.now().strftime("%H:%M:%S"))
    reloj_label.after(1000, actualizar_reloj)

# --- UI ---
root = tk.Tk()
root.title("Sistema de Estacionamiento")
root.geometry("1200x700")

# Menú superior
menubar = tk.Menu(root)
opciones_menu = tk.Menu(menubar, tearoff=0)
opciones_menu.add_command(label="Exportar a Excel", command=guardar_excel)
opciones_menu.add_command(label="Exportar a CSV", command=guardar_csv)
menubar.add_cascade(label="Más", menu=opciones_menu)
root.config(menu=menubar)

# Contenedor principal
frame_main = tk.Frame(root)
frame_main.pack(fill="both", expand=True)

# Cabecera (30%)
frame_cabecera = tk.Frame(frame_main, height=210, bg="lightgray")
frame_cabecera.pack(fill="x")
frame_cabecera.pack_propagate(False)

# Izquierda - entradas
frame_izq = tk.Frame(frame_cabecera, bg="lightgray")
frame_izq.pack(side="left", fill="both", expand=True, padx=10, pady=10)

frame_sup = tk.Frame(frame_izq, bg="lightgray")
frame_sup.pack(fill="x", expand=True)
tk.Label(frame_sup, text="Patente", bg="lightgray").grid(row=0, column=0)
entry_patente = tk.Entry(frame_sup)
entry_patente.grid(row=1, column=0, padx=5)

tk.Label(frame_sup, text="Sector", bg="lightgray").grid(row=0, column=1)
combo_sector = ttk.Combobox(frame_sup, values=["1", "2", "3"])
combo_sector.grid(row=1, column=1, padx=5)

tk.Label(frame_sup, text="Tiempo Estimado (h)", bg="lightgray").grid(row=0, column=2)
entry_tiempo = tk.Entry(frame_sup)
entry_tiempo.grid(row=1, column=2, padx=5)

frame_inf = tk.Frame(frame_izq, bg="lightgray")
frame_inf.pack(fill="x", expand=True, pady=10)

btn_registrar = tk.Button(frame_inf, text="Registrar", command=registrar)
btn_registrar.grid(row=0, column=0, padx=5)
btn_buscar = tk.Button(frame_inf, text="Buscar Vehículo", command=buscar_vehiculo)
btn_buscar.grid(row=0, column=1, padx=5)
btn_cobrar = tk.Button(frame_inf, text="Cobrar", command=cobrar)
btn_cobrar.grid(row=0, column=2, padx=5)

# Derecha - reloj
reloj_label = tk.Label(frame_cabecera, text="", font=("Segoe UI", 30), fg="white", bg="black", padx=20)
reloj_label.pack(side="right", fill="y")
actualizar_reloj()

# Cuerpo (70%)
frame_cuerpo = tk.Frame(frame_main, bg="#f0f0f0")
frame_cuerpo.pack(fill="both", expand=True)

columns = ("patente", "sector", "ingreso", "egreso", "tiempo_estimado", "tiempo_total", "precio_hora", "precio_total", "pagado")
tree = ttk.Treeview(frame_cuerpo, columns=columns, show="headings")
tree.pack(fill="both", expand=True)

for col in columns:
    tree.heading(col, text=col.replace("_", " ").capitalize())

mostrar_datos()
root.mainloop()
