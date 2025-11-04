# Entorno Profesional en Python - Parte 7

## Análisis de Datos y Visualización con Gráficos

En esta sección, el objetivo fue leer, procesar y visualizar datos de un archivo CSV que contiene información sobre la población mundial.
* Lectura y Filtrado de Datos: 
Se utilizó Python para leer un archivo data.csv. Se implementaron filtros para aislar datos específicos, como los países pertenecientes a un continente en particular (África y Sudamérica).
* Generación de Gráficos:
* - Se crearon gráficos de pastel (pie charts) para mostrar la distribución porcentual de la población entre los países de un continente.
* - Se generaron gráficos de barras para visualizar la evolución de la población de un país específico a lo largo del tiempo.

* Resolución de Errores: 
Durante el proceso, se solucionó un error en el código que impedía la correcta generación de los gráficos. El problema se resolvió reubicando la línea de código ```charts.generate_pie_chart()``` para que se ejecutara en el momento adecuado.

* Uso de Librerías: 
Para estas tareas se utilizaron librerías como pandas para la manipulación de datos y matplotlib para la creación de las visualizaciones.

## Python para Backend: Web Server con FastAPI
Se avanza con Python para el backend, construyendo un servidor web propio utilizando el ecosistema de Python.

* Herramientas Utilizadas:
 - FastAPI: Un framework de Python para crear aplicaciones web y APIs de forma rápida y segura. Se destaca por su alto rendimiento y su capacidad para generar documentación automática.
* - Uvicorn: Un servidor ASGI (Asynchronous Server Gateway Interface) de alto rendimiento, utilizado para ejecutar aplicaciones como las creadas con FastAPI.
* Proceso:
* 1. Se instala FastAPI y Uvicorn.
* 2. Se crea una instancia de la aplicación FastAPI.
Se definen las rutas (endpoints) de la API usando decoradores. Por ejemplo, una ruta principal (/) y una ruta de contacto (/contact).
Cada ruta devuelve una respuesta, que puede ser una lista, un diccionario (JSON) o incluso contenido HTML.
Se utiliza HTMLResponse para devolver páginas web dinámicas.
El servidor se ejecuta con Uvicorn, que recarga automáticamente los cambios en el código (--reload), facilitando el desarrollo.
Dockerización de Aplicaciones Python
El enfoque fue empaquetar las aplicaciones de Python en contenedores de Docker, creando entornos aislados y portables. Esto permite ejecutar aplicaciones con scripts y también dockerizar un servidor web.
Configuración del Entorno Docker:
Se solucionó un error inicial activando la integración de Docker con WSL 2 (Windows Subsystem for Linux) en la configuración de Docker Desktop.
Se corrigió un problema de permisos que impedía la conexión con el Docker daemon, ejecutando los comandos con sudo.
Creación de Archivos Docker:
Dockerfile: Se definió la imagen del contenedor, especificando la versión de Python (ej. FROM python:3.10), el directorio de trabajo (WORKDIR /app), la copia de los archivos necesarios (COPY), y la instalación de las dependencias (RUN pip install -r requirements.txt).
docker-compose.yml: Se orquestó el servicio, indicando cómo construir la imagen a partir del Dockerfile y mapeando los puertos (ej. 80:80) para que el servidor web sea accesible.
Automatización y Desarrollo: Se utilizó la vinculación de archivos (volúmenes) para que los cambios en el código local se reflejen en tiempo real dentro del contenedor. Este truco mejora la experiencia de desarrollo, ya que no es necesario reconstruir la imagen con cada cambio.
Ejecución del Contenedor: Se construyó y ejecutó el contenedor con los comandos docker-compose build y docker-compose up -d. Finalmente, se verificó que el servicio web estaba activo y respondiendo a las peticiones en localhost