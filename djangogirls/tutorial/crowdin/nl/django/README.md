# Wat is Django?

Django (*/ˈdʒæŋɡoʊ/ jang-goh*) is een gratis en open source web-applicatie framework, geschreven in Python. Een web-framework is een set onderdelen die je helpen om sneller en makkelijker websites te maken.

Als je een website aan het bouwen bent, dan heb je altijd een vergelijkbare set aan onderdelen nodig: een manier om met gebruikersauthenticatie om te gaan (registreren, inloggen, uitloggen), een beheerderspaneel voor de website, formulieren, een manier om bestanden te uploaden, etc.

Gelukkig hebben andere mensen lang geleden al ondekt dat webontwikkelaars eenzelfde soort problemen ondervinden wanneer ze een nieuwe site maken, dus besloten ze samen te werken en frameworks te ontwikkelen (Django is hier een van) die al gemaakte componenten geven die je kan gebruiken.

Frameworks bestaan om ervoor te zorgen dat je niet het wie opnieuw hoeft uit te vinden en je te helpen een deel van de lasten te verlichten wanneer je een nieuwe site bouwt.

## Waarom heb je een framework nodig?

Om te begrijpen waar Django nou precies voor is, moeten we eens een beter blik werpen op de servers. Het eerste wat een server moet weten is dat je wilt dat het je een webpagina 'served'.

Stel je een postbus (port) voor die binnenkomende brieven (requests) controleert. Dit wordt gedaan door een webserver. De webserver leest de brief en stuurt een reactie door middel van een webpagina. Maar wanneer je wat wilt sturen, heb je ook wat inhoud nodig. Django is iets wat je helpt de inhoud te creëren.

## Wat gebeurt er als iemand een website opvraagt van jouw server?

Wanneer een 'request' bij een webserver aankomt, wordt deze doorgestuurd naar Django, welke uit probeert te zoeken wat er nou precies is aangevraagd. Het neemt eerst het adres van de webpagina en probeert uit te zoeken wat te doen. Dit deel wordt gedaan door Django's **urlresolver** (het adres van een website wordt een URL genoemd - Uniform Resource Locator - dus de naam *urlresolver* is logisch). Het is niet heel slim - het neemt een lijst met patronen en probeert een overeenkomst met de URL te vinden. Django controleert de patronen van boven naar beneden en als iets overeen komt stuurt Django het 'request' door naar de bijbehorende functie (welke *view* wordt genoemd).

Stel je een postbode met een brief voor. Ze loopt langs de straat en controleert elk huisnummer met die op de brief. Wanneer het overeenkomt, brengt ze de brief daar. Dit is hoe de urlresolver werkt!

In de *view*functie worden alle interessante dingen gedaan: we kunnen naar een databse kijken om wat informatie te vinden. Misschien heeft de gebruiker gevraagd om iets in de data te wijzigen? Zoals een brief die zegt "Gelieve de beschrijving van mijn baan te wijzigen." De *view* kan controleren of je toestemming hebt om dit te doen, dan de beschrijving van je baan voor je updaten en een bericht terugsturen: "Gedaan!". Vervolgens genereert de *view* een reactie en kan Django dit naar de gebruikers website sturen.

Natuurlijk is de beschrijving hierboven een beetje vereenvoudigt, maar je hoeft nog niet alle technische dingen te begrijpen. Een algemeen idee van hoe het werkt is genoeg.

Dus inplaats van te veel in de details te gaan, zullen we simpelweg beginnen met iets in Django te maken en leren we de belangrijke onderdelen onderweg!