CSS - ¡Hazlo bonito!
++++++++++++++++++++

Nuestro blog todavía se ve bastante feo, ¿verdad? ¡Es hora de hacerlo
bonito! Vamos a usar CSS para eso.

¿Qué es CSS?
============

CSS ('Cascading Style Sheets', que significa 'hojas de estilo en
cascada') es un lenguaje utilizado para describir el aspecto y el
formato de un sitio web escrito en lenguaje de marcado (como HTML).
Trátalo como maquillaje para nuestra página web ;).

Pero no queremos empezar de cero otra vez, ¿verdad? Una vez más,
usaremos algo que ya ha sido hecho por programadores y publicado en
Internet de forma gratuita. Ya sabes, re-inventar la rueda no es
divertido.

¡Vamos a usar Bootstrap!
========================

Bootstrap es uno de los frameworks de HTML y CSS mas populares para
desarrollar sitios bonitos: http://getbootstrap.com/

Fue escrito por programadores que trabajaban para Twitter y ahora está
siendo desarrollado por voluntarios de todo el mundo.

Instalar Bootstrap
==================

Para instalar Bootstrap, tienes que agregar esto al ``<head>`` en tu
archivo ``.html`` (``blog/templates/blog/post_list.html``):

.. code:: html

    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">

Esto no añade archivos a tu proyecto, sólo hace referencia a archivos
que existen en internet. Adelante, abre tu sitio y actualiza la página.
¡Ahí lo tienes!

.. figure:: bootstrap1.png
   :alt: Figura 14.1

   Figura 14.1

¡Se ve mucho mejor!

Archivos estáticos en Django
============================

Finalmente nos vamos a fijar en estas cosas que hemos estado llamando
**archivos estáticos**. Los archivos estáticos son todos tus CSS e
imágenes; archivos que no son dinámicos, por lo que su contenido no
depende del contexto de la petición y serán iguales para cada usuario.

Dónde poner los archivos estáticos para Django
----------------------------------------------

Django ya sabe dónde encontrar los archivos estáticos para la aplicación
"admin". Ahora necesitamos agregar algunos archivos estáticos para
nuestra propia aplicación, ``blog``.

Hacemos esto creando una carpeta llamada ``static`` dentro de la
estructura de la aplicación que llamamos blog:

::

    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    └── mysite

Django encontrará automáticamente cualquier carpeta que se llame
"static" dentro de las carpetas de tus aplicaciones y podrá utilizar su
contenido como archivos estáticos.

¡Tu primer archivo CSS!
=======================

Creemos un archivo CSS ahora, para agregar tu propio estilo a tu página
web. Crea un nuevo directorio llamado ``css`` dentro de tu directorio
``static``. Después crea un nuevo archivo llamado ``blog.css`` dentro de
este directorio ``css``. ¿Lista?

::

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css

¡Es hora de escribir algo de CSS! Abre el archivo
``blog/static/css/blog.css`` en tu editor de código.

No nos adentraremos mucho en la personalización y aprendizaje sobre CSS
aquí. Es muy fácil y lo puedes aprender por tu cuenta después de este
taller. Hay una recomendación de un curso gratuito para aprender más al
final de esta página.

Pero vamos a hacer un poco al menos. ¿Tal vez podríamos cambiar el color
de nuestro título? Los ordenadores utilizan códigos especiales para
entender los colores. Empiezan con ``#`` y les siguen 6 letras (A-F) y
números (0-9). Puedes encontrar códigos de color, por ejemplo, aquí:
http://www.colorpicker.com/. También puedes utilizar `colores
predefinidos <http://www.whoishostingthis.com/resources/css-colors/>`__
utilizando su nombre en inglés, como ``red`` y ``green``.

En tu archivo ``blog/static/css/blog.css`` deberías agregar el siguiente
código:

.. code:: css

    h1 a {
        color: #FCA205;
    }

``h1 a`` es un selector CSS. Esto significa que estamos aplicando
nuestros estilos a cualquier elemento ``a`` dentro de un elemento ``h1``
(p. ej. cuando tenemos en código algo como:
``<h1><a href="">link</a></h1>``). En este caso le estamos diciendo que
cambie el color a ``#FCA205``, que es naranja. Por supuesto, ¡puedes
poner tu propio color aquí!

En el archivo CSS se definen los estilos de los elementos que se
encuentran en el archivo HTML. Los elementos se identifican por el
nombre del elemento (p. ej. ``a``. ``h1``, ``body``), el atributo
``class`` o el atributo ``id``. Class e id son nombres que le asignas tú
misma al elemento. Clases definen grupos de elementos e ids apuntan a
elementos específicos. Por ejemplo, la siguiente etiqueta puede
identificarse mediante CSS usando el nombre de etiqueta ``a``, la clase
``external_link`` o el id ``link_to_wiki_page``:

.. code:: html

    <a href="http://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page">

Lee sobre `Selectores de CSS en
w3schools <http://www.w3schools.com/cssref/css_selectors.asp>`__.

Entonces, necesitamos decirle a nuestra plantilla HTML que hemos añadido
algún CSS. Abre el archivo ``blog/templates/blog/post_list.html`` y
añade esta línea al principio del todo:

.. code:: html

    {% load staticfiles %}

Aquí sólo estamos cargando archivos estáticos :). Luego, entre el
``<head>`` y ``</head>``, después de los enlaces a los archivos CSS de
Bootstrap (el navegador lee los archivos en el orden que son dados, de
ese modo el código en nuestro archivo puede sobre-escribir el código en
los archivos de Bootstrap), añade la siguiente línea:

.. code:: html

    <link rel="stylesheet" href="{% static 'css/blog.css' %}">

El navegador lee los archivos en el orden en que el que son presentados,
por lo tanto nos tenemos que asegurar que están en el lugar correcto. De
otra forma el código en nuestro archivo quizás sobre-escriba el código de
los archivos de Bootstrap. Le acabamos de decir a nuestra plantilla
dónde se encuentra nuestro archivo CSS.

Ahora tu archivo debería tener este aspecto:

.. code:: html

    {% load staticfiles %}
    <html>
        <head>
            <title>Django Girls blog</title>
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
            <link rel="stylesheet" href="{% static 'css/blog.css' %}">
        </head>
        <body>
            <div>
                <h1><a href="/">Django Girls Blog</a></h1>
            </div>

            {% for post in posts %}
                <div>
                    <p>published: {{ post.published_date }}</p>
                    <h1><a href="">{{ post.title }}</a></h1>
                    <p>{{ post.text|linebreaks }}</p>
                </div>
            {% endfor %}
        </body>
    </html>

De acuerdo, ¡guarda el archivo y actualiza el sitio!

.. figure:: color2.png
   :alt: Figura 14.2

   Figura 14.2

¡Buen trabajo! ¿Tal vez nos gustaría también dar un poco de aire a
nuestro sitio web y aumentar el margen en el lado izquierdo?. ¡Vamos a
intentarlo!

.. code:: css

    body {
        padding-left: 15px;
    }

Añade esto a tu CSS, guarda el archivo y ¡mira cómo funciona!

.. figure:: margin2.png
   :alt: Figura 14.3

   Figura 14.3

¿Quizá podríamos personalizar la tipografía del título? Pega esto en la
sección ``<head>`` del archivo ``blog/templates/blog/post_list.html``:

.. code:: html

    <link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">

Esta línea va a importar una tipografía llamada *Lobster* de Google
Fonts (https://www.google.com/fonts).

Ahora añade la línea ``font-family: 'Lobster';`` en el archivo CSS
``blog/static/css/blog.css`` dentro del bloque de declaración ``h1 a``
(el código entre llaves ``{`` y ``}``) y actualiza la página:

.. code:: css

    h1 a {
        color: #FCA205;
        font-family: 'Lobster';
    }

.. figure:: font.png
   :alt: Figura 14.3

   Figura 14.3

¡Genial!

Como se mencionó anteriormente, CSS tiene un concepto de clases que
básicamente permite nombrar una parte del código HTML y aplicar estilos
sólo a esta parte, sin afectar a otras. Es muy útil si tienes dos divs
que hacen algo muy diferente (como el encabezado y la entrada), por lo
que no quieres que tengan el mismo aspecto. Una clase puede ayudarte a
hacer que se vean diferente.

Adelante, nombra algunas partes del código HTML. Añade una clase llamada
``page-header`` a tu ``div`` que contiene el encabezado, así:

.. code:: html

    <div class="page-header">
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>

Y ahora añade una clase ``post`` a tu ``div`` que contiene una entrada
del blog.

.. code:: html

    <div class="post">
        <p>published: {{ post.published_date }}</p>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>

Ahora agregaremos bloques de declaración a diferentes selectores. Los
selectores que comienzan con ``.`` hacen referencia a clases. Hay muchos
tutoriales y explicaciones sobre CSS en la Web para ayudarte a entender
el siguiente código. Por ahora, simplemente copia y pega este bloque de
código en tu archivo ``blog/static/css/blog.css``:

.. code:: css

    .page-header {
        background-color: #ff9400;
        margin-top: 0;
        padding: 20px 20px 20px 40px;
    }

    .page-header h1, .page-header h1 a, .page-header h1 a:visited, .page-header h1 a:active {
        color: #ffffff;
        font-size: 36pt;
        text-decoration: none;
    }

    .content {
        margin-left: 40px;
    }

    h1, h2, h3, h4 {
        font-family: 'Lobster', cursive;
    }

    .date {
        color: #828282;
    }

    .save {
        float: right;
    }

    .post-form textarea, .post-form input {
        width: 100%;
    }

    .top-menu, .top-menu:hover, .top-menu:visited {
        color: #ffffff;
        float: right;
        font-size: 26pt;
        margin-right: 20px;
    }

    .post {
        margin-bottom: 70px;
    }

    .post h1 a, .post h1 a:visited {
        color: #000000;
    }

Luego envuelve el código HTML que muestra los mensajes con declaraciones
de clases. Cambia esto:

.. code:: html

    {% for post in posts %}
        <div class="post">
            <p>published: {{ post.published_date }}</p>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}

en ``blog/templates/blog/post_list.html`` con esto:

.. code:: html

    <div class="content container">
        <div class="row">
            <div class="col-md-8">
                {% for post in posts %}
                    <div class="post">
                        <div class="date">
                            <p>published: {{ post.published_date }}</p>
                        </div>
                        <h1><a href="">{{ post.title }}</a></h1>
                        <p>{{ post.text|linebreaks }}</p>
                    </div>
                {% endfor %}
            </div>
        </div>
    </div>

Guarda estos archivos y actualiza tu sitio.

.. figure:: final.png
   :alt: Figura 14.4

   Figura 14.4

Woohoo! Parece increíble, ¿verdad? Mira el código que acabamos de pegar
y busca los lugares donde hemos agregado clases en el HTML y las hemos
usado en el CSS. ¿Dónde harías los cambios si quieres que la fecha sea
turquesa?

No tengas miedo de jugar un poco con este CSS e intentar cambiar algunas
cosas. Jugar con el CSS te ayudará a entender qué hacen las diferentes
cosas. Si rompes algo, no te preocupes, ¡siempre puedes deshacerlo!

Te recomendamos encarecidamente que hagas este `Curso de HTML & CSS de
Codeacademy <http://www.codecademy.com/tracks/web>`__ gratuito y online.
Te ayudará a aprender todo lo que necesitas saber sobre cómo hacer tus
sitios web más bonitos con CSS.

¡¿Lista para el siguiente capítulo?! :)

