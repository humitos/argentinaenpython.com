#!/usr/bin/env python3

EMAIL_CONFIRMATION = {
    'subject': 'Confirmación: Taller Django Girls en {city}',
    'body': '''Hola!

Te escribimos para comentarte que tu asistencia está *CONFIRMADA* para
participar en el evento "Taller Django Girls en {city}".

Fecha: {date}

Hora: {hour}.

Lugar: {place}

Web: {url}

Recordá que necesitás llevar una notebook/laptop para trabajar con
ella durante todo el día ya que no contamos con máquinas en el
auditorio.

Es importante que descargues previamente los recursos necesarios para
poder hacer el taller. Hemos creado un solo archivo para que este
proceso sea mucho más fácil. Descargalo de aquí (~175 Mb):

​http://argentinaenpython.com.ar/django-girls/djangogirls-recursos.zip

Como último favor, te pedimos que contestes este email para
confirmarnos que vas a asistir ya que hemos sobrepasado la cantidad de
inscriptos y hemos creado una lista de espera. Entonces, *cualquier
inconveniente* que tengas y no puedas asistir al taller, envianos un
email así otro puede ocupar ese lugar.

Si no contestas este email confirmando tu asistencia hasta {days} días
antes del evento, lamentablemente perderás tu cupo.

Además, te recomendamos que nos sigas en las redes sociales para estar
al tanto de las últimas novedades sobre este taller y otros eventos de
programación en Python que organizamos:

 * Twitter: https://twitter.com/argenpython/
 * Facebook: http://facebook.com/argentinaenpython/

Muchas gracias,

--

Manuel Kaufmann
-- ​http://argentinaenpython.com.ar/'''
}

EMAIL_WAITING_LIST = {
    'subject': 'Lista de espera: Taller Django Girls en {city}',
    'body': ''' Hola!

Te escribimos para comentarte que estás en *LISTA DE ESPERA* para
participar en el evento "Taller Django Girls en {city}"

Fecha: {date}

Hora: {hour}.

Lugar: {place}

Web: ​​{url}

Debido a que sobrepasamos el número de inscriptos disponibles para el
lugar, se hizo una selección basada en los formularios de registración
y has quedado en lista de espera.

¿Esto que quiere decir? La lista de espera es para aquellas personas
que quedaron seleccionadas pero que no podemos confirmar debido a la
cantidad de lugares que hay en el aula. En caso de que alguno de los
asistentes confirmados nos informe que no pueda concurrir el día del
taller, nos vamos a poner en contacto con vos para confirmar tu
asistencia.

Sí aún sigues interesada en participar, por favor responde a este
email.

Además, te recomendamos que nos sigas en las redes sociales para estar
al tanto de las últimas novedades sobre este taller y otros eventos de
programación en Python que organizamos:

 * Twitter: https://twitter.com/argenpython/
 * Facebook: http://facebook.com/argentinaenpython/

Muchas gracias,

--

Manuel Kaufmann
-- ​http://argentinaenpython.com.ar/'''
}

EMAIL_COACH = {
    'subject': 'Guía: Taller Django Girls en {city}',
    'body': '''Hola!

Te escribimos para comentarte que tu asistencia está *CONFIRMADA* para
participar en el evento "Taller Django Girls en {city}" como *GUÍA /
COACH*. ¡Muchísimas gracias! Este evento no podría ser posible sin tu
ayuda.

Fecha: {date}

Hora: {hour}.

Lugar: {place}

Web: ​{url}

Es importante que nos encontremos todos los que vamos a ser Guías una
media hora antes de comenzar el evento (a las 8 AM será la reunión)
así podemos conocernos y conversar previamente para coordinar cómo
será la jornada completa. Tené en cuenta que la idea de ser guía es
justamente ser eso: un guía, y no "hacer nosotros los ejercicios",
sino ayudarlos a que lo completen ellos solos, motivándolos a
investigar y resolver sus propios problemas a conciencia.

Además, te pedimos que leas la guía que Django Girls ha preparado para
los guías así todos seguimos la misma dinámica para el evento:

​http://coach.djangogirls.org/

Es importante que descargues previamente los recursos necesarios para
que los asistentes realicen el taller y lleves su contenido
descomprimido en un pendrive. Esto nos servirá en caso de tener algún
inconveniente con Internet y/o para acelerar el proceso.

Hemos creado un solo archivo para que este proceso sea mucho más
fácil. Descargalo de aquí (~175 Mb):

​http://argentinaenpython.com.ar/django-girls/djangogirls-recursos.zip

Como último favor, te pedimos que contestes este email para
confirmarnos que vas a asistir ya que hemos sobrepasado la cantidad de
inscriptos y hemos creado una lista de espera. Entonces, *cualquier
inconveniente* que tengas y no puedas asistir al taller, envianos un
email.

Si no contestas este email confirmando tu asistencia hasta {days} días
antes del evento, lamentablemente perderás tu cupo.

Además, te recomendamos que nos sigas en las redes sociales para estar
al tanto de las últimas novedades sobre este taller y otros eventos de
programación en Python que organizamos:

 * Twitter: https://twitter.com/argenpython/
 * Facebook: http://facebook.com/argentinaenpython/

Muchas gracias,

--

Manuel Kaufmann
-- ​http://argentinaenpython.com.ar/'''
}


EMAIL_SURVEY = {
    'subject': 'Comentarios post Django Girls',
    'body': '''Hola,

Nos gustaría saber tu opinión sobre el "Taller de programación para
mujeres" que se realizó el {date} en {place}. Para eso hemos creado
una pequeña encuesta donde podés dejarnos tu opinión de forma anónima
y ayudarnos a mejorar los próximos talleres.

Ingresando al siguiente link podrás responder todas las preguntas que
quieras y dejarnos tus comentarios y/o sugerencias.

{link}

¡Muchas gracias!

--

Manuel Kaufmann
-- ​http://argentinaenpython.com.ar/'''
}

DATE = 'Sábado 9 de Enero de 2016'
HOUR = '8:30hs (puntual) a 18:30hs'
PLACE = 'Laboratoria LA (Ave. Pardo 601 oficina 1104 - Piso 11, Miraflores, Lima, Perú)'
CITY = 'Lima'
URL = 'http://argentinaenpython.com.ar/django-girls-lima/'
DAYS = 5

emails = [EMAIL_CONFIRMATION, EMAIL_WAITING_LIST, EMAIL_COACH]

for email in emails:
    for k, v in email.items():
        print(k.upper())
        print('-' * len(k), end='\n\n')
        print(v.format(
            date=DATE,
            hour=HOUR,
            place=PLACE,
            city=CITY,
            url=URL,
            days=DAYS,
        ), end='\n\n')

    input('Presiona una tecla para ver el siguiente email...')
