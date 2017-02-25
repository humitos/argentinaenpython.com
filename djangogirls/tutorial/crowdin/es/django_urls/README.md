# URLs en Django

Estamos a punto de construir nuestra primera página web: ¡una página de inicio para el blog! Pero primero, vamos a aprender un poco acerca de las urls de Django.

## ¿Qué es una URL?

Una URL es simplemente una dirección web. Puedes ver una URL cada vez que visitas una página. Se ve en la barra de direcciones del navegador (¡sí! ¡`127.0.0.1:8000` es una URL! Y `https://djangogirls.com` también es una URL):

![URL][1]

 [1]: images/url.png

Cada página en Internet necesita su propia URL. De esta manera tu aplicación sabe lo que debe mostrar a un usuario que abre una URL. En Django utilizamos algo que se llama `URLconf` (configuración de URL). URLconf es un conjunto de patrones que Django intentará comparar con la URL recibida para encontrar la vista correcta.

## ¿Cómo funcionan las URLs en Django?

Vamos a abrir el archivo `mysite/urls.py` en el editor de código de tu elección y veamos lo que tiene:

    python
    from django.conf.urls import include, url
    from django.contrib import admin
    
    urlpatterns = [
        # Examples:
        # url(r'^$', 'mysite.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),
    
        url(r'^admin/', include(admin.site.urls)),
    ]
    

Como puedes ver, Django ya puso algo aquí por nosotras.

Las líneas que comienzan con `#` son comentarios. Significa que esas líneas no serán ejecutadas por Python. Muy útil, ¿no?

La URL del admin, que visitaste en el capítulo anterior, ya está aquí:

    python
        url(r'^admin/', include(admin.site.urls)),
    

Esto significa que para cada URL que empieza con `admin/` Django encontrará su correspondiente *view*. En este caso estamos incluyendo muchas URLs del admin así que está todo empaquetado en un pequeño archivo. Es más limpio y legible.

## Regex

¿Te preguntas cómo compara Django las direcciones URL con las vistas? Bueno, esta parte es complicada. Django usa `regex`, abreviatura de "expresiones regulares". Regex tiene muchas normas (¡un montón!) que forman un patrón de búsqueda. Como las regex son un tema avanzado, no vamos a entrar en detalle de cómo funcionan.

Si aún así quieres entender cómo hemos creado los patrones, aquí hay un ejemplo del proceso. Sólo necesitaremos un grupo limitado de reglas para expresar el patrón que estamos buscando, en concreto:

    ^ denota el principio del texto
    $ denota el final del texto
    \d representa un dígito
    + indica que el ítem anterior debería ser repetido por lo menos una vez
    () para encerrar una parte del patrón
    

Cualquier otra cosa en la definición de la URL será tomada literalmente.

Ahora imagina que tienes un sitio web con una dirección como esta: `http://www.mysite.com/post/12345/`, donde `12345` es el número de post.

Escribir vistas separadas para todos los números de entradas en el blog sería realmente molesto. Con las expresiones regulares podemos crear un patrón que coincidirá la URL y extraerá el número para nosotras: `^post/(\d+)/$`. Analicemos esta expresión parte por parte para entender qué es lo que estamos haciendo aquí:

*   **^post/** le está diciendo a Django que tome cualquier cosa que tenga `post/` al principio de la URL (justo antes de `^`)
*   **(\d+)** significa que habrá un número (de uno o más dígitos) y que queremos que ese número sea capturado y extraído
*   **/** le dice a Django que otro caracter `/` debería venir a continuación
*   **$** indica el final de la URL, lo que significa que sólo coincidirán con este patrón las cadenas que terminen en `/`

## ¡Tu primera URL de Django!

¡Es hora de crear nuestra primera URL! Queremos que 'http://127.0.0.1:8000/' sea la página de inicio del blog y que muestre una lista de entradas.

También queremos mantener limpio el archivo `mysite/urls.py`, así que vamos a importar las urls de nuestra aplicación `blog` en el archivo principal `mysite/urls.py`.

Adelante, elimina las líneas comentadas (líneas que comienzan por `#`) y añade una línea que importará `blog.urls` en la url principal (`''`).

El archivo `mysite/urls.py` debería verse ahora así:

    python
    from django.conf.urls import include, url
    from django.contrib import admin
    
    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'', include('blog.urls')),
    ]
    

Ahora Django redirigirá todo lo que entre a 'http://127.0.0.1:8000/' hacia `blog.urls` y buscará más instrucciones allí.

Cuando se escriben expresiones regulares en Python siempre se pone `r` delante de la cadena. Esto le da una pista a Python de que la cadena puede contener caracteres especiales que no son para Python en sí, sino para la expresión regular.

## blog.urls

Crea un nuevo archivo vacío `blog/urls.py`. ¡Muy bien! Agrega estas primeras dos líneas:

    python
    from django.conf.urls import url
    from . import views
    

Aquí sólo estamos importando métodos de Django y todas nuestras `vistas` de la aplicación del `blog` (aún no tenemos ninguna, pero llegaremos a eso en un minuto!)

Luego de esto, podemos agregar nuestro primer patrón URL:

    python
    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
    ]
    

Como puedes ver, ahora estamos asignando una vista `view` llamada `post_list` al URL `^$`. Esta expresión regular coincidirá con `^` (un inicio) seguido de `$` (un final), por lo tanto sólo una cadena vacía coincidirá. Es correcto, porque en el sistema de resolución de URL de Django, 'http://127.0.0.1:8000/' no forma parte de la URL. Este patrón le dirá a Django que `views.post_list` es el lugar correcto al que ir si alguien entra a tu sitio web con la dirección 'http://127.0.0.1:8000/'.

La última parte `name='post_list'` es el nombre de la URL que se utilizará para identificar a la vista. Puede coincidir con el nombre de la vista pero también puede ser algo completamente distinto. Utilizaremos las URL con nombre más delante en el proyecto así que es importante darle un nombre a cada URL de la aplicación. También deberíamos intentar mantener los nombres de las URL únicos y fáciles de recordar.

¿Todo bien? Abre http://127.0.0.1:8000/ en tu navegador para ver el resultado.

![Error][2]

 [2]: images/error1.png

Ya no hay un "Funciona", ¿eh? No te preocupes, es sólo una página de error, ¡no hay nada que temer!. En realidad son muy útiles:

Puedes leer que no hay ningún **atributo 'post_list'**. ¿Recuerdas *post_list* de algo? ¡Así es como habíamos llamado a nuestra vista! Esto quiere decir que tenemos todo en su lugar pero todavía no hemos creado la *vista*. No te preocupes, ya llegaremos a eso.

> Si quieres saber más sobre Django URLconfs, mira la documentación oficial: https://docs.djangoproject.com/en/1.8/topics/http/urls/