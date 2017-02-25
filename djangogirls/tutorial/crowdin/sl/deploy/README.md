# Postavitev!

> **Opomba** Nekatera mesta tega poglavja se vam bodo morda zdela zahtevna. Ne vrzite puške v koruzo in se prebijte do konca; postavitev je pomemben korak v razvoju spletne strani. To poglavje se nahaja na sredini vodiča, zato da vam lahko vaš mentor oz. mentorica pomaga pri zahtevnejših korakih objave spletne strani. Tako lahko vodič končate tudi sami, če bi vam slučajno zmanjkalo časa.

Dostop do vaše spletne strani je trenutno mogoč samo prek vašega računalnika, zato se bomo sedaj posvetili postavitvi! Postavitev pomeni objaviti vašo aplikacijo na spletu, da bodo ljudje lahko končno uvideli vašo aplikacijo :).

Sedaj že veste, da mora biti spletna stran na strežniku. Obstaja veliko ponudnikov spletnega gostovanja. Mi bomo uporabili ponudnika, ki ima dokaj enostavni postopek postavitve: [PythonAnywhere][1]. PythonAnywhere je brezplačno gostovanje za manjše aplikacije, ki nimajo velikega števila obiskovalcev, kar zadostuje našim trenutnim potrebam.

 [1]: http://pythonanywhere.com/

Pri postavitvi bomo uporabili še eno zunanjo storitev: [GitHub][2] - storitev za gostovanje kode. Seveda so na voljo tudi druge rešitve, a večina programerjev ima GitHub račun. In sedaj ga imate tudi vi!

 [2]: http://www.github.com

GitHub je vmesni korak v postopku prenosa kode na in iz PythonAnywhere.

# Git

Git je "sistem za porazdeljeno dokumentiranje sprememb in izdajanje različic datotek", ki ga uporablja veliko programerjev. Ta programska oprema sledi spremembam v vaših datotekah, kar vam omogoča, da lahko v nadaljevanju prikličete prejšnje različice. Delovanje je podobno "Sledi spremembam" v programu Microsoft Word, vendar veliko bolj zmogljivo.

## Namestitev Git

> **Opomba** Če ste programsko opremo že namestili, lahko ta korak preskočite in pričnite z ustvarjanjem svojega Git repozitorija.

{% include "deploy/install_git.md" %}

## Ustvarimo Git repozitorij

Git sledi sprememba določenemu naboru datotek, ki ga imenujemo repozitorij kode (ali na kratko "repo"). Ustvarimo repozitorij za naš projekt. Odprite upravljalnik in v imeniku `djangogirls` zaženite te ukaze:

> **Opomba** Preverite delujoči imenik, tako da zaženete ukaz `pwd` (OSX/Linux) oziroma `cd` (Windows), To storite preden inicializirate repozitorij. Nahajati se morate v mapi `djangogirls`.

    $ git init
    Inicializir prazen Git repozitorij v ~/djangogirls/.git/
    $ git config --global user.name "Vaše ime"
    $ git config --global user.email vaš.naslov@primer.si
    

Git repozitorij je treba inicializirati le enkrat na projekt (uporabniško ime in e-poštni naslov pa nastavite samo enkrat).

Git sledi spremembam datotek in map v tem imeniku. Kaj pa če želimo, da sistem ne sledi spremembam določenih datotek? V izvirnem imeniku ustvarimo datoteko `.gitignore`. Odprite urejevalnik in ustvarite novo datoteko s sledečo vsebino:

    *.pyc
    __pycache__
    myvenv
    db.sqlite3
    .DS_Store
    

Datoteko shranite kot `.gitignore` v vrhnjo mapo "djangogirls".

> **Opomba** Ne pozabite pike na začetku imena, saj je pomembna! Če imate težave (tako na primer operacijski sistem Mac ni naklonjen ustvarjanju datotek v programu Finder, katerih ime se začnejo s piko), uporabite preverjeno možnost "Shrani kot".

Dobra navada je, da zaženete ukaz `git status` preden zaženete `git add` oziroma ne veste, kaj je bilo spremenjeno. Na tak način se izognete neprijetnim presenečenjem, kot na primer dodajanju ali potrjevanju napačnih datotek. Ukaz `git status` vrne informacije o datotekah, ki jim sistem ne sledi/niso spremenjene/niso pripravljene za potrditev, o stanju vej in številne druge podatke. Izhod izgleda nekako tako:

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
    

Na koncu shranimo spremembe. V vašem upravljalniku zaženite te ukaze:

    $ git add -A .
    $ git commit -m "My Django Girls app, first commit"
     [...]
     13 files changed, 200 insertions(+)
     create mode 100644 .gitignore
     [...]
     create mode 100644 mysite/wsgi.py
    

## Prenos kode na GitHub

Pojdite na [GitHub.com][2] in se registrirajte (če ste to že storili tekom priprave na delavnico, je to super!)

Nato ustvarite repozitorij in ga poimenujte "my-first-blog". Ne izberite "initialise with a README", opcijo .gitignore pa pustite prazno (to smo že storili) in pri License pustite None.

![][3]

 [3]: images/new_github_repo.png

> **Opomba** Ime `my-first-blog` je pomembno -- lahko določite drugačno ime. Ker pa ta vodič velikokrat uporablja to ime, je bolj priročno, če uporabite kar to ime. Če uporabite ime `my-first-blog`, si poenostavite učenje..

Na naslednjem posnetku boste videli URL kloniranega repozitorija. Izberite različico "HTTPS" in jo kopirajte. Kmalu jo bomo prilepili v terminal:

![][4]

 [4]: images/github_get_repo_url_screenshot.png

Sedaj moramo povezati Git repozitorij na našem računalniku z repozitorijem na spletnem mestu GitHub.

V konzoli vnesite ta ukaz (namesto `<your-github-username>` vnesite svoje GitHub uporabniško ime in odstranite lomljene oklepaje):

    $ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
    $ git push -u origin master
    

Vnesite GitHub uporabniško ime in geslo. Sedaj se vam more pojaviti nekaj takšnega:

    Username for 'https://github.com': hjwp
    Password for 'https://hjwp@github.com':
    Counting objects: 6, done.
    Writing objects: 100% (6/6), 200 bytes | 0 bytes/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/hjwp/my-first-blog.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.
    

<!--TODO: maybe do ssh keys installs in install party, and point ppl who dont have it to an extention -->

Vaša koda je spletnem metu GitHub. Pojdite na spletno stran in se prepričajte! Vaša koda je v odlični družbi projektov - [Django][5], [Django Girls Tutorial][6] in drugih krasnih odprtokodnih programskih projektov, ki svojo kodo gostijo na spletnem mestu GitHub :)

 [5]: https://github.com/django/django
 [6]: https://github.com/DjangoGirls/tutorial

# Nastavitev bloga na PythonAnywhere

> **Opomba** Če že imate PythonAnywhere račun, ni potrebno ustvariti novega.

{% include "deploy/signup_pythonanywhere.md" %}

## Prenos kode na PythonAnywhere

Ko se registrirate na PythonAnywhere, vas aplikacija preusmeri na pregledno ploščo oziroma stran "Consoles". Zaženite upravljalnik "Bash" -- to je PythonAnywhere različica upravljalnika, ki je podoben tistemu na vašem računalniku.

> **Opomba** PythonAnywhere je zgrajen na sistemu Linux. Če uporabljate Winodws, bo upravljalnik rahlo nevajen.

Prenesimo kodo iz spletnega mesta GitHub, tako da ustvarimo "klon" repozitorija. V upravljalniku vtipkajte (ne pozabite zamenjati `<your-github-username>` z vašim uporabniškim imenom):

    $ git clone https://github.com/<your-github-username>/my-first-blog.git
    

S tem ukazom na PythonAnywhere prenesete kopijo vaše kode. Preverite prenos tako, da zaženete `tree my-first-blog`:

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
    

### Virtualno okolje na PythonAnyhwere

Na enak način, kot ste na svojem računalniku ustvarili virtualno okolje z ukazom virtualenv, lahko na PythonAnywhere ustvarite virtualno okolje. V ukazni lupini zaženite:

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
    

> **Opomba** Ukaz `pip install` lahko traja nekaj minut. Potrpežljivost je vrlina! Kljub temu: če izvajanje ukaza traja več kot 5 minut, je prišlo do napake. Obrnite se na vašega mentorja.

<!--TODO: think about using requirements.txt instead of pip install.-->

### Zbiranje statičnih datotek.

Vas zanima kaj je "whitenoise"? To je orodje za streženje t.i. "statičnih dodatek". Statične datoteke so datoteke, ki se praviloma ne spreminjajo in ne izvajajo programske kode. Primer statičnih datotek so datoteke HTML in CSS. Te datoteke se na strežnikih obnašajo drugače, kot se obnašajo na naših računalnikih, zato potrebujete orodja, kot na primer "whitenoise", da jih strežete.

S statičnimi datotekami se bomo podrobneje seznanili v nadaljevanju, ko bomo urejali CSS datoteko za našo stran.

Zaenkrat je dovolj, da vemo, da moramo na strežniku zagnati tudi ukaz `collectstatic`. S pomočjo tega ukaza Django na strežniku zbere vse statične datoteke, ki jih potrebuje. Zaenkrat so to večinoma datoteke za stran admin.

    (mvenv) $ python manage.py collectstatic
    
    You have requested to collect static files at the destination
    location as specified in your settings:
    
        /home/edith/my-first-blog/static
    
    This will overwrite existing files!
    Are you sure you want to do this?
    
    Type 'yes' to continue, or 'no' to cancel: yes
    

Vtipkajte "yes" in zaženite stroj! Ali tudi vas pogled na tiskanje neskončnih strani nedojemljivega besedila napolni s toplino? Predlagamo, da samodejno tiskanje računalnika pospremite z zvoki. Brp, brp brp...

    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/actions.min.js'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/inlines.min.js'
    [...]
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/changelists.css'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/base.css'
    62 static files copied to '/home/edith/my-first-blog/static'.
    

### Ustvarjanje podatkovne baze na PythonAnywhere

Še ena zadeva, kjer se vaš računalniku in strežnik razlikujeta: uporabljata različne baze podatkov. Posledično se lahko razlikujejo tudi uporabniški računi in objave na računalniku in strežniku.

Bazo podatkov na strežniku zaženemo tako, kot smo jo zagnali na računalniku - z ukazoma `migrate` in `createsuperuser`:

    (mvenv) $ python manage.py migrate
    Operations to perform:
    [...]
      Applying sessions.0001_initial... OK
    
    
    (mvenv) $ python manage.py createsuperuser
    

## Objava bloga kot spletne aplikacije

Naša koda je na PythonAnywhere, naše virtualno okolje je pripravljeno, statične datoteke so zbrane in podatkovna baza je inicializirana. Vse je pripravljeno za objavo spletne aplikacije!

Za dostop do pregledne plošče klikniti na logotip PythonAnywhere. Kliknite na zavihek **Web** in izberite **Add a new web app**.

Potem ko potrdite domensko ime, izberite **manual configuration** (NB *not* opcija"Django"). Izberite **Python 3.4** in pritisnite Next, da zaprete čarovnika.

> **Opomba** Pazite, da izberete "Manual configuration" in ne "Dajngo", ker smo preveč cool, da bi uporabljali privzete nastavitve PythonAnywhere ;-)

### Nastavitve virtualnega okolja

Preusmerjeni boste na zaslon za nastavitve PythonAnywhere za vašo spletno aplikacijo. Ob vsaki spremembi aplikacije na strežniku morate na to stran.

![][7]

 [7]: images/pythonanywhere_web_tab_virtualenv.png

V oddelku "Virtualenv" izberite rdeče besedilo "Enter the path to a virtualenv", in vnesite: `/home/<your-username>/my-first-blog/myvenv/`. Pred nadaljevanjem kliknite modro komponento z oznako za izbrano, da shranite pot.

> **Opomba** Po potrebi zamenjajte vaše uporabniško ime. Če se zmotite, PythonAnywhere prikaže opozorilo.

### Nastavitev datoteke WSGI

Django uporablja "protokol WSGI". To je standard za streženje spletnih strani s Pythonom, ki ga podpira PythonAnywhere. Če želimo, da PythonAnywhere prepozna naš Django blog, moramo uredit konfiguracijsko datoteko WSGI.

Kliknite na povezavo "WSGI configuration file" (v oddelku "Code", ki se nahaja tik pod vrhom strani -- pisalo bo nekaj podobnega `/var/www/<your-username>_pythonanywhere_com_wsgi.py`). Odpre se urejevalnik.

Vsebino zamenjajte s tem:

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
    

> **Opomba** Ne pozabite vnesti vaše uporabniško ime na mestu, kjer je navedeno `<your-username>`

Ta datoteke pove PythonAnywhere kje se nahaja vaša spletna aplikacija in kakšno je ime nastavitvene datoteke za Django. Datoteka nastaviti tudi orodje "whitenoise".

Pritisnite **Save** in pojdite nazaj na zavihek **Web**.

To je to! Pritisnite gumb **Reload** in lahko si boste ogledali vašo aplikacijo. Na vrhu strani se bo pojavila povezava od strani.

## Nasveti za razhroščevanje

Če opazite napako, ko greste na vašo spletno stran, je prvi naslov za razhroščevanje **error log**. Povezavo najdete v zavihku [Web][8] na PythonAnywhere. Preverite, ali je zabeleženo kakšno sporočilo o napakah; novejše so na dnu. Pogoste napake so:

 [8]: https://www.pythonanywhere.com/web_app_setup/

*   Preskočili ste kak korak v upravljalniku: ustvariti virtualno okolje, aktivacija virtualnega okolja, namestitev Django, zagon ukaza collectstatic, migracija podatkovne baze.

*   Nepravilen vnos poti do virtualnega okolja v zavihku Web -- če gre za to napako, boste verjetno zagledali majhno rdečo sporočilo.

*   Napaka v konfiguracijski datotke WSGI -- ali je pot do mape my-first-blog pravilna?

*   Ali sta različici Pythona v virtualnem okolju in spletni aplikaciji enaki? Obe morata biti 3.4.

*   Na spletni strani [general debugging tips on the PythonAnywhere wiki][9] so navedeni številni primeri.

 [9]: https://www.pythonanywhere.com/wiki/DebuggingImportError

Vedno pa se lahko obrnete na vašega mentorja!

# Aplikacija je v etru!

Na privzeti strani mora pisati "Welcome to Django", tako kot na vašem računalniku. Poizkusite dodati `/admin/` na koncu URL-ja in prikazati se morala admin stran. Prijavite se z uporabniškim imenom in geslom. Sedaj lahko dodajate nove objave na strežniku.

Dajte si *VELIK* aplavz! Postavitev na strežnik je med najzahtevnejšimi koraki spletnega razvoja in nemalokrat traja več dni, preden deluje, tako kot mora. Vam pa je uspelo zagnati spletno stran, kar tako!