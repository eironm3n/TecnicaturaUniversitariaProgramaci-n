from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3, os
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB = os.path.join(BASE_DIR, 'base.db')
PRECIO_HORA_DEFAULT = 1500

app = Flask(__name__, static_folder='static', template_folder='templates')

# ── DB helpers ─────────────────────────────────────────────

def init_db():
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS vehiculos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patente TEXT UNIQUE,
            sector TEXT,
            ingreso TEXT,
            egreso TEXT,
            tiempo_min INTEGER,
            precio_hora INTEGER,
            precio_total INTEGER,
            pago TEXT DEFAULT 'No')''')
        conn.commit()

# ── Rutas ─────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html', tarifa=PRECIO_HORA_DEFAULT)

@app.route('/vehiculos')
def vehiculos():
    with sqlite3.connect(DB) as conn:
        registros = conn.execute('SELECT * FROM vehiculos ORDER BY id DESC').fetchall()
    return jsonify(registros)

@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.get_json()
    patente = data['patente']
    sector = data['sector']
    precio_hora = int(data['precio_hora'] or PRECIO_HORA_DEFAULT)
    ingreso = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        try:
            cur.execute('INSERT INTO vehiculos(patente,sector,ingreso,precio_hora) VALUES (?,?,?,?)',
                        (patente, sector, ingreso, precio_hora))
            conn.commit()
        except sqlite3.IntegrityError:
            return 'Patente ya registrada', 400
    return '', 204

@app.route('/cobrar', methods=['POST'])
def cobrar():
    vid = request.json['id']
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute('SELECT ingreso, precio_hora FROM vehiculos WHERE id=?', (vid,))
        row = cur.fetchone()
        if not row:
            return 'Registro no válido', 400
        ingreso_dt = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        egreso_dt = datetime.now()
        minutos = int((egreso_dt - ingreso_dt).total_seconds() / 60)
        total = int((minutos / 60) * row[1])
        cur.execute('''UPDATE vehiculos SET egreso=?, tiempo_min=?, precio_total=?, pago='Si' WHERE id=?''',
                    (egreso_dt.strftime('%Y-%m-%d %H:%M:%S'), minutos, total, vid))
        conn.commit()
    return '', 204

if __name__ == '__main__':
    init_db()
    app.run(debug=True)