# Veröffentlichen!

> **Hinweis** Durch das folgende Kapitel muss man sich manchmal durchbeißen. Bleib dran und gib nicht auf; die Website zu veröffentlichen ist ein sehr wichtiger Schritt. Dieses Kapitel ist in der Mitte des Tutorials platziert, damit dir dein Mentor mit dem etwas anspruchsvolleren Vorgang der Veröffentlichung deiner Website helfen kann. Den Rest des Tutorials kannst Du dann auch alleine beenden, sollte die Zeit nicht ausreichen.

Bis jetzt lief die Website nur auf deinem Computer, jetzt wollen wir sie veröffentlichen (deploy)! Deploy bedeutet, dass Du Deine Anwendung im Internet veröffentlichst, so dass endlich jeder darauf zugreifen kann :).

Wie Du ja schon gelernt hast, muss eine Webseite auf einem Server liegen. Im Internet gibt es sehr viele Server-Anbieter. Wir werden einen Anbieter mit relativ einfachem Veröffentlichungsprozess (deployment process) verwenden: [PythonAnywhere][1]. PythonAnywhere ist kostenlos für kleine Anwendungen, die nicht von vielen Besuchern aufgerufen werden. Also erstmal genau das richtige für dich.

 [1]: http://pythonanywhere.com/

Als weiteren externen Dienst werden wir [GitHub][2] nutzen, einen "Code Hosting"-Dienst. Es gibt noch andere solcher Dienste, aber die meisten Programmierer haben heute ein Konto bei Github, und du gleich auch!

 [2]: http://www.github.com

GitHub wird unsere Basis für die Übertragung unseres Code von und nach PythonAnywhere sein.

# Git

Git ist ein "Versionsverwaltungssystem", das von vielen Programmierern benutzt wird. Diese Software kann Änderungen an Dateien über die Zeit verfolgen, so dass du bestimmte Versionen im Nachhinein wieder aufrufen kannst. Ein bisschen wie die "Track Changes" Funktion in Microsoft Word, aber viel leistungsfähiger.

## Git installieren

> **Hinweis** Falls du die Installationsschritte bereits durchgeführt hast, dann kannst du mit dem nächsten Abschnitt fortfahren und deine Git-Repository erstellen.

{% include "code_editor/instructions.md" %}

## Unser Git-Repository

Git verwaltet die Veränderungen an einer Sammlung von Dateien in einem sogenannte Repository (oder kurz "Repo"). Legen wir eines für unser Projekt an. Öffne deine Konsole und gibt folgende Kommandos im `djangogirls`-Verzeichnis ein:

> **Hinweis** Überprüfe dein aktuelles Arbeitsverzeichnis mit dem Befehl `pwd` (OSX/Linux) oder `cd` (Windows) bevor du das Repository initialisierst. Du musst im `djangogirls`-Verzeichnis sein.

    $ git init 
    Initialized empty Git repository in ~/djangogirls/.git/ 
    $ git config --global user.name "Dein Name" 
    $ git config --global user.email you@example.com
    

Die Initialisierung einer Git-Repository müssen wir nur einmal pro Projekt machen. (und du musst nicht erneut deinen Benutzernamen und E-Mail-Adresse eingeben).

Git wird die Änderungen an all den Dateien und Ordnern in diesem Verzeichnis aufzeichnen, aber wir wollen, dass einige Dateien ignoriert werden. Dazu legen wir eine Datei `.gitignore` im Basisverzeichnis des Repos an. Öffne Deinen Editor und erstelle eine neue Datei mit dem folgenden Inhalt:

    *.pyc
    __pycache__
    myvenv
    db.sqlite3
    .DS_Store
    

Speichere die Datei mit dem Namen `.gitignore` im "djangogirls"-Verzeichnis.

> **Hinweis** Der Punkt am Anfang des Dateinames ist wichtig! Wenn du Schwierigkeiten beim Erstellen haben solltest (Macs lassen z.B. im Finder keine Dateien mit Punkt am Anfang erzeugen), dann verwende die "Speichern unter"-Funktion im Editor, das sollte immer funktionieren. [Punkt-Dateien sind auf Linux und OS X "versteckte Dateien".]

Es ist hilfreich den Befehl `git status` vor `git add` auszuführen oder immer dann, wenn du dir unsicher bist, was geändert wurde. Das schützt vor manchen Überraschungen wie z.B. das falsche Hinzufügen oder Übertragen von Dateien. Das `git status`-Kommando gibt Informationen über unbeobachtete/veränderte/hinzugefügte Dateien, den Verzweigungsstatus und einiges mehr wieder. Die Ausgabe sollte diesem ähnlich sein:

    $ git status 
    On branch master 
    
    Initial commit 
    
    Untracked files:
       (use "git add <file>..." to include in what will be committed) 
    
            .gitignore
             blog/
             manage.py
             mysite/ 
    
    nothing added to commit but untracked files present (use "git add" to track)
    

Nun speichern wir unsere Änderungen durch folgende Eingabe in der Konsole:

    $ git add -A .
    $ git commit -m "Meine Django Girls App, erster Commit"
     [...]
     13 files changed, 200 insertions(+)
     create mode 100644 .gitignore
     [...]
     create mode 100644 mysite/wsgi.py
    

## Den Code auf GitHub veröffentlichen

Öffne [GitHub.com][2] und registriere dich für ein neues, kostenloses Benutzerkonto. (Wenn du das bereits in deiner Vorbereitung auf dem Workshop getan hast, dann ist das großartig!)

Erstelle dann ein neues Repository und gib ihm den Namen "my-first-blog". Lass das Kontrollkästchen "initialise with a README" deaktiviert, die Einstellung der Option .gitignore frei (das haben wir schon von Hand gemacht) und lass die Lizenz auf "None".

![][3]

 [3]: images/new_github_repo.png

> **Achtung** Der Name `my-first-blog` ist wichtig -- du kannst auch einen anderen wählen, aber er wird im folgenden noch sehr oft vorkommen und du wirst immer daran denken müssen ihn in den Anweisungen entsprechend anzupassen. Lass es besser erst mal bei `my-first-blog`.

Auf der nächsten Seite wird dir die Clone URL des Repos angezeigt. Nimm die HTTPS-Variante, kopiere sie und füge sie in der Konsole ein:

![][4]

 [4]: images/github_get_repo_url_screenshot.png

Nun müssen wir das Git Repository auf deinem Computer mit dem auf GitHub verbinden.

Gib Folgendes in deine Konsole ein (Ersetze dabei `<your-github-username>` durch deinen Benutzernamen, den du bei der Erstellung deines GitHub-Kontos benutzt hast, aber ohne die eckigen Klammern):

    $ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
    $ git push -u origin master
    

Gibt deinen GitHub Benutzernamen und dein Passwort ein und du solltest etwas ähnliches wie das hier sehen:

    Username for 'https://github.com': hjwp
    Password for 'https://hjwp@github.com':
    Counting objects: 6, done.
    Writing objects: 100% (6/6), 200 bytes | 0 bytes/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/hjwp/my-first-blog.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.
    

<!--TODO: maybe do ssh keys installs in install party, and point ppl who dont have it to an extention -->

Dein Code ist jetzt auf GitHub. Schau gleich mal nach! Dort ist dein Code du in guter Gesellschaft - [Django][5], das [Django Girls Tutorial][6] und viele andere großartige Open Source Software-Projekte haben ihren Code auf GitHub :)

 [5]: https://github.com/django/django
 [6]: https://github.com/DjangoGirls/tutorial

# Dein Blog auf PythonAnywhere aufsetzen

> **Hinweis** Es ist möglich, dass du bereits ein PythonAnywhere Konto angelegt hast. Wenn ja, dann brauchst du das nicht nochmal machen.

{% include "deploy/signup_pythonanywhere.md" %}

## Den Code nach PythonAnywhere übertragen

Sobald du dich für PythonAnywhere angemeldet hast, wirst du zu deinem Dashboard bzw. deiner "Konsole" weitergeleitet. Wähle die Option zum Starten einer "Bash"--, das ist die PythonAnywhere Version einer Konsole, genau wie die auf deinem Computer.

> **Hinweis** PythonAnywhere basiert auf Linux. Wenn du Windows benutzt, dann sieht die Konsole etwas anders aus als die Konsole auf deinen Computer.

Lass uns den Code von GitHub auf Pythonanywhere übertragen indem wir einen "Klon" unseres Repositoriums erzeugen. Tippe das Folgende in die Konsole auf PythonAnywhere (vergesse nicht deinen GitHub Benutzernamen an Stelle von `<your-github-username>` zu benutzen):

    $ git clone https://github.com/<your-github-username>/my-first-blog.git
    

Dies wird eine Kopie deines Codes auf PythonAnywhere übertragen. Überprüfe es indem du eingibst `tree my-first-blog`:

    $ tree my-first-blog
    my-first-blog/
    ├── blog
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
    

### Erstelle eine virtualenv auf PythonAnywhere

Genauso wie du auf deinen eigenen Computer eine virtualenv erstellt hast, kannst du auch eine auf PythonAnywhere erstellen. Schreibe Folgendes in die Bash:

    $ cd my-first-blog
    
    $ virtualenv --python=python3.4 myvenv
    Running virtualenv with interpreter /usr/bin/python3.4
    [...]
    Installing setuptools, pip...done.
    
    $ source myvenv/bin/activate 
    
    (mvenv) $ pip install django whitenoise 
    Collecting django 
    [...] 
    Successfully installed django-1.8.2 whitenoise-2.0
    

> **Hinweis** Der Schritt `pip install` kann ein paar Minuten dauern. Hab etwas Geduld! Aber, wenn es länger als 5 Minuten dauern sollte, dann ist etwas falsch gelaufen. Frage am besten deinen Coach.

<!--TODO: think about using requirements.txt instead of pip install.-->

### Statische Dateien sammeln.

Hast du dich gefragt was die "whitenoise" Sache war? Es ist ein Werkzeug um so genannte "statische Dateien" zu betreuen. Statische Dateien wie z. B. HTML oder CSS Dateien sind Daten, welche sich nicht regelmäßig verändern oder Programmcode ausführen. Sie funktionieren anders auf Servern als auf unseren eigenen Computern und wir brauchen ein Werkzeug wie "whitenoise" um sie zu betreuen.

Wir werden später im Tutorial ein wenig mehr über statische Dateien erfahren wenn wir das CSS für unsere Site bearbeiten.

Für`s Erste müssen wir nur ein extra Kommando auf dem Server ausführen, genannt `collectstatic`. Es befiehlt Django alle statischen Dateien die es auf dem Server braucht, einzusammeln. Im Moment sind dies hauptsächlich Dateien, welche die Admin Site hübsch aussehen lassen.

    (mvenv) $ python manage.py collectstatic
    
    You have requested to collect static files at the destination
    location as specified in your settings:
    
        /home/edith/my-first-blog/static
    
    This will overwrite existing files!
    Are you sure you want to do this?
    
    Type 'yes' to continue, or 'no' to cancel: yes
    

Tippe "yes" ein und es verschwindet! Liebst du es nicht auch Computer dazu zu bringen Seiten über Seiten von undurchdringbaren Text auszugeben? Ich mache immer kleine Geräusche um das zu begleiten. Brp, brp brp...

    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/actions.min.js'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/inlines.min.js'
    [...]
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/changelists.css'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/base.css'
    62 static files copied to '/home/edith/my-first-blog/static'.
    

### Erstellen einer Datenbank auf PythonAnywhere

Hier ist ein weiterer Unterschied zwischen deinen Computer und einem Server: unterschiedliche Datenbanken werden benutzt. Dadurch können sich Benutzerkonten und Posts auf dem Server und auf deinen Computer unterscheiden.

Wir initialisieren die Datenbank auf dem Server genauso wie wir es auf deinen Computer mit `migrate` und `createsuperuser` gemacht haben:

    (mvenv) $ python manage.py migrate 
    Operations to perform: 
    [...]
       Applying sessions.0001_initial... OK 
    
    
    (mvenv) $ python manage.py createsuperuser
    

## Veröffentlichen unseres Blogs als eine Web App

Jetzt ist unser Code auf PythonAnywhere, unser virtualenv ist bereit, die statischen Dateien sind gesammelt und die Datenbank ist initialisiert. Wir sind bereit es als Web App zu veröffentlichen!

Klicke zurück zum PythonAnywhere Dashboard indem du auf ihr Logo klickst und klicke auf den **Web** Menüpunkt. Schließlich klicke auf **Add a new web app**.

Nach der Bestätigung deines Domain Namens, wähle **manual configuration** (NB *nicht* die"Django" Option) in der Auswahl. Als nächstes wähle **Python 3.4** und klicke "Next" um den Assistenten zu beenden.

> **Hinweis** Stelle sicher, dass du die "Manual configuration" Option ausgewählt hast und nicht die "Django". Wir sind einfach zu cool für das Standard PythonAnywhere Django Setup :-)

### Angeben des Virtualenv

Du wirst weitergeleitet auf den PythonAnywhere Konfigurationsschirm für deine Webapp. Dies ist wohin du gehen musst wann immer du Änderungen an deiner App auf dem Server vornehmen willst.

![][7]

 [7]: images/pythonanywhere_web_tab_virtualenv.png

In der "Virtualenv" Sektion, klicke auf den roten Text, welcher sagt:"Enter the path to a virtualenv" und gebe ein: `/home/<your-username>/my-first-blog/myvenv/`. Klicke auf die blaue Box mit dem Häkchen um den Pfad zu speichern bevor es weitergeht.

> **Hinweis** Ersetze deinen eigenen Benutzernamen soweit erforderlich. Falls du einen Fehler machst, wird dir PythonAnywhere eine kleine Warnung anzeigen.

### Konfigurieren der WSGI-Datei

Django funktioniert durch Verwendung des "WSGI Protokolls", ein Standard um Websites mit Python zu versorgen, welcher von PythonAnywhere unterstützt wird. Die Art wie wir PythonAnywhere konfigurieren unseren Django Blog zu erkennen, geschieht durch editieren einer WSGI Konfigurationsdatei.

Klicke auf den "WSGI configuration file" Link (in der "Code" Sektion im oberen Teil der Seite -- es sollte ungefähr so benannt sein `/var/www/<your-username>_pythonanywhere_com_wsgi.py`) und du wirst zu einem Editor geführt.

Lösche alle Inhalte und ersetze sie durch etwas wie dies:

    python
    import os
    import sys
    
    path = '/home/<your-username>/my-first-blog'  # use your own username here
    if path not in sys.path:
        sys.path.append(path)
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    
    from django.core.wsgi import get_wsgi_application
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(get_wsgi_application())
    

> **Hinweis** Vergiss nicht deinen Benutzernamen an die Stelle `<your-username>` einzusetzen

Die Aufgabe dieser Datei ist es Pythonanywhere zu sagen wo unsere Web App lebt und wie der Django Einstellungsdateiname ist. Es richtet außerdem das "whitenoise" Werkzeug für statische Dateien ein.

Klick auf **Save** und gehe dann zu dem **Web**-Tab zurück.

Wir sind fertig! Drücke auf den großen grünen **Reload** Knopf und du kannst dir deine Applikation anschauen. Du findest einen Link zu ihr oben auf der Seite.

## Debugging Tipps

Falls du einen Fehler, beim Versuch deine Seite zu besuchen, siehst, ist der erste Ort an dem man nach Debugging Infos schauen sollte dein **error log**. Sie finden einen Link dazu auf dem PythonAnywhere [Web tab][8]. Schaue nach ob Fehlermeldungen enthalten sind; die neuesten sind unten. Häufige Probleme sind:

 [8]: https://www.pythonanywhere.com/web_app_setup/

*   Einen der Schritte vergessen, die wir in der Konsole gemacht haben: das virtualenv kreieren, es aktivieren, Django in es zu installieren, collectstatic auszuführen, die Datenbank zu migrieren.

*   Einen Fehler in dem virutalenv Pfad auf dem Web Tab machen -- falls es ein Problem gibt, wird normalerweise dann eine kleine rote Fehlermeldung dort erscheinen.

*   Einen Fehler in der WSGI Konfigurationsdatei machen -- hast du den Pfad zu deinem my-first-blog Ordner richtig?

*   Hast du die selbe Version von Python für dein virtualenv gewählt wie für deine Web App? Beide sollten 3.4 sein.

*   Es gibt einige [general debugging tips on the PythonAnywhere wiki][9].

 [9]: https://www.pythonanywhere.com/wiki/DebuggingImportError

Und denk dran, dein Coach ist da um dir zu helfen!

# Du bist live!

Die Standardseite für deine Site sollte anzeigen "Welcome to Django", genauso wie auf deinem lokalen Computer. Probiere `/admin/` am Ende der URL hinzuzufügen und du gelangst zur Adminseite. Melde dich mit deinen Benutzernamen und Passwort an. Wie du siehst, kannst du neue Posts auf dem Server hinzufügen.

Klopf dir *kräftig* auf die Schulter! Server Einrichtungen sind einige der kompliziertesten Dinge der Web Entwicklung und es dauert oftmals mehrere Tage bis man sie zum Laufen bringt. Aber du hast deine Site live, im echten Internet, einfach so!