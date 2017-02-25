# Erweitere deine Anwendung

Wir haben nun all die notwendigen Schritte abgeschlossen um eine Website zu erstellen: wir wissen wie wir ein Model, eine URL, einen View und ein Template erstellen. Wir wissen auch wie wir unsere Webseite verschönern können. 

Zeit zum Üben!

Das erste das unser Blog offensichtlich braucht ist eine Seite auf der ein Blogpost dargestellt wird, oder?

Wir haben bereits ein `Post` Model, deshalb brauchen wir dieses nicht mehr zu `models.py` hinzufügen.

## Erstelle eine Template Verknüpfung zu einem post's detail

Wir beginnen damit einen Link in der `blog/templates/blog/post_list.html` Datei zu erstellen. Bis jetzt sieht sie so aus:

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        {% for post in posts %}
            <div class="post">
                <div class="date">
                    {{ post.published_date }}
                </div>
                <h1><a href="">{{ post.title }}</a></h1>
                <p>{{ post.text|linebreaks }}</p>
            </div>
        {% endfor %}
    {% endblock content %}
    
    

{% raw %}Wir wollen einen Link von einem Post Titel in der Post Liste zu einer Post Detail Seite haben. Ändern wir `<h1><a href="">{{ post.title }}</a></h1>` so dass es zu den Post`s Detail Seite verlinkt:{% endraw %}

    html 
    <h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
    

{% raw %}Es ist an der Zeit, dass mysteriöse `{% url 'post_detail' pk=post.pk %}` zu erklären. Wie du dir wahrscheinlich schon denkst, bedeutet `{% %}`, dass wir Django Template Tags verwenden. Dieses Mal verwenden wir eines, dass eine URL für uns erzeugen wird!{% endraw %}

`blog.views.post_detail` ist der Pfad zu einem `post_detail` *view*, den wir erstellen wollen. Beachte bitte: `blog` ist der Name unserer App (das Verzeichnis `blog`), `views`kommt aus der `views.py` Datei und der letzte Teil - `post_detail` - ist der Name des Views..

Wenn wir jetzt auf http://127.0.0.1:8000/ gehen, bekommen wir einen Fehler (so wie erwartet, da wir ja noch keine URL oder *view* für `post_detail` haben). Er wird folgendermaßen aussehen:

![NoReverseMatch error][1]

 [1]: images/no_reverse_match2.png

## Erstelle eine URL zu einem post's detail

Lass uns eine URL in `urls.py` machen für unseren `post_detail` *view*!

Wir wollen, dass unser erster post's detail unter dieser **URL** angezeigt werden soll: http://127.0.0.1:8000/post/1/

Lass uns eine URL in der Datei `blog/urls.py` anlegen, um Django auf einen *view* hinzuweisen, genannt `post_detail`, welcher einen ganzen Blog Post anzeigen wird. Füge die Zeile `url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),` zu der Datei `blog/urls.py` hinzu. Die Datei sollte so aussehen:

    python 
    from django.conf.urls import include, url 
    from . import views 
    
    urlpatterns = [
         url(r'^$', views.post_list, name='post_list'),
         url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'), 
    ]
    

Dieser Teil `^post/(?P<pk>[0-9]+)/$` sieht beängstigend aus aber hab keine Angst - wir erklären es dir: - es beginnt mit `^` --"Der Anfang" -`post/` bedeutet lediglich die URL sollte nach dem Anfangdas Wort **post** und **/** enthalten. So weit so gut. - `(?P<pk>[0-9]+)` - dieser Teil ist schwieriger. Er bedeutet, dass Django alles was hier steht in einer Variable namens `pk` zu einem View transferiert. `[0-9]` sagt uns, dass hier nur eine Zahl, kein Buchstabe, stehen darf (also alles zwischen 0 und 9). `+`bedeutet, dass hier mehr mindestens eine (oder mehrere) Zahl(en) stehen müssen. Also so etwas wie `http://127.0.0.1:8000/post//` geht nicht, aber `http://127.0.0.1:8000/post/1234567890/` ist genau richtig! - `/` -dann brauchen wir **/** wieder - `$` - "Ende"!

Also wenn du `http://127.0.0.1:8000/post/5/` in deinen Browser eingibst, wird Django verstehen, dass du nach einem *view* suchst, der `post_detail` heißt und dem *view* übergeben, dass die Variable `pk` gleich `5` ist.

`pk` ist eine Abkürzung für `primary key`. Diese Bezeichnung wird oft in Django Projekten benutzt. Du kannst deine Variable aber nennen wie du willst (aber denk daran: Kleinbuchstaben und `_` anstelle von Leerzeichen). Zum Beispiel anstelle von `(?P<pk>[0-9]+)` können wir die Variable `post_id` nehmen, dieser Teil würde also `(?P<post_id>[0-9]+)` lauten.

Ok, wir haben ein neues URL Muster zu der Datei `blog/urls.py` hinzugefügt! Lass uns die Seite http://127.0.0.1:8000/ aktualisieren. Boom! Erneut ein Fehler! Wie erwartet!

![AttributeError][2]

 [2]: images/attribute_error2.png

Erinnerst du dich das was der nächste Schritt ist? Natürlich: einen View hinzufügen!

## Füge eine post's detai View hinzu

Dieses Mal bekommt unser *view* den extra Parameter `pk`. Unser *view* muss diesen abfangen, richtig? Also definieren wir unsere Function mit `def post_detail(request, pk):`. Beachte, dass wir genau den gleichen Variablennamen benutzen müssen, wie in urls festgelegt (`pk`). Eine fehlerhafte Variable führt zu einem Fehler!

Jetzt wollen wir also genau einen Blog Eintrag. Wir könbnen dies erreichen indem wir ein Queryset folgendermaßen schreiben:

    Post.objects.get(pk=pk)
    

Aber bei diesem Code gibt es ein Problem. Wenn `Post` keinen `primary key` (`pk`) hat bekommen wir einen schlimmen Fehler!

![DoesNotExist error][3]

 [3]: images/does_not_exist2.png

Das wollen wir nicht! Aber natürlich stellt uns Django etwas zur Verfügung um dieses Problem zu umgehen: `get_object_or_404`. Wenn es keinen `Post` mit einem gegebenen `pk` gibt wird er eine schönere Seite anzeigen (die sogenannte `Page Not Found 404` Seite).

![Page not found][4]

 [4]: images/404_2.png

Die gute Neuigkeit ist, dass du auch deine eigene `Page not found` (Seite nicht gefunden) Seite machen kannst und diese so hübsch machen kannst, wie du willst. Aber da das gerade nicht so wichtig ist, überspringen wir das erstmal.

Okay, es wird Zeit den *view* zu unserer `views.py` Datei hinzuzufügen!

Wir öffnen `blog/views.py` und fügen folgenden Code hinzu:

    from django.shortcuts import render, get_object_or_404
    

Bei den anderen `from` Zeilen. Am Ende der Datei fügen wir unseren *view* hinzu:

    def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})
    

Super. Lass uns nun http://127.0.0.1:8000/ aktualisieren.

![Post list view][5]

 [5]: images/post_list2.png

Es hat funktioniert! Aber was passiert, wenn du auf den Link im Blog Titel klickst?

![TemplateDoesNotExist error][6]

 [6]: images/template_does_not_exist2.png

Oh nein! Ein anderer Fehler! Aber wir wissen ja schon, wie wir mit diesem umgehen, oder? Wir müssen ein Template hinzufügen!

## Erzeuge ein Template für post detail

Wir erstellen eine Datei in `blog/templates/blog` mit dem Namen `post_detail.html`.

Das sieht dann so aus:

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        <div class="post">
            {% if post.published_date %}
                <div class="date">
                    {{ post.published_date }}
                </div>
            {% endif %}
            <h1>{{ post.title }}</h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endblock %}
    

Wir erweitern wieder `base.html`. Im `content`Block wollen wir das Publikationsdatum eines Post (published_date), falls es existiert, anzeigen und auch den Titel und Text. Aber wir müssen noch ein paar wichtige Dinge klären, oder?

{% raw %}`{% if ... %} ... {% endif %}` ist ein Template Tag, den wir nutzen känen um etwas zu überprüfen (erinnerst du dich `if ... else ..` aus dem Kapitel **Einführung in Python** ?). In diesem Szenario wollen wir prüfen ob ein post's `published_date` nicht leer ist. {% endraw %}

Okay, wir aktualisieren die Seite und sehen, dass `Page not found` nun weg ist.

![Post detail page][7]

 [7]: images/post_detail2.png

Yeah! Es funktioniert!

## Eins noch: Zeit zum Deploy!

Es wäre schön zu sehen, ob deine Website noch auf PythonAnywhere funktioniert, richtig? Lass uns erneut Bereitstellen.

    $ git status 
    $ git add -A . 
    $ git status 
    $ git commit -m "Added view and template for detailed blog post as well as CSS for the site." 
    $ git push
    

*   Dann, in einer [PythonAnywhere Bash Konsole][8]:

 [8]: https://www.pythonanywhere.com/consoles/

    $ cd my-first-blog 
    $ source myvenv/bin/activate 
    (myvenv)$ git pull 
    [...] 
    (myvenv)$ python manage.py collectstatic 
    [...]
    

*   Springe zum Ende noch schnell auf den [Web tab][9] und klicke auf **Reload**.

 [9]: https://www.pythonanywhere.com/web_app_setup/

Und das war's! Glückwunsch :)