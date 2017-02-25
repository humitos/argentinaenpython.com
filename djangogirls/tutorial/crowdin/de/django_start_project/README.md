# Dein erstes Django Projekt!

> Teile dieses Kapitels basieren auf den Tutorials der Geek Girls Carrots (http://django.carrots.pl/).
> 
> Teile dieses Kapitels basieren auf dem [Django-Marcador Lernprogramm][1] lizenziert unter Creative Commons Attribution-ShareAlike 4.0 International License. Für das "django-marcador tutorial" liegt das Urheberrecht bei Markus Zapke-Gründemann u.a.

 [1]: http://django-marcador.keimlink.de/

Wir werden ein einfaches Blog erstellen.

Der erste Schritt ist, ein neues Django Projekt zu starten. Im Grunde bedeutet dies, dass wir einige Skripte ausführen werden, die von Django zur Verfügung gestellt werden, um ein Skelett eines Django Projekts für uns zu erzeugen. Dies ist nur ein Haufen von Verzeichnissen und Dateien, die wir später verwenden werden.

Die Namen einiger Dateien und Verzeichnisse sind sehr wichtig für Django. Die Dateien, die erstellt werden, solltest Du nicht umbenennen. Sie an eine andere Stelle zu verschieben, ist auch keine gute Idee. Django muss zwingend eine gewisse Struktur erhalten um wichtige Dinge wiederzufinden.

> Denk daran, alles in der "Virtualenv"-Umgebung auszuführen. Wenn Du kein Präfix `(Myvenv)` in Deiner Konsole siehst, musst Du Deine Virtualenv-Umgebung aktivieren. Wie das gemacht wird, erklären wir im Kapitel **Django-Installation** im Abschnitt **Arbeit mit Virtualenv**. Eingeben von `myvenv\Scripts\activate` in Windows oder `source myvenv/bin/activate` in Mac OS / Linux wird das für dich erreichen.

In deiner MacOS oder Linux Konsole solltest du den folgenden Befehl ausführen; **vergiss nicht den Punkt `.` am Ende** einzufügen:

    (myvenv) ~/djangogirls$ django-admin startproject mysite .
    

Unter Windows; **vergiss nicht den Punkt `.` am Ende** einzufügen:

    (myvenv) C:\Users\Name\djangogirls> django-admin startproject mysite .
    

> Der Punkt `.` ist sehr wichtig, weil er dem Skript mitteilt, dass Django in deinem aktuellen Verzeichnis installiert werden soll. (der Punkt `.` ist eine Schnellreferenz dafür)
> 
> **Hinweis** Wenn du die oben angegebenen Kommandos eingibst, denk dran, tippe nur das ein, das mit `django-admin` oder `django-admin.py` anfängt. `(myvenv) ~/djangogirls$` und `(myvenv) C:\Users\Name\djangogirls>` sind nur Teile von dem, was dir angezeigt wird in der Eingabeaufforderung, wenn die Konsole auf deine Eingabe wartet.

`django-admin.py` ist ein Skript, welches Verzeichnisse und Dateien für dich erstellt. Du solltest jetzt eine Verzeichnisstruktur haben, die folgendermaßen aussieht:

    djangogirls
    ├───manage.py
    └───mysite
            settings.py
            urls.py
            wsgi.py
            __init__.py
    

`manage.py` ist ein Script, das das Management Deines Projekts unterstützt. Mit dem Script bist Du unter anderem in der Lage den Webserver auf Deinem Rechner zu starten, ohne etwas weiteres installieren zu müssen.

Die Datei `settings.py` beinhaltet die Konfiguration Deiner Website.

Erinnerst du dich als wir über den Postboten gesprochen haben, der überlegt, wohin er den Brief liefern soll? Die `urls.py` Datei beinhaltet eine Liste von Patterns, die vom `urlresolver` benutzt werden.

Lass uns kurz die anderen Dateien vergessen - wir werden sie nicht verändern. Denk aber dran, sie nicht versehentlich zu löschen!

## Einstellungen anpassen

Wir werden die Einstellungen in `mysite/settings.py` anpassen. Öffne dazu den zuvor installierten Editor.

Es wäre schön, wenn die richtige Zeit auf deiner Webseite eingestellt ist. Gehe zu der [wikipedia timezones list][2] und kopiere deine zutreffende Zeitzone (time zone, TZ). (z.B. `Europe/Berlin`)

 [2]: http://en.wikipedia.org/wiki/List_of_tz_database_time_zones

In settings.py finde die Zeile, welche `TIME_ZONE` enthält und ändere sie zu deiner Zeitzone:

    python
    TIME_ZONE = 'Europe/Berlin'
    

Ändere "Europe/Berlin", wenn zutreffend

Des Weiteren brauchen wir einen Dateipfad für sogenannte "statische" Dateien (static files). Wir werden später im Tutorial genauer klären, was wir darunter verstehen. Gehe ganz ans Ende der Datei und füge unter `STATIC_URL` einen neuen Eintrag `STATIC_ROOT` ein.

    python
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    

## Eine Datenbank erstellen

Es gibt viele verschiedene Datenbanksysteme, in denen wir Daten für unsere Website speichern können. Wir werden das Standard-System `sqlite3` nutzen..

Das sollte schon in der `mysite/settings.py`-Datei eingestellt sein:

    python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    

Um eine Datenbank für unser Blog zu erstellen, müssen wir folgenden Befehl in der Konsole ausführen (Dazu müssen wir in dem `djangogirls`-Verzeichnis sein, in dem sich auch die `manage.py`-Datei befindet). Wenn alles glatt läuft, sollte das so aussehen:

    (myvenv) ~/djangogirls$ python manage.py migrate 
    Operations to perform: 
      Synchronize unmigrated apps: messages, staticfiles
      Apply all migrations: contenttypes, sessions, admin, auth Synchronizing apps without migrations:
       Creating tables...
          Running deferred SQL...
       Installing custom SQL...
    Running migrations: 
      Rendering model states... DONE 
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK 
      Applying contenttypes.0002_remove_content_type_name... OK 
      Applying auth.0002_alter_permission_name_max_length... OK 
      Applying auth.0003_alter_user_email_max_length... OK 
      Applying auth.0004_alter_user_username_opts... OK  
     Applying auth.0005_alter_user_last_login_null... OK 
      Applying auth.0006_require_contenttypes_0002... OK
      Applying sessions.0001_initial... OK
    

Und wir sind fertig! Zeit, unseren Webserver zu starten um zu sehen, ob unsere Website funktioniert!

Kontrolliere, dass du in dem Verzeichniss bist, in dem die `manage.py`-Datei liegt (das `djangogirls`-Verzeichnis). Wir starten den Webserver, in dem wir in der Konsole `python manage.py runserver` ausführen:

    (myvenv) ~/djangogirls$ python manage.py runserver
    

Wenn du Windows benutzt und dies mit dem `UnicodeDecodeError` fehlschläft, verwende diesen Befehl:

    (myvenv) ~/djangogirls$ python manage.py runserver 0:8000
    

Jetzt wollen wir schauen, ob unsere Website funktioniert: Öffne deinen Browser( Firefox, Chrome, Safari, Internet Explorer oder was du sonst nutzt) und gib folgende Adresse ein:

    http://127.0.0.1:8000/
    

Der Webserver wird deine Eingabeaufforderung übernehmen, bis du ihn wieder stoppst. Um weiterhin Kommandos einzugeben während er läuft, öffne eine neue Konsole und aktiviere dein virtualenv. Um den Webserver zu stoppen, wechsel zurück in das Fenster iin dem er läuft und drücke STRG+C - Steuerung und C gleichzeitig (in Windows kann es sein, dass du STRG und Pause drücken musst).

Glückwunsch! Du hast gerade deine erste Website erstellt und sie auf deinem Webserver laufen! Ist das nicht toll?

![Es hat funktioniert!][3]

 [3]: images/it_worked2.png

Bereit für den nächsten Schritt? Es wird Zeit ein paar Inhalte hinzuzufügen!