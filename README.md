# Descripcion

En primera instancia, se desarrolló el servicio backend utilizando Python y Flask. Los endpoints implementados son "/random-cat" para visualizar imágenes de gatos y "/example" para pruebas. Posteriormente, se configuró un pipeline para subir la imagen a Docker Hub y, adicionalmente, subir automáticamente cualquier modificación realizada en el repositorio a Docker Hub.

# Instrucciones

Se deben utilizar 2 comandos claves para ejecutar el servicio, como primer paso se hace pull de la ultima version de la imagen mediante:**"docker pull edjaramillo/flask-cat-app:latest"**

 Despues se corre dicha imagen en un contenedor para poder visualizar los endpoint correctamente de manera local con el siguiente comando: **"docker run -d -p 5000:5000 edjaramillo/flask-cat-app:latest"**
