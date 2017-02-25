# CSS - fă-o frumos!

Blog-ul nostru încă arată destul de urât, corect? E timpul să-l facem frumos! Pentru asta vom folosi CSS.

## Ce este CSS?

CSS (Cascading Style Sheets) sau foi de stil în cascadă este un limbaj folosit pentru descrierea aspectului și formatarea unui site Web scris într-un limbaj de marcare (cum ar fi HTML). Gândește-te la asta ca la machiajul site-ului nostru ;).

Dar nu dorim să începem totul de la zero, corect? Vom mai folosi din nou ceea ce a fost deja făcut de programatori și lansat pe Internet gratuit. Precum știm, nu e vesel sa reinventezi roata.

## Să folosim procesul de Bootstrap!

Bootstrap este unul dintre cele mai populare framework-uri HTML și CSS pentru a crea site-uri frumoase: http://getbootstrap.com/

Acesta a fost scris de către programatori care au lucrat pentru Twitter, și acum este dezvoltat de voluntari din întreaga lume.

## Instalăm Bootstrap

Pentru a instala Bootstrap, va fi nevoie sa adaugi `<<head>>`-ul în file-ul `.html` (`blog/templates/blog/post_list.html`):

    html
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    

Acest lucru nu va adăuga nici un fișier la proiect. El doar indică la niște fișiere care deja există pe net. Doar deschide site-ul tău și actualizează pagina. Iată-l!

![Figura 14.1][1]

 [1]: images/bootstrap1.png

Deja arată mai frumos!

## Fișierele statice în Django

În sfârșit ne vom uit la lucrurile care le numeam **fișiere statice**. Fișierele statice sunt toate imaginile și fișierele CSS -- fișierele care nu sunt dinamice, astfel încât conținutul lor nu depind de nimic și ele vor fi aceleași pentru orice utilizator.

### Unde trebuiesc puse fișierele statice pentru Django

Precum ai văzut, când rulăm `collectstatic` pe server, Django deja știe unde sa găsească fișierele statice pentru aplicația încorporată "admin". Ne-a rămas doar sa adăugăm niște fișiere statice pentru aplicația noastră, `blog`.

Facem asta prin crearea unui dosar numit `static` înăuntrul blog-ului:

    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    └── mysite
    

Django va găsi automat orice dosar numit "static" în dosarele aplicației și va putea folosi conținutul lor ca fișiere statice.

## Primul fișier CSS!

Sa creăm un fișier CSS, pentru a adaugă stilul tău propriu la pagina web. Crează un director nou numit `css` în interiorul directorului `static`. Apoi crează un nou fișier numit `blog.css` înăuntrul directorului `css`. Ready?

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css
    

Timpul pentru a scrie niște CSS! Deschide fișierul `blog/static/css/blog.css` în editorul de cod.

Nu ne vom adânci prea tare în personalizarea și învățarea CSS aici, deoarece el este destul de ușor și îl poți învăța singur dupa workshop. Și chiar recomandăm sa faci asta [Codeacademy HTML & CSS course][2] pentru a învăța totul de ce ai nevoie pentru a face site-urile mult mai frumoase cu CSS.

 [2]: http://www.codecademy.com/tracks/web

Dar hai să facem cel puțin ceva. Poate am putea schimba culoarea header-ului? Pentru a înțelege culorile, calculatoarele ulilizează niște coduri speciale. Ele încep cu `#` și sunt urmate de 6 litere (A-F) și cifre (0-9). Poți găsi coduri de culori ca exemplu aici:http://www.colorpicker.com/. Poți de asemenea utiliza [culori predefinite][3], precum `red` - roșu și `green` - verde.

 [3]: http://www.w3schools.com/cssref/css_colornames.asp

Adaugă următorul cod în fișierul `blog/static/css/blog.css`:

    css
    h1 a {
        color: #FCA205;
    }
    

`h1 a` este un Selector CSS. Asta înseamnă că noi aplicăm stilurile noastre pentru orice element `a` înăuntru la un element `h1` (de ex. când avem în cod ceva asemănător la:`<h1><a href="">link</a></h1>`). În acest caz, noi spunem să își schimbe culoarea în `#FCA205`, care reprezintă oranjul. Desigur poți pune culoarea ta proprie aici!

Într-un fișier CSS determinăm stilurile pentru elementele într-un fișier HTML. Elementele sunt identificate prin numele elementului (de ex. `a`, `h1`, `body`), atributul `class` sau atributul `id`. Numele de clase și id le definești singur. Clasele definesc grupuri de elemente, și id-urile indică la niște elemente anumite. De exemplu, următorul tag poate fi identificat de CSS folosing un nume de tag `a`, clasa `external_link`, sau id-ul `link_to_wiki_page`:

    html
    <a href="http://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page">
    

Citește despre [CSS Selectors in w3schools][4].

 [4]: http://www.w3schools.com/cssref/css_selectors.asp

Apoi avem nevoie să-i spunem șablonului nostru HTML că am adăugat CSS. Deschide fișierul `blog/templates/blog/post_list.html` și adaugă această linie chiar la început:

    html
    {% load staticfiles %}
    

Aici noi doar încărcăm fișierele statice :). Apoi, între `<head>` și `</head>`, după link-urile spre fișierele CSS Bootstrap (browser-ul citește fișierele în ordinea dată, și în așa mod codul din fișierul nostru ar putea suprascrie fișierele Bootstrap), adaugă această linie:

    html
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    

În acest moment i-am spus șablonului unde se află fișierul nostru CSS.

Fișierul tău trebuie să arate așa:

    html
    {% load staticfiles %}
    <html>
        <head>
            <title>Django Girls blog</title>
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
            <link rel="stylesheet" href="{% static 'css/blog.css' %}">
        </head>
        <body>
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
        </body>
    </html>
    

Bine, salvează fișierul și actualizează pagina!

![Figura 14.2][5]

 [5]: images/color2.png

Bună treabă! Poate ai vrea să-i dai site-ului un pic de air și să mărești marginea din partea stângă? Să încercăm!

    css
    body {
        padding-left: 15px;
    }
    

Adaugă asta la CSS-ul tău, salvează fișierul și vezi cum a lucrat!

![Figura 14.3][6]

 [6]: images/margin2.png

Poate putem personaliza font-ul din header? Inserează aceasta în `<head>` din fișierul `blog/templates/blog/post_list.html`:

    html
    <link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
    

Această linie de cod va importa un font numit *Lobster* din Fonturile Google (https://www.google.com/fonts).

Acum adaugă linia `font-family: 'Lobster';` în fișierul CSS`blog/static/css/blog.css` în blocul `h1 a` (codul dintre acoladele `{` și`}`) și acualizează pagina:

    css
    h1 a {
        color: #FCA205;
        font-family: 'Lobster';
    }
    

![Figura 14.3][7]

 [7]: images/font.png

Grozav!

După cum am menționat mai sus, CSS are un concept de clase, care în principiu permite să numești o parte din codul HTML și să aplici stiluri doar pe partea aceasta, neafectând alta. Este super util să ai două div-uri, dacă ele fac ceva complet diferit (precum headerul și postarea), și nu vrei să arate la fel.

Numește câteva părți din codul HTML. Adaugă o clasă numită `page-headers` la `div`-ul care conține headerul:

    html
    <div class="page-header">
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>
    

Acum adaugă o clasă `post` la `div`-ul care conține un post de blog.

    html
    <div class="post">
        <p>published: {{ post.published_date }}</p>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
    

Acum vom adăuga blocuri de declarare la selectoare diferite. Selectoarele care încep cu `.` se referă la clase. Există multe tutoriale și explicații despre CSS pe Web care te ajută să înțelegi următorul cod. Pentru moment, doar copiază-l și inserează-l in fișierul `blog/static/css/blog.css`:

    css
    .page-header {
        background-color: #ff9400;
        margin-top: 0;
        padding: 20px 20px 20px 40px;
    }
    
    .page-header h1, .page-header h1 a, .page-header h1 a:visited, .page-header h1 a:active {
        color: #ffffff;
        font-size: 36pt;
        text-decoration: none;
    }
    
    .content {
        margin-left: 40px;
    }
    
    h1, h2, h3, h4 {
        font-family: 'Lobster', cursive;
    }
    
    .date {
        float: right;
        color: #828282;
    }
    
    .save {
        float: right;
    }
    
    .post-form textarea, .post-form input {
        width: 100%;
    }
    
    .top-menu, .top-menu:hover, .top-menu:visited {
        color: #ffffff;
        float: right;
        font-size: 26pt;
        margin-right: 20px;
    }
    
    .post {
        margin-bottom: 70px;
    }
    
    .post h1 a, .post h1 a:visited {
        color: #000000;
    }
    

Apoi selectează codul HTML care afișează posturile cu declarațiile de clase. Înlocuiește asta:

    html
    {% for post in posts %}
        <div class="post">
            <p>published: {{ post.published_date }}</p>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
    

în `blog/templates/blog/post_list.html` cu asta:

    html
    <div class="content container">
        <div class="row">
            <div class="col-md-8">
                {% for post in posts %}
                    <div class="post">
                        <div class="date">
                            {{ post.published_date }}
                        </div>
                        <h1><a href="">{{ post.title }}</a></h1>
                        <p>{{ post.text|linebreaks }}</p>
                    </div>
                {% endfor %}
            </div>
        </div>
    </div>
    

Salvează fișierele și actualizează site-ul.

![Figura 14.4][8]

 [8]: images/final.png

Woohoo! Arată minunat, nu? Codul care l-am inserat nu este foare greu de înțeles și ar trebui să fii capabilă să înțelegi o mare parte doar uitându-te în el.

Nu-ți fie teamă să te joci cu acest CSS și să schimbi unele lucruri. În cazul în care nu lucrează ceva nu-ți fă griji, întotdeauna există posibilitatea să-l refaceți!

Oricum, îți recomandăm să iei aceste cursuri online gratuite [Codeacademy HTML & CSS course][2] ca niște temă pentru acasă după workshop pentru a învăța totul de ce ai nevoie să știi despre cum să faci site-urile web mai frumoase cu CSS.

Gata pentru capitolul următor?! :)