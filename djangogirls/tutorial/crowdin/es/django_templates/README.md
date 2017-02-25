# Plantillas de Django

¡Es hora de mostrar algunos datos! Para ello Django incorpora unas etiquetas de plantillas, **template tags**, muy útiles.

## ¿Qué son las etiquetas de plantilla?

Verás, en HTML no se puede escribir código Python porque los navegadores no lo entienden. Sólo saben HTML. Sabemos que HTML es bastante estático, mientras que Python es mucho más dinámico.

Las **template tags de Django** nos permiten comunicar elementos de Python a HTML, para que puedas construir sitios web dinámicos más rápida y fácilmente. ¡Ostras!

## Mostrar la plantilla post list

En el capítulo anterior le dimos a nuestra plantilla una lista de entradas en la variable `posts`. Ahora la vamos a mostrar en HTML.

Para imprimir una variable en una plantilla de Django, utilizamos llaves dobles con el nombre de la variable dentro, así:

    html
    {{ posts }}
    

Prueba esto en la plantilla `blog/templates/blog/post_list.html`. Sustituye todo desde el segundo `<div>` al tercer `</div>` por `{{ posts }}`. Guarda el archivo y refresca la página para ver los resultados:

![Figura 13.1][1]

 [1]: images/step1.png

Como puedes ver, lo que hemos conseguido es esto:

    [<Post: Mi segundo post>, <Post: Mi primer post>]
    

Significa que Django lo entiende como una lista de objetos. ¿Recuerdas de **Introducción a Python** cómo podemos mostrar listas? Sí, ¡con bucles for! En una plantilla de Django se hacen así:

    html
    {% for post in posts %}
        {{ post }}
    {% endfor %}
    

Prueba esto en tu plantilla.

![Figura 13.2][2]

 [2]: images/step2.png

¡Funciona! Pero queremos que se muestren como las entradas de blog estáticas que creamos anteriormente en el capítulo de **Introducción a HTML**. Usted puede mezclar HTML y etiquetas de plantilla. Nuestro `body` se verá así:

    html
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
    

{% raw %}Todo lo que pongas entre `{% for %}` y `{% endfor %}` se repetirá para cada objeto de la lista. Refresca la página:{% endraw %}

![Figura 13.3][3]

 [3]: images/step3.png

¿Has notado que utilizamos una notación diferente esta vez `{{ post.title }}` o `{{ post.text }}`? Estamos accediendo a los datos en cada uno de los campos definidos en nuestro modelo `Post`. También el `|linebreaks` está pasando el texto de las entradas a través de un filtro para convertir saltos de línea en párrafos.

## Una cosa más

Sería bueno ver si tu sitio web seguirá funcionando en la Internet pública, ¿no? Vamos a intentar desplegar de nuevo en PythonAnywhere. Aquí va un resumen de los pasos...

*   Primero, sube tu código a GitHub

    $ git status
    [...]
    $ git add -A .
    $ git status
    [...]
    $ git commit -m "Modified templates to display posts from database."
    [...]
    $ git push
    

*   Luego, vuelve a entrar en [PythonAnywhere][4] y ve a tu **consola Bash** (o inicia una nueva), y ejecuta:

 [4]: https://www.pythonanywhere.com/consoles/

    $ cd my-first-blog
    $ git pull
    [...]
    

*   Finalmente, ve a la [pestaña Web][5] y presiona **Reload** en tu aplicación web. ¡Tu actualización debería verse!

 [5]: https://www.pythonanywhere.com/web_app_setup/

¡Felicidades! Ahora sigue adelante, trata de agregar una nueva entrada usando el panel de administrador de Django (¡recuerda agregar published_date!) y luego actualiza tu página para ver si aparece tu nuevo post.

¿Funciona de maravilla? ¡Estamos orgullosas! Aléjate un rato del ordenador, te has ganado un descanso. :)

![Figura 13.4][6]

 [6]: images/donut.png