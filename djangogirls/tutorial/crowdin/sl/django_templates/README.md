# Djangove predloge

Vstavimo na spletno stran nekaj besedila! Django nam pri tem izdatno pomaga z značkami **template**.

## Kaj so značke template?

Pythonove programske kode ne moreš pisati direktno v HTML, saj brskalniki Pythona ne marajo. Všeč jim je le HTML. Vemo, da je HTML dokaj statičen jezik, medtem ko je Python zelo dinamičen.

Djangove značke **template** nam pomagajo pri združitvi obeh omenjenih lastnosti. Z njimi bomo lahko hitro zgradili dinamično spletno stran.

## Prikazovanje objav na blogu

V prejšnjem poglavju smo seznam objav shranili v spremenljivko `posts`. Te objave moramo še prikazati kot HTML.

Za izpis spremenljivke v Djangovih predlogah bomo uporabili zavite oklepaje, znotraj njih pa bomo dali spremenljivko:

    html
    {{ posts }}
    

Naredi to v predlogi `blog/templates/blog/post_list.html`. Vso kodo med drugo značko `<div>` in tretjo značko `</div>` z `{{ posts }}`. Datoteko shrani, osveži stran in si oglej rezultate:

![Figure 13.1][1]

 [1]: images/step1.png

Vse, kar smo dobili, je tole:

    [<Post: My second post>, <Post: My first post>]
    

Django torej našo spremenljivko razume kot seznam objektov. Se še spomniš, kako se v Pythonu izpiše elemente seznama? Prav si uganila. Z zanko! V predlogah zanko narediš takole:

    html
    {% for post in posts %}
        {{ post }}
    {% endfor %}
    

Preizkusi to še v svoji predlogi.

![Figure 13.2][2]

 [2]: images/step2.png

Deluje! Vendar pa bi bilo boljše, če bi bila objava oblikovana nekoliko lepše. Recimo tako kot je bila v poglavju **Uvod v HTML**. K sreči se izkaže, da lahko v značke template dodajamo tudi HTML kodo. `body` bo zdaj zgledal takole:

    html
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
    

{% raw %}Vsa koda, ki je med `{% for %}` in `{% endfor %}` se bo ponovila za vsak objekt v seznamu. Osveži svojo stran:{% endraw %}

![Figure 13.3][3]

 [3]: images/step3.png

Si opazila, da smo tokrat uporabili nekoliko drugačno kodo? Kaj je razlika med `{{ post.title }}` in `{{ post.text }}`? Razlika je v tem, da dostopamo do različnih delov naše baze podatkov `Post`. Ukaz post.title dostopa do podatka o naslovu objave, post.text pa do vsebine, `| linebreaks` pa nam pomaga pri preoblikovanju besedila v odstavke.

## Še nekaj

Spletno stran bi si radi ogledali še javno, na internetu. Ponovno jo moramo torej prekopirati na PythonAnywhere. Kako se že to naredi...

*   Za začetek kodo prenesimo na Github

    $ git status
    [...]
    $ git add -A .
    $ git status
    [...]
    $ git commit -m "Modified templates to display posts from database."
    [...]
    $ git push
    

*   Nato se ponovno prijavi v [Pythona nAnywhere][4], pojdi na **Bash console**(ali pa odpri novo) in zaženi:

 [4]: https://www.pythonanywhere.com/consoles/

    $ cd my-first-blog
    $ git pull
    [...]
    

*   Za konec se premakni na [Web tab][5] in v svoji aplikaciji pritisni **Reload**. Najnovejša verzija tvoje strani je objavljena!

 [5]: https://www.pythonanywhere.com/web_app_setup/

Čestitke! Zdaj lahko v Django adminu dodajaš nove objave (ne pozabi objavi dodati podatka published_date!). Ko objavo dodaš, osveži stran in si jo oglej.

Deluje? Odlično! Naredila si že ogromno, zato si zaslužiš kratek odmor. ;)

![Figure 13.4][6]

 [6]: images/donut.png