import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os

DB_NAME = 'estacionamiento.db'
TXT_NAME = 'registro_estacionamiento.txt'

# --- DB setup ---
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS vehiculos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patente TEXT NOT NULL,
    ingreso TEXT NOT NULL,
    egreso TEXT,
    tiempo TEXT,
    precio_por_hora REAL,
    precio_total REAL
)
''')
conn.commit()

# --- Funciones CRUD ---
def guardar_en_txt(data):
    with open(TXT_NAME, 'a', encoding='utf-8') as f:
        f.write(f"{data['patente']} | {data['ingreso']} | {data['egreso']} | {data['tiempo']} | {data['precio_por_hora']} | {data['precio_total']}\n")

def registrar():
    patente = entry_patente.get().upper().strip()
    if not patente:
        messagebox.showerror("Error", "Debe ingresar una patente.")
        return

    ingreso = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO vehiculos (patente, ingreso) VALUES (?, ?)", (patente, ingreso))
    conn.commit()
    messagebox.showinfo("Registro", f"Vehículo {patente} registrado a las {ingreso}.")
    entry_patente.delete(0, tk.END)

def retirar():
    patente = entry_patente.get().upper().strip()
    if not patente:
        messagebox.showerror("Error", "Debe ingresar una patente.")
        return

    cursor.execute("SELECT id, ingreso FROM vehiculos WHERE patente = ? AND egreso IS NULL", (patente,))
    row = cursor.fetchone()

    if not row:
        messagebox.showerror("No encontrado", f"No se encontró vehículo activo con patente {patente}.")
        return

    id_registro, ingreso_str = row
    ingreso = datetime.strptime(ingreso_str, '%Y-%m-%d %H:%M:%S')
    egreso = datetime.now()
    tiempo = (egreso - ingreso).total_seconds() / 3600
    precio_por_hora = 500.0
    precio_total = round(precio_por_hora * tiempo, 2)

    cursor.execute('''
        UPDATE vehiculos
        SET egreso = ?, tiempo = ?, precio_por_hora = ?, precio_total = ?
        WHERE id = ?
    ''', (
        egreso.strftime('%Y-%m-%d %H:%M:%S'),
        f"{tiempo:.2f}",
        precio_por_hora,
        precio_total,
        id_registro
    ))
    conn.commit()

    guardar_en_txt({
        'patente': patente,
        'ingreso': ingreso_str,
        'egreso': egreso.strftime('%Y-%m-%d %H:%M:%S'),
        'tiempo': f"{tiempo:.2f}",
        'precio_por_hora': precio_por_hora,
        'precio_total': precio_total
    })

    messagebox.showinfo("Retirado", f"{patente} retirado. Tiempo: {tiempo:.2f} h. Total: ${precio_total}")
    entry_patente.delete(0, tk.END)

def buscar():
    patente = entry_patente.get().upper().strip()
    if not patente:
        messagebox.showerror("Error", "Debe ingresar una patente.")
        return

    cursor.execute("SELECT * FROM vehiculos WHERE patente = ?", (patente,))
    rows = cursor.fetchall()
    if not rows:
        messagebox.showinfo("Sin resultados", f"No se encontró información de {patente}")
    else:
        resultados = "\n".join(
            [f"ID: {r[0]} | Ingreso: {r[2]} | Egreso: {r[3]} | Total: ${r[6] or 0}" for r in rows]
        )
        messagebox.showinfo("Resultado", resultados)

def eliminar():
    patente = entry_patente.get().upper().strip()
    if not patente:
        messagebox.showerror("Error", "Debe ingresar una patente.")
        return

    confirm = messagebox.askyesno("Eliminar", f"¿Eliminar todos los registros de {patente}?")
    if confirm:
        cursor.execute("DELETE FROM vehiculos WHERE patente = ?", (patente,))
        conn.commit()
        messagebox.showinfo("Eliminado", f"Registros de {patente} eliminados.")
        entry_patente.delete(0, tk.END)

# --- Interfaz Gráfica ---
root = tk.Tk()
root.title("Gestión de Estacionamiento")
root.geometry("420x250")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

tk.Label(frame, text="Patente:", font=("Arial", 12)).grid(row=0, column=0, sticky="e", pady=10)
entry_patente = tk.Entry(frame, font=("Arial", 12), width=20)
entry_patente.grid(row=0, column=1, pady=10)

btn_frame = tk.Frame(frame, pady=10)
btn_frame.grid(row=1, column=0, columnspan=2)

tk.Button(btn_frame, text="Registrar Ingreso", width=20, font=("Arial", 10), command=registrar).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Retirar Vehículo", width=20, font=("Arial", 10), command=retirar).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Buscar", width=20, font=("Arial", 10), command=buscar).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Eliminar Registros", width=20, font=("Arial", 10), command=eliminar).grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
