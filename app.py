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
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint de ejemplo con HTML creativo
@app.route('/example', methods=['GET'])
def example_endpoint():
    html_message = """
    <html>
        <head>
            <style>
                /* Estilos para el contenedor principal */
                .container {
                    background-color: #f0f0f0;
                    padding: 20px;
                    border-radius: 10px;
                }
                /* Estilos para el texto */
                p {
                    font-family: Arial, sans-serif;
                    font-size: 16px;
                    color: #333;
                }
                /* Estilos para la forma de burbuja */
                .bubble {
                    width: 250px;
                    height: 150px;
                    background-color: #fff;
                    border-radius: 50% 50% 0 50%;
                    position: relative;
                    margin: 20px auto;
                    border: 2px solid #333;
                }
                /* Estilos para la punta de la burbuja */
                .bubble::before {
                    content: '';
                    width: 40px;
                    height: 40px;
                    background-color: #fff;
                    position: absolute;
                    bottom: -20px;
                    right: -20px;
                    border-right: 2px solid #333;
                    border-bottom: 2px solid #333;
                    border-radius: 0 50% 0 0;
                    transform: rotate(45deg);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="bubble">
                    <p>¡Bienvenido a nuestro ejemplo!</p>
                </div>
                <p>Este es un ENDPOINT de ejemplo. Si deseas ver fotos de GATOS, dirígete al directorio "/random-cat".</p>
            </div>
        </body>
    </html>
    """
    return html_message

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
