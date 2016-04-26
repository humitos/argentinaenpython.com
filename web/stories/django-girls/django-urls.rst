Django urls
+++++++++++

Estamos a punto de construir nuestra primera página web: ¡una página de
inicio para el blog! Pero primero, vamos a aprender un poco acerca de
las urls de Django.

¿Qué es una URL?
================

Una URL es simplemente una dirección web. Puedes ver una URL cada vez
que visitas una página, se ve en la barra de direcciones del navegador
(¡sí! ¡\ ``127.0.0.1:8000`` es una URL! Y ``https://djangogirls.com``
también es una URL):

.. figure:: url.png
   :alt: Url

   Url

Cada página en Internet necesita su propia URL. De esta manera tu
aplicación sabe lo que debe mostrar a un usuario que abre una URL. En
Django utilizamos lo que se llama ``URLconf`` (configuración de URL).
URLconf es un conjunto de patrones que Django intentará comparar con la
URL recibida para encontrar la vista correcta.

¿Cómo funcionan las URLs en Django?
===================================

Vamos a abrir el fichero ``mysite/urls.py`` en el editor de código de tu
elección y ver lo que tiene:

.. code:: python

    """mysite URL Configuration

    [...]
    """
    from django.conf.urls import url
    from django.contrib import admin

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
    ]

Como puedes ver, Django ya puso algo aquí para nosotras.

Las líneas entre triple commillas (``'''`` or ``"""``) son llamadas
«docstrings». Puedes escribirlas al inicio del archivo, clase o método
para describir que hacen. No son ejecutadas por Python.

Ya está aquí la URL de admin, que visitaste en el capítulo anterior:

.. code:: python

        url(r'^admin/', admin.site.urls),

Esto significa que para cada URL que empieza con ``admin/`` Django
encontrará su correspondiente *view*. En este caso estamos incluyendo
muchas URLs del admin así que está todo empaquetado en un pequeño
archivo. Es más limpio y legible.

Regex
=====

¿Te preguntas cómo compara Django las direcciones URL con las vistas?
Bueno, esta parte es difícil. Django usa ``regex``, abreviatura de
"expresiones regulares". Regex tiene muchas (¡un montón!) de normas que
forman un patrón de búsqueda. Como los regex son un tema avanzado, no
vamos a entrar en detalle de cómo funcionan.

Si aún así quieres entender cómo hemos creado los patrones, aquí hay un
ejemplo del proceso. Sólo necesitaremos un grupo limitado de reglas para
expresar el patrón que estamos buscando, en concreto:

::

    ^ denota el principio del texto
    $ denota el final del texto
    \d representa un dígito
    + indica que el ítem anterior debería ser repetido <b>por lo menos</b> una vez
    () para encerrar una parte del patrón

Cualquier otra cosa en la definición de la URL será tomada literalmente.

Ahora imagina que tienes un sitio web con una dirección como esta:
``http://www.mysite.com/post/12345/``, donde ``12345`` es el número de
post.

Escribir vistas separadas para todos los números de post sería realmente
molesto. Con las expresiones regulares podemos crear un patrón que
coincidirá la URL y extraerá el número para nosotras: ``^post/(\d+)/$``.
Analicemos esta expresión parte por parte para entender qué es lo que
estamos haciendo aquí:

-  **^post/** le está diciendo a Django que tome cualquier cosa que
   tenga ``post/`` al principio de la URL (justo antes de ``^``)
-  **(+)** significa que habrá un número (de uno o más dígitos) y que
   queremos que ese número sea capturado y extraído
-  **/** le dice a Django que otro caracter ``/`` debería venir a
   continuación
-  **$** indica el final de la URL, lo que significa que sólo
   coincidirán con este patrón las cadenas que terminen en ``/``

¡Tu primera URL de Django!
==========================

¡Es hora de crear nuestra primera URL! Queremos que
'http://127.0.0.1:8000/' sea la página de inicio del blog y que muestre
una lista de entradas.

También queremos mantener limpio el archivo ``mysite/urls.py``, así que
vamos a importar las urls de nuestra aplicación ``blog`` en el archivo
principal ``mysite/urls.py``.

Adelante, agrega una línea que importe ``blog.urls`` en la url principal
(``''``). Nota que estamos usando la función ``include`` aquí, por lo
tanto vas a tener que agregarla en el ``import`` de la primera línea del
archivo.

El archivo ``mysite/urls.py`` debería verse ahora así:

.. code:: python

    from django.conf.urls import include, url
    from django.contrib import admin

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'', include('blog.urls')),
    ]

Ahora Django redirigirá todo lo que entre a 'http://127.0.0.1:8000/'
hacia ``blog.urls`` y buscará más instrucciones allí.

Cuando se escriben expresiones regulares en Python siempre se pone ``r``
delante de la cadena. Esto le da una pista a Python de que la cadena
puede contener caracteres especiales que no son para Python en sí, sino
para la expresión regular.

blog.urls
=========

Crea un nuevo archivo vacío ``blog/urls.py``. ¡Muy bien! Agrega estas
primeras dos líneas:

.. code:: python

    from django.conf.urls import url
    from . import views

Aquí sólo estamos importando métodos de Django y todas nuestras
``vistas`` de la aplicación del ``blog`` (aún no tenemos ninguna, pero
llegaremos a eso en un minuto!)

Luego de esto, podemos agregar nuestro primer patrón URL:

.. code:: python

    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
    ]

Como puedes ver, ahora estamos asignando una vista ``view`` llamada
``post_list`` al URL ``^$``. Esta expresión regular coincidirá con ``^``
(un inicio) seguido de ``$`` (un final), por lo tanto sólo una cadena
vacía coincidirá. Es correcto, porque en el sistema de resolución de URL
de Django, 'http://127.0.0.1:8000/' no forma parte de la URL. Este
patrón le dirá a Django que ``views.post_list`` es el lugar correcto al
que ir si alguien entra a tu sitio web con la dirección
'http://127.0.0.1:8000/'.

La última parte ``name='post_list'`` es el nombre de la URL que se
utilizará para identificar a la vista. Puede coincidir con el nombre de
la vista pero también puede ser algo completamente distinto.
Utilizaremos las URL con nombre más delante en el proyecto así que es
importante darle un nombre a cada URL de la aplicación. También
deberíamos intentar mantener los nombres de las URL únicos y fáciles de
recordar.

Si ahora intentas visitar http://127.0.0.1:8000/, encontraŕas un mensaje
del estilo 'web page not available'. Esto es porque el servidor
(¿recuerdas haber escrito ``runserver``?) no está ejecutándose ya. Ve a
la ventana de consola y busca el porqué.

.. figure:: error1.png
   :alt: Error

   Error

Tu consola está mostrando un error, pero no te preocupes. Estos mensajes
son muy útiles:

Te está diciendo **no attribute 'post\_list'**. Ese es el noombre de al
*view* que Django está tratando de encontrar y user, pero no la hemos
creado todavía. No te preocupes, ya llegaremos ahí.

    Si quieres saber más sobre Django URLconfs, mira la documentación
    oficial: https://docs.djangoproject.com/en/1.9/topics/http/urls/

