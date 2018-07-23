# Django ORM und QuerySets

In diesem Kapitel lernst du wie sich Django mit der Datenbank verbindet und Daten darin speichert. Lass uns los legen!

## Was ist ein QuerySet?

Ein QuerySet ist im Wesentlichen eine Liste von Objekten eines bestimmten Models. Mit dem QuerySet kann man Daten aus der Datenbank auslesen, filtern und ordnen.

Am besten wir sehen uns das an einem Beispiel an. Versuchen wir's?

## Django Shell

Öffne deine lokale Konsole (nicht in PythonAnywhere) und tippe diese Kommando ein:

    (myvenv) ~/djangogirls$ python manage.py shell
    

Das sollte angezeigt werden:

    (InteractiveConsole)
    >>>
    

Du befindest dich jetzt in Djangos interaktiver Konsole. Das ist fast das gleiche wie die Python Prompt aber mit etwas zusätzlicher Django Magie :) . Natürlich sind alle Python Kommandos hier trotzdem vorhanden.

### Alle Objekte

Zunächst wollen wir alle unsere Blogposts ansehen. Das kannst du mit folgendem Kommando erreichen:

    >>> Post.objects.all()
    Traceback (most recent call last):
          File "<console>", line 1, in <module>
    NameError: name 'Post' is not defined
    

Ups! Das gibt einen Fehler. Die Konsole sagt uns, dass es noch keine Posts gibt. Das stimmt! Wir haben vergessen diese vorher zu importieren!

    >>> from blog.models import Post
    

Das lässt sich einfach ändern: Wir importieren `Post` aus `blog.models` . Jetzt versuchen wir nochmal alle Posts anzeigen zu lassen:

    >>> Post.objects.all()
    [<Post: my post title>, <Post: another post title>]
    

Das ist die Liste, die wir vorhin schon erstellt haben! Wir haben diese Posts mit der Django Admin Oberfläche erstellt. Aber jetzt wollen wir mit Python neue Einträge erstellen, also wie machen wir das?

### Objekt erstellen

So erstellst du ein neues Post Objekt in der Datenbank:

    >>> Post.objects.create(author=me, title='Sample title', text='Test')
    

Allerdings fehlt noch eine Zutat: `me` . Wir müssen eine Instanz des Models `User` als Autor übergeben. Wie macht man das?

Als erstes müssen wir das User Model importieren:

    >>> from django.contrib.auth.models import User
    

Welche User sind in unserer Datenbank vorhanden? Finde es damit heraus:

    >>> User.objects.all()
    [<User: ola>]
    

Das ist der Superuser, den wir vorhin erstellt haben! Lass uns jetzt eine Instanz des Users erstellen:

    me = User.objects.get(username='ola')
    

Wie du siehst haben wir jetzt einen `User` mit einem `username` der 'ola' heißt. Schön! Natürlich musst du diesen zu deinem eigenen Benutzernamen ändern.

Jetzt können wir schließlich unseren Post erstellen:

    >>> Post.objects.create(author=me, title='Sample title', text='Test')
    

Super! Wollen wir nachsehen ob es funktioniert hat?

    >>> Post.objects.all()
    [<Post: my post title>, <Post: another post title>, <Post: Sample title>]
    

Da ist es, ein weiterer Post in der Liste!

### Mehrere Posts hinzufügen

Du kannst jetzt noch ein bisschen damit rumprobieren und noch weitere Posts hinzufügen. Mach noch 2-3 weitere und geh dann zum nächsten Punkt.

### Objekte filtern

Eine wichtige Aufgabe von QuerySets ist, dass sie Einträge filtern können. Zum Beispiel wollen wir alle Posts des Users Ola finden. Dafür nehmen wir `filter` statt `all` in `Post.objects.all()`. In den Klammern schreiben wir die Bedingung(en) hinein, die erfüllt werden müssen, damit ein Blog Post in unser Queryset kommt. Hier ist es so, dass `author` gleich `me` ist. In Django schreiben wir deshalb: `author=me`. Jetzt sieht unser Code folgendermaßen aus:

    >>> Post.objects.filter(author=me)
    [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]
    

Oder vielleicht wollen wir alle Posts haben, die das Wort "title" im `title` Feld haben?

    >>> Post.objects.filter(title__contains='title')
    [<Post: Sample title>, <Post: 4th title of post>]
    

> **Anmerkung** Zwischen `title` und `contains` befinden sich zwei Unterstriche (`_`). Das ORM von Django nutzt diese Syntax um Feldnamen ("title") und Operationen oder Filter ("contains") voneinander zu trennen. Wenn du nur einen Unterstrich benutzt, bekommst du enen Fehler wie "FieldError: Cannot resolve keyword title_contains".

Du kannst auch eine Liste aller bereits publizierten Posts erhalten indem wir nach allen Posts suchen, deren `published_date` in der Vergangenheit liegt:

> > > from django.utils import timezone Post.objects.filter(published_date__lte=timezone.now()) []

Unglücklicherweise ist der Post den wir von der Python Konsole hinzugefügt haben noch nicht veröffentlicht. Das können wir ändern! Als Erstes erhalte eine Instanz eines Post, den wir veröffentlichen wollen:

    >>> post = Post.objects.get(title="Sample title")
    

Dann publizieren wir ihn mit unserer `publish` Methode!

    >>> post.publish()
    

Jetzt versuche eine Liste von veröffentlichten Post zu bekommen (drücke den Pfeil nach oben Knopf 3 Mal und drücke `enter`):

    >>> Post.objects.filter(published_date__lte=timezone.now())
    [<Post: Sample title>]
    

### Objekte anordnen

Mit den QuerySets kannst du eine Liste auch nach bestimmten Kriterien ordnen. Lass uns das ausprobieren mit dem `created_date` Feld:

    >>> Post.objects.order_by('created_date')
    [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]
    

Wir können die Reihenfolge auch umdrehen indem wir "`-`" davor schreiben:

    >>> Post.objects.order_by('-created_date')
    [<Post: 4th title of post>,  <Post: My 3rd post!>, <Post: Post number 2>, <Post: Sample title>]
    

### Verkettung von QuerySets

Du kannst auch QuerySets kombinieren indem du sie zusammen **verkettest**:

    >>> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    

Dies ist wirklich mächtig und lässt dich ziemlich komplexe Abfragen schreiben.

Cool! Jetzt bist du bereit für den nächsten Teil! Um die Konsole zu schließen schreib das:

    >>> exit()