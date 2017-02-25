# Django Templates

Es wird Zeit ein paar Daten anzuzeigen! Django bringt dafür bereits ein paar sehr hilfreiche **template tags** mit.

## Was sind template tags?

Also in HTML kann man nicht wirklich Python Code schreiben, weil es der Browser nicht verstehen würde. Er kennt nur HTML. Wir wissen, dass HTML eher statisch ist im Gegensatz zum dynamischeren Python.

Mit **Django template tags** kann man Python-artige Dinge zu HTML machen, so dass man einfach und schnell dynamische Websites machen kann. Super!

## Anzeigen des Post List Templates

Im vorangegangen Kapitel haben wir unserem Template eine Liste von Posts übergeben in der `posts` Variable. Diese werden wir jetzt in HTML anzeigen.

Um eine Variable im Django Template darzustellen nehmen wir doppelte, geschweifte Klammern mit dem Namen der Variable darin, so wie hier:

    html
    {{ posts }}
    

Versuche dies in deinem `blog/templates/blog/post_list.html` Template. Ersetze alles vom zweiten `<div>` bis zum dritten `<div>` mit `{{ posts }}`. Speichern Sie die Datei und aktualisieren Sie die Seite um die Ergebnisse anzuzeigen:

![Abbildung 13.1][1]

 [1]: images/step1.png

Wie du siehst haben wir nun das:

    [<Post: My second post>, <Post: My first post>]
    

Das heißt Django versteht es als Liste von Objekten. Kannst du dich noch an die Einführung von Python erinnern, wie man Listen anzeigen kann? Ja, mit for-Schleifen! In einem Django Template benutzt du sie so:

    html
    {% for post in posts %}
        {{ post }}
    {% endfor %}
    

Versuch das in deinem Template.

![Abbildung 13.2][2]

 [2]: images/step2.png

Es funktioniert! Aber wir wollen, dass die Posts so angezeigt wie die statischen Posts, die wir vorhin im **Introduction to HTML** Kapitel erstellt haben. Du kannst HTML und Template Tags mischen. Unser `body` sollte dann so aussehen:

    html
    <div>
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>
    
    {% for post in posts %}
        <div>
            <p>published: {{ post.published_date }}</p>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
    

{% raw %}Alles was du zwischen `{% for %}`und `{% endfor %}` schreibst, wird für jedes Objekt in der Liste wiederholt. Aktualisiere deine Seite:{% endraw %}

![Abbildung 13.3][3]

 [3]: images/step3.png

Ist dir aufgefallen, dass wir eine etwas andere Notation diesmal benutzen bei `{{ post.title }}` oder `{{ post.text }}`? Wir greifen auf Daten von jedem Feld unseres `Post` Models zu. Außerdem konvertiert ("pipe") der `|linebreaks` Befehl in den Texten der Posts Zeilenumbrüche in Absätze.

## Und zum Schluss

Es wäre gut zu sehen ob deine Website noch immer im öffentlichen Internet funktioniert, richtig? Lass uns versuchen wieder zu PythonAnywhere hochzuladen. Hier ist eine Zusammenfassung der Schritte...

*   Zuerst schiebe deinen Code auf GitHub

    $ git status 
    [...]
    $ git add -A . 
    $ git status 
    [...]
    $ git commit -m "Modified templates to display posts from database." 
    [...] $ git push
    

*   Dann logge dich wieder ein bei [PythonAnywhere][4] und gehe zu deiner **Bash console** (oder starte eine neue) und gebe ein:

 [4]: https://www.pythonanywhere.com/consoles/

    $ cd my-first-blog
    $ git pull 
    [...]
    

*   Zum Schluss hüpf noch einmal kurz rüber zum [Web tab][5] und drück auf **Reload** auf deiner Web App. Deine Änderungen sollten jetzt live sein!

 [5]: https://www.pythonanywhere.com/web_app_setup/

Herzlichen Glückwunsch! Du kannst jetzt in der Django Admin Oberfläche neue Posts hinzufügen (denk daran published_date hinzuzufügen!), dann aktualisiere die Site um zu sehen, ob der neue Post auch erscheint.

Funktioniert super? Wir sind stolz auf dich! Steh kurz ein bisschen vom Computer auf. Du hast dir eine Pause verdient :)

![Abbildung 13.4][6]

 [6]: images/donut.png