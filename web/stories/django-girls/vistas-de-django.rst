Vistas de Django - ¡Es hora de crear!
+++++++++++++++++++++++++++++++++++++

Es hora de deshacerse del error que hemos creado en el capítulo anterior
:)

Una vista, *view*, es un lugar donde ponemos la "lógica" de nuestra
aplicación. Pedirá información del ``modelo`` que has creado antes y se
la pasará a la ``plantilla``. Crearemos una plantilla en el próximo
capítulo. Las vistas son sólo métodos de Python que son un poco más
complicados que los que escribimos en el capítulo de **Introducción a
Python**.

Las Vistas se colocan en el archivo ``views.py``. Agregaremos nuestras
*views* al archivo ``blog/views.py``.

blog/views.py
=============

Bien, vamos abrir este archivo y ver lo que contiene:

.. code:: python

    from django.shortcuts import render

    # Create your views here.

No demasiadas cosas aquí todavía.

Las líneas que comienzan con ``#`` son comentarios. Esto significa que
esas líneas no serán ejecutadas por Python. Muy útiles, ¿no?

La *view* más simple puede ser como esto:

.. code:: python

    def post_list(request):
        return render(request, 'blog/post_list.html', {})

Como puedes ver, hemos creado un método (``def``) llamado ``post_list``
que recibe una petición, ``request``, y devuelve, ``return``, un método
``render`` que renderizará (construirá) la plantilla
``blog/post_list.html``.

Guarda el fichero, ve a http://127.0.0.1:8000/ y veamos lo que tenemos
ahora.

¡Otro error! Leamos lo que está pasando ahora:

.. figure:: error.png
   :alt: Error

   Error

Esto muestra que el servidor está ejecutándose nuevamente al menos, pero
todavía no luce bien, ¿no? No te preocupes, es sólo una página de error,
¡nada de qué asustarse!. Puedes leer *TemplateDoesNotExist*. ¡Vamos a
arreglar este error y a crear una plantilla en el siguiente capítulo!

    Aprende más sobre las vistas de Django leyendo la documentación
    oficial: https://docs.djangoproject.com/en/1.9/topics/http/views/

