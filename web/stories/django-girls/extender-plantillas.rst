Extender Plantillas
+++++++++++++++++++

Otra cosa buena que Django tiene para tí es la **extensión de
plantillas**. ¿Qué significa esto? Significa que puedes usar las mismas
partes de tu HTML para diferentes páginas de tu sitio web.

De esta forma no tienes que repetir el código en cada uno de los
archivos cuando quieres usar una misma información o un mismo esquema. Y
si quieres cambiar algo, no necesitas hacerlo en cada plantilla.

Creando una plantilla base
==========================

Una plantilla base es la plantilla más básica que extiendes en cada
página de tu sitio web.

Vamos a crear un archivo ``base.html`` en ``blog/templates/blog/``:

::

    blog
    └───templates
        └───blog
                base.html
                post_list.html

Luego ábrelo y copia todo lo que hay en ``post_list.html`` al archivo
``base.html``, de la siguiente manera:

.. code:: html

    {% load staticfiles %}
    <html>
        <head>
            <title>Django Girls blog</title>
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
            <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
            <link rel="stylesheet" href="{% static 'css/blog.css' %}">
        </head>
        <body>
            <div class="page-header">
                <h1><a href="/">Django Girls Blog</a></h1>
            </div>

            <div class="content container">
                <div class="row">
                    <div class="col-md-8">
                    {% for post in posts %}
                        <div class="post">
                            <div class="date">
                                {{ post.published_date }}
                            </div>
                            <h1><a href="">{{ post.title }}</a></h1>
                            <p>{{ post.text|linebreaksbr }}</p>
                        </div>
                    {% endfor %}
                    </div>
                </div>
            </div>
        </body>
    </html>

Luego, en ``base.html`` reemplaza por completo tu ``<body>`` (todo lo
que haya entre ``<body>`` and ``</body>``) con esto:

.. code:: html

    <body>
        <div class="page-header">
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>
        <div class="content container">
            <div class="row">
                <div class="col-md-8">
                {% block content %}
                {% endblock %}
                </div>
            </div>
        </div>
    </body>

Básicamente remplazamos todo entre ``{% for post in posts %}{% endfor %}`` con:

.. code:: html

    {% block content %}
    {% endblock %}

¿Qué significa esto? Acabas de crear un ``block``, una template tag que
te permite insertar HTML en este bloque en otras plantillas que
extiendan esta plantilla (``base.html``). Te mostraremos como hacer esto
en un momento.

Ahora guarda ``base.html`` y abre tu archivo
``blog/templates/blog/post_list.html`` de nuevo. Elimina todo lo que
está por encima de ``{% for post in posts %}`` y debajo de ``{% endfor
%}``. Cuando lo hayas hecho, el archivo deberá lucir similar a esto:

.. code:: html

    {% for post in posts %}
        <div class="post">
            <div class="date">
                {{ post.published_date }}
            </div>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaksbr }}</p>
        </div>
    {% endfor %}

Queremos utilizar esto como parte de nuestro template para todos los
bloques de contenido. ¡Es hora de agregar etiquetas de bloques a este
archivo!

Quieres que la etiqueta de bloque coincida con la etiqueta en el
archivo ``base.html``. También querrás que este incluya todo el código
que pertenece al bloque ``content`` (contenido). Para hacer eso, pon
todo entre ``{% block content %}`` y ``{% endblock content %}``. Así:

.. code:: html


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
    {% endblock %}

Sólo nos falta una cosa. Necesitamos conectar estas dos plantillas.
¡Esto es de lo que se trata la extensión de plantillas! Vamos a hacer
esto agregando un bloque de extensión al principio del archivo. De esta
forma:

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
    {% endblock %}

¡Eso es todo! Verifica que tu sitio web aún funcione apropiadamente :)

    Si tienes un error ``TemplateDoesNotExist`` que diga que no hay un
    archivo ``blog/base.html`` y tienes ``runserver`` ejecutándose en la
    consola, intenta pararlo (presionando Ctrl+C - las teclas Control y
    C juntas) y reinicialo ejecutando el comando
    ``python manage.py runserver``.

