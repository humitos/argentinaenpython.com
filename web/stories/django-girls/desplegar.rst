¡Desplegar!
+++++++++++

.. admonition:: Nota

   El siguiente capítulo puede ser, a veces, un poco difícil de
   seguir. Se persistente y acábalo. El despliegue es una parte
   importante del proceso en el desarrollo web. Este capítulo está
   situado en el medio del tutorial para que tu tutora o tutor pueda
   ayudarte a poner tu sitio web en línea, lo que puede ser un proceso
   algo más complicado. Esto significa que podrás acabar el tutorial
   por tu cuenta si se te acaba el tiempo.

Hasta ahora tu sitio web estaba disponible sólo en tu ordenador, ¡ahora
aprenderás cómo desplegarlo! El despliegue es el proceso de publicar tu
aplicación en internet para que la gente pueda acceder y ver tu
aplicación :).

Como ya has aprendido, un sitio web tiene que estar en un servidor. Hay
muchos proveedores de servidores disponibles en Internet. Vamos a
utilizar uno que tiene un proceso de despliegue relativamente sencillo:
`PythonAnywhere <http://pythonanywhere.com/>`__. PythonAnywhere es
gratis para pequeñas aplicaciones que no tienen demasiados visitantes,
definitivamente suficiente para este caso.

El otro servicio externo que vamos a utilizar es
`GitHub <http://www.github.com>`__, un servicio de alojamiento de
código. Hay otras opciones por ahí, pero hoy en día casi todas las
programadoras y programadores tienen una cuenta de GitHub, ¡y ahora tú
también la vas a tener!

Usaremos GitHub como paso intermedio para transportar nuestro código
desde y hasta PythonAnywhere.

Git
===

Git es un "sistema de control de versiones" que utilizan muchas
programadoras y programadores. Este software puede rastrear los cambios
realizados en archivos a lo largo del tiempo de forma que puedas
recuperar una versión específica más tarde. Es un poco parecido a la
opción de "control de cambios" de Microsoft Word, pero mucho más
potente.

Instalar Git
------------

.. admonition:: Nota

   Si ya has hecho los pasos de instalación, no hace falta que hagas
   esto otra vez. Puedes avanzar a la siguiente sección y empezar a
   crear tu repositorio Git.

Windows
~~~~~~~

Puedes descargar Git de `git-scm.com <http://git-scm.com/>`__. Puedes
hacer clic en "Next" para todos los pasos excepto en uno; en el quinto
paso titulado "Adjusting your PATH environment", elije "Run Git and
associated Unix tools from the Windows command-line" (la última opción).
Aparte de eso, los valores por defecto funcionarán bien. "Checkout
Windows-style, commit Unix-style line endings" también está bien.

MacOS
~~~~~

Descarga Git de `git-scm.com <http://git-scm.com/>`__ y sigue las
instrucciones.

Linux
~~~~~

Si no lo tienes ya instalado, git debería estar disponible a través del
administrador de paquetes, prueba con:

Debian or Ubuntu
^^^^^^^^^^^^^^^^

::

    $ sudo apt-get install git

Fedora (up to 21)
^^^^^^^^^^^^^^^^^

::

    $ sudo yum install git

Fedora (22+)
^^^^^^^^^^^^

::

    $ sudo dnf install git

Es hora de registrar una cuenta gratuita de tipo "Beginner" en
PythonAnywhere.

-  `www.pythonanywhere.com <https://www.pythonanywhere.com/>`__

.. admonition:: Nota
   
   Cuando elijas tu nombre de usuario ten en cuenta que la URL de tu
   blog tendrá la forma ``nombredeusuario.pythonanywhere.com``, así
   que o bien elije tu propio apodo o bien un nombre que describa
   sobre qué trata tu blog.

Iniciar nuestro repositorio Git
-------------------------------

Git rastrea los cambios realizados a un grupo determinado de archivos en
lo que llamamos un repositorio de código (abreviado "repo"). Iniciemos
uno para nuestro proyecto. Abre la consola y ejecuta los siguientes
comandos en el directorio de ``djangogirls``:

.. admonition:: Nota

   Comprueba el directorio de trabajo actual con el comando ``pwd``
   (OSX/Linux) o ``cd`` (Windows) antes de inicializar el
   repositorio. Deberías estar en la carpeta ``djangogirls``.

::

    $ git init
    Initialized empty Git repository in ~/djangogirls/.git/
    $ git config --global user.name "Tu nombre"
    $ git config --global user.email tu@ejemplo.com

Inicializar el repositorio git es algo que sólo necesitamos hacer una
vez por proyecto (y no tendrás que volver a poner tu usuario y correo
electrónico nunca más).

Git llevará un registro de los cambios realizados en todos los archivos
y carpetas en este directorio, pero hay algunos archivos que queremos
que ignore. Esto lo hacemos creando un archivo llamado ``.gitignore`` en
el directorio base. Abre tu editor y crea un nuevo archivo con el
siguiente contenido:

::

    *.pyc
    __pycache__
    myvenv
    db.sqlite3
    /static
    .DS_Store

Y guárdalo como ``.gitignore`` en la primera carpeta "djangogirls".

.. admonition:: Nota

   ¡El punto al principio del nombre del archivo es importante! Si
   tienes dificultades para crearlo (a los Mac no les gusta que crees
   archivos que empiezan por punto desde Finder, por ejemplo), usa la
   opción "Guardar como" en tu editor, eso no falla.

.. admonition:: Nota
   
   Uno de los archivos que agregaste a tu ``.gitignore`` es el archivo
   ``db.sqlite3``. Este archivo es tu base de datos local, donde todos
   los artículos de blog son guardados. No queremos agregar esto a tu
   repositorio porque tu sitio web en PythonAnywhere usará una base de
   datos diferente. Esa base de datos puede ser SQLite, como en tu
   máquina de desarrollo, pero usualmente usarás una llamada MySQL que
   puede manejar mucho más visitantes a tu sitio que SQLite.  De
   cualquier manera, ignorar tu base de datos SQLite en la copia de
   GitHub significa que todos los artículos de blog que crees van a
   estar disponibles solo localmente y tendrás que agregarlos
   nuevamente en producción. Debes pensar en tu base de datos local
   como un lugar donde puedes jugar y probar diferentes cosas sin
   tener miedo de que vas a borrar los verdaderos artículos de blog de
   sitio web.

Es buena idea utilizar el comando ``git status`` antes de ``git add`` o
en cualquier momento en que no estés segura de lo que ha cambiado. Esto
ayudará a evitar sorpresas como agregar o hacer commit de los archivos
equivocados. El comando ``git status`` devuelve información sobre los
archivos sin seguimiento (untracked), modificados, preparados (staged),
el estado de la rama y mucho más. La salida debería ser similar a:

::

    $ git status
    On branch master

    Initial commit

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

            .gitignore
            blog/
            manage.py
            mysite/

    nothing added to commit but untracked files present (use "git add" to track)

Y finalmente guardamos nuestros cambios. Ve a tu consola y ejecuta estos
comandos:

::

    $ git add --all .
    $ git commit -m "Mi app Django Girls, primer commit"
     [...]
     13 files changed, 200 insertions(+)
     create mode 100644 .gitignore
     [...]
     create mode 100644 mysite/wsgi.py

Enviar nuestro código a GitHub
------------------------------

Ve a `GitHub.com <http://www.github.com>`__ y registra una nueva cuenta
gratuita. (Si ya lo hiciste en la preparación del taller, ¡genial!)

Luego, crea un nuevo repositorio con el nombre "mi-primer-blog". Deja
desmarcada la opción "Initialise with a README", deja la opción
.gitignore en blanco (lo hemos hecho a mano) y deja la licencia como
"None".

.. admonition:: Nota

   El nombre ``mi-primer-blog`` es importante. Podrías elegir otra
   cosa, pero va a aparecer muchas veces en las instrucciones que
   siguen y tendrías que sustituirlo cada vez. Probablemente sea más
   sencillo quedarte con el nombre ``mi-primer-blog``.

En la próxima pantalla verás la URL para clonar tu repositorio. Elige la
versión "HTTPS", cópiala y en un momento la pegaremos en la consola:

Ahora tenemos que conectar el repositorio Git de tu ordenador con el que
está en GitHub.

Escribe lo siguiente en la consola (sustituye ``<tu-usuario-github>``
por el nombre de usuario que elegiste al crear tu cuenta de GitHub, pero
sin los signos de mayor y menor):

::

    $ git remote add origin https://github.com/<tu-usuario-github>/mi-primer-blog.git
    $ git push -u origin master

Escribe tu nombre de usuario y contraseña de GitHub y deberías ver algo
así:

::

    Username for 'https://github.com': hjwp
    Password for 'https://hjwp@github.com':
    Counting objects: 6, done.
    Writing objects: 100% (6/6), 200 bytes | 0 bytes/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/hjwp/mi-primer-blog.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.

.. raw:: html

   <!--TODO: maybe do ssh keys installs in install party, and point ppl who dont have it to an extention -->

Tu código está ahora en GitHub. ¡Ve y míralo! Verás que está en buena
compañía; `Django <https://github.com/django/django>`__, el `Tutorial de
Django Girls <https://github.com/DjangoGirls/tutorial>`__ y muchos otros
grandes proyectos de código abierto también alojan su código en GitHub
:)

Configurar nuestro blog en PythonAnywhere
=========================================

.. admonition:: Nota

   Puede que ya hayas creado una cuenta en PythonAnywhere
   durante los paso de instalación. Si es así, no necesitas hacerlo de
   nuevo.

Es hora de registrar una cuenta gratuita de tipo "Beginner" en
PythonAnywhere.

-  `www.pythonanywhere.com <https://www.pythonanywhere.com/>`__

.. admonition:: Nota

   Cuando elijas tu nombre de usuario ten en cuenta que la URL de tu
   blog tendrá la forma ``nombredeusuario.pythonanywhere.com``, así
   que o bien elije tu propio apodo o bien un nombre que describa
   sobre qué trata tu blog.

Cargar nuestro código en PythonAnywhere
---------------------------------------

Cuando te hayas registrado en PythonAnywhere serás redirigida a tu panel
de control o página "Consoles". Elije la opción para iniciar una consola
"Bash". Es la versión PythonAnywhere de una consola, como la que tienes
en tu PC.

.. admonition:: Nota

   PythonAnywhere está basado en Linux, por lo que si estás en Windows
   la consola será un poco distinta a la que tienes en tu ordenador.

Vamos a bajar nuestro código de GitHub a PythonAnywhere mediante la
creación de un "clon" del repositorio. Escribe lo siguiente en la
consola de PythonAnywhere (no te olvides de utilizar tu nombre de
usuario de GitHub en lugar de ``<tu-usuario-github>``):

::

    $ git clone https://github.com/<tu-usuario-github>/mi-primer-blog.git

Esto va a descargar una copia de tu código en PythonAnywhere.
Compruébalo escribiendo ``tree mi-primer-blog``:

::

    $ tree mi-primer-blog
    mi-primer-blog/
    ├── blog
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

Crear un virtualenv (o entorno virtual) en PythonAnywhere
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tal y como hiciste en tu propio ordenador, puedes crear un virtualenv en
PythonAnywhere. En la consola Bash, escribe:

::

    $ cd mi-primer-blog

    $ virtualenv --python=python3.4 myvenv
    Running virtualenv with interpreter /usr/bin/python3.4
    [...]
    Installing setuptools, pip...done.

    $ source myvenv/bin/activate

    (myvenv) $  pip install django~=1.9.0
    Collecting django
    [...]
    Successfully installed django-1.9


.. admonition:: Nota

   El paso ``pip install`` puede llevar un par de minutos.
   ¡Paciencia, paciencia! Pero si tarda más de 5 minutos, algo va mal.
   Pregunta a tu tutora o tutor.


Crear la base de datos en PythonAnywhere
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aquí hay otra cosa que es diferente entre tu computadora y el servidor:
éste utiliza una base de datos diferente. Por lo tanto, las cuentas de
usuario y las entradas pueden ser diferentes en el servidor y en tu
computadora.

Podemos inicializar la base de datos en el servidor igual que lo hicimos
en nuestra computadora, con ``migrate`` y ``createsuperuser``:

::

    (myvenv) $ python manage.py migrate
    Operations to perform:
    [...]
      Applying sessions.0001_initial... OK


    (myvenv) $ python manage.py createsuperuser

Publicar nuestro blog como una aplicación web
---------------------------------------------

Ahora nuestro código está en PythonAnywhere, el virtualenv está listo,
los archivos estáticos han sido recopilados y la base de datos está
inicializada. ¡Estamos listas para publicarla como una aplicación web!

Haz clic en el logo de PythonAnywhere para volver al panel principal y
haz clic en la pestaña **Web**. Por último, pincha en **Add a new web
app**.

Después de confirmar tu nombre de dominio, elige **manual
configuration** o "configuración manual" (NB la opción "Django" *no*) en
el diálogo. Luego elige **Python 3.4** y haz clic en "Next" para
terminar con el asistente.

.. admonition:: Nota

   Asegúrate de elegir la opción de "Manual configuration", no la de
   "Django". Somos demasiado buenas para la configuración por defecto
   de Django de PythonAnywhere ;-)

Configurar el virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~

Serás redirigida a la pantalla de configuración de PythonAnywhere para
tu aplicación web, a la que deberás acceder cada vez que quieras hacer
cambios en la aplicación del servidor.

En la sección "Virtualenv", haz clic en el texto rojo que dice "Enter
the path to a virtualenv" ("Introduce la ruta a un virtualenv") y
escribe: ``/home/<tu-usuario>/mi-primer-blog/myvenv/``. Haz clic en el
cuadro azul seleccionado para guardar la ruta antes de continuar.


.. admonition:: Nota
   
   Sustituye tu propio nombre de usuario como corresponda. Si cometes
   un error, PythonAnywhere te mostrará una pequeña advertencia.

Configurar el archivo WSGI
~~~~~~~~~~~~~~~~~~~~~~~~~~

Django funciona utilizando el "protocolo WSGI", un estándar para servir
sitios web que usan Python, que PythonAnywhere soporta. La forma de
configurar PythonAnywhere para que reconozca nuestro blog Django es
editar un archivo de configuración WSGI.

Haz clic en el enlace "WSGI configuration file" (en la sección "Code" en
la parte de arriba de la página; se llamará algo parecido a
``/var/www/<tu-usuario>_pythonanywhere_com_wsgi.py``) y te redirigirá al
editor.

Borra todo el contenido y reemplázalo con algo como esto:

.. code:: python

    import os
    import sys

    path = '/home/<tu_nombre_de_usuario>/mi-primer-blog/mysite'  # use your own username here
    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

    from django.core.wsgi import get_wsgi_application
    from django.contrib.staticfiles.handlers import StaticFilesHandler
    application = StaticFilesHandler(get_wsgi_application())


.. admonition:: Nota

   No olvides sustituir tu propio nombre de usuario donde pone
   ``<tu-usuario>``
		
.. admonition:: Nota
		   
   En la línea tres, nos estamos asegurando que PythonAnywhere sepa
   cómo encontrar nuestra aplicación. Es muy importante que el nombre
   de la ruta sea correcto y especialmente, que no haya espacios
   extras ahí. De otra forma verás un "ImportError" en registro de
   errores.

Este archivo se encarga de decirle a PythonAnywhere dónde vive nuestra
aplicación web y cómo se llama el archivo de configuración de Django.

La línea con ``StaticFilesHandler`` es para manejar nuestros CSS. De
esto se ocupa automáticamente el comando ``runserver`` durante el
desarrollo local. Encontrarás un poco más sobre archivos estáticos luego en
este tutorial, cuando edites los CSS de tu sitio.

Dale a **Save** y vuelve a la pestaña **Web**.

¡Todo listo! Dale al botón verde grande que dice **Reload** y podrás ver
tu aplicación. Verás un enlace a ella en la parte de arriba de la
página.

Consejos de depuración
----------------------

Si ves un error cuando intentas visitar tu página, el primer lugar donde
buscar información de depuración es el **registro de errores**.
Encontrarás un enlace a él en la `pestaña
Web <https://www.pythonanywhere.com/web_app_setup/>`__ de
PythonAnywhere. Mira a ver si hay algún mensaje de error ahí. Los más
recientes están al final. Los problemas más comunes incluyen:

-  Olvidar alguno de los pasos que hicimos en la consola: crear el
   virtualenv, activarlo, instalar Django en él, inicializar la base de
   datos.

-  Cometer un error en la ruta del virtualenv en la pestaña Web; suele
   haber un mensajito de error de color rojo, si hay algún problema.

-  Cometer un error en el archivo de configuración WSGI; ¿has puesto
   bien la ruta a la carpeta mi-primer-blog?

-  ¿Has elegido la misma versión de Python para el virtualenv y para la
   aplicación web? Ambas deberían ser 3.4.

-  Hay algunos `consejos generales de depuración en el wiki de
   Pythonanywhere <https://www.pythonanywhere.com/wiki/DebuggingImportError>`__

Y recuerda, ¡tu tutora está ahí para ayudarte!

¡Estás en vivo!
===============

La página predeterminada de tu sitio debería decir "Welcome to Django",
igual que en tu PC local. Intenta agregar ``/admin/`` al final de la URL
y te redirigirá al panel de administración. Ingresa con tu nombre de
usuario y contraseña y verás que puedes agregar nuevas entradas en el
servidor.

Una vez que hayas creado algunos artículos de blog, puedes volver a tu
instancia local (no la de PythonAnywhere). Desde ahí podrías trabajar en
tu instancia local para hacer algunos cambios. Estos son los pasos
comunes en el desarrollo web (hacer cambios locales, enviarlos a GitHub,
descargarlos en el servidor web). Esto te permite trabajar y
experimentar sin romper tu sitio web en vivo. Muy bueno, ¿no?

¡Date una *GRAN* palmada en la espalda! Los despliegues en el servidor
son una de las partes más complejas del desarrollo web y muchas veces a
la gente le cuesta varios días tenerlo funcionando. Pero tú tienes tu
sitio en vivo, en Internet de verdad, ¡así como suena!
