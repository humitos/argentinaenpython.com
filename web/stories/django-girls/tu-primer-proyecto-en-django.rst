¡Tu primer proyecto en Django!
++++++++++++++++++++++++++++++

    Parte de este capitulo esta basado en los tutoriales de Geek Girls
    Carrots (http://django.carrots.pl/).

    Parte de este capítulo se basa en el `django-marcador
    tutorial <http://django-marcador.keimlink.de/>`__ bajo licencia de
    Creative Commons Attribution-ShareAlike 4.0 internacional. El
    tutorial de django-marcador tiene derechos de autor de Markus
    Zapke-Gündemann et al.

¡Vamos a crear un blog sencillo!

El primer paso es iniciar un nuevo proyecto de Django. Básicamente,
significa que vamos a lanzar unos scripts proporcionados por Django que
nos crearán el esqueleto de un proyecto de Django. Son solo un montón de
directorios y archivos que usaremos más tarde.

Los nombres de algunos archivos y directorios son muy importantes para
Django. No deberías renombrar los archivos que estamos a punto de crear.
Moverlos a un lugar diferente tampoco es buena idea. Django necesita
mantener una cierta estructura para poder encontrar cosas importantes.}

    Recuerda ejecutar todo en el virtualenv. Si no ves un prefijo
    ``(myvenv)`` en tu consola necesitas activar tu virtualenv.
    Explicamos cómo hacerlo en el capítulo de **Instalación de Django**
    en la sección **Trabajar con virtualenv**. Basta con escribir
    ``myvenv\Scripts\activate`` en Windows o
    ``source myvenv/bin/activate`` en Mac OS / Linux.

En MacOS o Linux deberías ejecutar el siguiente comando en la consola;
**no te olvides de añadir el punto ``.`` al final**:

::

    (myvenv) ~/djangogirls$ django-admin startproject mysite .

En Windows; **no te olvides de añadir el punto ``.`` al final**:

::

    (myvenv) C:\Users\Name\djangogirls> django-admin startproject mysite .

    El punto ``.`` es crucial porque le dice al script que instale
    Django en el directorio actual (para el cual el punto ``.`` sirve de
    abreviatura)

.. admonition:: Nota

   Cuando escribas los comandos de arriba acuérdate de que sólo tienes
   que escribir la parte que empieza por ``django-admin`` o
   ``django-admin.py``. Las partes de ``(myvenv) ~/djangogirls$`` y
   ``(myvenv) C:\Users\Name\djangogirls>`` que mostramos aquí son sólo
   ejemplos del mensaje que aparecerá en tu línea de comandos.

``django-admin.py`` es un script que creará los archivos y directorios
para ti. Ahora deberías tener una estructura de directorios parecida a
esto:

::

    djangogirls
    ├───manage.py
    └───mysite
            settings.py
            urls.py
            wsgi.py
            __init__.py

``manage.py`` es un script que ayuda con la administración del sitio.
Con él podremos iniciar un servidor web en nuestro ordenador sin
necesidad de instalar nada más, entre otras cosas.

El archivo ``settings.py`` contiene la configuración de tu sitio web.

¿Recuerdas cuando hablamos de una cartera que debía comprobar dónde
entregar una carta? El archivo ``urls.py`` contiene una lista de los
patrones utilizados por ``urlresolver``.

Por ahora vamos a ignorar el resto de ficheros porque no los vamos a
cambiar. ¡Sólo acuérdate de no borrarlos accidentalmente!

Cambiar la configuración
========================

Vamos a hacer algunos cambios en ``mysite/settings.py``. Abre el archivo
usando el editor de código que has instalado anteriormente.

Sería bueno tener el horario correcto en nuestro sitio web. Ve a la
`lista de husos horarios de
Wikipedia <http://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__
y copia tu zona horaria (TZ). (por ejemplo, ``Europe/Berlin`` )

En settings.py, encuentra la línea que contiene ``TIME_ZONE`` y
modifícala para elegir tu propia zona horaria:

.. code:: python

    TIME_ZONE = 'Europe/Berlin'

Modificando "Europe/Berlin" como corresponda

También necesitaremos agregar una ruta para los archivos estáticos
(aprenderemos todo sobre los archivos estáticos y CSS más tarde en este
tutorial). Ve hacia abajo hasta el *final* del archivo, y justo por
debajo de la entrada ``STATIC_URL``, agrega una nueva llamada
``STATIC_ROOT``:

.. code:: python

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

Configurar una base de datos
============================

Hay una gran variedad de opciones de bases de datos para almacenar los
datos de tu sitio. Utilizaremos el que viene por defecto, ``sqlite3``.

Este ya está configurado en esta parte de tu archivo
``mysite/settings.py``:

.. code:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

Para crear una base de datos para nuestro blog, ejecutemos lo siguiente
en la consola: ``python manage.py migrate`` (necesitamos estar en el
directorio de ``djangogirls`` que contiene el archivo ``manage.py``). Si
eso va bien, deberías ver algo así:

::

    (myvenv) ~/djangogirls$ python manage.py migrate
    Operations to perform:
      Apply all migrations: auth, admin, contenttypes, sessions
    Running migrations:
      Rendering model states... DONE
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying sessions.0001_initial... OK

Y, ¡terminamos! Es hora de iniciar el servidor web y ver si está
funcionando nuestro sitio web!

Debes estar en el directorio que contiene el archivo ``manage.py`` (en
la carpeta ``djangogirls``). En la consola, podemos iniciar el servidor
web ejecutando ``python manage.py runserver``:

::

    (myvenv) ~/djangogirls$ python manage.py runserver

Si estás en Windows y te falla con un error ``UnicodeDecodeError``,
utiliza en su lugar este comando:

::

    (myvenv) ~/djangogirls$ python manage.py runserver 0:8000

Ahora todo lo que necesitas hacer es comprobar que tu sitio se esté
ejecutando. Abre el navegador (Firefox, Chrome, Safari, Internet
Explorer o el que utilices) y escribe la dirección:

::

    http://127.0.0.1:8000/

El servidor web tomará el control de la línea de comandos hasta que tú
lo pares. Para escribir más comandos mientras está funcionando, abre una
nueva consola y activa el virtualenv. Para parar el servidor web, pasa a
la ventana donde se esté ejecutando y pulsa CTRL+C, las teclas Control y
C a la vez ( en Windows puede que tengas que pulsar Ctrl+Pausa).

¡Enhorabuena! ¡Has creado tu primer sitio web y lo has iniciado usando
un servidor web! ¿No es genial?

.. figure:: it_worked2.png
   :alt: ¡Funcionó!

   ¡Funcionó!

¿Preparada para el próximo paso? ¡Es momento de crear algo de contenido!

