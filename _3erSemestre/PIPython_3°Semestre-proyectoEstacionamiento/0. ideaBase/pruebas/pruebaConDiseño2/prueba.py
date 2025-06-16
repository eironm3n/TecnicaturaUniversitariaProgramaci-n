import re, sqlite3, time
from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox
from openpyxl import Workbook, load_workbook

DB = "estacionamiento.db"
XL = "estacionamiento.xlsx"
TABLA = "vehiculos"
DATE_FMT = "%Y-%m-%d %H:%M:%S"

# --------- ESQUEMA ---------
REQ_COLS = {
    "patente","ingreso","egreso","sector",
    "tiempo_estimado","tiempo_total",
    "precio_por_hora","precio_total"
}
def check_schema():
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLA}'")
    if cur.fetchone():
        cur.execute(f"PRAGMA table_info({TABLA})")
        if not REQ_COLS.issubset({c[1] for c in cur.fetchall()}):
            cur.execute(f"DROP TABLE {TABLA}")
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLA}(
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
    con.commit(); con.close()

# --------- VALIDACIÓN PATENTE ---------
PLATE_RE = re.compile(r"^[A-Za-z0-9]{4}-[A-Za-z0-9]{4}-[A-Za-z0-9]{4}$")

# --------- CRUD BÁSICO ---------
def export_excel():
    rows = get_all()
    wb = Workbook(); ws = wb.active
    ws.append(["Patente","Ingreso","Egreso","Sector",
               "Tiempo estimado","Tiempo total",
               "Precio/h","Precio total"])
    for r in rows:
        ws.append(r)
    wb.save(XL)

def get_all():
    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute(f"""
        SELECT patente, ingreso, egreso, sector,
               tiempo_estimado, tiempo_total,
               precio_por_hora, precio_total
        FROM {TABLA} ORDER BY id DESC
    """); rows = cur.fetchall(); con.close()
    return rows

def registrar():
    pat = e_patente.get().strip().upper()
    sect = cb_sector.get()
    t_est_raw = e_tiempo.get().strip()
    if not PLATE_RE.match(pat):
        status.set("Patente inválida (formato XXXX-XXXX-XXXX)")
        return
    if not sect: status.set("Seleccione sector"); return
    t_est = float(t_est_raw) if t_est_raw else None

    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute(f"""
        INSERT INTO {TABLA} (patente, ingreso, sector, tiempo_estimado,
                             precio_por_hora)
        VALUES (?,?,?,?,?)
    """,(pat, datetime.now().strftime(DATE_FMT), sect, t_est, 500))
    con.commit(); con.close()
    limpiar_inputs(); recargar_tabla(); export_excel()
    status.set(f"{pat} registrado")

def limpiar_inputs():
    e_patente.delete(0,END); e_tiempo.delete(0,END); cb_sector.current(0)

def seleccionar(evt):
    sel = tree.focus()
    if not sel: return
    vals = tree.item(sel)["values"]
    e_ingreso.delete(0,END); e_ingreso.insert(0, vals[1])
    e_egreso.delete(0,END);  e_egreso.insert(0, vals[2])

def actualizar_tiempos():
    sel = tree.focus()
    if not sel:
        messagebox.showwarning("Aviso","Seleccione una fila"); return
    patente = tree.item(sel)["values"][0]
    nuevo_ing = e_ingreso.get().strip()
    nuevo_egr = e_egreso.get().strip()

    con = sqlite3.connect(DB); cur = con.cursor()
    cur.execute(f"SELECT egreso, precio_total, ingreso FROM {TABLA} WHERE patente=?",(patente,))
    egreso_db, pagado, ing_db = cur.fetchone()

    # validar formatos
    try:
        if nuevo_ing: datetime.strptime(nuevo_ing, DATE_FMT)
        if nuevo_egr: datetime.strptime(nuevo_egr, DATE_FMT)
    except ValueError:
        messagebox.showerror("Error","Formato de fecha/hora inválido"); return

    # restricciones
    if nuevo_egr and not pagado:
        messagebox.showerror("Denegado","Solo se edita 'Egreso' si ya está pagado")
        return

    # calcular tiempo_total y precio_total si ambos tiempos están
    tiempo_total = None; precio_total = None
    if nuevo_ing and nuevo_egr:
        dt_in = datetime.strptime(nuevo_ing, DATE_FMT)
        dt_out = datetime.strptime(nuevo_egr, DATE_FMT)
        horas = (dt_out-dt_in).total_seconds()/3600
        tiempo_total = round(horas,2); precio_total = round(horas*500,2)

    cur.execute(f"""
        UPDATE {TABLA}
        SET ingreso=?, egreso=?, tiempo_total=?, precio_total=?
        WHERE patente=?""",
        (nuevo_ing or ing_db, nuevo_egr or egreso_db,
         tiempo_total, precio_total, patente))
    con.commit(); con.close()
    recargar_tabla(); export_excel()

def recargar_tabla():
    tree.delete(*tree.get_children())
    for r in get_all():
        tag = "salio" if r[2] else "entra"
        tree.insert("",END,values=r,tags=(tag,))
    tree.tag_configure("salio",background="#40e0d0")
    tree.tag_configure("entra",background="white")

# --------- RELOJ ---------
def tick():
    reloj.set(time.strftime("%H:%M:%S"))
    root.after(1000,tick)

# --------- UI ---------
check_schema()
root = Tk(); root.title("Estacionamiento"); root.geometry("1080x540")

## fila de entrada + reloj
fila = Frame(root,padx=10,pady=10); fila.pack(fill=X)
Label(fila,text="Patente").grid(row=0,column=0)
e_patente = Entry(fila,width=16,font=("Consolas",11)); e_patente.grid(row=0,column=1,padx=6)

Label(fila,text="Sector de estacionamiento").grid(row=0,column=2)
cb_sector = ttk.Combobox(fila,values=[f"Sector {i}" for i in range(1,5)],
                         width=12,state="readonly"); cb_sector.current(0)
cb_sector.grid(row=0,column=3,padx=6)

Label(fila,text="Tiempo estimado (h)").grid(row=0,column=4)
e_tiempo = Entry(fila,width=6); e_tiempo.grid(row=0,column=5,padx=6)

Button(fila,text="Registrar",command=registrar).grid(row=0,column=6,padx=15)

reloj = StringVar()
Label(fila,textvariable=reloj,font=("Consolas",16),fg="navy").grid(row=0,column=7,sticky="e")
tick()  # inicia reloj

## área de edición Ingreso / Egreso
edit = Frame(root,padx=10); edit.pack(fill=X)
Label(edit,text="Ingreso").grid(row=0,column=0,sticky="e")
e_ingreso = Entry(edit,width=20); e_ingreso.grid(row=0,column=1,padx=5)
Label(edit,text="Egreso").grid(row=0,column=2,sticky="e")
e_egreso  = Entry(edit,width=20); e_egreso.grid(row=0,column=3,padx=5)
Button(edit,text="Actualizar",command=actualizar_tiempos).grid(row=0,column=4,padx=10)

status = StringVar(); Label(root,textvariable=status,fg="blue").pack()

## tabla
cols = ("patente","ingreso","egreso","sector",
        "tiempo_estimado","tiempo_total",
        "precio_por_hora","precio_total")
tree = ttk.Treeview(root,columns=cols,show="headings",height=15)
for c in cols:
    tree.heading(c,text=c.replace("_"," ").title())
    tree.column(c,width=130 if c not in {"ingreso","egreso"} else 160)
tree.pack(fill=BOTH,expand=True,padx=10,pady=10)
tree.bind("<<TreeviewSelect>>",seleccionar)

recargar_tabla()
root.mainloop()
