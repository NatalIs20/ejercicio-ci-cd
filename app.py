from flask import Flask, render_template, jsonify
from trabajos import obtener_trabajos, obtener_trabajo_por_id

app = Flask(__name__)

@app.route('/')
def index():
    nombre = "Estudiante UTTT"
    return render_template('index.html', nombre=nombre)

@app.route('/api/status')
def status():
    return {"status": "ok", "entorno": "contenedor-docker", "version": "1.1.0"}

@app.route('/trabajos')
def trabajos():
    return jsonify(obtener_trabajos())

@app.route('/trabajos/<int:trabajo_id>')
def trabajo_detalle(trabajo_id):
    trabajo = obtener_trabajo_por_id(trabajo_id)
    if trabajo is None:
        return jsonify({"error": "Trabajo no encontrado"}), 404
    return jsonify(trabajo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)