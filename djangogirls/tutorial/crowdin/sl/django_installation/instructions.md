> To poglavje deloma temelji na vodiču Geek Girls Carots (http://django.carrots.pl/).
> 
> To poglavje deloma temelji na vodiču [django-marcador tutorial](http://django-marcador.keimlink.de/), ki je zaščiten preko Creative Commons Attribution-ShareAlike 4.0 International License. Vodič django-marcador tutorial je avtorsko delo Markus Zapke-Gründemann et al.

## Virtualno okolje

Preden namestiš Django, se boš seznanila z zelo uporabnim orodjem, ki ti bo omogočilo vzpostavitev urejenega delovnega prostora. Ta korak sicer ni obvezen, vendar pa je zelo priporočljiv. Uporaba virtualnega okolja nam dolgoročno prihrani veliko težav!

Ustvarimo torej **virtualno okolje** (angl. virtual environment ali *virtualenv*). Navidezno/virtualno okolje bo omejilo spremembe, ki jih bomo naredili v Pythonu in Djangu, le na naš projekt. To pomeni, da omenjene spremembe ne bodo vplivale na noben drug projekt, ki ga imaš morda tudi na računalniku. To se zdi smiselno.

Za začetek najdi imenik, v katerem želiš ustvariti `virtualno okolje`. Recimo tvoj domači imenik. Na Windowsih verjetno zgleda nekako tako `C:\Users\Name` (`Name` je seveda ime trenutnega uporabnika).

V tem vodiču bomo v tvojem domačen imeniku ustvarili nov imenik `djangogirls`:

    mkdir djangogirls
    cd djangogirls
    

Zdaj bomo ustvarili navidezno okolje `myvenv`. Splošen ukaz zgleda nekako takole:

    python3 -m venv myvenv
    

### Windows

`Virtualno okolje` ustvariš tako, da odpreš ukazno vrstico in v njej poženeš ukaz `C:\Python34\python -m venv myvenv`. It will look like this:

    C:\Users\Name\djangogirls> C:\Python34\python -m venv myvenv
    

kjer je `C:\Python34\python` imenik, v katerem imaš nameščen Python in `myvenv` ime `virtualnega okolja`. Ubistvu si lahko zmisliš katerokoli ime, ki vsebuje le male črke in ne vsebuje presledkov, naglasov in podobnih posebnih znakov. Dobro je tudi, da je ime kratko, saj ga boš velikokrat uporabljala!

### Linux in OS X

Ustvarjanje `virtualnega okolja na Linuxu in OS X ustvariš s pomočjo ukaza <code>python3 -m venv myvenv`. Takole:

    ~/djangogirls$ python3 -m venv myvenv
    

myvenv je ime tvojega virtualnega okolja. Ubistvu si lahko zmisliš katerokoli ime, ki vsebuje le male črke in ne vsebuje presledkov, naglasov in podobnih posebnih znakov. Dobro je tudi, da je ime kratko, saj ga boš velikokrat uporabljala!

> **OPOMBA:** Zagon virtualnega okolja na operacijskem sistemu Ubuntu 14.04, na zgoraj opisan način, trenutno vrne napako:
> 
>     Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1
>     
> 
> To lahko rešiš tako, da raje uporabiš ukaz `virtualenv`.
> 
>     ~/djangogirls$ sudo apt-get install python-virtualenv
>     ~/djangogirls$ virtualenv --python=python3.4 myvenv
>     

## Delo z virtualnim okoljem

S prejšnjimi ukazi si ustvarila imenik z imenom `myvenv` (oziroma z imenom, ki si ga izbrala sama), ki predstavlja virtualno okolje (v bistvu je to zgolj kup imenikov in datotek).

#### Windows

Virtualno okolje zaženeš takole:

    C:\Users\Name\djangogirls> myvenv\Scripts\activate
    

#### Linux in OS X

Virtualno okolje zaženeš takole:

    ~/djangogirls$ source myvenv/bin/activate
    

Ne pozabi nadomestiti imena `myvnev` z imenom, ki se ga izbrala!

> **OPOMBA:** če `source` noče delovati, poskusi naslednje:
> 
>     ~/djangogirls$ . myvenv/bin/activate
>     

Virtualno okolje je bilo uspešno zagnano, če tvoja ukazna vrstica zgleda takole:

    (myvenv) C:\Users\Name\djangogirls>
    

ali:

    (myvenv) ~/djangogirls$
    

Kot vidiš, se je na začetku vrstice pojavila predpona `(myvenv)`!

Ko delaš z virtualnim okoljem, je privzeta različica `pythona` enaka tisti, ki jo ima virtualno okolje. Zato lahko vedno uporabljaš ukaz `python` namesto `python3`.

OK, teren je pripravljen. Končno lahko namestimo Django!

## Namestitev Djanga

Django bomo namestili s pomočjo orodje `pip`. V ukazni vrstici poženi ukaz `pip install django==1.8` (nujno moraš uporabiti dvojni enečaj: `==`).

    (myvenv) ~$ pip install django==1.8
    Downloading/unpacking django==1.8
    Installing collected packages: django
    Successfully installed django
    Cleaning up...
    

na Windowsih

> Če dobiš napako, ko zaženeš ukaz pip, preveri, če kateri od starševskih imenikov imenika, v katerem imaš svoj projekt, vsebuje presledke, posebne znake ali tuje znake (recimo `C:\Users\User Name\djangogirls`). Če jih ima, projekt premakni kam drugam (recimo `C:\djangogirls`). Ko ga premakneš, ponovno zaženi zgornji ukaz.

na Linuxu

> Če dobiš napako, ko zaženeš ukaz pip na operacijskem sistemu Ubuntu 12.04, poženi ukaz `python -m pip install -U --force-reinstall pip`.

To je to! Zdaj si (končno) pripravljena, da narediš svojo Django aplikacijo!