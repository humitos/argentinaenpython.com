# Django admin

Za dodajanje, urejanje in brisanje objav, bomo uporabljali Django admin.

Odpri datoteko `blog/admin.py` in njeno vsebino zamenjaj s sledečo:

    python
    from django.contrib import admin
    from .models import Post
    
    admin.site.register(Post)
    

Kot vidiš, smo uvozili paket Post o katerem smo govorili v prejšnjem poglavju. Če hočemo, da bomo podatki, ki jih bomo s paketom Post ustvarili vidni, ga moramo registrirati z `admin.site.register(Post)`.

OK, zdaj si lahko bolj podrobno ogledamo Post. Ne pozabi v ukazni vrstici pognati ukaza `python manage.py runserver`. Pojdi zdaj v brskalnik in vpiši naslov http://127.0.0.1:8000/admin/ Prikazala se bo taka stran:

![Login page][1]

 [1]: images/login_page2.png

Za prijavo v sistem, moramo najprej ustvariti uporabnika. Kot prvega bomo ustvarili administratorja. V ukazni vrstici poženi ukaz `python manage.py createsuperuser`. Ko se program uspešno zažene, vpiši uporabniško ime (male črke, brez presledkov), elektronski naslov in geslo. Ko vnašaš geslo, se ne bo izpisovalo, kaj pišeš in tako tudi mora biti. Vnesi torej geslo in pritisni `enter`. Izhod programa bo približno tak:

    (myvenv) ~/djangogirls$ python manage.py createsuperuser
    Username: admin
    Email address: admin@admin.com
    Password:
    Password (again):
    Superuser created successfully.
    

Vrni se v brskalnik. Vpiši prej izbrane podatke in se prijavi.

![Django admin][2]

 [2]: images/django_admin3.png

Dodaj še par objav. Vsebina le-teh trenutno za nas ni važna. Lahko kar prekopiraš nekaj besedila iz našega vodiča. :)

Prepričaj pa se, da ima vsaj par od teh objav (vendar ne vse) določen datum objave. To nam bo prišlo prav kasneje.

![Django admin][3]

 [3]: images/edit_post3.png

Če želiš o Django adminu izvedeti še kaj več, si poglej dokumentacijo: https://docs.djangoproject.com/en/1.8/ref/contrib/admin/

Zdaj je primeren trenutek, da si vzameš malce pavze. Pravkar si naredila svojo prvo bazo podatkov, zato si jo vsekakor zaslužiš!