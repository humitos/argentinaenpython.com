# Django URLs

Wie sind dabei unsere erste Website zu machen --eine Homepage für unseren Blog! Aber zunächst lernen wir etwas über Django urls.

## Was ist eine URL?

Die URL ist einfach eine Web-Adresse. Du kannst eine URL sehen, jedes Mal, wenn du eine Website besuchst - es ist in der Adressleiste des Browsers sichtbar (ja! `127.0.0.1:8000` ist eine URL! Und `https://djangogirls.com` ist auch eine URL):

![Url][1]

 [1]: images/url.png

Jede Seite im Internet braucht seine eigene URL. Dadurch weiß dein Browser was sie dem Nutzer, der eine URL öffnet, zeigen soll. In Django verwenden wir eine sogenannte `URLconf` (URL Konfiguration). URLconf ist eine Ansammlung von Mustern, die Django versuchen wird mit der empfangenen URL in Übereinstimmung zu bringen, um die richtige View zu finden.

## Wie funktionieren URLs in Django?

Öffne die `mysite/urls.py` Datei in deinem Code Editor nach Wahl und schaue dir an wie sie aussieht:

    python 
    from django.conf.urls import include, url 
    from django.contrib import admin 
    
    urlpatterns = [ 
        # Examples:  
        # url(r'^$', 'mysite.views.home', name='home'),  
        # url(r'^blog/', include('blog.urls')), 
    
        url(r'^admin/', include(admin.site.urls)), 
    ]
    

Wie du siehst hat Django hier schon etwas für uns eingefügt.

Zeilen, die mit `#` anfangen sind Kommentare - das bedeutet, dass diese Zeilen von Python nicht ausgeführt werden. Praktisch oder?

Die admin URL, die du im vorangehenden Kapitel bereits besucht hast, ist schon da:

    python   
      url(r'^admin/', include(admin.site.urls)),
    

Für jede URL, die mit mit `admin/` beginnt, wird Django einen entsprechenden View finden mit *view*. Wir fügen hier einige admin URLs ein, dadurch wird nicht alles in eine Datei gepackt --es bleibt lesbarer und sauberer.

## Regex

Du fragst dich WIE Django den richtigen View zu einer URL findet? Nun, das ist ein bisschen komplizierter. Django benutzt `regex` kurz für "regular expressions". (reguläre Ausdrücke). Regex besteht aus vielen Regeln (wirklich vielen!) aus denen ein Suchschema aufgebaut ist. Da regexes ein fortgeschrittenes Thema sind, werden wir jetzt nicht in Details gehen wie sie genau funktionieren.

Wenn es immer noch dein Wunsch ist, zu verstehen wie wir die Muster erstellt haben, ist hier ein Beispiel des Prozesses - wir brauchen nur eine eingeschränkte Menge der Regeln um das Muster nach dem wir suchen auszudrücken, namentlich:

    ^ für den Anfang eines Textes 
    $ für das Ende eines Textes 
    \d für eine Nummer 
    + um anzuzeigen, dass das vorhergehende Element mind. 1 mal wiederholt werden soll 
    () um Teile des Musters zu erfassen
    

Alles andere in der Url-Definition wird wörtlich genommen.

Jetzt stell dir vor du hast eine Website mit der Adresse: `http://www.mysite.com/post/12345/` wobei `12345` die Nummer deines Posts ist.

Eigene Views für jeden einzelnen Post zu schreiben wäre ziemlich nervig. Mit regulären Asudrücken können wir ein Muster erstellen, welches auf die URL passt und die Nummer extrahieren wird: `^post/(\d+)/$`. Lass es uns in kleine Häppchen aufteilen, um zu verstehen was wir hier genau tun:

*   **^post/** bedeutet Django Alles einzulesen, dass `post/` am Anfang der Url hat (gleich nach `^`)
*   **(\d+)** bedeutet, dass es eine Zahl gibt (eine oder mehrere Nummern) und wir wollen diese Zahl eingelesen und ausgewertet haben
*   **/** bedeutet Django, dass ein weiteres `/` Zeichen folgen soll
*   **$** deutet dann das Ende der URL an; meinend dass nur Zeichenfolgen die auf `/` enden dem Muster entsprechen

## Deine erste Django URL!

Es wird Zeit deine erste URL zu erstellen! Wir wollen, dass 'http://127.0.0.1:8000/' die Homepage unseres Blogs wird und eine Liste unserer Posts zeigt.

Wir wollen auch, dass die `mysite/urls.py` Datei sauber bleibt. Deshalb importieren wir urls unserer `blog` Applikation in die `mysite/urls.py` Hauptdatei.

Fang damit an die auskommentierten Zeilen (Zeilen mit `#`) zu löschen und füge die Zeile hinzu, die unsere `blog.urls` in die Haupt-URL importieren wird (`''`).

Dein `mysite/urls.py` File sollte jetzt so aussehen:

    python 
    from django.conf.urls import include, url 
    from django.contrib import admin 
    
    urlpatterns = [   
      url(r'^admin/', include(admin.site.urls)),  
      url(r'', include('blog.urls')), 
    ]
    

Django wird nun alle Aufrufe von 'http://127.0.0.1:8000/' auf `blog.urls` umleiten und dort nach weiteren Anweisungen schauen.

Beim Schreiben von regulären Ausdrücken in Python geschieht die immer mit `r` vor der Zeichenfolge. Dies ist ein hilfreicher Hinweis an Python, dass die Zeichenfolge unter Umständen spezielle Zeichen enthalten kann, welche nicht für Python an sich gerichtet sind sondern für die regulären Ausdrücke.

## blog.urls

Erstelle eine neue, leere Datei `blog/urls.py`. Alles klar! Füge nun diese beiden Zeilen hinzu:

    python 
    from django.conf.urls import url 
    from . import views
    

Hier importieren wir erstmal nur die Methoden von Django und alles aus den `views` unserer `blog` Applikation (wir haben noch keine, aber dazu kommen wir gleich!)

Danach können wir unser erstes URL Pattern hinzufügen:

    python 
    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
    ]
    

Hier haben wir nun einen `view` mit dem Namen `post_list` zu `^$` URL hinzugefügt. Dieser reguläre Ausdruck wird dem Anfang `^` gefolgt von dem ende `$` passen - so dass nur eine leere Zeichenfolge zutrifft. Und das ist auch richtig so weil in Django die URL Auflösung nach 'http://127.0.0.1:8000/' kein Teil der URL ist. Dieses Muster zeigt Django auf, dass `views.post_list` der Ort ist, wenn jemand auf deine Website mit der 'http://127.0.0.1:8000/' Adresse geht.

Der letzte Teil `name='post_list'` ist der Name der URL, die genutzt wird den 'view' zu identifizieren. Diese kann identisch mit dem Namen der 'view' sein, sie kann aber auch etwas total Anderes sein. Wir werden später die benannten URLs in dem Projekt benutzen daher ist es wichtig jede URL in der App zu benennen. Wir sollten außerdem versuchen die Namen der URLs einzigartig und einfach zu merken zu halten.

Alles klar? Öffne http://127.0.0.1:8000/ in deinem Browser um das Ergebnis zu sehen.

![Fehler][2]

 [2]: images/error1.png

Dort steht nicht mehr "It works"? Keine Sorge, es ist nur eine Fehler Seite. Nichts wovor man Angst haben muss! Sie sind eigentlich sehr hilfreich:

Dort steht, es gibt keine **no attribute 'post_list'**. Erinnert dich *post_list* an etwas? So haben wir unseren View genannt! Das heißt, dass alles bereits an Ort und Stelle ist aber wir haben bislang einfach noch keinen *view* erzeugt. Keine Sorge, das machen wir gleich.

> Wenn du mehr über Django URLconfs lernen willst, dann öffne die offizielle Dokumentation: https://docs.djangoproject.com/en/1.8/topics/http/urls/