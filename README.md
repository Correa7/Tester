# Proyecto Final Comisión 31090 - Python
# Read Me

### Requerimientos

- Python 3.10.6
- Django 4.0.6
- Pillow  9.2.0

### Instalaciones

- pip install django
- pip install Pillow

### Paquetes instalados


-pip list:  

       asgiref          3.5.2
       certifi          2022.6.15
       distlib          0.3.5
       dj-database-url  1.0.0
       Django           4.0.6
       filelock         3.7.1
       gunicorn         20.1.0
       Pillow           9.2.0
       pipenv           2022.7.4
       platformdirs     2.5.2
       six              1.16.0
       sqlparse         0.4.2
       tzdata           2022.1
       virtualenv       20.15.1
       virtualenv-clone 0.5.7
       whitenoise       6.2.0 



### Proyecto


***Objetivos***

- Desarrollar una WEB Django con patrón MVT con una temática definida por el equipo de trabajo.
- Trabajar exitosamente y de forma coordinada en equipo bajo el entorno de GitHub.
- Aplicar los conocimientos aprendidos durante las clases en un sitio web completamente funcional


***Integrantes***

- Kedy Acuña
- César Damián Correa
- Augusto Römer


***Temática***

Página web para refugio de mascotas que permita interactuar con el usuario y agilizar proceso de adopción. 
También brindar difusión para que se incorporen perros y gatos al refugio, así como gestionar la recepción de donaciones.


**link del video de la presentacion**

https://youtu.be/ZJQNNjskmp8


***Contenido y funcionalidades***


Index:

       NavBar: 
              Secciones: INICIO, ABOUT, MASCOTAS,REFUGIOS, LOGUIN, REGISTER 
       NavBar (Usuario logueado):
              Secciones: INICIO,ABOUT,MASCOTAS,REFUGIOS,DONACIONES, USUARIO (CrearPerfil, Eliminar Usuario,logout).
       NavBar (Usuario con Permisos logueado):
              INICIO,ABOUT,MASCOTAS(cargar mascota),REFUGIOS   (cargar refugio),DONACIONES, USUARIO(Perfil, eliminar usuario,Logout).


Para acceder: 

- 1 A traves del Boton Register.
       - 1.1. Ingresar un nombre de usuario.
       - 1.2. Ingresar un correo electronico.
       - 1.3. Ingresar una contraseña.
       - 1.4. Repetir la misma contraseña.
       - 1.5.1 Ingresar en la administración de Django ingresando http://127.0.0.1:8000/admin/ en el navegador:
       - 1.5.2 ingresar con el usuario admin contraseña: 123.
       - 1.5.3 Ingresar en usuario buscar el usuario creado en el punto 1.1, en parte de permisos seleccionar el combo "Es staff"y presionar el botón guarda.
       - 1.5.4 Cerrar la sesión del admin.
       - 1.5.5 volver a la aplicación http://127.0.0.1:8000/ 
       - 1.5.6 seleccionar "Login".
       - 1.5.7 ingresar los datos del usuario del punt 1.

- 2 Una vez logueado acceder a crear perfil:

       - 2.1 completar los campos y podemos selecionar para subir una imagen.
       - 2.2 Una vez creado el perfil, En la seccion perfil se encontraran las opciones para  Editar el perfil. Ademas del boton de editiar Usuario.
       - 2.3 Ingresando en edicion, nos redirige a la pagina con el formulario con los datos para sobreescribirlos y/o eliminar.
       - 2.4 Una vez logueado tiene acceso a: la seccion Donaciones, Funcion Adopcion y Voluntario.

- 3 Módulo Mascotas:
       - 3.1.1 Vista de listado de mascotas cargadas.
       - 3.1.2 Herramienta de búsqueda de mascota por nombre.
       - 3.1.3 Vista de la ficha de la mascota buscada.
       - 3.1.4 Acceso al boton adopcion.
       - 3.2.1 Si el usuario tiene permisos, accede a la carga de una mascota, a su edicion y elminacion.
       - 3.2.2 Accediendo a Detalles, acceso a editar y eliminar ficha de la mascota mediante formulario.
       - 3.3.1 Acceso a  creacion, edicion , y eliminado de ficha veterinaria asociada a la mascota mediante formulario.
         
- 4 Módulo Refugios:
       - 4.1.1. Listas de refugios cargados buscado.
       - 4.1.2. Herramienta de búsqueda de refugio por nombre.
       - 4.1.3  Detalle de refugio, Ficha de refugio y Perfil de refugio.
       - 4.1.4  Acceso al boton Voluntario.
       - 4.2.1. Si el usuario tiene permisos: Acceso a carga de refugio mediante formulario.
       - 4.2.2 En detalle de refugio, Acceso a edicion y eliminacion de Ficha de refugio mediante formulario.
       - 4.2.3 En detalle de refugio, Acceso a Creacion, edicion y eliminacion de Perfil de refugio mediante formulario.

- 5 Seccion About:
       - 5.1.1 Sobre el Proyecto.
       - 5.1.2 El Equipo.
       - 5.1.3 Contactos.

- 6  Carrousel:
       - 6.1.1 Acceso a mascotas y Newsletter.
       - 6.1.2 Acceso a Voluntarios y Newsletter.
