.. title: Aprendé Python con Software Libre
.. slug: aprende-python-con-software-libre
.. date: 2015-10-23 12:36:10 UTC-03:00
.. tags: 
.. category: 
.. link: 
.. description: ¿Hace mucho querés aprender Python y colaborar en un proyecto de Software Libre? ¡Hoy es tu oportunidad!
.. type: text

¿Hace mucho querés aprender Python y colaborar en un proyecto de
Software Libre? ¡Hoy es tu oportunidad!

En :doc:`Argentina en Python <index>` tenemos algunos proyectos que
nos gustaría empujar y captar más programadores para que nos ayuden en
su desarrollo y mantenimiento a futuro. La idea es colaborar con estos
proyectos a modo de `mentorship
<https://es.wikipedia.org/wiki/Mentor%C3%ADa>`_ por parte nuestra para
que de paso vayas aprendiendo Python en el camino. ¿Suena interesante
no?

Los proyectos que tenemos "a medio desarrollo" al día de la fecha,
son:

* `Tutorial de Python <https://github.com/PyAr/tutorial/>`_:
  traducción oficial del tutorial de Python realizada por Python
  Argentina.

  * Lo principal que necesita el tutorial es una versión en `.epub`
    para dispositivos móviles.
  * Además un mantenimiento constante en cuanto a sus traducciones.

* `uPOI <https://github.com/humitos/osm-pois/>`_: sitio web read-only
  sobre Puntos de Interés utilizando los mapas de OpenStreetMap.

  * Necesitamos hacer una migración de `static site` a una versión en
    Django que sea read-write (con la posibilidad de agregar puntos
    por los usuarios) y así crear sus propios mapas.

  * Cada mapa creado por el usuario deberá poder exportar los datos de
    POIs en diferentes formatos: GPX, GeoJSON, etc.

  * Esos mapas deberán tener una dirección única, por ejemplo:
    http://pyar.upoi.org, para mostrar el mapa de miembros de Python
    Argentina.

* `PyFi Spot <https://github.com/humitos/pyfispot/>`_: portal cautivo
  desarrollado en Python + Flask.

  * Falta un sistema de administración de usuarios, servicios
    (start/stop/etc) y manejo de datos.

  * Mejoras y optimizaciones en las reglas *iptables* y configuraciones
    de los programas utilizados.

Todos los proyectos se encuentran en GitHub.com, por lo que si te
interesa participar en uno y ser guiado por nosotros, no dudes en
escribirnos, seleccionar un issue, hacer algunas preguntas y ponerte a
trabajar. Una vez que hayas completado la tarea, realizas un PR [#]_ y
analizamos juntos el conjunto de cambio en caso de que haya que hacer
algunas modificaciones.

¡Te esperamos!

.. [#] si no sabes como se realiza, ¡te podemos ayudar!
