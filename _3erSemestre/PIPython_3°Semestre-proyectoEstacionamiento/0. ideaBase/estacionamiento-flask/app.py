from flask import Flask, render_template, request, jsonify, send_file
import sqlite3
from datetime import datetime
from openpyxl import Workbook
import csv
import io

app = Flask(__name__)

DB_FILE = "base.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vehiculos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patente TEXT,
        sector TEXT,
        ingreso TEXT,
        egreso TEXT,
        tiempo_estimado TEXT,
        tiempo_total TEXT,
        precio_hora REAL,
        precio_total REAL,
        pago_confirmado INTEGER DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

init_db()

def dict_from_row(row):
    return {
        "id": row[0],
        "patente": row[1],
        "sector": row[2],
        "ingreso": row[3],
        "egreso": row[4],
        "tiempo_estimado": row[5],
        "tiempo_total": row[6],
        "precio_hora": row[7],
        "precio_total": row[8],
        "pago_confirmado": bool(row[9]),
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vehiculos", methods=["GET"])
def get_vehiculos():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vehiculos")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([dict_from_row(row) for row in rows])

@app.route("/registrar", methods=["POST"])
def registrar():
    data = request.json
    patente_raw = data.get("patente", "")
    patente = agregar_guion_patente(patente_raw)
    sector = data.get("sector", "")
    ingreso = data.get("ingreso", "") or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    egreso = data.get("egreso", "")
    tiempo_estimado = data.get("tiempo_estimado", "")
    precio_hora = 1500.0
    precio_total = 0.0
    tiempo_total = ""

    if not patente or not sector or not ingreso:
        return jsonify({"error": "Patente, Sector e Ingreso son obligatorios."}), 400

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO vehiculos (patente, sector, ingreso, egreso, tiempo_estimado, tiempo_total, precio_hora, precio_total)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (patente, sector, ingreso, egreso, tiempo_estimado, tiempo_total, precio_hora, precio_total))
    conn.commit()
    conn.close()

    return jsonify({"message": "Vehículo registrado."})

def agregar_guion_patente(patente_sin_guion: str) -> str:
    """Asume patente de 6 caracteres, le agrega guion luego del 3er caracter."""
    p = patente_sin_guion.replace("-", "").upper()
    if len(p) == 6:
        return p[:3] + "-" + p[3:]
    return p

@app.route("/buscar", methods=["GET"])
def buscar():
    patente_raw = request.args.get("patente", "")
    patente = agregar_guion_patente(patente_raw)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vehiculos WHERE patente=?", (patente,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return jsonify(dict_from_row(row))
    else:
        return jsonify({"error": "Vehículo no encontrado."}), 404

@app.route("/cobrar", methods=["POST"])
def cobrar():
    data = request.json
    vehiculo_id = data.get("id")
    egreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not vehiculo_id:
        return jsonify({"error": "ID de vehículo requerido."}), 400

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT ingreso, precio_hora FROM vehiculos WHERE id=?", (vehiculo_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return jsonify({"error": "Vehículo no encontrado."}), 404

    ingreso_str, precio_hora = row
    ingreso_dt = datetime.strptime(ingreso_str, "%Y-%m-%d %H:%M:%S")
    egreso_dt = datetime.strptime(egreso, "%Y-%m-%d %H:%M:%S")
    tiempo_total = str(egreso_dt - ingreso_dt)

    horas = (egreso_dt - ingreso_dt).total_seconds() / 3600
    precio_total = round(horas * precio_hora, 2)

    cursor.execute('''
        UPDATE vehiculos
        SET egreso=?, tiempo_total=?, precio_total=?, pago_confirmado=1
        WHERE id=?
    ''', (egreso, tiempo_total, precio_total, vehiculo_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Pago registrado.", "precio_total": precio_total})

@app.route("/exportar/<tipo>", methods=["GET"])
def exportar(tipo):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vehiculos")
    rows = cursor.fetchall()
    conn.close()

    if tipo == "excel":
        wb = Workbook()
        ws = wb.active
        ws.append(["ID", "Patente", "Sector", "Ingreso", "Egreso", "Tiempo Estimado", "Tiempo Total", "Precio Hora", "Precio Total", "Pagó"])
        for row in rows:
            # transformar pago_confirmado de 0/1 a "Sí"/"No"
            r = list(row)
            r[-1] = "Sí" if r[-1] else "No"
            ws.append(r)
        output = io.BytesIO()
        wb.save(output)
        output.seek(0)
        return send_file(output, download_name="registro_estacionamiento.xlsx", as_attachment=True)

    elif tipo == "csv":
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["ID", "Patente", "Sector", "Ingreso", "Egreso", "Tiempo Estimado", "Tiempo Total", "Precio Hora", "Precio Total", "Pagó"])
        for row in rows:
            r = list(row)
            r[-1] = "Sí" if r[-1] else "No"
            writer.writerow(r)
        output.seek(0)
        return send_file(io.BytesIO(output.getvalue().encode()), mimetype='text/csv', download_name="registro_estacionamiento.csv", as_attachment=True)

    else:
        return jsonify({"error": "Tipo de archivo no soportado."}), 400

if __name__ == "__main__":
    app.run(debug=True)
