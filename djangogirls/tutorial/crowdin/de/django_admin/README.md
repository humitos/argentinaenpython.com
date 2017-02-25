# Django Administration

Zum hinzufügen, bearbeiten und löschen von Blogposts benutzen wir Django Admin, das eingebaute Administrations-Backend von Django.

Öffne die Datei `blog/admin.py` und ersetze den Inhalt wie folgt:

    python
    from django.contrib import admin
    from .models import Post
    
    admin.site.register(Post)
    

Wie du siehst, importieren wir hier das Model "Post", das wir im vorigen Kapitel erstellt haben. Damit unser Model auf der Admin-Seite sichtbar wird, müssen wir es mit `admin.site.register(Post)` registrieren.

Okay, wir sehen uns nun unser Post Model an. Denk daran `python manage.py runserver` in die Konsole einzugeben um den Webserver zu starten. Öffne dann deinen Browser und gib die Adresse http://127.0.0.1:8000/admin/ ein. Du solltest nun eine Login Seite wie diese sehen:

![Anmeldeseite][1]

 [1]: images/login_page2.png

Um dich einzuloggen, musst du einen *superuser* erzeugen - einen Benutzer, welcher Kontrolle über Alles auf der Site hat. Gehe zurück zu der Kommandozeile und tippe ein `python manage.py createsuperuser`, und drücke Enter. Wenn aufgefordert, tippe deinen Benutzernamen (Kleinbuchstaben, keine Leerzeichen), E-Mail-Adresse und Passwort ein. Keine Sorge, dass du das Passwort nicht siehst, das du gerade eingibst - das soll so sein. Tippe es einfach ein und drücke `Enter` um fortzufahren. Du solltest nun folgendes sehen (wobei Username und Email deine sein sollten):

    (myvenv) ~/djangogirls$ python manage.py createsuperuser
    Username: admin
    Email address: admin@admin.com
    Password:
    Password (again):
    Superuser created successfully.
    

Geh nochmal in deinen Browser und log dich mit den Daten des Superusers ein, den du gerade erstellt hast. Du solltest nun das Django Admin Dashboard sehen.

![Django Administration][2]

 [2]: images/django_admin3.png

Gehe zu Posts und experimentiere ein wenig damit. Füge 5 oder 6 Blog Posts hinzu. Mach dir keine Sorgen wegen des Inhalts - du kannst einfach etwas Text aus diesem Tutorial kopieren und einfügen um Zeit zu sparen :-).

Achte darauf, dass bei wenigstens zwei oder drei Posts (aber nicht bei allen) das Veröffentlichungsdatum (publish date) eingetragen ist. Das werden wir später noch brauchen.

![Django Administration][3]

 [3]: images/edit_post3.png

Wenn du mehr über Django Admin wissen willst solltest du dir hier die Django Dokumentation ansehen: https://docs.djangoproject.com/en/1.8/ref/contrib/admin/

Jetzt ist wahrscheinlich ein guter Moment um dir einen Kaffee (oder Tee) zu gönnen und neue Kraft tanken. Du hast dein erstes Django Model erstellt - du hast dir eine kleine Pause verdient!