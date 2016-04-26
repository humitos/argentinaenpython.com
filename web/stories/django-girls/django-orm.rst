ORM de Django y QuerySets
+++++++++++++++++++++++++

En este capítulo aprenderás cómo Django se conecta a la base de datos y
almacena los datos en ella. ¡Vamos a sumergirnos!

¿Qué es un QuerySet?
====================

Un QuerySet es, en esencia, una lista de objetos de un modelo
determinado. Un QuerySet te permite leer los datos de base de datos,
filtrarlos y ordenarlos.

Es más fácil de aprender con ejemplos. Vamos a intentarlo, ¿de acuerdo?

Django shell
============

Abre la consola local (no la de PythonAnywhere) y escribe este comando:

::

    (myvenv) ~/djangogirls$ python manage.py shell

El resultado debería ser:

::

    (InteractiveConsole)
    >>>

Ahora estás en la consola interactiva de Django. Es como la consola de
Python, pero con un toque de magia Django :). Puedes utilizar todos los
comandos Python aquí también, por supuesto.

Ver todos los objetos
---------------------

Vamos a intentar mostrar todas nuestras entradas primero. Puedes hacerlo
con el siguiente comando:

::

    >>> Post.objects.all()
    Traceback (most recent call last):
          File "<console>", line 1, in <module>
    NameError: name 'Post' is not defined

¡Uy! Apareció un error. Nos dice que no hay ningún objeto Post. Esto es
correcto, ¡nos olvidamos de importarlo primero!

::

    >>> from blog.models import Post

Esto es simple: importamos el modelo ``Post`` de ``blog.models``. Vamos
a intentar mostrar todos los posts nuevamente:

::

    >>> Post.objects.all()
    [<Post: my post title>, <Post: another post title>]

¡Es una lista de las entradas que hemos creado antes! Las hemos creado
usando la interfaz del administrador de Django. Sin embargo, ahora
queremos crear nuevas entradas usando Python, ¿cómo lo hacemos?

Crear objetos
-------------

Esta es la forma de crear un nuevo objeto Post en la base de datos:

::

    >>> Post.objects.create(author=me, title='Sample title', text='Test')

Pero nos falta un ingrediente aquí: ``me``. Necesitamos pasar una
instancia del modelo ``User`` como autor. ¿Eso cómo se hace?

Primero importemos el modelo User:

::

    >>> from django.contrib.auth.models import User

¿Qué usuarios tenemos en nuestra base de datos? Veamos:

::

    >>> User.objects.all()
    [<User: ola>]

¡Es el súper usuario que hemos creado antes! Vamos a obtener una
instancia de ese usuario ahora:

::

    me = User.objects.get(username='ola')

Como puedes ver, ahora obtenemos, ``get``, un usuario, ``User``, con un
``username`` que es igual a 'ola'. ¡Genial! Por supuesto, tienes que
ajustarlo a tu nombre de usuario.

Ahora ya podemos crear nuestra entrada:

::

    >>> Post.objects.create(author=me, title='Sample title', text='Test')

¡Hurra! ¿Quieres comprobar si ha funcionado?

::

    >>> Post.objects.all()
    [<Post: my post title>, <Post: another post title>, <Post: Sample title>]

¡Ahí está, una entrada más en la lista!

Añade más entradas
------------------

Ahora puedes divertirte un poco y añadir más entradas para ver cómo
funciona. Añade 2 o 3 más y avanza a la siguiente parte.

Filtrar objetos
---------------

Una parte importante de los QuerySets es la habilidad para filtrarlos.
Digamos que queremos encontrar todas las entradas cuyo autor sea el User
ola. Usaremos ``filter`` en vez de ``all`` en ``Post.objects.all()``.
Entre paréntesis estableceremos qué condición (o condiciones) debe
cumplir una entrada del blog para terminar en nuestro queryset. En
nuestro caso sería ``author`` es igual a ``me``. La forma de escribirlo
en Django es: ``author=me``. Ahora nuestro bloque de código tiene este
aspecto:

::

    >>> Post.objects.filter(author=me)
    [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]

¿O quizá queremos ver todas las entradas que contengan la palabra
'title' en el campo ``title``?

::

    >>> Post.objects.filter(title__contains='title')
    [<Post: Sample title>, <Post: 4th title of post>]


.. admonition:: Nota

   Hay dos guiones bajos (``_``) entre ``title`` y ``contains``. El
   ORM de Django utiliza esta sintaxis para separar los nombres de los
   campos ("title") de las operaciones o filtros ("contains"). Si sólo
   utilizas un guión bajo, obtendrás un error como "FieldError: Cannot
   resolve keyword title\_contains".

También puedes obtener una lista de todas las entradas publicadas. Lo
hacemos filtrando las entradas que tienen la fecha de publicación,
``published_date``, en el pasado:

::
   
   >>> from django.utils import timezone
   >>> Post.objects.filter(published\_date\_\_lte=timezone.now()) []

Por desgracia, la entrada que hemos añadido desde la consola de Python
no está publicada todavía. ¡Eso lo podemos cambiar! Primero obtenemos
una instancia de la entrada que queremos publicar:

::

    >>> post = Post.objects.get(title="Sample title")

¡Y luego publícala con el método ``publish``!

::

    >>> post.publish()

Ahora vuelve a intentar obtener la lista de entradas publicadas (pulsa
la tecla de arriba 3 veces y pulsa ``intro``):

::

    >>> Post.objects.filter(published_date__lte=timezone.now())
    [<Post: Sample title>]

Ordenar objetos
---------------

Los QuerySets también te permiten ordenar la lista de objetos.
Intentemos ordenarlos por el campo ``created_date``:

::

    >>> Post.objects.order_by('created_date')
    [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]

También podemos invertir el orden agregando ``-`` al principio:

::

    >>> Post.objects.order_by('-created_date')
    [<Post: 4th title of post>,  <Post: My 3rd post!>, <Post: Post number 2>, <Post: Sample title>]

Encadenar QuerySets
-------------------

También puedes combinar QuerySets **encadenando** uno con otro:

::

    >>> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

Es muy potente y te permite escribir consultas bastante complejas.

¡Genial! ¡Ahora estás lista para la siguiente parte! Para cerrar la
consola, escribe esto:

::

    >>> exit()
    $

