import sqlite3
from tkinter import *
from tkinter import ttk
from datetime import datetime

DB_PATH = "estacionamiento.db"
TABLA   = "vehiculos"

# -------- estructura requerida --------
CAMPOS_REQ = {
    "patente", "ingreso", "egreso", "sector",
    "tiempo_estimado", "tiempo_total",
    "precio_por_hora", "precio_total"
}

def check_schema():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLA}'")
    if cur.fetchone():
        cur.execute(f"PRAGMA table_info({TABLA})")
        cols = {c[1] for c in cur.fetchall()}
        if not CAMPOS_REQ.issubset(cols):
            cur.execute(f"DROP TABLE {TABLA}")
            con.commit()
            create_table(cur)
    else:
        create_table(cur)
    con.commit(); con.close()

def create_table(cur):
    cur.execute(f"""
        CREATE TABLE {TABLA} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patente TEXT NOT NULL,
            ingreso TEXT NOT NULL,
            egreso TEXT,
            sector TEXT,
            tiempo_estimado REAL,
            tiempo_total REAL,
            precio_por_hora REAL,
            precio_total REAL
        )
    """)

# -------- CRUD básico --------
def registrar():
    pat   = e_patente.get().strip().upper()
    sect  = combo_sector.get()
    test  = e_tiempo.get().strip()
    t_est = float(test) if test else None   # opcional

    if not pat or not sect:
        status.set("Patente y Sector son obligatorios"); return

    ing = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    con = sqlite3.connect(DB_PATH); cur = con.cursor()
    cur.execute(f"""
        INSERT INTO {TABLA} (patente, ingreso, sector, tiempo_estimado)
        VALUES (?,?,?,?)
    """, (pat, ing, sect, t_est))
    con.commit(); con.close()

    with open("registro.txt","a",encoding="utf-8") as f:
        f.write(f"{pat} | {ing} | {sect} | {t_est or ''}\n")

    e_patente.delete(0,END); e_tiempo.delete(0,END); combo_sector.current(0)
    status.set(f"Registrado {pat} en {sect}")
    cargar_tabla()

def cargar_tabla():
    for i in tree.get_children(): tree.delete(i)
    con = sqlite3.connect(DB_PATH); cur = con.cursor()
    cur.execute(f"""
        SELECT patente, ingreso, egreso, sector,
               tiempo_estimado, tiempo_total,
               precio_por_hora, precio_total
        FROM {TABLA}
        ORDER BY id DESC
    """)
    for row in cur.fetchall():
        tree.insert("",END,values=row)
    con.close()

# -------- interfaz --------
check_schema()

root = Tk(); root.title("Estacionamiento"); root.geometry("940x420")

# fila de entradas
frm_inputs = Frame(root, padx=10, pady=10)
frm_inputs.pack(fill=X)

Label(frm_inputs,text="Patente").grid(row=0,column=0, padx=5)
e_patente = Entry(frm_inputs,width=12,font=("Arial",11)); e_patente.grid(row=0,column=1, padx=5)

Label(frm_inputs,text="Sector de estacionamiento").grid(row=0,column=2, padx=5)
combo_sector = ttk.Combobox(frm_inputs,values=[f"Sector {i}" for i in range(1,5)],
                            state="readonly",width=12,font=("Arial",11))
combo_sector.grid(row=0,column=3, padx=5); combo_sector.current(0)

Label(frm_inputs,text="Tiempo estimado (h)").grid(row=0,column=4, padx=5)
e_tiempo = Entry(frm_inputs,width=8,font=("Arial",11)); e_tiempo.grid(row=0,column=5, padx=5)

Button(frm_inputs,text="Registrar ingreso",command=registrar).grid(row=0,column=6, padx=10)

# estado
status = StringVar(); Label(root,textvariable=status,fg="blue").pack()

# tabla
cols = ("patente","ingreso","egreso","sector",
        "tiempo_estimado","tiempo_total",
        "precio_por_hora","precio_total")
tree = ttk.Treeview(root,columns=cols,show="headings",height=12)
for c in cols:
    tree.heading(c,text=c.replace("_"," ").title())
    w = 110 if c not in {"ingreso","egreso"} else 150
    tree.column(c,width=w)

tree.pack(fill=BOTH,expand=True,padx=10,pady=10)

cargar_tabla()
root.mainloop()
