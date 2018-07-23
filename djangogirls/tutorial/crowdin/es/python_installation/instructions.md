> Esta sección está basada en un tutorial por Geek Girls Carrots (http://django.carrots.pl/)

Django está escrito en Python. Necesitamos Python para hacer cualquier cosa en Django. ¡Vamos a empezar con la instalación! Queremos que instales Python 3.4, así que si tienes alguna versión anterior, deberás actualizarla.

### Windows

Puedes descargar Python para Windows desde el sitio web https://www.python.org/downloads/release/python-343/. Después de descargar el archivo ***.msi**, debes ejecutarlo (haz doble click en el archivo) y sigue las instrucciones. Es importante recordar la ruta (el directorio) donde se ha instalado Python. ¡Será necesario más adelante!

Algo para tener en cuenta: en la segunda pantalla del asistente de instalación, llamada "Customize", asegúrate de ir hacia abajo y elegir la opción "Add python.exe to the Path", como se muestra aquí:

![No te olvides de agregar Python al Path](../python_installation/images/add_python_to_windows_path.png)

### Linux

Es muy posible que ya tengas Python instalado de serie. Para verificar que ya lo tienes instalado (y qué versión es), abre una consola y escribe el siguiente comando:

    $ python3 --version
    Python 3.4.2
    

Si no tienes instalado Python o si deseas una versión diferente, puedes instalarla de la siguiente manera:

#### Debian o Ubuntu

Escribe este comando en tu consola:

    sudo apt-get install python3.4
    

#### Fedora (hasta 21)

Usa este comando en tu consola:

    sudo yum install python3.4
    

#### Fedora (22 +)

Usa este comando en tu consola:

    $ sudo dnf instalar python3.4
    

### OS X

Debes ir al sitio web https://www.python.org/downloads/release/python-342/ y descargar el instalador de Python:

  * Descargar el archivo *Mac OS X 64-bit/32-bit installer*,
  * Haga doble clic en *python-3.4.3-macosx10.6.pkg* para ejecutar al instalador.

Verifica que la instalación fue correcta abriendo la aplicación de *Terminal* y ejecutando el comando `python3`:

    $ python3 --version
    Python 3.4.2
    

* * *

Si tienes alguna duda o si algo salió mal y no sabes cómo resolverlo - ¡pide ayuda a tu tutor! A veces las cosas no van bien y que es mejor pedir ayuda a alguien con más experiencia.