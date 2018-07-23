# Django-Formulare

Als letztes möchten wir auf unserer Website noch die Möglichkeit haben Blog Posts hinzuzufügen und zu editieren. Die Django `admin` Oberfläche ist cool, aber eher schwierig anzupassen und hübsch zu machen. Mit Formularen , `forms` , haben wir die absolute Kontrolle über unser Interface, wir können fast alles machen was man sich vorstellen kann.

Das Gute an Django Forms ist, dass man sie entweder vollständig selbst definieren kann oder eine `ModelForm` benutzt, welche den Inhalt des Formulars in das Model speichert.

Genau das wollen wir jetzt machen: Wir erstellen ein Formular für unser `Post` Model.

So wie die anderen wichtigen Django Teile kommen auch die Forms in eine eigene Datei: `forms.py`.

Wir erstellen nun eine Datei mit diesem Namen im `blog` Verzeichnis.

    blog
       └── forms.py
    

Okay, jetzt öffnen wir es und fügen folgenden Code hinzu:

    python 
    from django import forms 
    
    from .models import Post 
    
    class PostForm(forms.ModelForm):
         class Meta:
             model = Post
             fields = ('title', 'text',)
    

Zuerst müssen wir die Django Forms importieren (`from django import forms`) und natürlich auch unser `Post` Model (`from .models import Post`).

Richtig geraten! `PostForm` ist der Name unseres Formulars. Wir müssen Django mitteilen, dass dieses Form ein `ModelForm` ist (dann zaubert Django ein bisschen). `forms.ModelForm` ist dafür verantwortlich.

Als nächstes sehen wir uns `class Meta` an, womit wir Django sagen welches Model benutzt werden soll um dieses Form zu erstellen (`model = Post`).

Als letztes können wir dann bestimmen, welche(s) Feld(er) in unserem Formular sein sollen. In diesem Fall wollen wir nur den `title` und `text` sichtbar machen- `author` sollte die Person sein, die gerade eingeloggt ist (Du!) und `created_date` sollte automatisch generiert werden, wenn der Post erstellt wird (also im Code). Stimmt's?

Und das war's! Jetzt müssen wir das Formular nur noch in einem *view* benutzen und im template darstellen.

Also erstellen wir nochmal einen Link auf die Seite, eine URL, einen View und ein Template.

## Link auf eine Seite mit dem Form

Die Zeit ist gekommen `blog/templates/blog/base.html` zu öffnen. Wir fügen einen Link in `div` hinzu mit dem Namen `page-header`:

    html 
    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    

Merk dir, dass wir unseren neuen View `post_new` nennen wollen.

Nach Hinzufügen der Zeile sieht deine HTML Datei so aus:

    html 
    {% load staticfiles %} 
    <html>
         <head>
             <title>Django Girls blog</title>
             <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
             <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
             <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>         <link rel="stylesheet" href="{% static 'css/blog.css' %}">
         </head>
         <body>
             <div class="page-header">
                 <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
                 <h1><a href="/">Django Girls Blog</a></h1>
             </div>
             <div class="content container">
                 <div class="row">
                     <div class="col-md-8">
                         {% block content %}
                         {% endblock %}
                     </div>
                 </div>
             </div>
         </body> 
    </html>
    

Nach dem Speichern und neu Laden von http://127.0.0.1:8000 siehst du den bekannten `NoReverseMatch` Fehler, oder?

## URL

Wir öffnen `blog/urls.py` und fügen eine Zeile hinzu:

    python
         url(r'^post/new/$', views.post_new, name='post_new'),
    

Der finale Code sieht dann so aus:

    python 
    from django.conf.urls import include, url 
    from . import views 
    
    urlpatterns = [ 
        url(r'^$', views.post_list, name='post_list'), 
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),  
        url(r'^post/new/$', views.post_new, name='post_new'), 
    ]
    

Nach dem neu Laden der Seite sehen wir einen `AttributeError`, weil wir noch keinen `post_new` View haben. Wir fügen ihn gleich hinzu!

## Der post_new View

Jetzt wird es Zeit die `blog/views.py` Datei zu öffnen und die folgenden Zeilen zu den anderen `from` Zeilen hinzuzufügen:

    python 
    from .forms import PostForm
    

und unseren *view*:

    python 
    def post_new(request):
         form = PostForm()
         return render(request, 'blog/post_edit.html', {'form': form})
    

Um ein neues `PostForm` zu erstellen, rufen wir die `PostForm()` Methode auf und übergeben sie an das Template. Wir kommen gleich nochmal zu dem *view* zurück, aber jetzt erstellen wir schnell ein Template für das Form.

## Vorlage

Wir müssen eine Datei `post_edit.html` im Verzeichnis `blog/templates/blog` erstellen. Damit ein Formular funktioniert benötigen wir einige Dinge:

*   wir müssen das Formular anzeigen. Wir können das, zum Beispiel, mit einem simplen `{% raw %}{{ form.as_p }}{% endraw %}` tun.
*   die Zeile oben muss mit einem HTML-Formular-Tag eingeschlossen werden `<form method="POST">...</form>`
*   wir benötigen einen `Save` Button. Wir machen das mit einem HTML button: `<button type="submit">Save</button>`
*   und schließlich nach dem öffnenden `<form ...>` Tag müssen wir hinzufügen `{% raw %}{% csrf_token %}{% endraw %}`. Dies ist sehr wichtig, da es deine Formulare sicher macht! Django wird sich beschweren wenn du dies vergißt und versuchst das Formular zu speichern:

![CSFR Forbidden page][1]

 [1]: images/csrf2.png

O.k., also mal sehen, wie der HTML-Code in `post_edit.html` aussehen sollte:

    html 
    {% extends 'blog/base.html' %} 
    
    {% block content %}
         <h1>New post</h1>
         <form method="POST" class="post-form">{% csrf_token %}
             {{ form.as_p }}
             <button type="submit" class="save btn btn-default">Save</button>
         </form> 
    {% endblock %}
    

Zeit zu aktualisieren! Yay! Das Formular wird angezeigt!

![Neues Formular][2]

 [2]: images/new_form2.png

Aber warte mal eine Minute! Wenn du irgendetwas eintippst in das `title` oder `text` Feld und versuchst zu speichern - was wird wohl passieren?

Nichts! Wir sind wieder Mal auf der selben Seite und unser Text ist vershwunden... und kein neuer Post ist hinzugefügt worden. Also was lief schief?

Die Antwort ist: nichts. Wir müssen einfahc noch etwa mehr Arbeit an unserem *view* vornehmen.

## Speichern des Formulars

Öffne `blog/views.py` erneut. Aktuell ist Alles in dem Formular `post_new` dies:

    python 
    def post_new(request):
         form = PostForm()
         return render(request, 'blog/post_edit.html', {'form': form})
    

Wenn wir das Formular übermitteln, werden wir zurückgebracht zu der gleichen Ansicht aber dieses Mal haben wir mehr Daten in `request`, genauer in `request.POST` (der Name hat nichts zu tun mit "Post" sondern damit dass wir Daten "posten"). Erinnerst du dich daran, dass in unserer HTML Datei unsere `<form>` Definition die Variable `method="POST"` hatte? Alle Felder aus dem Formular sind jetzt in `request.POST`. Du solltest `POST` nicht umbenennen (der einzige andere Wert für `method` ist `GET` aber wir haben keine Zeit den Unterschied hier zu erklären).

So haben wir aus unserem *view* zwei separate Situationen zu handhaben. Als Erstes: Wenn wir zum ersten Mal auf die Seite zugreifen und wir ein leeres Formular wollen. Zweitens: Wenn wir zurück zu der *view* gehen, mit all den Formulardaten, die wir gerade eingegeben haben. Daher müssen wir eine Bedingung hinzufügen (dafür werden wir `if` verwenden).

    python 
    if request.method == "POST":  
       [...] 
    else: 
       form = PostForm()
    

Es ist Zeit, die Punkte `[...]` auszufüllen. Wenn `method` `POST` ist, dann wollen wir die `PostForm` mit Daten aus dem Formular konstruieren, richtig? Wir tun das mit:

    python 
    form = PostForm(request.POST)
    

Einfach! Als nächste müssen wir testen ob das Formular korrekt ist (alle benötigten Felder sind ausgefüllt, keine inkorrekten Werte werden gespeichert). Wir tun das mit `form.is_valid()`.

Wir überprüfen, ob das Formular gültig ist und wenn ja, können wir es speichern!

    python 
    if form.is_valid(): 
        post = form.save(commit=False) 
        post.author = request.user 
        post.published_date = timezone.now() 
        post.save()
    

Im Grunde haben wir hier zwei Dinge: Wir speichern das Formular mit `form.save` und wir fügen einen Autor hinzu (da es bislang kein `author` Feld in der `PostForm` gab und dieses Feld notwendig ist!). `commit=False` bedeutet, dass wir das `Post` Modell noch nicht speichern wollen - wir wollen den Autor erst noch hinzufügen. Die meiset Zeit wirst du `form.save()` benutzen ohne `commit=False` aber in diesem Fall müssen wir es so tun. `post.save()` wird Änderungen beibehalten (den Autor hinzufügen) und ein neuer Blog ist erschaffen!

Schließlich, wäre es genial wenn wir direkt zu der `post_detail` Seite gehen können für unsere neu erstellten Blog Post`s, richtig? Um dies zu tun benötigen wir einen weiteren Import:

    python 
    from django.shortcuts import redirect
    

Füge dies direkt am Anfang der Datei hinzu. Jetzt endlich können wir sagen: Gehe zu der `post_detail` Seite für unsere neu erstellten Post`s.

    python 
    return redirect('blog.views.post_detail', pk=post.pk)
    

`blog.views.post_detail` ist der Name unseres views zu dem wir springen wollen. Erinnerst du dich, dass dieser *view* einen `pk` benötigt? Um ihn an den view weiterzugeben, benutzen wir `pk=post.pk` wobei `post` unser neu erstellter Blog Post ist!

Ok wir haben jetzt eine ganze Menge geredet aber du willst bestimmt sehen wie die gesamte *view* aussieht, richtig?

    python 
    def post_new(request): 
        if request.method == "POST":   
           form = PostForm(request.POST)  
           if form.is_valid():   
               post = form.save(commit=False)   
               post.author = request.user    
               post.published_date = timezone.now() 
               post.save()   
               return redirect('blog.views.post_detail', pk=post.pk)   
          else:   
              form = PostForm() 
         return render(request, 'blog/post_edit.html', {'form': form})
    

Schauen wir mal ob es funktioniert. Gehe zu der Seite http://127.0.0.1:8000/post/new/, füge einen `title` und `text` hinzu und speichere es... und Voilà! Die neue Blog-Post wird hinzugefügt, und wir werden auf die `Post_detail` Seite umgeleitet!

Du hast vielleicht bemerkt, dass wir das Veröffentlichungsdatum festlegen bevor wir den Post veröffentlichen. Später werden wir einen *publish button* in **Django Girls Tutorial: Extensions** einführen.

Das ist genial!

## Formularvalidierung

Jetzt zeigen wir dir wie cool Django Formulare sind. Ein Blog Post muss `title` und `text` Felder besitzen. In unserem `Post` Modell sagten wir nicht (im Gegensatz zu dem `published_date`), dass diese Felder nicht benötigt sind, also nahm Django standardmäßig an, dass diese angegeben sein müssen.

Versuch das Formular ohne `title` und `text` zu speichern. Rate, was passieren wird!

![Formularvalidierung][3]

 [3]: images/form_validation2.png

Django kümmert sich darum sicherzustellen, dass alle Felder in unserem Formular richtig sind. Ist das nicht großartig?

> Da wir vor Kurzem das Django Admin Interface benutzt haben, denkt das System, dass wir noch angemeldet sind. Es gibt einige Situationen, welche dazu führen können, dass wir ausgelogged werden (Schließen des Browsers, Neustarten der Datenbank etc). Wenn du feststellst, dass du Fehlermeldungen bei der Post Erstellung bekommst, die auf nicht angemeldete Nutzer zurückzuführen ist dann gehe zu der Admin Seite http://127.0.0.1:8000/admin und logge dich erneut ein. Dies wird das Problem zeitweise lösen. Es gibt eine permanente Lösung, die auf dich im **Homework: add security to your website!** Kapitel nach dem Haupttutorial wartet.

![Logged in error][4]

 [4]: images/post_create_error.png

## Formular bearbeiten

Jetzt wisen wir wie wir ein neues Formular hinzufügen. Aber was ist wenn wir ein bereits bestehendes bearbeiten wollen? Es ist sehr ähnlich zu dem, was wir gerade getan haben. Lass uns schnell ein paar wichtige Dinge erstellen (falls du etwas nicht verstehst, solltest du deinen Coach fragen oder in den vorherigen Kapiteln nachschlagen, da wir all die Schritte bereits behandelt haben).

Öffne `blog/templates/blog/post_detail.html` und füge diese Zeile hinzu:

    python 
    <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    

damit die Vorlage so aussieht:

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        <div class="post">
            {% if post.published_date %}
                <div class="date">
                    {{ post.published_date }}
                </div>
            {% endif %}
            <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
            <h1>{{ post.title }}</h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endblock %}
    

In `blog/urls.py` fügen wir folgende Zeile ein:

    python  
       url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    

Wir werden die Vorlage `blog/templates/blog/post_edit.html` wiederverwenden daher ist das letzte verbliebende eine *view</1.></p> 
Öffne `blog/views.py` und füge ganz am Ende der Datei folgendes hinzu:

    python
    def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    

Sieht genauso aus wie unsere `post_new` view, richtig? Aber nicht ganz. Erste Abweichung: wir übergeben einen zusätzlichen `pk` Parameter von den Url`s. Als Nächstes: Wir bekommen das `Post` Modell, welches wir bearbeiten wollen mit `get_object_or_404(Post, pk=pk)` und dann, wenn wir ein Formular erstellt haben, übergeben wir diesen Post als `instance` sowohl wenn wir das Formular speichern:

    python 
    form = PostForm(request.POST, instance=post)
    

als auch wenn wir ein Formular mit diesem Post zum ediitieren öffnen:

    python 
    form = PostForm(instance=post)
    

Ok, lass uns mal schauen ob das funktioniert! Gehe auf die `post_detail` Seite. Dort sollte ein Editier-Knopf in der oberen rechten Ecke sein:

![Schaltfläche "Bearbeiten"][5]

Wenn du darauf klickst, siehst du das Formular mit unserem Blog Post:

![Formular bearbeiten][6]

Zöger nicht den Titel oder den Text zu ändern und die Änderungen zu speichern!

Herzlichen Glückwunsch! Deine Anwendung wird langsam immer vollständiger!

Falls du mehr Informationen über Django Formulare benötigst solltest du die offizielle Dokumentation lesen: https://docs.djangoproject.com/en/1.8/topics/forms/

## Sicherheit

In der Lage zu sein neue Post`s zu erstellen nur indem man einen Link klickt ist großartig! Aber im Moment ist jeder der deine Seite besucht in der Lage, einen neuen Blog Post zu veröffentlichen und das ist etwas, dass du garantiert nicht willst. Lass es uns so einrichten, dass der Button nur für dich sichtbar ist und nicht für jeden.

In `blog/templates/blog/base.html`, finde unseren `page-header` `div` und das Anchor Tag, welches du zuvor eingefügt hast. Es sollte so aussehen:

    html 
    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    

Wir fügen ein weiteres `{% if %}` Tag dazu ein, was dafür sorgt, dass der Link nur für angemeldete Nutzer angezeigt wird. Im Moment bist das also nur du! Ändere den `<a>` Tag zu folgendem:

    html 
    {% if user.is_authenticated %}  
        <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
     {% endif %}
    

Dieses `{% if %}` sorgt dafür, dass der Link nur zu dem Browser geschickt wird, wenn der anfragende Nutzer auch angemeldet ist. Dies verhindert die Erzeugung neuer Post`s nicht komplett, ist aber ein sehr guter erster Schritt. In der Erweiterungslektion kümmern wir uns ausgiebiger um Sicherheit.

Da du wahrscheinlich angemeldet bist, wirst du nichts Neues sehen wenn du die Seite aktualisierst. Lade die Seite in einem neuen Browser oder im Inkognito Modus und du wirst sehen, dass der Link nicht auftaucht!

## Eins noch: Zeit zum Deploy!

Mal sehen, ob all dies auf PythonAnywhere funktioniert. Zeit für ein weiteres Bereitstellen!

*   Als erstes, übergebe deinen neuen Code und lade ihn auf GitHub hoch

    $ git status 
    $ git add -A . 
    $ git status 
    $ git commit -m "Added views to create/edit blog post inside the site." 
    $ git push
    

*   Dann, in einer [PythonAnywhere Bash Konsole][7]:

    $ cd my-first-blog 
    $ source myvenv/bin/activate 
    (myvenv)$ git pull 
    [...] 
    (myvenv)$ python manage.py collectstatic 
    [...]
    

*   Springe zum Ende noch schnell auf den [Web tab][8] und klicke auf **Reload**.

Und das war's! Glückwunsch :)

 [5]: images/edit_button2.png
 [6]: images/edit_form2.png
 [7]: https://www.pythonanywhere.com/consoles/
 [8]: https://www.pythonanywhere.com/web_app_setup/