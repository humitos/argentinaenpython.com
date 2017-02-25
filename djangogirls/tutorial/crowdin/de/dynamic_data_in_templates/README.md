# Dynamische Daten in Vorlagen

Wir haben nun schon einige Bestandteile fertig an verschiedenen Orten: das `Post` Model ist definiert in `models.py`, wir haben die `post_list` in `views.py` and das Template hinzugefügt. Aber wie schaffen wir es nun, dass unsere Posts wirklich im HTML Template erscheinen? Den das wollen wir schließlich erreichen: Wir wollen bestimmte Inhalte (die in der Datenbank gespeicherten Models) auf schöne Weise in unserem Template anzeigen, richtig?

Genau dafür sind die *views* zuständig: die Verbindung zwischen den Models und den Templates. In unserem `post_list` *View* müssen wir die Models addressieren, die wir anzeigen wollen und diese dem Template übergeben. Im Grunde entscheiden wir im *view* was (also welches Model) im Template angezeigt wird.

OKay, wie machen wir das jetzt?

Wir öffnen unsere Datei `blog/views.py`. Bisher sieht unser `post_list` *view* folgendermaßen aus:

    python
    from django.shortcuts import render
    
    def post_list(request):
        return render(request, 'blog/post_list.html', {})
    

Erinnerst du dich als wir davon gesprochen haben, dass wir den Code in verschiedene Dateien einfügen müssen? Jetzt ist es an der Zeit das Model, dass wir in `models.py` beschrieben haben einzufügen. Wir fügen den Befehl `from .models import Post` folgendermaßen ein:

    python
    from django.shortcuts import render
    from .models import Post
    

Der Punkt nach dem `from` bedeutet *current directory*, also das aktuelle Verzeichnis oder *current application*, aktuelle Anwendung. Da `views.py` und `models.py` im gleichen Verzeichnis sind können wir einfach den Punkt `.` und den Namen der Datei (ohne `.py`) benutzen. Dann importieren wir den Namen des Models (`Post`).

Und als nächstes? Um tatsächlich Blog Posts aus dem `Post` Model anzusprechen brauchen wir etwas, das `QuerySet` heißt.

## QuerySet

Dir sollte jetzt schon ungefähr wissen, wie QuerySets funktionieren. Wir haben darüber im Kapitel [Django ORM (QuerySets)][1] gesprochen.

 [1]: ../django_orm/README.md

Wir wollen nun also eine Liste von von Blog Posts die publiziert und nach `published_date` sortiert sind, oder? Das haben wir bereits im Kapitel QuerySets gemacht!

    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    

Dieses Teil Code fügen wir jetzt in `blog/views.py` ein, indem wir es zur Funktion `def post_list(request)` hinzufügen:

    python
    from django.shortcuts import render
    from django.utils import timezone
    from .models import Post
    
    def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {})
    

Beachte, dass wir eine *Variable* erstellen für unser QuerySet: `posts`. Du kannst sie dir als Name unseres QuerySets vorstellen. Ab jetzt beziehen wir uns auf es mit diesem Namen.

Ferner benutzt der Code die `timezone.now()` Funktion also müssen wir einen Import für `timezone` hinzufügen.

Als letztes fehlt noch, dass wir das `posts` QuerySet dem Template übergeben (wie wir es dann anzeigen wird im nächsten Kapitel erklärt).

In der `render` Funktion haben wir schon einen Parameter mit `request` (also alles was wir vom User über das Internet bekommen) und ein Template File `'blog/post_list.html'`. Der letzte Parameter, der so aussieht: `{}` ist der Ort, wo wir nähere Beschreibungen, welche das Template nutzt, einfügen können. Wir müssen ihnen einen Namen geben (wobei wir bei `'posts'` bleiben :)). Es sollte nun so aussehen: `{'posts': posts}`. Bitte bemerke, dass der Teil vor `:` ein String ist; du musst ihn mit Anführungszeichen umschliessen `''`.

Am Ende sollte deine `blog/views.py` Datei folgendermaßen aussehen:

    python
    from django.shortcuts import render
    from django.utils import timezone
    from .models import Post
    
    def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})
    

Das war's! Nun gehen wir zurück ins Template und zeigen das QuerySet an!

Wenn du mehr über QuerySets in Djago erfahren willst dann sieh unter diesem Link nach: https://docs.djangoproject.com/en/1.8/ref/models/querysets/