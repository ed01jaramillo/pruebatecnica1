from flask import Flask, jsonify, send_file
import requests
from io import BytesIO

app = Flask(__name__)

# Endpoint para obtener una imagen aleatoria de un gato
@app.route('/random-cat', methods=['GET'])


def get_random_cat():
    try:
        response = requests.get('https://cataas.com/cat')
        response.raise_for_status()  # Verifica si hay errores en la solicitud HTTP
        image_data = BytesIO(response.content)
        return send_file(image_data, mimetype='image/jpeg')
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

# Endpoint de ejemplo para devolver un valor X
@app.route('/example', methods=['GET'])
def example_endpoint():
    data = {'message': 'Este es un ENDPOINT de ejemplo, si quieres ver fotos de GATOS dirigete al directorio "/random-cat" con la direccion local'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
