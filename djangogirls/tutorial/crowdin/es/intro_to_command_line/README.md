# Introducción a la interfaz de línea de comandos

Es emocionante, ¿verdad? Vas a escribir tu primera línea de código en pocos minutos :)

**Permítenos presentarte a tu primer nuevo amigo: ¡la línea de comandos!**

Los siguientes pasos te mostrarán cómo usar aquella ventana negra que todos los hackers usan. Puede parecer un poco aterrador al principio pero es solo un mensaje en pantalla que espera a que le des órdenes.

> **Nota** Tenga en cuenta que a lo largo de este libro usamos los términos 'directorio' y 'carpeta' indistintamente pero son la misma cosa.

## ¿Qué es la línea de comandos?

La ventana que se llama generalmente la **línea de comandos** o la **interfaz de línea de comandos**, es una aplicación basada en texto para ver, manejar y manipular archivos en tu ordenador. Al igual que Windows Explorer o Finder en Mac, pero sin la interfaz gráfica. Otros nombres para la línea de comandos son: *cmd*, *CLI*, *símbolo del sistema*, *consola* o *terminal*.

## Abrir la interfaz de línea de comandos

Lo primero que debemos hacer para empezar a experimentar con nuestra interfaz de línea de comandos es abrirla.

### Windows

Ir al menú Inicio → Todos los programas → Accesorios → Command Prompt

### Mac OS X

Aplicaciones → Servicios → Terminal

### Linux

Está probablemente en Aplicaciones → Accesorios → Terminal, pero eso depende de tu distribución. Si no lo encuentras, Googlealo :)

## Prompt

Ahora deberías ver una ventana blanca o negra que está esperando tus órdenes.

Si estás en Mac o Linux, probablemente verás `$`, así:

    $
    

En Windows, es un signo así `>`, como este:

    >
    

Cada comando será precedido por este signo y un espacio, pero no tienes que escribirlo. Tu computadora lo hará por ti :)

> Sólo una pequeña nota: en tu caso puede que haya algo como `C:\Users\ola>` o `Olas-MacBook-Air:~ ola$` antes del prompt y eso está perfecto. En este tutorial lo simplificaremos lo más posible.

## Tu primer comando (¡BIEN!)

Vamos a empezar con algo simple. Escribe este comando:

    $ whoami
    

o

    > whoami
    

Y pulsa `intro`. Este es nuestro resultado:

    $ whoami olasitarska
    

Como puedes ver, el ordenador ha imprimido tu nombre de usuario. Genial, ¿eh?:)

> Trata de escribir cada comando, no copies y pegues. ¡Te acordarás más de esta manera!

## Fundamentos

Cada sistema operativo tiene un conjunto diferente de comandos para la línea de comandos, así que asegúrate de seguir las instrucciones para tu sistema operativo. Vamos a intentarlo, ¿de acuerdo?

### Directorio actual

Estaría bien saber dónde estamos ahora, ¿verdad? Vamos a ver. Escribe este comando y pulsa `intro`:

    $ pwd
    /Users/olasitarska
    

Si estás en Windows:

    > cd 
    C:\Users\olasitarska
    

Probablemente verás algo similar en tu máquina. Una vez que abres la línea de comandos generalmente empiezas en el directorio home de tu usuario.

> Nota: 'pwd' significa 'print working directory' - en español, 'mostrar directorio de trabajo'.

* * *

### Listar ficheros y directorios

¿Qué hay aquí? Sería bueno saber. Veamos:

    $ ls
    Applications
    Desktop
    Downloads
    Music
    ...
    

Windows:

    > dir
    Directory of C:\Users\olasitarska
    05/08/2014 07:28 PM <DIR> Applications
    05/08/2014 07:28 PM <DIR> Desktop
    05/08/2014 07:28 PM <DIR> Downloads
    05/08/2014 07:28 PM <DIR> Music
    ...
    

* * *

### Cambia el directorio actual

Ahora, vayamos a nuestro directorio Desktop, el escritorio:

    $ cd Desktop
    

Windows:

    > cd Desktop
    

Comprueba si realmente ha cambiado:

    $ pwd 
    /Users/olasitarska/Desktop
    

Windows:

    > cd 
    C:\Users\olasitarska\Desktop
    

¡Aquí está!

> Truco pro: si escribes `cd D` y luego pulsas `tab` en el teclado, la línea de comandos automáticamente completará el resto del nombre para que puedas navegar más rápido. Si hay más de una carpeta que empiece con "D", presiona el botón `tab` dos veces para obtener una lista de opciones.

* * *

### Crear directorio

¿Qué tal si creamos un directorio de práctica en el escritorio? Lo puedes hacer de esta manera:

    $ mkdir practice
    

Windows:

    > mkdir practice
    

Este pequeño comando creará una carpeta con el nombre `practice` en el escritorio. ¡Puedes comprobar si está ahí mirando en el escritorio o ejecutando el comando `ls` o `dir`! Inténtalo :)

> Truco pro: Si no quieres escribir una y otra vez los mismos comandos, prueba pulsando la `flecha arriba` y la `flecha abajo` de tu teclado para ir pasando por los comandos utilizados recientemente.

* * *

### ¡Ejercicios!

Un pequeño reto para ti: en el recién creado directorio `practice` crea un directorio llamado `test`. Utiliza los comandos `cd` y `mkdir`.

#### Solución:

    $ cd practice
    $ mkdir test
    $ ls
    test
    

Windows:

    > cd practice
    > mkdir test
    > dir
    05/08/2014 07:28 PM <DIR> test
    

¡Enhorabuena! :)

* * *

### Limpieza

No queremos dejar un lío, así que vamos a eliminar todo lo que hemos hecho hasta este momento.

En primer lugar, tenemos que volver al escritorio:

    $ cd ..
    

Windows:

    > cd ..
    

Usar `..` con el comando `cd` hará que cambie el directorio actual al directorio padre (es el que contiene el directorio actual).

Revisa dónde estás:

    $ pwd 
    /Users/olasitarska/Desktop
    

Windows:

    > cd 
    C:\Users\olasitarska\Desktop
    

Es el momento de eliminar el directorio `practice`:

> **Atención**: Eliminar archivos utilizando `del`, `rmdir` o `rm` hace que no puedan recuperarse, lo que significa que los *archivos borrados desaparecerán para siempre* Así que ten mucho cuidado con este comando.

    $ rm -r practice
    

Windows:

    > rmdir /S practice
    practice, Are you sure <Y/N>? Y
    

¡Hecho! Para asegurarnos de que realmente se ha eliminado, vamos a comprobarlo:

    $ ls
    

Windows:

    > dir
    

### Salida

¡Esto es todo por ahora! Ya puedes cerrar la línea de comandos sin problema. Vamos a hacerlo al estilo hacker, ¿vale?:)

    $ exit
    

Windows:

    > exit
    

Genial, ¿no? :)

## Resumen

Aquí hay una lista de algunos comandos útiles:

| Comando (Windows) | Comando (Mac OS / Linux) | Descripción                  | Ejemplo                                           |
| ----------------- | ------------------------ | ---------------------------- | ------------------------------------------------- |
| exit              | exit                     | Cierra la ventana            | **exit**                                          |
| cd                | cd                       | Cambia el directorio         | **cd test**                                       |
| dir               | ls                       | Lista directorios/archivos   | **dir**                                           |
| copy              | cp                       | Copia de archivos            | **copy c:\test\test.txt c:\windows\test.txt** |
| move              | mv                       | Mueve archivos               | **move c:\test\test.txt c:\windows\test.txt** |
| mkdir             | mkdir                    | Crea un nuevo directorio     | **mkdir testdirectory**                           |
| del               | rm                       | Elimina archivos/directorios | **del c:\test\test.txt**                        |

Estos son sólo unos pocos de los comandos que se pueden ejecutar en la línea de comandos, pero hoy no vas a utilizar ninguno más.

Si tienes curiosidad, [ss64.com][1] contiene una referencia completa de comandos para todos los sistemas operativos.

 [1]: http://ss64.com

## ¿Lista?

¡Vamos a sumergirnos en Python!