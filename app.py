from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

# Ruta para obtener los datos del archivo JSON
@app.route('/poos', methods=['GET'])
def get_poos():
    try:
        # Cargar datos desde el archivo JSON
        data_path = os.path.join(os.path.dirname(__file__), 'data', 'poos.json')
        with open(data_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
