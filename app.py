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
        # Crear una respuesta con la imagen y el título
        return send_file(image_data, mimetype='image/jpeg', as_attachment=True, attachment_filename='imagen_gato.jpg', add_etags=False, cache_timeout=0), "IMAGEN DE GATO RECIBIDA: "
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500


# Endpoint de ejemplo para devolver un valor X
@app.route('/example', methods=['GET'])
def example_endpoint():
    data = {'message': 'Este es un valor de ejemplo'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
