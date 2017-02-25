# Django-Modelle

Wir erstellen jetzt etwas damit wir alle Posts von unseren Blog speichern können. Aber um das zu tun, müssen wir zunächst über `Objekte` sprechen.

## Objekte

Eine Herangehensweise an das Programmieren ist das so genannte `objektorientierte Programmieren`. Die Idee dahinter ist, dass wir Dinge und ihre Interaktion miteinander modellieren können, an Stelle alles als langweilige Kette von Programmbefehlen hintereinanderzuschreiben.

Was ist denn nun ein Objekt? Ein Objekt ist eine Sammlung von Eigenschaften und Aktionsmöglichkeiten. Das klingt erst einmal kommisch, aber hier haben wir gleich ein Beispiel.

Wenn wir zum Beispiel eine Katze modellieren wollen, erschaffen wir ein Objekt `Katze`, welches einige Eigenschaften, z.B. `farbe`, `alter`, `Stimmung` (beispielsweise gut, schlecht oder müde ;)), `Besitzer` (dieser ist wiederum eine `Person`-Objekt oder die Eigenschaft bleibt, im Falle eines Streuners, leer).

Dann bekommt die `Katze` noch einige Aktionsmöglichkeiten: `schnurren`, `kratzen` oder `füttern` (hier bekäme die Katze ein bisschen `Katzenfutter`, welches wieder ein eigenes Objekt mit Eigenschaften wie zum Beispiel `Geschmack` sein könnte).

    Katze
    --------
    farbe
    alter
    stimmung
    besitzerin
    schnurren()
    kratzen()
    fuettern(katzenfutter)
    
    
    Katzenfutter
    --------
    geschmack
    

Der Gedanke dahinter ist also, echte Dinge mit Hilfe von Eigenschaften (genannt `Objekteigenschaften`) und Aktionsmöglichkeiten (genannt `Methoden`) im Programmcode zu beschreiben).

Wie also modellieren wir Blogposts? Schließlich wollen wir ja ein Blog bauen, nicht wahr?

Wir müssen folgende Frage beantworten: Was ist ein Blogpost? Welche Eigenschaften sollte er haben?

Nun, zum einen braucht unser Blogpost Text mit dem Inhalt und einem Titel, oder? Außerdem wäre es schön zu wissen, wer ihn geschrieben hat - wir brauchen also noch einen Autor. Schließlich wollten wir wissen, wann der Post geschrieben und veröffentlicht wurde.

    Post 
    -------- 
    titel 
    text 
    autor 
    datum_erstellung
    datum_veroeffentlichung
    

Was für Dinge könnte man mit einem Blogpost machen? Es wäre schön, wenn wir eine `Methode` hätten, die den Post veröffentlicht, nicht wahr?

Wir brauchen also eine `veröffentlichen`-Methode.

Da wir jetzt wissen, was wir erreichen wollen, können wir nun damit anfangen, es in Django zu formulieren!

## Ein Django-Modell

Da wir jetzt in etwa wissen, was ein Objekt ist, wollen wir ein Django-Modell für unsere Blogposts erstellen.

Ein Modell in Django ist ein spezielles Objekt - eines, das in unserer Datenbank gespeichert werden kann. Eine Datenbank ist erstmal eine Sammlung von Daten. Dies ist ein Ort, in dem Sie Informationen zu Benutzern, Ihre Blog-Posts, etc. speichern möchten. Wir benutzen dafür eine SQLite-Datenbank,. Dasist die Voreinstellung in Django - für uns wird das erst einmal ausreichen.

Du kannst dir ein Modell wie eine Tabelle mit Spalten ("Feldern", englisch "fields") und Zeilen (Datensätzen) vorstellen.

### Eine Applikation für unser Blog

Um unsere Webseite aufgeräumt zu halten, werden wir eine eigene Anwendung für unser Projekt erstellen, wir nennen das eine Applikation. Wir wollen uns gleich daran gewöhnen, alles ordentlich und sortiert zu halten. Um eine Applikation zu erstellen, müssen wir das folgende Kommando in der Konsole ausführen (wieder in dem `djangogirls`-Verzeichnis, in dem die `manage.py`-Datei liegt):

    (myvenv) ~/djangogirls$ python manage.py startapp blog
    

Wie du sehen kannst wurde ein neues `blog`-Verzeichnis erstellt welches schon einige Dateien enthält. Das Verzeichnis und die Dateien unseres Projektes sollten jetzt so aussehen:

    djangogirls 
    ├── mysite 
    | __init__.py
    | settings.py
    | urls.py 
    | wsgi.py 
    ├── manage.py 
    └── blog   
         ├── migrations
         | __init__.py 
         ├── __init__.py
         ├── admin.py 
         ├── models.py
         ├── tests.py    
         └── views.py
    

Nach dem Erstellen der Applikation müssen wir Django noch sagen, dass diese auch genutzt werden soll. Das können wir in der Datei `mysite/settings.py` einstellen. Wir suchen den Eintrag `INSTALLED_APPS` und fügen darin die Zeile `'blog',` direkt über der schließenden Klammer `)` ein. Das sollte dann so aussehen:

    python 
    INSTALLED_APPS = (
         'django.contrib.admin', 
         'django.contrib.auth', 
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages', 
         'django.contrib.staticfiles', 
         'blog', 
    )
    

### Das Blogpost-Modell

Alle Objekte bzw. Modelle unserer Applikation werden in der `blog/models.py`-Datei definiert. Dies ist also der richtige Platz für unser Blogpost-Modell.

Lass uns `blog/models.py` öffnen, lösche alles darin und schreibe Code wie diesen:

    python 
    from django.db import models 
    from django.utils import timezone 
    
    
    class Post(models.Model):  
       author = models.ForeignKey('auth.User') 
       title = models.CharField(max_length=200)
       text = models.TextField()  
       created_date = models.DateTimeField(    
               default=timezone.now)  
       published_date = models.DateTimeField(    
              blank=True, null=True) 
    
        def publish(self):     
          self.published_date = timezone.now()   
          self.save()   
    
       def __str__(self):    
         return self.title
    

> Kontrolliere nochmal, dass du zwei Unterstriche (`_`) vor und hinter dem `str` gesetzt hast. Diese Konvention wird häufig in Python benutzt und manchmal nennen wir es "dunder" (kur für Doppel Unterstrich).

Es sieht kompliziert aus, oder? Aber keine Sorge, wir werden erklären, was diese Zeilen bedeuten!

Die Zeilen die mit `from` oder `import` beginnen sind Zeilen, die PYthon sagen Sachen aus anderen Dateien mitzunutzen. Anstadt häufig genutzte Sachen in jede Date einzeln zu kopieren, können wir sie mit `... from ... import ... </0> einbinden. import ...`.

0>class Post(models.Model):</code> - Diese Zeile definiert unser Modell).

*   `class` ist ein spezielles Schlüsselwort, womit wir angeben dass wir hier ein Objekt definieren wollen.
*   `Post` ist der Name unseres Modells. Wir können ihm auch einen anderen Namen geben (aber wir müssen spezielle und Leerzeichen vermeiden). Beginne einen Klassenname immer mit einem Großbuchstaben.
*   `models.Model` meint, dass der Post ein Django Modell ist, so dass Django weiß, es soll in der Datenbank gespeichert werden.

Jetzt definieren wir die eigenschaften über die wir gesprochen haben: `title`, `text`, `created_date`, `published_date` und `author`. Um dies zu tun, müssen wir einen Typen für jedes Feld definieren. (Ist es Text? Eine Zahl? Ein Datum? Eine Beziehung zu einem anderen Objekt, bsp. ein Benutzer?).

*   `models.CharField` - dies ist wie du Text mit einer limitierten Anzahl an Zeichen definierst.
*   `models.TextField` - dies ist für langen Text ohne Limit. Klingt doch wie perfekt wie Blog Post Inhalte, richtig?
*   `models.DateTimeField` - dies ist ein Datum und eine Uhrzeit.
*   `models.ForeignKey` - dies ist eine Verlinkung zu einem anderen Model.

Wir werden nicht den gesamten Code hier erklären da es einfach zu lange dauern würde. Du solltest einen Blick auf die offizielle Dokumentation von Django werfen wenn du mehr über Modellfelder und wie man auch andere Dinge als die oben beschriebenen definiert, wissen möchtest (https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types).

Was ist mit `def publish(self):`? Es ist genau die `publish` Methode über die wir vorher bereits sprachen. `def` bedeutet, es ist eine Funktion/Methode und `publish` ist der Name der Methode. Du kannst den Namen der Methode ändern wenn du das möchtest. Die Benennungsregel ist, dass wir Kleinbuchstaben und Unterstriche statt Leerzeichen verwenden. Eine Methode, welche den Durchschnittspreis berechnet, könnte zum Beispiel `calculate_average_price` genannt werden.

Methoden geben oftmals etwas zurück (english: `return`). Es gibt ein Beispiel dafür in der `__str__` Methode. In diesem Szenario, wenn wir `__str__()` aufrufen bekommen wir einen Text (**string**) mit einem Post Titel zurück.

Wenn dir noch etwas über Methoden nicht klar ist, dann zöger nicht deinen coach zu fragen! Wir wissen, dass es kompliziert ist, vor allem, wenn du gleichzeitig lernst was Objekte und Funktionen sind. Aber hoffentlich sieht es etwas weniger wie Magie für dich jetzt aus!

### Tabellen für Modelle in deiner Datenbank erstellen

Der letzte Schritt hier ist unser neues Modell unserer Datenbank hinzuzufügen. Als Erstes müssen wir Django klarmachen, dass wir einige Änderungen an unserem Model vorgenommen haben (wir haben es gerade erst kreiert!). Gebe ein `python manage.py makemigrations blog`. Das sieht dann so aus:

    (myvenv) ~/djangogirls$ python manage.py makemigrations blog 
    Migrations for 'blog': 
       0001_initial.py: 
       - Create model Post
    

Django hat für uns eine Migrationsdatei vorbereitet, welche wir jetzt auf unsere Datenbank anwenden müssen. Tippe `python manage.py migrate blog` und der Output sollte sein:

    (myvenv) ~/djangogirls$ python manage.py migrate blog
    Operations to perform: 
       Apply all migrations: blog 
    Running migrations: 
      Rendering model states... DONE 
      Applying blog.0001_initial... OK
    

Hurra! Unser Post Modell ist ab sofort in unserer Datenbank! Es wäre doch schön es zu sehen, richtig? Springe zum nächsten Kapitel um zu sehen, wie dein Post aussieht!