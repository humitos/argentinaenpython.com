Plantillas de Django
++++++++++++++++++++

¡Es hora de mostrar algunos datos! Para ello Django incorpora unas
etiquetas de plantillas, **template tags**, muy útiles.

¿Qué son las template tags?
===========================

Verás, en HTML no se puede escribir código Python porque los navegadores
no lo entienden. Sólo saben HTML. Sabemos que HTML es bastante estático,
mientras que Python es mucho más dinámico.

Las **template tags de Django** nos permiten transferir elementos
Pythonescos a HTML, para que puedas construir sitios web dinámicos más
rápido y fácil. ¡Ostras!

Mostrar la plantilla post list
==============================

En el capítulo anterior le dimos a nuestra plantilla una lista de
entradas en la variable ``posts``. Ahora la vamos a mostrar en HTML.

Para imprimir una variable en una plantilla de Django, utilizamos llaves
dobles con el nombre de la variable dentro, así:

.. code:: html

    {{ posts }}

Pruébalo en la plantilla ``blog/templates/blog/post_list.html``.
Sustituye todo desde el segundo ``<div>`` al tercer ``</div>`` por
``{{ posts }}``. Guarda el archivo y refresca la página para ver el
resultado:

.. figure:: dt_step1.png
   :alt: Figura 13.1

   Figura 13.1

Como puedes ver, lo que hemos conseguido es esto:

.. code:: python

   [<Post: My second post>, <Post: My first post>]

Significa que Django lo entiende como una lista de objetos. ¿Recuerdas
de **Introducción a Python** cómo podemos mostrar listas? Sí, ¡con
bucles for! En una plantilla de Django se hacen así:

.. code:: html

    {% for post in posts %}
        {{ post }}
    {% endfor %}

Pruébalo en tu plantilla.

.. figure:: dt_step2.png
   :alt: Figura 13.2

   Figura 13.2

¡Funciona! Pero queremos que se muestren como los posts estáticos que
creamos anteriormente en el capítulo de **Introducción a HTML**. Puedes
mezclar HTML y template tags. Nuestro ``body`` se verá así:

.. code:: html

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

Todo lo que pongas entre ``{% for %}`` y ``{% endfor %}`` se
repetirá para cada objeto de la lista. Refresca la página:

.. figure:: dt_step3.png
   :alt: Figura 13.3

   Figura 13.3

¿Has notado que utilizamos una notación diferente esta vez
``{{ post.title }}`` o ``{{ post.text }}``? Estamos accediendo a datos
en cada uno de los campos definidos en nuestro modelo ``Post``. También
el ``|linebreaks`` está pasando el texto de las entradas a través de un
filtro para convertir saltos de línea en párrafos.

Una cosa más
============

Estaría bien ver si tu sitio web seguirá funcionando en la Internet
pública, ¿verdad? Vamos a intentar desplegar de nuevo en PythonAnywhere.
Aquí va un resumen de los pasos...

-  Primero, sube tu código a GitHub

::

    $ git status
    [...]
    $ git add --all .
    $ git status
    [...]
    $ git commit -m "Modified templates to display posts from database."
    [...]
    $ git push

-  Luego, vuelve a entrar en
   `PythonAnywhere <https://www.pythonanywhere.com/consoles/>`__ y ve a
   tu **consola Bash** (o inicia una nueva), y ejecuta:

::

    $ cd mi-primer-blog
    $ git pull
    [...]

-  Finalmente, ve a la `pestaña
   Web <https://www.pythonanywhere.com/web_app_setup/>`__ y presiona
   **Reload** en tu aplicación web. ¡Tu actualización debería poder
   verse! Si las entradas de blog no coinciden con las que aparecen en
   tu servidor local, eso está bien. Las bases de datos de tu
   computadora local y la de Python Anywhere no se sincronizan con el
   resto de tus archivos.

¡Enhorabuena! Ahora ve e intenta agregar una nueva entrada desde el panel
de administrador de Django (¡recuerda agregar published\_date!) y luego
actualiza tu página para ver si aparece la nueva entrada.

¿Funciona de maravilla? ¡Estamos orgullosas! Aléjate un rato del
ordenador, te has ganado un descanso. :)

.. figure:: donut.png
   :alt: Figura 13.4

   Figura 13.4

