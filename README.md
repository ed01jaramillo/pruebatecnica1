# pruebatecnica1

En primera instancia se realizó el servicio backend utilizando python y flask asi mismo los endpoint utilizados en este caso son "/random-cat" para ver las imagenes de gatos y "/example" para pruebas, luego se configuró un pipeline para subir la imagen a Docker hub y adicionalmente subir automaticamente cualquier modificacion que se haga en el repositorio hacia Docker hub.

# Instrucciones

Se deben utilizar 2 comandos claves para ejecutar el servidor, como primer paso se hace pull de la ultima version de la imagen mediante:"docker pull edjaramillo/flask-cat-app:latest"

 Despues se corre dicha imagen en un contenedor para poder visualizar los endpoint correctamente de manera local con el siguiente comando: "docker run -d -p 5000:5000 edjaramillo/flask-cat-app:latest"
