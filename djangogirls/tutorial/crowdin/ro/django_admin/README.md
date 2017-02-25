# Consola de admin din Django

Pentru adăugarea, editarea și ștergerea articolelor ce tocmai le-am descris în modele, vom utiliza consola de admin din Django.

Deschide fișierul `blog/admin.py` și înlocuiește conținutul său cu textul următor:

    python
    from django.contrib import admin
    from .models import Post
    
    admin.site.register(Post)
    

Așa cum poți observa, importăm (includem) modelul Post definit în capitolul anterior. Pentru a face modelul vizibil în consola de admin, trebuie să înregistrăm modelul cu instrucțiunea `admin.site.register(Post)`.

OK, acum este timpul să ne uităm la modelul Post. Reamintește-ți să rulezi comanda ` python manage.py runserver ` în linia de comandă pentru a rula serverul web. Deschide browserul web și introdu adresa http://127.0.0.1:8000/admin/. Vei vedea o pagină de login asemănătoare cu:

![Pagina de login][1]

 [1]: images/login_page2.png

Pentru a te loga în consola de admin, trebuie să creezi un *superuser* - un utilizator ce are control asupra tuturor resurselor din site. Pentru a crea un superuser trebuie să rulezi din linia de comandă `python manage.py createsuperuser`. Ți se va cere să introduci username (cu litere mici și fără spații), o adresă de email și parolă pentru user. Nu-ți face griji pentru că nu vezi ce parolă introduci - este comportamentul dorit. Introdu-o și apasă `enter` pentru a continua. Ceea ce vei vedea trebuie să fie asemănătoare cu (unde username și email ar trebui să fie cele introduse de tine):

    (myenv) ~/djangogirls$ python manage.py createsuperuser
    Username: admin
    Email address: admin@admin.com
    Password:
    Password (again):
    Superuser created successfully.
    

Întoarce-te la browserul web. Conectează-te cu credențialele superuserului pe care tocmai l-ai creat; vei putea să vezi consola de admin din Django.

![Consola de admin din Django][2]

 [2]: images/django_admin3.png

Navighează la secțiunea Posts și experimenteză puțin. Adaugă cinci sau șase postări de blog. Nu-ți face griji pentru conținut - poți copia niște text din acest tutorial ca să salvezi timp :).

Asigură-te că cel puțin două sau trei postări (dar nu toate) au setat câmpul publish date. Va fi de folos mai târziu.

![Consola de admin din Django][3]

 [3]: images/edit_post3.png

Dacă vrei să afli mai multe despre consola de Django admin, poți găsi documentația de Django la: https://docs.djangoproject.com/en/1.8/ref/contrib/admin/

Ăsta este un moment bun să-ți iei o cafea (sau ceai) sau ceva de mâncare pentru a prinde energie. Ai creat primul tău model de Django - meriți o pauză!