import sqlite3
import os
from tkinter import *
from tkinter import ttk
from datetime import datetime

DB_PATH = "estacionamiento.db"
TABLA = "vehiculos"
CAMPOS_REQUERIDOS = {
    "patente", "ingreso", "egreso", "tiempo", "precio_por_hora",
    "precio_total", "lugar_ingreso", "tiempo_estimado"
}

def verificar_estructura():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
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
            precio_total REAL,
            lugar_ingreso TEXT,
            tiempo_estimado REAL
        )
    """)

def registrar():
    patente = entrada_patente.get().strip().upper()
    lugar = entrada_lugar.get().strip()
    tiempo_est = entrada_tiempo.get().strip()

    if not patente or not lugar or not tiempo_est:
        resultado.set("Todos los campos son obligatorios.")
        return

    try:
        tiempo_est = float(tiempo_est)
    except ValueError:
        resultado.set("El tiempo estimado debe ser un número.")
        return

    ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO {TABLA} (patente, ingreso, lugar_ingreso, tiempo_estimado)
        VALUES (?, ?, ?, ?)
    """, (patente, ingreso, lugar, tiempo_est))
    conn.commit()
    conn.close()

    guardar_txt(patente, ingreso, lugar, tiempo_est)
    resultado.set(f"Patente {patente} registrada.")
    entrada_patente.delete(0, END)
    entrada_lugar.delete(0, END)
    entrada_tiempo.delete(0, END)
    cargar_tabla()

def guardar_txt(patente, ingreso, lugar, tiempo):
    with open("registro.txt", "a") as f:
        f.write(f"{patente}, {ingreso}, {lugar}, {tiempo} hs\n")

def cargar_tabla():
    for fila in tabla.get_children():
        tabla.delete(fila)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT patente, ingreso, lugar_ingreso, tiempo_estimado, egreso,
               tiempo, precio_por_hora, precio_total
        FROM {TABLA}
    """)
    registros = cursor.fetchall()
    conn.close()

    for row in registros:
        tabla.insert("", "end", values=row)

# --- Interfaz ---
verificar_estructura()

ventana = Tk()
ventana.title("Estacionamiento")
ventana.geometry("900x500")

Label(ventana, text="Patente:").pack()
entrada_patente = Entry(ventana, font=("Arial", 12))
entrada_patente.pack()

Label(ventana, text="Lugar de Ingreso:").pack()
entrada_lugar = Entry(ventana, font=("Arial", 12))
entrada_lugar.pack()

Label(ventana, text="Tiempo Estimado (horas):").pack()
entrada_tiempo = Entry(ventana, font=("Arial", 12))
entrada_tiempo.pack()

Button(ventana, text="Registrar ingreso", command=registrar).pack(pady=10)

resultado = StringVar()
Label(ventana, textvariable=resultado, fg="blue").pack(pady=5)

# Tabla visual
frame_tabla = Frame(ventana)
frame_tabla.pack(fill=BOTH, expand=True)

columnas = (
    "patente", "ingreso", "lugar_ingreso", "tiempo_estimado",
    "egreso", "tiempo", "precio_por_hora", "precio_total"
)
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

for col in columnas:
    tabla.heading(col, text=col.replace("_", " ").title())
    tabla.column(col, width=110)

tabla.pack(fill=BOTH, expand=True)

cargar_tabla()
ventana.mainloop()
