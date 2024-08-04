# Descripcion - Prueba45

Primero, se desarrolló el servicio backend utilizando Python y Flask, implementando dos endpoints: "/random-cat" para visualizar imágenes de gatos y "/example" para pruebas. Luego, se configuró un pipeline para subir la imagen a Docker Hub y automatizar la actualización de cualquier modificación realizada en el repositorio. Además, se utilizaron variables de entorno secretas para almacenar las credenciales de usuario y contraseña de Docker Hub, mejorando así la seguridad en el código del pipeline.

# Instrucciones

Se deben utilizar 2 comandos claves en el terminal CMD para ejecutar el servicio, como primer paso se hace pull de la ultima version de la imagen mediante:**"docker pull edjaramillo/flask-cat-app:latest"**

 Despues se corre dicha imagen en un contenedor para poder visualizar los endpoint correctamente de manera local con el siguiente comando: **"docker run -d -p 5000:5000 edjaramillo/flask-cat-app:latest"**

Para poder ver las imagenes aleatorias de los gatos se debe ingresar a la siguiente direccion local como ejemplo: **http://localhost:5000/random-cat**

Cabe resaltar que se debe tener Docker Desktop descargado e instalado en el sistema.
