from flask import Flask, render_template, request, jsonify
from tinydb import TinyDB, where
import datetime

app = Flask(__name__)
db = TinyDB('db.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alta', methods=['POST'])
def alta():
    data = request.get_json()
    patente = data['patente']
    ingreso = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.insert({'patente': patente, 'ingreso': ingreso, 'pagado': False})
    return jsonify({'message': 'Patente agregada correctamente'}), 200

@app.route('/listar', methods=['GET'])
def listar():
    registros = db.all()
    return jsonify(registros), 200

@app.route('/actualizar', methods=['POST'])
def actualizar():
    data = request.get_json()
    patente_original = data['patente_original']
    patente_nueva = data['patente_nueva']

    db.update({'patente': patente_nueva}, (where('patente') == patente_original) & (where('pagado') == False))
    return jsonify({'message': 'Patente actualizada correctamente'}), 200

@app.route('/eliminar', methods=['POST'])
def eliminar():
    data = request.get_json()
    patente = data['patente']
    db.remove(where('patente') == patente)
    return jsonify({'message': 'Patente eliminada correctamente'}), 200

@app.route('/cobrar', methods=['POST'])
def cobrar():
    data = request.get_json()
    patente = data['patente']
    precio_hora = float(data['precio_hora'])

    registro = db.get(where('patente') == patente)
    if registro and not registro['pagado']:
        ingreso_time = datetime.datetime.strptime(registro['ingreso'], "%Y-%m-%d %H:%M:%S")
        ahora = datetime.datetime.now()
        tiempo_total = ahora - ingreso_time
        horas = max(1, int(tiempo_total.total_seconds() // 3600))
        monto_total = horas * precio_hora

        db.update({'pagado': True}, where('patente') == patente)

        return jsonify({'monto_total': monto_total}), 200
    else:
        return jsonify({'message': 'Patente no encontrada o ya cobrada'}), 400

if __name__ == '__main__':
    app.run(debug=True)
