Este proyecto trata de una CRUD de noticias con comentarios en una base de datos.

El proyecto está hecho con el framewrok Flask, usando la librería SQLAlchemy para la conexión con la base de datos SQLite.


Cuerpo del proyecto:
- clases
    - database.py
    - query.py
- Models
    - news.py
- utils
    - validators.py
- database.sb
- main.py
- README.md
- requirements.txt

La carpeta 'clases' contiene el archivo database.py y query.py que hace la conexión a la base de datos y las consultas, respectivamente.

La carpeta 'Models' tiene el archivo news.py que tiene la clase News y Comment que crean las tablas en la base de datos.

La carpeta 'utils' contiene el arcivo que valida los datos para poder crear, leer, actuaizar y eliminar una noticia.

En el archivo requirements.txt están las dependencias necesarias para el funcionamiento del proyecto.