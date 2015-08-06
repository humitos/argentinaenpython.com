.. title: Donaciones para arreglo de vehículo
.. slug: donaciones/arreglo-de-vehiculo
.. date: 2015-04-06 11:12:58 UTC-03:00
.. tags: donaciones, argentina en python
.. link: 
.. description: 
.. type: text
.. nocomments: True

.. class:: alert alert-success

   ¡Batiendo records! Llegamos a recaudar el dinero necesario en menor
   tiempo de lo esperado, y además, sobrepasamos el monto total.

.. class:: alert alert-info

   De cualquier modo, si querés apoyar económicamente al proyecto para
   futuros eventos, :doc:`hacé click aquí <donaciones>`.

Luego de mucho esfuerzo, hemos llegado a una etapa del viaje donde se
empiezan a notar los hitos alcanzados [#]_ [#]_ [#]_ [#]_ [#]_ como
así también las complicaciones económicas para seguir adelante. Y
como todo buen programador, ya habiendo hecho los tests
correspondiente, veo que algunos empiezan a fallar cuando son
proyectados a futuro.

::

   test_sprint_resistencia (tests.test_Sprint_resistencia.SprintResistencia) ... ok
   test_cubiertas_delanteras (tests.test_peugeot206.Peugeot206) ... ok
   test_aceite_y_filtros (tests.test_peugeot206.Peugeot206) ... ok
   test_bateria (tests.test_peugeot206.Peugeot206) ... FAIL
   test_bieleta (tests.test_peugeot206.Peugeot206) ... FAIL
   test_cubiertas_traseras (tests.test_peugeot206.Peugeot206) ... FAIL
   test_pyday_formosa (tests.test_pyday_formosa.PyDayFormosa) ... ok
   test_pyday_asuncion (tests.test_pyday_asuncion.PyDayAsuncion) ... ok

   ======================================================================
   FAIL: test_bateria (tests.test_peugeot206.Peugeot206)
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "./test_peugeot206.py", line 71, in test_bateria
       self.assertGreaterThan(MONEY, 0)
   AssertionError: 'Not enought money'

   ======================================================================
   FAIL: test_vieleta (tests.test_peugeot206.Peugeot206)
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "./test_peugeot206.py", line 71, in test_vieleta
       self.assertGreaterThan(MONEY, 0)
   AssertionError: 'Not enought money'

   [...]

   ----------------------------------------------------------------------
   Ran 8 tests in 0.214s

   FAILED (failures=3)


Es por eso que hemos habilitado una nueva página de donaciones con el
objetivo de reparar los daños que ha estado sufriendo el auto en los
últimos meses. Si bien *errante*, nuestro auto estrella, no tiene
nada que esté **sumamente roto** hay algunas piezas que ya se *hacen
notar* y que requieren la atención de un mecánico. Estas piezas son:

* Batería ($ 1200)
* Bieleta ($ 250)
* Cubiertas traseras ($ 2200)
* Circuito eléctrico ($ 1500)
* Mano de obra ($ 850)

Eso da un total de $ 6000 (**USD 600**) [#]_, aproximadamente.

La **fecha límite** para realizar las donaciones es el **15 de Mayo de
2015** ya que cerca de esa fecha estamos dejando la Argentina (luego
del evento `SciPy Latinoamérica <http://scipyla.org/conf/2015/>`_) y
queremos aprovechar a hacer los arreglos allí para abaratar los
costos.

 *Todo el dinero recaudado* será utilizado para el mantenimiento del
 vehículo.

Como forma de agradecimiento personal y del proyecto :doc:`Argentina
en Python <index>`, vamos a agregar tu nombre / empresa a la
:doc:`lista de colaboradores <donaciones/colaboradores>` y si te
parece apropiado también pondremos el logo en esta página y el monto
donado. Además de un Tweet en la cuenta de `@argenpython
<http://twitter.com/argenpython/>`_ el día de la donación y
agradecimientos en un `post
<http://elblogdehumitos.com.ar/posts/el-destino-de-tu-donacion/>`_ que
se escribirá luego de concluídos los arreglos.

Al día de la fecha hemos recibido un total de *$ 11620.15 (193.67%)* en
esta etapa de donaciones.

.. raw:: html

   <div class="progress" style="width: 70%; height: 40px; margin-left: auto; margin-right: auto;">
     <div class="progress-bar progress-bar-success progress-bar-striped active" role="progressbar" style="width: 52%;">
       <div style="margin-top: 10px;">100 %</div>
     </div>

     <div class="progress-bar progress-bar progress-bar-striped active" role="progressbar" style="width: 48%;">
       <div style="margin-top: 10px;">93.67 %</div>
     </div>
   </div>

Hacé click en el siguite botón para enterarte sobre cuáles son los
medios disponibles a la fecha para realizar las donaciones:

.. raw:: html

   <div style="text-align: center; margin-top: 25px; margin-bottom: 25px;">
     <a class="btn btn-lg btn-primary" href="/donaciones/medios/">
       Realizar donación
     </a>
   </div>

.. class:: lead align-center

   ¡Muchas gracias por colaborar!

----

.. [#] `#PyDayAsunción: un éxito arrollador
       <http://elblogdehumitos.com.ar/posts/pydayasuncion-un-exito-arrollador/>`_
.. [#] `PyDay Formosa <http://elblogdehumitos.com.ar/posts/pyday-formosa/>`_
.. [#] `Primer Sprint de Python en Resistencia, Chaco
       <http://elblogdehumitos.com.ar/posts/primer-sprint-de-python-en-resistencia-chaco/>`_
.. [#] `Charla abierta de OpenStreetMap en Las Breñas
       <http://elblogdehumitos.com.ar/posts/charla-abierta-de-openstreetmap-en-las-brenas/>`_
.. [#] `Curso de Python en Paraná
       <http://elblogdehumitos.com.ar/posts/curso-de-python-en-parana/>`_
.. [#] los precios están basados en los listados de Mercado Libre Argentina
