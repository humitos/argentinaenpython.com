.. title: ¿Donde está humitos?
.. slug: donde-esta-humitos
.. date: 2014-11-24 13:50:09 UTC-03:00
.. tags: argentina en python, mapas, blog, python
.. link: 
.. description: Este mapa es útil para saber en qué lugar estoy *aproximadamente* en este momento y cual es la ruta aproximada *planificada* a futuro
.. type: text
.. previewimage: preview.jpg
.. template: storymap.tmpl

.. raw:: html

   <style>
     ul.simple {
         list-style: none;
     }
   </style>

Este mapa es útil para saber en qué lugar estoy *aproximadamente* en
este momento y cual es la ruta aproximada *planificada* a futuro, con
el fin de :doc:`contactar con gente de la zona <contacto>` para así
poder :doc:`coordinar algo relacionado al proyecto
<eventos/organizar>` (u otra cosa de interés mutuo) y organizar para
encontrarnos en las cercanías.


* |destinos| destinos que tenemos pensado visitar en los próximos meses
* |visitados| lugares visitados desde el inicio del proyecto

.. |destinos| image:: /assets/img/marker-icon-red.png
.. |visitados| image:: /assets/img/marker-icon-green.png

.. raw:: html

   <div id="map"></div>

¿Cómo funciona este mapa?
-------------------------

En pocas palabras, cuando me conecto a internet se envía una señal a
mi blog para que actualice la posición en la que me encuentro,
utilizando la información de la conexión a internet para saber dónde
estoy.

Como el proceso es automático, permite que tenga una actualización
mucho más precisa a la que yo le podría dar concientemente cada vez
que cambio de posición.

----

¿Cómo funciona *exactamente*... ?
---------------------------------

En profundidad, lo que hago es, mediante javascript, descargo el
archivo `my-position.json` que es dónde están las coordenadas de mi
posición actual y lo muestro en el mapa:

.. listing:: donde-esta-humitos/geolocation.js javascript
   :start-line: 115
   :end-line: 133


#. Descarga el archivo `my-position.json`
#. Crea el ícono del autito
#. Agrega el punto que está en `my-position.json` al mapa
#. Centra el mapa en esa posición


Ese `my-position.json` lo genero con un script Python.

.. listing:: donde-esta-humitos/geolocation.py python
   :start-line: 164
   :end-line: 181


#. Utiliza la librería *geocoder* para obtener las coordenadas de mi
   dirección de IP
#. Loguea todo el proceso para, en caso de haber un error, saber qué
   ocurrió
#. Guarda en el archivo `my-position.json` la longitud y latitud
#. Sube el nuevo `my-position.json` (con las nuevas coordenadas) al
   servidor utilizando `scp`

.. note::

   Utilizo un `time.sleep(WAIT_BEFORE_QUERY)` así le doy un tiempo a
   NM para tener acceso a internet.


Ese script Python lo ejecuto con NetworkManager cuando este se conecta
a una red.

.. listing:: donde-esta-humitos/geoblog bash

.. note::

   Este script va copiado en la carpeta
   `/etc/NetworkManager/dispatch.d/geoblog` y *root* tiene que ser el
   owner del archivo para que NM lo ejecute correctamente.

Básicamente lo que hace es ejecutar el script Python `geolocation.py`
si la interfaz es levantada (*up*).

.. note::

   Es necesario usar *&* al final de cada comando así se ejecuta en
   background ya que NetworkManager `tiene un bug
   <https://bugzilla.redhat.com/show_bug.cgi?id=982734>`_ que mata los
   scripts si demoran más de 3 segundos. Como yo necesito acceso a
   internet para comprobar mi posición, me lo estaba matando.

¡Eso es todo!
