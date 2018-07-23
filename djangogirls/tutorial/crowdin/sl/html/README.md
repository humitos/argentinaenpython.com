# Uvod v HTML

Kaj je predloga?

Predloga je datoteka, ki se uporablja za predstavitev različnih informacij v podobni obliki - predlogo lahko recimo uporabiš, ko nekomu pišeš pismo, saj je sama oblika pisma vedno podobna (naslov prejemnika, uvodni pozdrav,...), vsebina pa se spreminja glede na to, komu pismo pošiljaš.

Djangove predloge so napisane v jeziku HTML (omenili smo ga v poglavju **Kako deluje internet**).

## Kaj je HTML?

HTML je preprost jezik, ki ga razumejo vsi spletni brskalniki - kot so recimo Chrome, Firefox in Safari - in z njegovo pomočjo prikazujejo spletne strani.

HTML je kratica za "HyperText Markup Language". **HyperText** pomeni, da gre za vrsto besedila, ki vsebuje povezave (oziroma hiperpovezave) med (spletnimi) stranmi. **Markup** pomeni značka. V jeziku HTML namreč poznamo veliko posebnih značk (oznak), ki brskalnikom povedo, kako oblikovati besedilo, ki neki znački sledi. Vsaka značka se začne z znakom `<`, ki mu sledi ime značke in konča z znakom `>`. Že samo z značkami lahko zgradimo kakršnokoli spletno stran.

## Tvoja prva predloga!

Predloga je torej zgolj HTML datoteka, ki vsebuje nekaj posebnih ukazov (značk) in besedilo.

Vse predloge bomo shranjevali v mapo `blog/templates/blog`. Za začetek moraš torej, znotraj osnovnega imenika blog, ustvariti mapo `templates`. Znotraj te naredi še mapo `blog`:

    blog
    └───templates
        └───blog
    

(Verjetno se sprašuješ, zakaj potrebujemo dva imenika z imenom `blog`. Tak način razporeditve imenikov se izkaže za uporabnega, ko delamo na nekem večjem projektu, ki je zgrajen iz večih Djangovih aplikacij.)

Ustvari datoteko `post_list.html` (zaenkrat naj bo prazna) in jo shrani v `blog/templates/blog`.

Zdaj si lahko stran ogledaš na naslovu http://127.0.0.1:8000/

> Če se ti spet pojavi napaka `TemplateDoesNotExists`, ponovno zaženi strežnik. Pojdi v ukazno vrstico, strežnik ustavi z Ctrl+C in ga ponovno zaženi z ukazom `python manage.py runserver`.

![Figure 11.1][1]

 [1]: images/step1.png

Napake ni več! Čestitke :) Vendar pa je naša stran zaenkrat še precej dolgočasna, saj ni na njej nič objavljenega. Zdaj je končno prišel čas, da to spremenimo.

V predlogo dodaj sledečo kodo:

    html
    <html>
        <p>Hi there!</p>
        <p>It works!</p>
    </html>
    

Kakšna je spletna stran zdaj? Oglej si jo na naslovu http://127.0.0.1:8000/

![Figure 11.2][2]

 [2]: images/step3.png

Deluje! Odlično :)

*   Značka, `<html>`, je začetek vsake spletne strani, značka `</html>` pa konec. Vsa preostala koda, ki jo bomo pisali, bo torej med tema dvema značkama
*   `<p>` označuje začetek novega odstavka, `</p>` pa konec

## Head & body

Vsaka spletna stran se deli na dva dela: **head** in **body**.

*   **head** je element, ki se ga na strani ne vidi. Kaj točno je njegov namen, bomo videli kasneje.

*   **body** je element, ki vsebuje "vidni" del strani. Velik del spletne strani je zgrajen na podlagi kode, ki je znotraj tega elementa.

V elementu `<head>` brskalniku pojasnimo določene lastnosti naše spletne strani, v elementu `<body>` pa opišemo samo vsebino strani.

V `head` damo lahko recimo element title. Takole:

    html
    <html>
        <head>
            <title>Ola's blog</title>
        </head>
        <body>
            <p>Hi there!</p>
            <p>It works!</p>
        </body>
    </html>
    

Shrani datoteko in osveži stran.

![Figure 11.3][3]

 [3]: images/step4.png

Si opazila, kako je brskalnik uporabil element title? Besedilo `<title>Ola's blog</title>` je privzel za naslov zavihka, v katerem je odprta tvoja stran.

Kot si verjetno že opazila, vsaki znački oblike <besedilo>, sledi značka oblike `<besedilo/>`. Temu rečemo, da druga značka *zapre* prvo. Opisane pare značk lahko *gnezdimo* (to pomeni, da neke značke ne smemo zapreti, dokler niso zaprte vse značke, ki so znotraj nje).

Predstavljaj si, da imaš veliko škatel, ki jih zlagaš eno v drugo. Največja je `<html></html>`. Znotraj nje položiš `<body></body>` in nato še v slednjo daš nove, manjše škatlice, kot je pri nas `<p></p>`.

Omenjena pravila o *gnezdenju* in *zapiranju* elementov, moraš vedno upoštevati, saj lahko brskalnik, v nasprotnem primeru, našo kodo napačno razume in stran napačno prikaže.

## Spreminjanje predlog

Malce se pozabavaj in svojo predlogo poskusi spremeniti! Tukaj je par uporabnih značk:

*   `<h1>naslov</h1>` - za najpomembnejše naslove
*   `<h2>podnaslov</h2>` - za malce manj pomembne naslove
*   `<h3>podnaslov podnaslova</h3>` ... in tako naprej, do `<h6>`
*   `<em>besedilo</em>` - za nagnjeno besedilo
*   `<strong>besedilo</strong>` - za odebeljeno besedilo
*   `<br />` - skok v novo vrstico (znotraj tega elementa besedila ni)
*   `<a href="http://djangogirls.org">link</a>` - povezava
*   `<ul><li>prvi element</li><li>drugi element</li></ul>` - za seznam, takšnega kot je ta, ki ga bereš
*   `<div></div>` - za definiranje novega dela spletne strani

Primer spremenjene predloge:

    html
    <html>
        
        <body>
            <div>
                <h1><a href="">Django Girls Blog</a></h1>
            </div>
    
            <div>
                <p>published: 14.06.2014, 12:14</p>
                <h2><a href="">My first post</a></h2>
                <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit ne mi porta gravida na eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
            </div>
    
            <div>
                <p>published: 14.06.2014, 12:14</p>
                <h2><a href="">My second post</a></h2>
                <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit ne mi porta gravida na eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut f.</p>
            </div>
        </body>
    </html>
    

V zgornji predlogi smo ustvarili tri elemente `div`.

*   Prvi element `div` vsebuje naslov tvojega blog - naslov in povezavo.
*   Drugi dva `div`-a vsebujeta objave na blogu z datumi objave, naslovi in vsebino objav.

Naša stran zdaj zgleda takole:

![Figure 11.4][4]

 [4]: images/step6.png

Super! Vendar pa je naš cilj, da prikažemo **različne** podatke (recimo objave na našem blogu) v **enaki obliki** (način razporeditve naslova, datuma in vsebine objave bo vedno enak). Zaenkrat naša predloga vedno prikaže **iste podatke**.

Naš cilj je, da prikažemo objave, ki smo jih dodali v Django adminu in ravno to bo vsebina naslednjega poglavja.

## Še nekaj: objavimo stran!

Vse narejene spremembe bi si bilo dobro ogledati še na "pravi" spletni strani. Prenesimo spremenjene datoteke na PythonAnywhere:

### Nalaganje kode na Github

Za začetek poglej, katere datoteke so bile spremenjene (na tvojem računalniku, ne na PythonAnywhere):

    $ git status
    

Prepričaj se, da si res v imeniku `djangogirls` in naroči `gitu`, da sporoči vse spremembe, ki so se zgodile znotraj tega imenika:

    $ git add -A .
    

> **Opomba** `-A` (okrajšava za "all" - vse) pomeni, da bo `git` kot spremembo javil tudi, če si neko datoteko zbrisala (sicer javi le, ko datoteko ustvariš ali spremeniš). Ne pozabi (poglavje 3), da je `.` oznaka za trenutni imenik.

Preden boš datoteke naložila, preveri, katere je `git` izbral (le-te bodo zelene barve):

    $ git status
    

Zagotoviti moramo še, da bo git zabeležil, kakšno spremembo smo naredili. Napisati moramo torej, kaj smo naredili (commit message). Napišeš lahko načeloma karkoli, vendar je zelo priporočljivo, da je opis smiseln, saj boš kasneje na podlagi tega opisa lahko ugotovila in kdaj si naredila določeno spremembo.

    $ git commit -m "Changed the HTML for the site."
    

> **Opomba:** Pri besedilo v git-u moraš vedno uporabiti dvojne narekovaje.

Zdaj lahko spremembe objavimo na Github:

    git push
    

### Nalaganje spremenjene kode na PythonAnywhere

*   Na PythonAnyehere pojdi na del strani, kjer je ukazna vrstica (Bash console). Poženi:

    $ cd ~/my-first-blog
    $ source myvenv/bin/activate
    (myvenv)$ git pull
    [...]
    (myvenv)$ python manage.py collectstatic
    [...]
    

Koda se zdaj nalaga na strežnik. Če želiš preveriti, ali se je že naložila, pojdi na **zavihek Files**in si oglej kodo.

*   Premakni se zdaj na zavihek [Web][5] in pritisni **Reload**.

 [5]: https://www.pythonanywhere.com/web_app_setup/

Tvoje spremembe so zdaj javno obavljene! Osveži stran in si jo oglej. Spremembe bi morale biti vidne.