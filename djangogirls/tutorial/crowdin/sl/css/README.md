# CSS - polepšaj svoj blog!

Naš blog zaenkrat nima ravno elegantnega videza. Čas je, da ga polepšamo! Uporabili bomo CSS.

## Kaj je CSS?

Cascading Style Sheets (CSS) je jezik, ki, s pomočjo posebnih ukazov, opisuje videz in obliko spletne strani. Lahko si ga predstavljaš kot make-up za spletne strani. :)

Vendar pa nima smisla, da bi znova začenjali iz nič. Raje uporabimo že narejeno odprtokodno orodje, ki so ga avtorji prijazno objavili na internetu. 

## Uporabimo Bootstrap!

Boostrap je eno izmed najbolj priljubljenih HTML in CSS orodij za razvijanje lepih spletnih strani: http://getbootstrap.com/

Razvili so ga programerji, ki so delali za Twitter, zdaj pa ga razvijajo prostovoljci iz vsega sveta.

## Namestitev Bootstrapa

Če želiš namestiti Bootstrap, moraš v svojo `.html` datoteko (`blog/templates/blog/post_list.html`) znotraj značke `<head>` dodati:

    html
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    

S tem datotek ne dodaš na svoj strežnik. To sta zgolj povezavi do datotek, ki se nahajata na neki drugi internetni strani. Ko povezavi dodaš, odpri svojo spletno stran, jo osveži in si oglej rezultat.

![Figure 14.1][1]

 [1]: images/bootstrap1.png

Malo bolje je že!

## Djangove statične datoteke

Podrobneje si poglejmo že omenjene, famozne **statične datoteke**. Statične datoteke so recimo vse CSS datoteke in slike -- datoteke, ki se ne spreminjajo glede na to, komu jih prikazujemo in ki se tudi s časom ne bodo bistveno spreminjale (v nasprotju s tekstovno vsebino našega bloga).

### Kje v Djangu živijo statčne datoteke

Ko smo na strežniku izvedli ukaz `collectstatic`, je Django že vedel, kje so shranjene statične datoteke za že narejeno "adminovo" aplikacijo. Statične datoteke moraš torej za začetek dodati v svojo aplikacijo `blog`.

To narediš tako, da, znotraj aplikacije blog, ustvariš nov imenik z imenom `static`:

    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    └── mysite
    

Django bo sam našel imenik, z imenom "static", ki je znotraj tvoje aplikacije. Njegovo vsebino bo smatral za statične datoteke.

## Prvi koraki v jeziku CSS!

Za začetek moramo ustvariti novo, prazno CSS datoteko. Najprej naredi nov imenik z imenom `css`, v njem pa še enega z imenom `static`. Nato znotraj imenika `css` ustvari novo css datoteko `blog.css`. Pripravljena?

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css
    

Končno lahko začnemo s pisanjem CSS kode! V svojem urejevalniku odpri prej ustvarjeno datoteko `blog/static/css/blog.css`.

Podrobno se z jezikom CSS ne bomo ukvarjali, saj je dokaj lahek in se ga lahko brez težav naučiš sama. Priporočamo ti vodič [Codeacademy HTML & CSS course][2], v katerem so zelo lepo predstavljene osnove dela z omenjenim jezikom.

 [2]: http://www.codecademy.com/tracks/web

Malce pa si vseeno poglejmo že zdaj. Si želiš recimo spremeniti barvo glave tvojega bloga? Za barve računalniki uporabljajo posebne kode. Te kode se začnejo z znakom `#`, ki mu sledi 6 črk (A-F) in/ali številk (0-9). Te kode najdeš tule: http://www.colorpicker.com/. Obstajajo pa tudi [vnaprej določene barve][3], ki jih lahko opišeš kar z angleškimi imeni, kot recimo `red` za rdečo in `green` za zeleno.

 [3]: http://www.w3schools.com/cssref/css_colornames.asp

V datoteko `blog/static/css/blog.css` dodaj sledečo kodo:

    css
    h1 a {
        color: #FCA205;
    }
    

`h1 a` je oznaka, ki pove, kateri del HTML kode želimo s CSS kodo, ki oznaki sledi, spremeniti. V tem primeru želimo spremeniti vse značke `a`, ki so znotraj značke `h1` (recimo tako: `<h1><a href="">link</a></h1>`). Koda, ki je znotraj zavitih oklepajev, bo spremenila barvo pisave v `#FCA205`, ki je odtenek oranžne. Barvo lahko seveda izbereš tudi po lastnem okusu!

V datoteki CSS bomo torej določili slog za vsak del HTML kode. Del HTML kode bomo določili kar z imeni značk (recimo `a`, `h1`, `body`) in posebnimi oznakami značk kot sta `class` in `id`. Class in id sta oznaki, ki ju za nek element določiš sama. Oznaka class opisuje skupino značk, id pa le eno samo značko. Sledečo značko lahko torej opišemo z imenom značke `a`, oznako class `external_link` in oznako id `link_to_wiki_page`:

    html
    <a href="http://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page">
    

Več o tem si lahko prebereš na strani [CSS Selectors in w3schools][4].

 [4]: http://www.w3schools.com/cssref/css_selectors.asp

Naši HTML predlogi moramo seveda povedati, da naj svoj izgled naredi po ukazih v narejeni CSS datoteki. Odpri torej datoteko `blog/templates/blog/post_list.html` in na začetek dodaj sledečo vrstico:

    html
    {% load staticfiles %}
    

S tem povemo, da bomo tu dodajali statične datoteke. Dodati moramo torej povezavo do naše datoteke. To bomo naredili med značkama `<head>` in `</head>`, za povezavami na datoteko z Bootstrap CSS-om (brskalnik datoteke dodaja po vrsti in bi, če bi našo datoteko dodali pred Bootstrapovo, lahko "povozil" katerega izmed naših ukazov). Dodati moraš torej sledeče:

    html
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    

S tem smo predlogi uspešno povedali, kje živi naš CSS. :)

Naša CSS datoteka trenutno zgleda takole:

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
    

OK, datoteko shrani in v brskalniku osveži spletno stran!

![Figure 14.2][5]

 [5]: images/color2.png

Odlično! Dodajmo strani še malo zamika na levi in desni.

    css
    body {
        padding-left: 15px;
    }
    

Ukaz padding torej nastavi zamik. Shrani datoteko in osveži stran!

![Figure 14.3][6]

 [6]: images/margin2.png

Kako pa bi spremenili vrsto pisave našega besedila? Znotraj značke `<head>` v datoteki `blog/templates/blog/post_list.html` dodaj:

    html
    <link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
    

Dodana povezava bo na stran uvozila pisavo *Lobster* iz strani Google Fonts (https://www.google.com/fonts).

V CSS datoteko `blog/static/css/blog.css` znotraj bloka `h1 a` (koda znotraj zavitih oklepajev `{` in `}`) dodaj še `font-family: 'Lobster';` in ponovno osveži spletno stran:

    css
    h1 a {
        color: #FCA205;
        font-family: 'Lobster';
    }
    

![Figure 14.3][7]

 [7]: images/font.png

Odlično!

Kot že omenjeno, nam razredi v jeziku CSS omogočajo, da določen slog dodelimo le delu HTML kode. To je zelo uporabno. Recimo, da imamo dve znački div, ki predstavljata dva povsem različna dela strani (kot sta glava in noga). V takem primeru želimo, da je videz vsake izmed njiju drugačen.

Poimenuj par delov svoje HTML kode. Za začetek dodaj razred z imenom `glava` znački `div`, ki vsebuje glavo spletne strani.

    html
    <div class="glava">
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>
    

Znački `div`, ki vsebuje objavo na blogu, dodaj razred `objava`.

    html
    <div class="objava">
        <p>published: {{ post.published_date }}</p>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
    

Zdaj lahko opisanim delom strani dodamo CSS kodo, ki bo določala oblikovanje le-teh. Koda, ki opisuje določen razred, se bo vedno začela z znakom `.` in takoj zatem imenom razreda. Obstaja ogromno vodičev o jeziku CSS, ki sledečo kodo opisujejo bolj podrobno. Za nas pa bo zaenkrat zadoščalo zgolj prekopiranje sledeče kode v datoteko `blog/static/css/blog.css`.

    css
    .glava {
        background-color: #ff9400;
        margin-top: 0;
        padding: 20px 20px 20px 40px;
    }
    
    .glava h1, .glava h1 a, .glava h1 a:visited, .glava h1 a:active {
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
    
    .objava {
        margin-bottom: 70px;
    }
    
    .objava h1 a, .objava h1 a:visited {
        color: #000000;
    }
    

Dodane CSS razrede moramo dodati še v našo HTML kodo. Zamenjaj tale del kode:

    html
    {% for post in posts %}
        <div class="objava">
            <p>published: {{ post.published_date }}</p>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
    

, ki se nahaja v datoteki `blog/templates/blog/post_list.html`, s sledečo kodo:

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
    

Shrani datoteko in osveži spletno stran.

![Figure 14.4][8]

 [8]: images/final.png

Stran zdaj izgleda precej bolje, kajne?

S CSS-om se lahko še sama malce poigraš, kaj spremeniš in dodaš. Če gre kaj narobe, se ne boj, preprosto zbriši svoj del kode, ki je povzročil težavo!

Priporočamo ti, da si pogledaš spletni tečaj [Codeacademy HTML & CSS course][2], saj se boš tako o CSS-u naučila še precej več.

Pripravljena na naslednje poglavje?! :)