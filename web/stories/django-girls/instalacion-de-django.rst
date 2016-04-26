Instalación de Django
+++++++++++++++++++++

  Parte de esta sección se basa en tutoriales de Geek Girls Carrots
  (http://django.carrots.pl/).

  Parte de este capítulo se basa en el `django-marcador tutorial
  <http://django-marcador.keimlink.de/>`__ bajo licencia Creative
  Commons Attribution-ShareAlike 4.0 internacional. El tutorial de
  django-marcador tiene derechos de autor de Markus Zapke-Gündemann
  et al.

.. admonition:: Nota

   Si ya has realizado los pasos de instalación, esto ya lo
   has hecho. ¡Puedes avanzar directamente al siguiente capítulo!


   
Entorno virtual
===============

Antes de instalar Django, instalaremos una herramienta extremadamente
útil que ayudará a mantener tu entorno de desarrollo ordenado en tu
computadora. Es posible saltarse este paso, pero es altamente
recomendable. ¡Empezar con la mejor configuración posible te ahorrará
muchos problemas en el futuro!

Así que, vamos a crear un **entorno virtual** (también llamado un
*virtualenv*). Virtualenv aísla tu configuración de Python/Django por
cada proyecto. Esto quiere decir que cualquier cambio que hagas en un
sitio web no afectará a ningún otro que estés desarrollando. Genial,
¿no?

Todo lo que necesitas hacer es encontrar un directorio en el que quieras
crear el ``virtualenv``; tu directorio home, por ejemplo. En Windows
puede verse como ``C:\Users\Name`` (donde ``Name`` es el nombre de tu
usuario).

Para este tutorial usaremos un nuevo directorio ``djangogirls`` en tu
directorio home:

::

    $ mkdir djangogirls
    $ cd djangogirls

Haremos un virtualenv llamado ``myvenv``. El comando general estará en
el formato:

::

    $ python3 -m venv myvenv

Windows
-------

Para crear un nuevo ``virtualenv``, debes abrir la consola (te lo
indicamos unos cuantos capítulos antes, ¿recuerdas?) y ejecuta
``C:\Python34\python -m venv myvenv``. Se verá así:

::

    C:\Users\Name\djangogirls> C:\Python34\python -m venv myvenv

en donde ``C:\Python34\python`` es el directorio en el que instalaste
Python previamente y ``myvenv`` es el nombre de tu ``virtualenv``.
Puedes utilizar cualquier otro nombre, pero asegúrate de usar minúsculas
y no dejar espacios, acentos o caracteres especiales. También es una
buena idea mantener el nombre corto. ¡Vas a referirte a él mucho!

Linux y OS X
------------

Crear un ``virtualenv`` en Linux y OS X es tan simple como ejecutar
``python3 -m venv myvenv``. Se verá así:

::

    $ python3 -m venv myvenv

``myvenv`` es el nombre de tu ``virtualenv``. Puedes usar cualquier otro
nombre, pero mantén el uso de minúsculas y no incluyas espacios. También
es buena idea mantener el nombre corto. ¡Vas a referirte muchas veces a
él!

.. admonition:: Nota

   En algunas version de Debian/Ubuntu quizás recibas el
   siguiente error:

   ::

      The virtual environment was not created successfully because ensurepip is not available.  On Debian/Ubuntu systems, you need to install the python3-venv package using the following command.
        apt-get install python3-venv
      You may need to use sudo with that command.  After installing the python3-venv package, recreate your virtual environment.

   En este caso, sigue las instrucciones de arriba e installa el
   paquete ``python3-venv`` así:

   ::

      $ sudo apt-get install python3-venv

.. admonition:: Nota
      
   Actualmente, iniciar el entorno virtual en Ubuntu 14.04 de
   esta manera produce el siguiente error:

   ::

      Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1

   Para resolver esto, utiliza el comando ``virtualenv`` en cambio.

   ::

      $ sudo apt-get install python-virtualenv
      $ virtualenv --python=python3.4 myvenv

Trabajar con virtualenv
=======================

Este comando anterior creará un directorio llamado ``myvenv`` (o
cualquier nombre que hayas escogido) que contiene nuestro entorno
virtual (básicamente un montón de archivos y carpetas).

Windows
-------

Inicia el entorno virtual ejecutando:

::

    C:\Users\Name\djangogirls> myvenv\Scripts\activate

Linux y OS X
------------

Inicia el entorno virtual ejecutando:

::

    $ source myvenv/bin/activate

¡Recuerda reemplazar ``myvenv`` con tu nombre de ``virtualenv`` que
hayas elegido!

.. admonition:: Nota

   a veces ``source`` podría no estar disponible. En ese caso
   trata hacerlo de esta forma:

   ::

      $ . myvenv/bin/activate

Sabrás que tienes ``virtualenv`` iniciado cuando veas que aparece este
este prefijo en el prompt de la consola ``(myvenv)``.

Cuando trabajes en un entorno virtual, ``python`` automáticamente se
referirá a la versión correcta, de modo que puedes utilizar ``python``
en vez de ``python3``.

Tenemos todas las dependencias importantes en su lugar. ¡Finalmente
podemos instalar Django!

Instalar Django
===============

Ahora que tienes tu ``virtualenv`` iniciado, puedes instalar Django
usando ``pip``. En la consola, ejecuta ``pip install django~=1.9``
(fíjate que utilizamos una tilde (signo de la ñ) y el signo igual:
``~=``).

::

    (myvenv) ~$ pip install django~=1.9.0
    Downloading/unpacking django==1.9
    Installing collected packages: django
    Successfully installed django
    Cleaning up...

En Windows

Si obtienes un error al ejecutar pip en Windows comprueba si la ruta
de tu proyecto contiene espacios, acentos o caracteres especiales (por
ejemplo, ``C:\Users\Nombre de Usuario\djangogirls``). Si lo tiene, por
favor considera usar otro lugar sin espacios, acentos o caracteres
especiales (sugerencia: ``C:\djangogirls``). Crea un nuevo entorno
virtual en este nuevo directorio, luego borra el viejo e intenta
ejecutar nuevamente el comando (mover el directorio del entorno no
funcionará debido a que virtualenv utiliza path absolutos).

en Windows 8 y Windows 10

Tu línea de comandos quizás se congele luego de intentar instalar
Django. Si esto sucede, en vez del comando anterior, prueba este:

::

   C:\Users\Name\djangogirls> python -m pip install django~=1.9.0

en Linux

Si obtienes un error al correr pip en Ubuntu 12.04 ejecuta ``python -m
pip install- U - force-resintall pip`` para arreglar la instalación de
pip en el virtualenv.

¡Eso es todo! ¡Ahora estás lista (por fin) para crear una aplicación
Django!

