# Tvoj prvi Django projekt!

> To poglavje delno temelji na vodiču Geek Girls Carrots (http://django.carrots.pl/).
> 
> To poglavje delno temelji na vodiču [django-marcador tutorial][1], ki je zaščiten preko Creative Commons Attribution-ShareAlike 4.0 International License. Vodič django-marcador tutorial je avtorsko delo Markus Zapke-Gründemann et al.

 [1]: http://django-marcador.keimlink.de/

Naredila boš svoj blog!

Za začetek ustvarimo nov Django projekt. To bomo naredili s pomočjo programčka, ki smo ga dobili ob namestitvi Djanga. Ustvaril nam bo nekaj imenikov in datotek, ki nam bodo omogočile lažji in hitrejši začetek.

Imena nekaterih imenikov in datotek so Djangu zelo pomembna. Zato datotek, ki jih bomo v nadaljevanju ustvarili, ne preimenuj. Prav tako jih raje ne premikaj. Django ima namreč za veliko datotek v spominu shranjeno, kje približno se nahajajo in kako se jim reče, zato ga lahko s spremembami zmedemo.

> Ne pozabi, da moraš projekt delati znotraj virtualnega okolja. Če torej na začetku vrstice v konzoli ne vidiš predpone kot je `(myvenv)`, moraš navidezno okolje zagnati. Kako se to naredi smo podrobno pojasnili v poglavjih **Namestitev Djanga** in **Osnove dela z ukazno vrstico**. V Windowsih vpiši `myvenv\Scripts\activate`, na Mac OS / Linux pa `source myvenv/bin/activate`.

V konzolo na MacOS ali Linux vpiši sledeči ukaz; **na konec ne pozabi dodati `.`**:

    (myvenv) ~/djangogirls$ django-admin startproject mysite .
    

Na Windowsih: **na konec ne pozabi dodati `.`**:

    (myvenv) C:\Users\Name\djangogirls> django-admin startproject mysite .
    

> Pika je pomembna, ker programu pove, da mora v trenutni imenik (okrajšava zanj je .) namestiti Django
> 
> **Opomba** Ko prepisuješ zgornje ukaze, ne pozabi, da moraš prepisati le od `django-admin` ali `django-admin.py` naprej. `(myvenv) ~/djangogirls$` in `(myvenv) C:\Users\Name\djangogirls>` sta le primera tega, kako mora zgledati vrstica v konzoli.

`django-admin.py` je program, ki bo zate naredil nekaj imenikov in datotek. Recimo takih:

    djangogirls
    ├───manage.py
    └───mysite
            settings.py
            urls.py
            wsgi.py
            __init__.py
    

`manage.py` je program, ki pomaga pri upravljanju spletne strani. Z njim bomo recimo na našem računalniku lahko zagnali strežnik.

`settings.py` vsebuje podatke o nastavitvah naše spletne strani.

`urls.py` pove, kateri del spletne strani naj se pokaže, ko v brskalnik vpišemo določen url naslov.

Ostale datoteke zaenkrat prezrimo, saj jih ne bomo rabili spreminjati. Nikakor pa jih ne spreminjaj ali briši!

## Spreminjanje nastavitev

Malce bomo spremenili datoteko `mysite/settings.py`. Odpri jo v urejevalniku programske kode, ki si ga prej namestila.

Na naši strani bi bilo dobro imeti pravilen čas in datum. Pojdi na [wikipedia timezones list][2] in prekopiraj ustrezen časovni pas (TZ). (npr. `Europe/Ljubljana` )

 [2]: http://en.wikipedia.org/wiki/List_of_tz_database_time_zones

V settings.py najdi vrstico, v kateri piše `TIME_ZONE` in to ustrezno spremeni v prej izbran časovni pas:

    python
    TIME_ZONE = 'Europe/Ljubljana'
    

Podatek "Europe/Ljubljana" lahko seveda ustrezno spremeniš

Djangu moramo povedati še, kje se nahajajo statične datoteke (več o njih bomo izvedeli kasneje). Premakni se na *konec*datoteke in pod `STATIC_URL` dodaj `STATIC_ROOT`:

    python
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    

## Namestitev podatkovne baze

Obstaja veliko različne programske opreme, ki lahko shranjuje podatke za našo stran (taki programski opremi rečemo podatkovna baza). Uporabili bomo privzeto, `sqlite3`.

Kot lahko opazimo v `mysite/settings.py`, je sqlite3 že nastavljena:

    python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    

Podatkovno bazo bomo ustvarili z ukazom: `python manage.py migrate` (biti moramo v imeniku `djangogirls`, saj le ta vsebuje datoteko `manage.py`). Pokazati se mora nekaj takšnega:

    (myvenv) ~/djangogirls$ python manage.py migrate
    Operations to perform:
      Synchronize unmigrated apps: messages, staticfiles
      Apply all migrations: contenttypes, sessions, admin, auth
    Synchronizing apps without migrations:
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
    

Končano! Zdaj lahko zaženemo strežnik in se prepričamo, da naša stran deluje!

Biti moraš v imeniku `djangogirls`, saj le ta vsebuje datoteko `manage.py`. Strežnik zaženeš tako, da v ukazno vrstico vpišeš `python manage.py runserver`:

    (myvenv) ~/djangogirls$ python manage.py runserver
    

Če si na Windowsih in dobiš napako `UnicodeDecodeError`, uporabi sledečo različico prejšnjega ukaza:

    (myvenv) ~/djangogirls$ python manage.py runserver 0:8000
    

Zdaj si lahko spletno stran končno ogledaš. Odpri svoj najljubši brskalnik in pojdi na naslov:

    http://127.0.0.1:8000/
    

Strežnik si bo ukazno vrstico vzel zase, dokler ga ne boš ustavila. Če želiš med tem, ko je strežnik zagnan, vpisati kak ukaz, moraš odpreti novo okno ukazne vrstice in ponovno aktivirati virtualno okolje. Strežnik ustaviš tako, da se premakneš v okno tisto okno ukazne vrstice v katerem teče in pritisneš CTRL+C - Control in C gumb naenkrat (na Windowsih pa v določenih primerih Ctrl+Break).

Čestitke! Naredila si svojo prvo spletno stran na svojem lastnem strežniku!

![Deluje!][3]

 [3]: images/it_worked2.png

Si pripravljena na naslednje poglavje? Čas je, da na našo stran kaj napišemo!