# Django-Ansichten - Zeit zum Gestalten!

Es wird jetzt Zeit den Bug, den wir im letzten Kapitel erzeugt haben, zu beheben :)

In den *view* schreiben wir die Logik unserer Anwendung. Es wird Informationen aus dem `model` anfragen, welches du zuvor erzeugt hast und diese an ein `template` weitergeben. Wir erzeugen ein Template im nächsten Kapitel. Ansichten (views) sind Pythonmethoden, die ein bisschen komplizierter sind als die, die wir im Kapitel **Introduction to Python** Kapitel gemacht haben.

Views kommen in die `views.py` Datei. Wir fügen nun also unsere *views* zur Datei `blog/views.py` hinzu.

## blog/views.py

OK, wir öffnen nun diese Datei und schauen was darin steht:

    python
    from django.shortcuts import render
    
    # Create your views here.
    

Es steht noch nicht viel darin. Der einfachste *view* kann folgendermaßen aussehen:

    python
    def post_list(request):
        return render(request, 'blog/post_list.html', {})
    

Du siehst hier, dass wir eine Methode (`def`) mit dem Namen `post_list` gemacht haben. Sie hat den Parameter `request`. In der Methode weisen wir mit `return` eine Rückgabe einer anderen Funktion `render` an. Diese wird unser template `blog/post_list.html` zusammenfügen ("render").

Speichere die Datei, öffne http://127.0.0.1:8000/ im Browser und schau nach was wir jetzt haben.

Einen anderen Fehler! Lies dir durch was da steht:

![Fehler][1]

 [1]: images/error.png

Der ist logisch: *TemplateDoesNotExist*. Wir haben ja noch kein Template erstellt. Lass uns diesen Bug im nächsten Kapitel beheben!

> Erfahre mehr über Django Views in der offiziellen Dokumentation: https://docs.djangoproject.com/en/1.8/topics/http/views/