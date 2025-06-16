import sqlite3
import os
from tkinter import *
from tkinter import ttk
from datetime import datetime

# --- CONFIGURACIÓN BASE DE DATOS ---
DB_PATH = "estacionamiento.db"
TABLA = "vehiculos"
CAMPOS_REQUERIDOS = {
    "patente", "ingreso", "egreso", "tiempo", "precio_por_hora", "precio_total"
}

def verificar_estructura():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Verificar si existe la tabla
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLA}'")
    existe = cursor.fetchone()

    if existe:
        cursor.execute(f"PRAGMA table_info({TABLA})")
        columnas_actuales = {col[1] for col in cursor.fetchall()}
        if not CAMPOS_REQUERIDOS.issubset(columnas_actuales):
            cursor.execute(f"DROP TABLE {TABLA}")
            conn.commit()
            crear_tabla(cursor)
    else:
        crear_tabla(cursor)

    conn.commit()
    conn.close()

def crear_tabla(cursor):
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLA} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patente TEXT NOT NULL,
            ingreso TEXT NOT NULL,
            egreso TEXT,
            tiempo TEXT,
            precio_por_hora REAL,
            precio_total REAL
        )
    """)

# --- FUNCIONES DEL CRUD ---
def registrar():
    patente = entrada_patente.get().strip().upper()
    ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not patente:
        resultado.set("Debe ingresar una patente")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO {TABLA} (patente, ingreso)
        VALUES (?, ?)
    """, (patente, ingreso))
    conn.commit()
    conn.close()

    guardar_txt(patente, ingreso)
    resultado.set(f"Patente {patente} registrada.")
    entrada_patente.delete(0, END)
    cargar_tabla()

def guardar_txt(patente, ingreso):
    with open("registro.txt", "a") as f:
        f.write(f"{patente}, {ingreso}\n")

def cargar_tabla():
    for fila in tabla.get_children():
        tabla.delete(fila)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"SELECT patente, ingreso, egreso, tiempo, precio_por_hora, precio_total FROM {TABLA}")
    registros = cursor.fetchall()
    conn.close()

    for row in registros:
        tabla.insert("", "end", values=row)

# --- INTERFAZ ---
verificar_estructura()

ventana = Tk()
ventana.title("Estacionamiento")
ventana.geometry("700x400")

Label(ventana, text="Patente:").pack(pady=5)
entrada_patente = Entry(ventana, font=("Arial", 12))
entrada_patente.pack()

Button(ventana, text="Registrar ingreso", command=registrar).pack(pady=5)

resultado = StringVar()
Label(ventana, textvariable=resultado, fg="blue").pack(pady=5)

# Tabla visual
frame_tabla = Frame(ventana)
frame_tabla.pack(fill=BOTH, expand=True)

columnas = ("patente", "ingreso", "egreso", "tiempo", "precio_por_hora", "precio_total")
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

for col in columnas:
    tabla.heading(col, text=col.replace("_", " ").title())
    tabla.column(col, width=100)

tabla.pack(fill=BOTH, expand=True)

cargar_tabla()
ventana.mainloop()
