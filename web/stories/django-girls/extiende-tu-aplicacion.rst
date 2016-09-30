Extiende tu aplicación
++++++++++++++++++++++

Ya hemos completado todos los pasos necesarios para la creación de
nuestro sitio web: sabemos cómo escribir un model, url, view y template.
También sabemos cómo hacer que nuestro sitio web se vea lindo.

¡Hora de practicar!

Lo primero que necesitamos en nuestro blog es, obviamente, una página
para mostrar un post, ¿cierto?

Ya tenemos un modelo ``Post``, así que no necesitamos agregar nada a
``models.py``.

Crea un enlace al detalle de una entrada
========================================

Vamos a empezar añadiendo un enlace dentro del archivo
``blog/templates/blog/post_list.html``. Hasta el momento debería verse
así:

.. code:: html

    {% extends 'blog/base.html' %}

    {% block content %}
        {% for post in posts %}
            <div class="post">
                <div class="date">
                    {{ post.published_date }}
                </div>
                <h1><a href="">{{ post.title }}</a></h1>
                <p>{{ post.text|linebreaksbr }}</p>
            </div>
        {% endfor %}
    {% endblock content %}

Queremos tener un enlace que vaya desde el título de la entrada
en la lista de entradas hasta la página de detalle de la entrada. Vamos
a cambiar ``<h1><a href="">{{ post.title }}</a></h1>`` para que enlace a
la página de detalle de la entrada:

.. code:: html

    <h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>

Es hora de explicar el misterioso ``{% url 'post_detail' pk=post.pk
%}``. Como probablemente sospeches, la notación ``{% %}`` significa
que estamos utilizando Django template tags. ¡Esta vez vamos a usar
una que creará una URL!

``blog.views.post_detail`` es una ruta hacia la *view*
``post_detail`` que queremos crear. Fíjate bien: ``blog`` es el nombre
de nuestra aplicación (el directorio ``blog``), ``views`` es el nombre
del archivo ``views.py`` y la última parte, ``post_detail``, es el
nombre de la *view*.

Ahora cuando vayamos a: http://127.0.0.1:8000/ tendremos un error
(como era de esperar, ya que no tenemos una URL o una *view* para
``post_detail``). Se verá así:

.. figure:: no_reverse_match2.png
   :alt: NoReverseMatch error

   NoReverseMatch error


Crea una URL al detalle de una entrada
======================================

Vamos a crear una URL en ``urls.py`` para nuestra *view*
``post_detail``!

Queremos que el detalle de la primera entrada se visualice en esta
**URL**: http://127.0.0.1:8000/post/1/

Vamos a crear una URL en el archivo ``blog/urls.py`` que dirija a Django
hacia una *view* llamada ``post_detail``, que mostrará una entrada de
blog completa. Añade la línea
``url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),``
al archivo ``blog/urls.py``. El archivo debería parecerse a esto:

.. code:: python

    from django.conf.urls import include, url
    from . import views

    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    ]

La parte de ``^post/(?P<pk>\d+)/$`` da un poco de miedo, pero no te
preocupes, te la vamos a explicar:

-  empieza por ``^`` de nuevo -- "el comienzo"
-  ``post/`` quiere decir que después del comienzo, la URL debería
   contener la palabra **post** y **/**. Por ahora todo bien.
-  ``(?P<pk>\d+)`` - esta parte es más complicada. Significa que Django
   cogerá todo lo que pongas aquí y lo transferirá a una vista como una
   variable llamada ``pk``. ``\d`` también nos dice que sólo puede ser
   un número, no una letra (todo lo que esté entre 0 y 9). ``+``
   significa que ahí tiene que haber uno o más dígitos. Así que algo
   como ``http://127.0.0.1:8000/post//`` no es válido, ¡pero
   ``http://127.0.0.1:8000/post/1234567890/`` es perfectamente
   aceptable! - ``/``
-  necesitamos **/** de nuevo
-  ``$`` - ¡"el final"!

Esto quiere decir que si pones ``http://127.0.0.1:8000/post/5/`` en tu
navegador, Django entenderá que estás buscando una *view* llamada
``post_detail`` y transferirá la información de que ``pk`` es igual a
``5`` a esa *view*.

``pk`` es la abreviatura de ``primary key``, clave primaria. Este nombre
se utiliza a menudo en proyectos de Django. Pero puedes nombrar la
variable como quieras (recuerda: ¡minúsculas y ``_`` en lugar de
espacios!). Por ejemplo en lugar de ``(?P<pk>\d+)`` podríamos tener la
variable ``post_id``, así que esto lo verías como: ``(?P<post_id>\d+)``.

Vale, ¡hemos añadido un nuevo patrón de URL a ``blog/urls.py``! Vamos a
refrescar la página: http://127.0.0.1:8000/ ¡Zas! ¡Otro error! ¡Era de
esperar!

.. figure:: attribute_error2.png
   :alt: AttributeError

   AttributeError


¿Recuerdas cuál es el próximo paso? Por supuesto: ¡agregar una vista!

Agrega una vista de detalle de la entrada
=========================================

Esta vez nuestra *view* tomará un parámetro adicional ``pk``. Nuestra
*view* necesita recibirlo, ¿verdad? Así que definiremos nuestra función
como ``def post_detail (request, pk):``. Ten en cuenta que tenemos que
usar exactamente el mismo nombre que especificamos en las urls (``pk``).
¡Omitir esta variable es incorrecto y resultará en un error!

Ahora, queremos obtener una sola entrada del blog. Para ello podemos
usar querysets como este:

::

    Post.objects.get(pk=pk)

Pero este código tiene un problema. Si no hay ningún ``Post`` con esa
``clave primaria`` (``pk``), ¡tendremos un error muy feo!

.. figure:: does_not_exist2.png
   :alt: DoesNotExist error

   DoesNotExist error


¡No queremos eso! Pero, por supuesto, Django viene con algo que se
encargará de ese problema por nosotros: ``get_object_or_404``. En caso
de que no haya ningún ``Post`` con el dado ``pk`` se mostrará una más
agradable página (``Page Not Found 404``).

.. figure:: 404_2.png
   :alt: Page not found

   Page not found


La buena noticia es que puedes crear tu propia página ``Page Not Found``
y diseñarla como desees. Pero por ahora no es tan importante, así que lo
omitiremos.

¡Es hora de agregar una *view* a nuestro archivo ``views.py``!

Deberíamos abrir ``blog/views.py`` y agregar el siguiente código:

.. code:: python

    from django.shortcuts import render, get_object_or_404

Cerca de otras líneas ``from``. Y en el final del archivo añadimos
nuestra *view*:

.. code:: python

    def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})

Sí. Es hora de actualizar la página: http://127.0.0.1:8000/

.. figure:: post_list2.png
   :alt: Post list view

   Post list view


¡Funcionó! Pero ¿qué pasa cuando haces click en un enlace en el título
del post?

.. figure:: template_does_not_exist2.png
   :alt: TemplateDoesNotExist error

   TemplateDoesNotExist error


¡Oh no! ¡Otro error! Pero ya sabemos cómo lidiar con eso, ¿no? ¡Tenemos
que agregar una plantilla!

Crear una plantilla para post detail
====================================

Crearemos un archivo en ``blog/templates/blog`` llamado
``post_detail.html``.

Se verá así:

.. code:: html

    {% extends 'blog/base.html' %}

    {% block content %}
        <div class="post">
            {% if post.published_date %}
                <div class="date">
                    {{ post.published_date }}
                </div>
            {% endif %}
            <h1>{{ post.title }}</h1>
            <p>{{ post.text|linebreaksbr }}</p>
        </div>
    {% endblock %}

Una vez más estamos extendiendo ``base.html``. En el bloque ``content``
queremos mostrar la fecha de publicación (si existe), título y texto de
nuestros posts. Pero deberíamos discutir algunas cosas importantes,
¿cierto?

``{% if ... %} ... {% endif %}`` es un template tag que
podemos usar cuando querramos ver algo (¿recuerdas ``if ... else ..``
del capítulo de **Introducción a Python**?). En este escenario queremos
comprobar si un post ``published_date`` no esta vacio.

Bien, podemos actualizar nuestra página y ver si ``Page Not Found`` se
ha ido.

.. figure:: post_detail2.png
   :alt: Post detail page

   Post detail page


¡Yay! ¡Funciona!

Una cosa más: ¡Tiempo de implementación!
========================================

Sería bueno verificar que tu sitio web aún funcionará en PythonAnywhere,
¿cierto? Intentemos desplegar de nuevo.

::

    $ git status
    $ git add --all .
    $ git status
    $ git commit -m "Added view and template for detailed blog post as well as CSS for the site."
    $ git push

-  Luego, en una `consola Bash de
   PythonAnywhere <https://www.pythonanywhere.com/consoles/>`__

::

    $ cd mi-primer-blog
    $ git pull
    [...]

-  Finalmente, ve a la pestaña
   `Web <https://www.pythonanywhere.com/web_app_setup/>`__ y haz click
   en **Reload**.

¡Y eso debería ser todo! Felicidades :)

