> Parte de esta sección está basada en tutoriales de Geek Girls Carrots (http://django.carrots.pl/).
> 
> Parte de este capítulo está basada en el [django-marcador tutorial](http://django-marcador.keimlink.de/) bajo licencia Creative Commons Attribution-ShareAlike 4.0 internacional. El tutorial de django-marcador tiene derechos de autor de Markus Zapke-Gündemann et al.

## Entorno virtual

Antes de instalar Django, instalaremos una herramienta extremadamente útil que ayudará a mantener tu entorno de desarrollo ordenado en tu computadora. Es posible saltarse este paso, pero es altamente recomendable. ¡Empezar con la mejor configuración posible te ahorrará muchos problemas en el futuro!

Así que, vamos a crear un **entorno virtual** (también llamado un *virtualenv*). Virtualenv aísla tu configuración de Python/Django por cada proyecto. Esto quiere decir que cualquier cambio que hagas en un sitio web no afectará a ningún otro que estés desarrollando. Genial, ¿no?

Todo lo que necesitas hacer es encontrar un directorio en el que quieras crear el `virtualenv`; tu directorio home, por ejemplo. En Windows puede verse como `C:\Users\Name` (donde `Name` es el nombre de tu usuario).

Para este tutorial usaremos un nuevo directorio `djangogirls` en tu directorio home:

    mkdir djangogirls
    cd djangogirls
    

Haremos un virtualenv llamado `myvenv`. El comando general estará en el formato:

    python3 -m venv myvenv
    

### Windows

Para crear un nuevo `virtualenv`, debes abrir la consola (te lo indicamos unos cuantos capítulos antes, ¿recuerdas?) y ejecuta `C:\Python34\python -m venv myvenv`. Se verá así:

    C:\Users\Name\djangogirls> C:\Python34\python -m venv myvenv
    

en donde `C:\Python34\python` es el directorio en el que instalaste Python previamente y `myvenv` es el nombre de tu `virtualenv`. Puedes utilizar cualquier otro nombre, pero asegúrate de usar minúsculas y no usar espacios, acentos o caracteres especiales. También es una buena idea mantener el nombre corto. ¡Vas a referirte a él mucho!

### Linux y OS X

Crear un `virtualenv` en Linux y OS X es tan simple como ejecutar `python3 -m venv myvenv`. Se verá así:

    ~/djangogirls$ python3 -m venv myvenv
    

`myvenv` es el nombre de tu `virtualenv`. Puedes usar cualquier otro nombre, pero sólo utiliza minúsculas y no incluyas espacios. También es una buena idea mantener el nombre corto. ¡Vas a referirte muchas veces a él!

> **NOTA:** Iniciar el entorno virtual en Ubuntu 14.04 de esta manera produce el siguiente error:
> 
>     Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1
>     
> 
> Para evitar esto, utiliza directamente el comando `virtualenv`.
> 
>     ~/djangogirls$ sudo apt-get install python-virtualenv
>     ~/djangogirls$ virtualenv --python=python3.4 myvenv
>     

## Trabajar con virtualenv

El comando anterior creará un directorio llamado `myvenv` (o cualquier nombre que hayas elegido) que contiene nuestro entorno virtual (básicamente un montón de archivos y carpetas).

#### Windows

Inicia el entorno virtual ejecutando:

    C:\Users\Name\djangogirls> myvenv\Scripts\activate
    

#### Linux y OS X

Inicia el entorno virtual ejecutando:

    ~/djangogirls$ source myvenv/bin/activate
    

¡Recuerda reemplazar `myvenv` con tu nombre de `virtualenv` que hayas elegido!

> **NOTA:** a veces `source` podría no estar disponible. En ese caso trata hacerlo de esta forma:
> 
>     ~/djangogirls$ . myvenv/bin/activate
>     

Sabrás que tienes `virtualenv` iniciado cuando veas que la línea de comando tiene este aspecto:

    (myvenv) C:\Users\Name\djangogirls>
    

o:

    (myvenv) ~/djangogirls$
    

¡Nota que el prefijo `(myvenv)` aparece!

Cuando trabajes en un entorno virtual, `python` automáticamente se referirá a la versión correcta, de modo que puedes utilizar `python` en vez de `python3`.

Ok, tenemos todas las dependencias importantes en su lugar. ¡Finalmente podemos instalar Django!

## Instalar Django

Ahora que tienes tu `virtualenv` iniciado, puedes instalar Django usando `pip`. En la consola, ejecuta `pip install django==1.8` (fíjate que utilizamos un doble signo igual: `==`).

    (myvenv) ~$ pip install django==1.8
    Downloading/unpacking django==1.8
    Installing collected packages: django
    Successfully installed django
    Cleaning up...
    

En Windows

> Si obtienes un error al ejecutar pip en Windows comprueba si la ruta de tu proyecto contiene espacios, acentos o caracteres especiales (por ejemplo, `C:\Users\User Name\djangogirls`). Si lo tiene, por favor considera moverla a otro lugar sin espacios, acentos o caracteres especiales (sugerencia: `C:\djangogirls`). Después de moverla ejecuta nuevamente el comando anterior.

en Linux

> Si obtienes un error al ejecutar pip en Ubuntu 12.04 ejecuta `python -m pip install- U - force-resintall pip` para arreglar la instalación de pip en el virtualenv.

¡Eso es todo! Ahora estás lista (por fin) para crear una aplicación Django!