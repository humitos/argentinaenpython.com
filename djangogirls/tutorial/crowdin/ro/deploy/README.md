# Implementează!

> **Notă**: Următorul capitol poate fi, uneori, un pic cam greu de înțeles. Persistă şi du-l până la capăt; deployment-ul este o parte importantă a procesului de dezvoltare a site-ului. Acest capitol este plasat la mijlocul tutorialului, astfel încât mentorul să te poată ajuta în procesul un pic mai complicat de a-ți duce website-ul online. Aceasta înseamnă că puteţi termina tutorialul pe cont propriu, dacă nu vă rămâne timp.

Până acum web-site-ul tău a fost disponibil doar pe calculatorul personal, însă acum vei învăța cum să-l transferi online! Deployment-ul este procesul de publicare a aplicației tale pe Internet, astfel încât aplicația să fie vizibilă pentru toți :).

Așa cum ați învățat, un website trebuie să fie localizat pe un server. Există o mulţime de furnizori de server disponibile pe internet. Vom folosi unul care simplifică procesul de deployment: [PythonAnywhere][1]. PythonAnywhere este gratuit pentru aplicațiile mici, care nu au prea mulți vizitatori, așa că îți va fi de ajuns și ție momentan.

 [1]: http://pythonanywhere.com/

Celălalt serviciu extern pe care-l vom utiliza este [GitHub][2], un serviciu de găzduire de cod. Există și altele, însă aproape toţi programatorii au un cont de GitHub acum, așa că, acum, vei avea și tu unul!

 [2]: http://www.github.com

Vom folosi GitHub ca ca următorul pas pentru a ne transfera codul nostru spre și dinspre PythonAnywhere.

# Git

Git este un "sistem de versionare" folosit de mulți programatori. Acest software poate să urmărească schimbările făcute în fișiere de-a lungul timpului, pentru a putea reveni la anumite versiuni mai târziu. Seamănă cu funcția de "urmărire modificări" din Microsoft Word, dar este mult mai puternic.

## Instalarea Git

> **Note** Dacă deja ai trecut prin pașii de instalare, nu e nevoie să o faci din nou - poți trece direct la următoarea secțiune și să creezi repository-ul tău Git.

{% include "deploy/install_git.md" %}

## Inițializarea repository-ului Git propriu

Git depistează modificările unui anumit set de fişiere în ceea ce se numeşte un repository de cod (sau, pe scurt, "repo"). Să începem unul pentru proiectul nostru. Deschideți consola şi executaţi aceste comenzi, în directoriul `djangogirls`:

> **Note** Verifică directorul curent de lucru prin comanda `pwd` (OSX/Linux) sau `cd` (Windows), înainte de a inițializa repository-ul. Ar trebui să fiți în mapa `djangogirls`.

    $ git init
    Initialized empty Git repository in ~/djangogirls/.git/
    $ git config --global user.name "Numele tău"
    $ git config --global user.email tu@exemplu.com
    

Iniţializarea repozitoriului Git este ceva ce trebuie să facem o singură dată pentru fiecare proiect (şi nu va trebui să re-introduceţi numele de utilizator si e-mail din nou de fiecare dată).

Git va urmări modificările făcute în toate fişierele şi mapele în această directorie, dar există unele fişiere pe vrem să le ignore. Facem acest lucru prin crearea unui fişier numit `.gitignore` în directoriul de bază. Deschide editorul de cod şi creați un nou fişier cu următorul conținut:

    *.pyc
    __pycache__
    myvenv
    db.sqlite3
    .DS_Store
    

Şi salvaţi-l ca `.gitignore` în folderul de nivel superior, "djangogirls".

> **Note** Punctul de la începutul numelui de fișier este important! Dacă aveţi orice dificultăţi în crearea ei (calculatoarelor Mac nu le place să creaţi fişiere care încep cu un punct prin intermediul programului Finder, de exemplu), utilizați opțiunea ”Salvează ca” în editorul vostru de cod, este o metodă sigură.

Este o idee bună să folosiți comanda `git status` înaintea celei de `git add` sau ori de câte ori nu ești sigură legat de ceea ce s-a schimbat. Acest lucru va preveni apariția surprizelor precum adăugarea sau commit-ul fișierelor greșite. Comanda `git status` întoarce informații despre orice fișier care nu se află sub urmărire, e modificat sau staged, informații despre statutul branchului și multe altele. Ieșirea acestei comenzi ar trebui să arate așa:

    Primul commit:
    
    Fișiere încă neurmărite:
      (folosiți "git add <nume-fișier>..." pentru a-l include în commit)
    
            .gitignore
            blog/
            manage.py
            mysite/
    
    nothing added to commit but untracked files present (use "git add" to track)
    

Și în cele din urmă salvăm modificările. Intră în consolă și rulează aceste comenzi:

    $ git add -A .
    $ git commit -m "Aplicatia mea Django Girls, primul commit."
     [...]
     13 files changed, 200 insertions(+)
     create mode 100644 .gitignore
     [...]
     create mode 100644 mysite/wsgi.py
    

## Trimiterea codului către GitHub

Mergi la [GitHub.com][2] și înregistrează-te pentru un cont nou, gratuit, de utilizator. (Dacă deja ai făcut asta în pregătirea workshop-ului, e grozav!)

Crează un repository nou, numindu-l "my-first-blog". Lasă opțiunea "initialise with a README" debifată, opțiunea .gitignore necompletată (am făcut asta manual) și License ca None (niciuna).

![][3]

 [3]: images/new_github_repo.png

> **Notă** Numele `my-first-blog` este important -- ai putea alege și altceva, dar va fi des folosit în instrucțiunile de mai jos și ar trebui să înlocuiești numele de fiecare dată. Probabil că este mai ușor să rămâi la numele `my-first-blog`.

Pe următorul ecran îți va fi arătat URL-ul pentru clonarea repository-ului tău. Alege versiunea "HTTPS", copiază linkul și îl vom adăuga în terminal în curând:

![][4]

 [4]: images/github_get_repo_url_screenshot.png

Acum trebuie să legăm repository-ul de Git de pe calculatorul tău de cel de pe GitHub.

Scrie următoarele în consolă (Înlocuiește `<your-github-username>` cu numele de utilizator introdus atunci când ți-ai creat contul de GitHub, dar fără parantezele angulare):

    $ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
    $ git push -u origin master
    

Introdu numele de utilizator și parola GitHub și ar trebui să vezi ceva de genul acesta:

    Username for 'https://github.com': hjwp
    Password for 'https://hjwp@github.com':
    Counting objects: 6, done.
    Writing objects: 100% (6/6), 200 bytes | 0 bytes/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/hjwp/my-first-blog.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.
     
    Context | Request Context.
    

<!--TODO: maybe do ssh keys installs in install party, and point ppl who dont have it to an extention -->

Codul tău este acum pe GitHub. Du-te și verifică-l! Vei găsi alături de el și - [Django][5], tutorialul [Django Girls Tutorial][6], și multe alte proiecte open source grozave. Și ele își găzduiesc codul pe GitHub :)

 [5]: https://github.com/django/django
 [6]: https://github.com/DjangoGirls/tutorial

# Setting up our blog on PythonAnywhere

> **Note** You might have already created a PythonAnywhere account earlier during the install steps - if so, no need to do it again.

{% include "deploy/signup_pythonanywhere.md" %}

## Pulling our code down on PythonAnywhere

When you've signed up for PythonAnywhere, you'll be taken to your dashboard or "Consoles" page. Choose the option to start a "Bash" console -- that's the PythonAnywhere version of a console, just like the one on your computer.

> **Note** PythonAnywhere is based on Linux, so if you're on Windows, the console will look a little different from the one on your computer.

Let's pull down our code from GitHub and onto PythonAnywhere by creating a "clone" of our repo. Type the following into the console on PythonAnywhere (don't forget to use your GitHub username in place of `<your-github-username>`):

    $ git clone https://github.com/<your-github-username>/my-first-blog.git
    

This will pull down a copy of your code onto PythonAnywhere. Check it out by typing `tree my-first-blog`:

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
    

### Creating a virtualenv on PythonAnywhere

Just like you did on your own computer, you can create a virtualenv on PythonAnywhere. In the Bash console, type:

    $ cd my-first-blog
    
    $ virtualenv --python=python3.4 myvenv
    Running virtualenv with interpreter /usr/bin/python3.4
    [...]
    Installing setuptools, pip...done.
    
    $ source myvenv/bin/activate
    
    (mvenv) $  pip install django whitenoise
    Collecting django
    [...]
    Successfully installed django-1.8.2 whitenoise-2.0
    

> **Note** The `pip install` step can take a couple of minutes. Patience, patience! But if it takes more than 5 minutes, something is wrong. Ask your coach.

<!--TODO: think about using requirements.txt instead of pip install.-->

### Collecting static files.

Were you wondering what the "whitenoise" thing was? It's a tool for serving so-called "static files". Static files are the files that don't regularly change or don't run programming code, such as HTML or CSS files. They work differently on servers compared to on our own computer and we need a tool like "whitenoise" to serve them.

We'll find out a bit more about static files later in the tutorial, when we edit the CSS for our site.

For now we just need to run an extra command called `collectstatic`, on the server. It tells Django to gather up all the static files it needs on the server. At the moment these are mostly files that make the admin site look pretty.

    (mvenv) $ python manage.py collectstatic
    
    You have requested to collect static files at the destination
    location as specified in your settings:
    
        /home/edith/my-first-blog/static
    
    This will overwrite existing files!
    Are you sure you want to do this?
    
    Type 'yes' to continue, or 'no' to cancel: yes
    

Type "yes", and away it goes! Don't you love making computers print out pages and pages of impenetrable text? I always make little noises to accompany it. Brp, brp brp...

    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/actions.min.js'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/inlines.min.js'
    [...]
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/changelists.css'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/base.css'
    62 static files copied to '/home/edith/my-first-blog/static'.
    

### Creating the database on PythonAnywhere

Here's another thing that's different between your own computer and the server: it uses a different database. So the user accounts and posts can be different on the server and on your computer.

We can initialise the database on the server just like we did the one on your own computer, with `migrate` and `createsuperuser`:

    (mvenv) $ python manage.py migrate
    Operations to perform:
    [...]
      Applying sessions.0001_initial... OK
    
    
    (mvenv) $ python manage.py createsuperuser
    

## Publishing our blog as a web app

Now our code is on PythonAnywhere, our virtualenv is ready, the static files are collected, and the database is initialised. We're ready to publish it as a web app!

Click back to the PythonAnywhere dashboard by clicking on its logo, and go click on the **Web** tab. Finally, hit **Add a new web app**.

After confirming your domain name, choose **manual configuration** (NB *not* the "Django" option) in the dialog. Next choose **Python 3.4**, and click Next to finish the wizard.

> **Note** Make sure you choose the "Manual configuration" option, not the "Django" one. We're too cool for the default PythonAnywhere Django setup ;-)

### Setting the virtualenv

You'll be taken to the PythonAnywhere config screen for your webapp, which is where you'll need to go whenever you want to make changes to the app on the server.

![][7]

 [7]: images/pythonanywhere_web_tab_virtualenv.png

In the "Virtualenv" section, click the red text that says "Enter the path to a virtualenv", and enter: `/home/<your-username>/my-first-blog/myvenv/`. Click the blue box with the check mark to save the path before moving on.

> **Note** Substitute your own username as appropriate. If you make a mistake, PythonAnywhere will show you a little warning.

### Configuring the WSGI file

Django works using the "WSGI protocol", a standard for serving websites using Python, which PythonAnywhere supports. The way we configure PythonAnywhere to recognise our Django blog is by editing a WSGI configuration file.

Click on the "WSGI configuration file" link (in the "Code" section near the top of the page -- it'll be named something like `/var/www/<your-username>_pythonanywhere_com_wsgi.py`), and you'll be taken to an editor.

Delete all the contents and replace them with something like this:

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
    

> **Note** Don't forget to substitute in your own username where it says `<your-username>`

This file's job is to tell PythonAnywhere where our web app lives and what the Django settings file's name is. It also sets up the "whitenoise" static files tool.

Hit **Save** and then go back to the **Web** tab.

We're all done! Hit the big green **Reload** button and you'll be able to go view your application. You'll find a link to it at the top of the page.

## Debugging tips

If you see an error when you try to visit your site, the first place to look for some debugging info is in your **error log**. You'll find a link to this on the PythonAnywhere [Web tab][8]. See if there are any error messages in there; the most recent ones are at the bottom. Common problems include:

 [8]: https://www.pythonanywhere.com/web_app_setup/

*   Forgetting one of the steps we did in the console: creating the virtualenv, activating it, installing Django into it, running collectstatic, migrating the database.

*   Making a mistake in the virtualenv path on the Web tab -- there will usually be a little red error message on there, if there is a problem.

*   Making a mistake in the WSGI configuration file -- did you get the path to your my-first-blog folder right?

*   Did you pick the same version of Python for your virtualenv as you did for your web app? Both should be 3.4.

*   There are some [general debugging tips on the PythonAnywhere wiki][9].

 [9]: https://www.pythonanywhere.com/wiki/DebuggingImportError

And remember, your coach is here to help!

# You are live!

The default page for your site should say "Welcome to Django", just like it does on your local computer. Try adding `/admin/` to the end of the URL, and you'll be taken to the admin site. Log in with the username and password, and you'll see you can add new Posts on the server.

Give yourself a *HUGE* pat on the back! Server deployments are one of the trickiest parts of web development and it often takes people several days before they get them working. But you've got your site live, on the real Internet, just like that!