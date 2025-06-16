import tkinter as tk
from tkinter import ttk, messagebox, Menu, filedialog
import sqlite3
from datetime import datetime
from openpyxl import Workbook, load_workbook
import csv
import os

# Base de datos SQLite (obligatorio)
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

# Excel default path
excel_file = "registro_estacionamiento.xlsx"

def actualizar_excel(ruta=None):
    """Guardar la base en Excel (ruta opcional para guardar en otro lugar)"""
    wb = Workbook()
    ws = wb.active
    ws.append(["Patente", "Sector", "Ingreso", "Egreso", "Tiempo estimado", "Tiempo total", "Precio por Hora", "Precio Total"])
    cursor.execute("SELECT * FROM vehiculos")
    for row in cursor.fetchall():
        ws.append(row)
    if ruta:
        wb.save(ruta)
    else:
        wb.save(excel_file)

def guardar_csv(ruta):
    """Guardar la base en CSV"""
    cursor.execute("SELECT * FROM vehiculos")
    datos = cursor.fetchall()
    with open(ruta, 'w', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow(["Patente", "Sector", "Ingreso", "Egreso", "Tiempo estimado", "Tiempo total", "Precio por Hora", "Precio Total"])
        escritor.writerows(datos)
    messagebox.showinfo("Guardado CSV", f"Archivo guardado correctamente en:\n{ruta}")

def registrar():
    patente = entry_patente.get()
    sector = combo_sector.get()
    tiempo_est = entry_tiempo.get()
    ingreso = entry_ingreso.get()
    egreso = entry_egreso.get()

    if not patente or not sector:
        messagebox.showerror("Error", "Patente y Sector son obligatorios.")
        return

    cursor.execute("INSERT INTO vehiculos (patente, sector, ingreso, egreso, tiempo_estimado, tiempo_total, precio_hora, precio_total) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (patente, sector, ingreso, egreso, tiempo_est, '', 0.0, 0.0))
    conn.commit()
    mostrar_datos()
    entry_patente.delete(0, tk.END)
    entry_tiempo.delete(0, tk.END)
    entry_ingreso.delete(0, tk.END)
    entry_egreso.delete(0, tk.END)

def mostrar_datos():
    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM vehiculos")
    for row in cursor.fetchall():
        color = "turquoise" if row[3] else "white"
        tree.insert("", tk.END, values=row, tags=(color,))
    tree.tag_configure("turquoise", background="turquoise")
    tree.tag_configure("white", background="white")

def actualizar_reloj():
    hora_actual = datetime.now().strftime("%H:%M:%S")
    reloj_label.config(text=hora_actual)
    reloj_label.after(1000, actualizar_reloj)

def guardar_excel_desde_menu():
    ruta = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                        filetypes=[("Archivos Excel", "*.xlsx")])
    if ruta:
        actualizar_excel(ruta)
        messagebox.showinfo("Guardado Excel", f"Archivo guardado correctamente en:\n{ruta}")

def guardar_csv_desde_menu():
    ruta = filedialog.asksaveasfilename(defaultextension=".csv",
                                        filetypes=[("Archivos CSV", "*.csv")])
    if ruta:
        guardar_csv(ruta)

# Ventana principal
root = tk.Tk()
root.title("Sistema de Estacionamiento")
root.geometry("1200x650")

# Menú superior con submenú "Más"
menu_bar = Menu(root)
root.config(menu=menu_bar)

menu_mas = Menu(menu_bar, tearoff=0)
menu_mas.add_command(label="Guardar Excel", command=guardar_excel_desde_menu)
menu_mas.add_command(label="Guardar CSV", command=guardar_csv_desde_menu)

menu_bar.add_cascade(label="Más", menu=menu_mas)

# Marco contenedor principal (rectángulo)
frame_principal = tk.Frame(root, bd=2, relief="groove")
frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Dividir frame_principal verticalmente en dos: cabecera (30%), cuerpo (70%)
frame_principal.rowconfigure(0, weight=3)  # 30%
frame_principal.rowconfigure(1, weight=7)  # 70%
frame_principal.columnconfigure(0, weight=1)

# --- CABECERA ---
frame_cabecera = tk.Frame(frame_principal)
frame_cabecera.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
frame_cabecera.columnconfigure(0, weight=7)
frame_cabecera.columnconfigure(1, weight=3)
frame_cabecera.rowconfigure(0, weight=1)

# Zona izquierda inputs
frame_izquierda = tk.Frame(frame_cabecera)
frame_izquierda.grid(row=0, column=0, sticky="nsew")

# Dividir verticalmente en dos bloques (arriba y abajo)
frame_izquierda.rowconfigure(0, weight=1)
frame_izquierda.rowconfigure(1, weight=1)
frame_izquierda.columnconfigure(0, weight=1)

# Bloque superior (Patente, Sector)
frame_bloque_sup = tk.Frame(frame_izquierda, bd=1, relief="ridge", padx=10, pady=10)
frame_bloque_sup.grid(row=0, column=0, sticky="nsew", pady=(0,5))

tk.Label(frame_bloque_sup, text="Patente", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=2, sticky="w")
entry_patente = tk.Entry(frame_bloque_sup, width=15, font=("Arial", 12))
entry_patente.grid(row=1, column=0, padx=5, pady=2, sticky="w")

tk.Label(frame_bloque_sup, text="Sector de estacionamiento", font=("Arial", 10)).grid(row=0, column=1, padx=5, pady=2, sticky="w")
combo_sector = ttk.Combobox(frame_bloque_sup, values=["Sector 1", "Sector 2", "Sector 3", "Sector 4"], width=15, font=("Arial", 12))
combo_sector.grid(row=1, column=1, padx=5, pady=2, sticky="w")
combo_sector.set("")

# Bloque inferior (Tiempo estimado, Ingreso, Egreso y botón)
frame_bloque_inf = tk.Frame(frame_izquierda, bd=1, relief="ridge", padx=10, pady=10)
frame_bloque_inf.grid(row=1, column=0, sticky="nsew", pady=(5,0))

tk.Label(frame_bloque_inf, text="Tiempo estimado", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=2, sticky="w")
entry_tiempo = tk.Entry(frame_bloque_inf, width=15, font=("Arial", 12))
entry_tiempo.grid(row=1, column=0, padx=5, pady=2, sticky="w")

tk.Label(frame_bloque_inf, text="Ingreso", font=("Arial", 10)).grid(row=0, column=1, padx=5, pady=2, sticky="w")
entry_ingreso = tk.Entry(frame_bloque_inf, width=18, font=("Arial", 12))
entry_ingreso.grid(row=1, column=1, padx=5, pady=2, sticky="w")

tk.Label(frame_bloque_inf, text="Egreso", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=2, sticky="w")
entry_egreso = tk.Entry(frame_bloque_inf, width=18, font=("Arial", 12))
entry_egreso.grid(row=1, column=2, padx=5, pady=2, sticky="w")

btn_registrar = tk.Button(frame_bloque_inf, text="Registrar", command=registrar)
btn_registrar.grid(row=1, column=3, padx=15, pady=2, sticky="e")

# Zona derecha: Reloj digital
reloj_label = tk.Label(frame_cabecera, text="", font=("Segoe UI", 30, "bold"), fg="white", bg="black", padx=20, pady=10)
reloj_label.grid(row=0, column=1, sticky="ne", padx=10, pady=10)
actualizar_reloj()

# --- CUERPO ---
frame_cuerpo = tk.Frame(frame_principal)
frame_cuerpo.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
frame_cuerpo.rowconfigure(0, weight=1)
frame_cuerpo.columnconfigure(0, weight=1)

columns = ("patente", "sector", "ingreso", "egreso", "tiempo_estimado", "tiempo_total", "precio_hora", "precio_total")
tree = ttk.Treeview(frame_cuerpo, columns=columns, show="headings")
tree.grid(row=0, column=0, sticky="nsew")

scrollbar = ttk.Scrollbar(frame_cuerpo, orient=tk.VERTICAL, command=tree.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
tree.configure(yscrollcommand=scrollbar.set)

for col, title in zip(columns, ["Patente", "Sector", "Ingreso", "Egreso", "Tiempo estimado", "Tiempo total", "Precio x Hora", "Precio Total"]):
    tree.heading(col, text=title)
    tree.column(col, anchor=tk.CENTER, width=120)

mostrar_datos()

root.mainloop()
