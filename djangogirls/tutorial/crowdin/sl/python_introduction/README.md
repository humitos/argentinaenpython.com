# Uvod v Python

> To poglavje delno temelji na vodiču Geek Girls Carrots (http://django.carrots.pl/).

Končno lahko začnemo s programiranjem!

## Pythonova ukazna vrstica

Za začetek odpri *ukazno vrstico*. Kako ? Spomni se poglavja [ Osnove dela z ukazno vrstico][1].

 [1]: ../intro_to_command_line/README.md

Ko imaš odprto, sledi nadaljnim navodilom.

Odpreti želimo Pythonovo ukazno vrstico, zato v ukazno vrstico vpiši `python` v Windowsih oziroma `python3` na Mac OS/Linux in pritisni `enter`.

    $ python3
    Python 3.4.3 (...)
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    

## Prvi ukaz v programske jeziku Python!

Ko si uspešno zagnala pythonovo ukazno vrstico, se je začetek vrstice spremenil v `>>>`. To pomeni, da lahko začneš z vpisovanjem Pythonovih ukazov. Ni ti treba vedno znova vpisovati znakov `>>>` - to bo zate naredil Python.

Če želiš Pythonovo ukazno vrstico zapreti, vanjo vpiši `exit()`, ali pa pritisni `Ctrl + Z` na Windowsih oziroma `Ctrl + D` na Mac OS/Linux. Opazila boš, da se vrstica ne bo več začenjala z `>>>`.

Za zdaj nas zapiranje ubistvu ne zanima. Naučimo se rajši še nekaj stvari o tej ukazni vrstici. Začnimo z nečim povsem preprostim. V Pythonovo ukazno vrstico vpiši nek matematični izraz, kot je recimo `2 + 3`, in pritisni `enter`.

    >>> 2 + 3
    5
    

Super! Hitro je izračunal. Preizkusi ga še s čim težjim. Recimo s temle: - `4 * 5` - `5 - 1` - `40 / 2`

Malo se še poigraj z računanjem, nato pa nadaljuj z branjem :).

Kot vidiš, je Python izvrsten kalkulator. To pa še zdaleč ni vse...

## Nizi

Pythonu gredo dobro tudi imena. Vpiši svoje ime znotraj narekovajev:

    >>> "Ana"
    'Ana'
    

Pravkar si naredila svoj prvi niz! To je zaporedje znakov, ki ga računalnik zna prebrati. Nizi se morajo vedno začeti in končati z enojnim `'` ali dvojnim `"` narekovajem (med njima ni razlike!). Narekovaji Pythonu povedo, da je tisto, kar je znotraj njih, niz.

Nize lahko združuješ. Takole:

    >>> "Pozdravljena " + "Ana"
    'Pozdravljena Ana'
    

Lahko jih množiš s številko:

    >>> "Ana" * 3
    'AnaAnaAna'
    

Če želiš, da je narekovaj del niza, lahko to narediš na dva načina.

Z uporabo dvojnih narekovajev:

    >>> "Spust'li smo eno črko."
    "Spust'li smo eno črko."
    

ali pa z uporabo enojnih narekovajev in leve poševnice (``):

    >>> 'Spust\'li smo eno črko.'
    'Spust'li smo eno črko.'
    

Super! Kako pa bi črke imena spremenila v velike tiskane?

    >>> "Ana".upper()
    'ANA'
    

Pravkar si uporabila **funkcijo** `upper`! Funkcija (kot je `upper`) je zaporedje ukazov, ki jih Python izvede na objektu (v našem primeru`"Ana"`), ko jo pokličeš.

Obstaja tudi funkcija, ki ti pove, koliko mest ima beseda!

    >>> len("Ana")
    3
    

Kot si opazila, smo funkcijo enkrat uporabili na koncu niza in prednjo postavili piko (`"Ana".upper()`), drugič pa smo niz dali kar v funkcijo (len("Ana")). Gre za to, da je, v nekaterih primerih, funkcija del objekta. `upper()` je recimo del objekta nizi. V takem primeri funkciji rečemo **meotda**. Po drugi strani pa je funkcija lahko povsem neodvisna in jo lahko uporabimo za katerikoli objekt. Tak primer je `len()`. Zato smo niz `"Ana"` prej lahko vstavili kar v funkcijo `len`.

### Povzetek

OK, zaenkrat vemo dovolj o nizih. Poglejmo, česa vsega smo se že naučili:

*   **Pythonova ukazna vrstica** - vanjo vpisujemo ukaze (kodo) in v zameno od Pythona dobimo odgovore - rezultate naših ukazov
*   **številke in nizi** - Python zna dobro računati in izvajati razne operacije na nizih
*   **operatorji** - kot recimo + in *, nam iz podanih vrednosti izračunajo nove 
*   **funkcije** - kot upper() in len(), izvedejo ukaze na objektih

To so osnove vsakega programskega jezika. Si pripravljena na kaj težjega? Seveda si!

## Napake

Misliš da bi se dalo, z ustrezno funkcijo, dobiti dolžino številke? Vpiši `len(304023)` in pritisni `enter`:

    >>> len(304023)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: object of type 'int' has no len()
    

Python nam javi napako! Reče, da objekt "int" (integer, celo število) nima dolžine. Kaj pa zdaj? Kateri objekti, ki jih poznamo, pa imajo dolžino? Nizi. Seveda! Poskusimo pretvoriti število v niz.

    >>> len(str(304023))
    6
    

Zmaga! S pomočjo funkcije `str()`, smo pretvorili objekt število v objekt niz in nato s pomočjo `len()` izračunali dolžino niza. Funkcija `str()` pretvori v niz katerikoli objekt.

*   Funkcija `str` pretvori poljuben objekt v objekt niz.
*   Funkcija `int` pretvori poljuben objekt v objekt število (**integer** oziroma int)

> Pomembno: število lahko vedno pretvorimo v niz, niza v število pa ne vedno - kakšno število pa bi bilo `int('pozdravljena')`?! :)

## Spremenljivke

Pomemben del vsakega programskega jezika so spremenljivke. Spremenljivka ni nič drugega kot ime, ki ga daš neki vrednosti (številki, nizu,...) in ga kasneje uporabiš za priklic te vrednosti. Programerji spremenljivke uporabljamo za shranjevanje podatkov in boljšo preglednost kode.

Naredimo spremenljivko z imenom `ime`:

    >>> ime = "Ana"
    

Vidiš? Povsem preprosto.

Kot si opazila, program ničesar izpisal. Kako torej vemo, kakšno vrednost ima spremenljivka? Še enkrat napiši ime spremenljivke in pritisni `enter`:

    >>> ime
    'Ana'
    

Super! Naredila si svojo prvo spremenljivko :)! Njeno vrednost pa lahko tudi spremeniš:

    >>> ime = "Anja"
    >>> ime
    'Anja'
    

Spremenljivke lahko podtikaš tudi funkcijam:

    >>> len(ime)
    4
    

Lepo :) Vrednost spremenljivke pa je seveda lahko karkoli. Recimo:

    >>> a = 4
    >>> b = 6
    >>> a * b
    24
    

Kaj pa se zgodi, če spremenljivko pokličemo z napačnim imenom? Poskusimo!

    >>> mesto = "Ljubljana"
    >>> mseto
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'mseto' is not defined
    

Python javi napako! Kot vidiš, ima Python različne vrste napak. Tej, ki nam jo javilo, se reče **NameError**. Python ti bo to napako javil, če boš poklicala spremenljivko, ki ne obstaja. Če boš kdaj naletela na to napako, torej vedno preverila, če si se zatipkala ali zmotila.

Poskusi ustvariti še kakšno drugo spremenljivko, da se z njimi še bolje spoznaš!

## Funkcija print

Napiši tole:

    >>> ime = 'Micka'
    >>> ime
    'Micka'
    >>> print(ime)
    Micka
    

Ko napišeš `ime`, se bo Pythonov tolmač odzval z *vrednostjo* spremenljivke 'ime', ki je v tem primeru niz , sestavljen iz črk M-i-c-k-a. Ko pa napišeš print(ime), bo Python "sprintal" vsebino spremenljivke na ekran, brez narekovajev.

Kasneje bomo videli, da je funkcija `print()` uporabna tudi, ko želimo izpisate vrednosti znotraj funkcije ali ko želimo izpisate vrednosti v večih vrsticah.

## Seznami

Polek nizov in števil Python pozna še mnoge druge objekte. Seznanili se bomo z objektom, ki mu rečemo **seznam**. Že ime nam namigne, kaj seznam je: objekt, ki je seznam objektov :)

Definirajmo torej naš prvi seznamček:

    >>> []
    []
    

Prazen je. To ni ravno navdušujoče. Naredi raje seznam loterijskih številk. Pisanje si zmanjšaj tako, da ga shraniš v spremenljivko:

    >>> loterija = [3, 42, 12, 19, 30, 59]
    

Tako, naredila si svoj prvi omembe vreden seznam. Kaj pa zdaj? Za začetek preveri, koliko je dolg. Kako se že to naredi? :)

    >>> len(loterija)
    6
    

Tako je! `len()` zna ugotoviti tudi dolžino seznama. To se izkaže za zelo uporabno. Razporedimo sedaj števila v seznamu po vrsti:

    >>> loterija.sort()
    

Ta metoda ne vrne ničesar. Spremeni pa vrsti red števil v seznamu. Izpiši seznam, da se prepričaš, če je Python naredil prav.

    >>> print(loterija)
    [3, 12, 19, 30, 42, 59]
    

Kot vidiš so števila res razporejena od najmanjšega proti največjemu. Čestitke!

Kaj pa, če bi želeli vrstni red obrniti? Poskusimo!

    >>> loterija.reverse()
    >>> print(loterija)
    [59, 42, 30, 19, 12, 3]
    

Tudi to gre brez težav. Kako pa bi v seznam dodala nov element?

    >>> loterija.append(199)
    >>> print(loterija)
    [59, 42, 30, 19, 12, 3, 199]
    

Če želiš dobiti iz seznama nek določen element, lahko to narediš s pomočjo **indeksov**. Indeks pove, na katerem mestu v seznamu se nek element nahaja. Pri je malce neobičajno le to, da se štetje mest začne z indeksom 0 in ne 1 kot si verjetno pričakovala. Napiši tole:

    >>> print(loterija[0])
    59
    >>> print(loterija[1])
    42
    

Do poljubnega elementa torej dostopamo z imenom seznama in želenim indeksom znotraj oglatih oklepajev.

S pomočjo** indeksov** lahko elemente iz seznama tudi odstranjuješ. Tu nam bo na pomoč priskočil ukaz **del**. Poglejmo si še par primerov.

    >>> print(loterija)
    [59, 42, 30, 19, 12, 3, 199]
    >>> print(loterija[0])
    59
    >>> del lotorija[0]
    >>> print(loterija)
    [42, 30, 19, 12, 3, 199]
    

Deluje! :)

Za zabavo lahko preizkusiš še indekse: 6, 7, 1000, -1, -6 ali -1000. Poskusi predvideti rezultat, še preden ti ga pove Python. So rezultati smiselni?

Vse metode, ki jih Python ima za sezname, si lahko ogledaš v Pythonovi dokumentaciji: https://docs.python.org/3/tutorial/datastructures.html

## Slovarji

Slovarji so dokaj podobni seznamom. Glavna razlika je v tem, da do elementov slovarja dostopaš s ključi. Ključ je lahko poljuben niz ali število. Prazen slovar definiramo takole:

    >>> {}
    {}
    

Uspešno si naredila prazen slovar! :)

Naredimo še enega, malo bolj zanimivega (vanj vstavi svoje podatke):

    >>> udeleženec = {'ime': 'Ana', 'država': 'Slovenija', 'najljubša_števila': [7, 42, 92]}
    

Ustvarila si slovar z imenom `udeleženec`, ki ima tri ključe:

*   Ključ `ime` ima vrednost `'Ana'` (`niz`),
*   `država` ima vrednost `'Slovenija'` (ponovno `niz`),
*   ključ `najljubša_števila` pa vrednost `[7, 42, 92]` (`seznam` s tremi elementi).

Vrednost ključev lahko ugotoviš tudi na sledeč način:

    >>> print(udeleženec['ime'])
    Ana
    

Dejansko je vse skupaj zelo podobno seznamom. Glavna razlika je v tem, da pri slovarjih do elementov lahko dostopaš ne da bi vedela njihov indeks - dovolj je da veš ime.

Kaj pa se zgodi, če od Pythona želimo vrednost ključa, ki ga ni? Kaj misliš? Poskusi!

    >>> udeleženec['ime']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'age'
    

Pridelali smo napako! Tej se reče **KeyError**. Python je prijazen in nam pove tudi, da je do take napake prišlo pri ključu `'ime'`.

Kdaj uporabiti slovar in kdaj seznam? To je dobro vprašanje. :) Razmisli o tem sama, nato pa poglej spodaj napisane odgovore.

*   So tvoji podatki urejeni (po abecedi, velikosti ipd.). Izberi seznam.
*   Imajo tvoji podatki edinstveno lastnost (ključ), po kateri jih lahko razlikuješ med seboj? Uporabi slovar.

Slovarji so, podobno kot seznami, *spremenljivi*. To pomeni, da jih lahko spreminjamo tudi, ko so že zgrajeni. Dodajamo lahko torej ključe/vrednosti. Takole:

    >>> udeleženec['najljubši_jezik'] = 'Python'
    

Na seznamih lahko (kdo bi si mislil :) ) uporabimo poznano funkcijo `len()`, ki nam vrne število parov ključ-vrednost. Preizkusimo:

    >>> len(udeleženec)
    4
    

Vse jasno? :) Slovarji se izkažejo za zelo močno orodje. To bomo pokazali s spodnjimi primeri.

Za brisanje elementov slovarja lahko uporabiš ukaz `del`. Če želiš recimo izbrisati ključ `'najljubša_števila'`, napiši sledeče:

    >>> del udeleženec['najljubša_števila']
    >>> udeleženec
    {'država': 'Slovenija', 'najljubši_jezik': 'Python', 'ime': 'Ana'}
    

Kot vidiš, para ključ-vrednost, pri katerem je ključ 'najljubša_števila', v slovarju ni več.

Pri slovarjih lahko vrednosti ključev tudi spremeniš. Takole:

    >>> udeleženec['država'] = 'Avstrija'
    >>> udeleženec
    {'država': 'Avstrija', 'najljubši_jezik': 'Python', 'ime': 'Ana'}
    

Vrednost ključa `'država'` se je spremenila iz 'Slovenija' v `'Avstrija'`. Super! :)

### Povzetek

Odlično ti gre! Zdaj veš že zelo veliko o programiranju. Povzemimo zadnja dognanja:

*   **napake** - veš kako se Python odziva, ko se pri programiranju zmotiš. Iz njegovega odziva znaš tudi razbrati, za katero vrsto napake gre
*   **spremenljivke** - imena za objekte, ki ti omogočajo, da lažje programiraš in tvojo kodo naredijo bolj pregledno
*   **seznami** - seznami objektov, shranjenih v določen vrstnem redu
*   **slovarji** - seznam objektov, predstavljenih s pari ključ-vrednost

Odlično! Gremo hitro naprej. :)

## Primerjanje

Pomemben del programiranja je primerjanje. Katero stvar je najlažje primerjati? Števila. Seveda! Poskusimo:

    >>> 5 > 2
    True
    >>> 3 < 1
    False
    >>> 5 > 2 * 2
    True
    >>> 1 == 1
    True
    >>> 5 != 2
    True
    

Kot vidiš zna Python res primerjati števila. Prav tako lahko primerja tudi rezultate metod.

Te zanima, zakaj smo uporabili dvojni enačaj `==`, ko smo ugotavljali, če sta dve števili enaki? Razlog je preprost. Enojni enačaj `=` uporabljamo že za definiranje spremenljivk. Zato, ko ugotavljaš, če sta dve stvari enaki, **vedno** uporabi dvojni enačaj `==`. Podobno lahko za ugotavljanje, če dve stvari nista enaki, uporabimo znak `!=`.

Poskusi še tole:

    >>> 6 >= 12 / 2
    True
    >>> 3 <= 2
    False
    

Kaj sta znaka `>` in `<`, je jasno, kaj pa `>=` in `<=`? Njun pomen je takle:

*   x `>` y pomeni: x je večje od y
*   x `<` y pomeni: x je manjše od y
*   x `<=` y pomeni: x je manjše ali enako y
*   x `>=` y means: x je večje ali enako y

Odlično! Naredi še par primerov. Recimo:

    >>> 6 > 2 and 2 < 3
    True
    >>> 3 > 2 and 2 < 1
    False
    >>> 3 > 2 or 2 < 1
    True
    

Python zna torej primerjati poljubno mnogo števil. Kako pa mu to uspe?

*   **and** - če uporabiš operator `and`, morata oba izraza vrniti vrednost True, da bo celoten izraz vrnil True
*   **or** - če uporabiš operator `or`, mora le eden izmed izrazov vrniti True, da je celoten izraz enak True

Si že slišala za izraz "primerjanje jabolk in pomaranč"? Si? Python tudi! Zanj takšno primerjanje enako sledečemu:

    >>> 1 > 'django'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unorderable types: int() > str()
    

Podobno napako smo že videli v prvi polovici tega poglavja. Python ne zna primerjati števil (int) in nizov (string), zato javi **TypeError** in nam pove, da teh dveh tipov med seboj ne moremo primerjati.

## Logika

V prejšnjih primerih si pravzaprav že uporabljala objekt, ki se mu v Python-u reče **Boolean** -- ta je verjetno najprijaznejši.

Obstajata zgolj in samo dve vrsti objekta Boolean: - True (resnica) - False (neresnica).

Vendar pa Python razume zgolj oznako 'True' (prva črka velika, ostale male). **Oznake true, TRUE, tRUE ne bodo delovale -- pravilna je le True** (enako seveda velja tudi za 'False').

Boolean lahko uporabimo tudi pri spremenljivkah! Takole:

    >>> a = True
    >>> a
    True
    

Lahko pa tudi tako:

    >>> a = 2 > 5
    >>> a
    False
    

Z objektom Boolean se lahko še bolje spoznaš tako da preizkusiš sledeče ukaze:

*   `True and True`
*   `False and True`
*   `True or 1 == 1`
*   `1 != 2`

Čestitke! Pravkar si spoznala enega izmed najbolj uporabnih pripomočkov pri programiranju - Boolean!

# Shranjevanje!

Dosedaj smo programsko kodo pisali kar direktno v tolmač, kar pa nas je precej omejevalo, saj smo lahko vnašali le eno vrstico kode naenkrat. Običajno programe najprej shranimo v datoteko, nato pa jih izvedeta **tolmač** ali **prevajalnik** programskega jezika, ki ga uporabljamo (v našem primeru je to Python). Zaenkrat smo programe izvajali s pomočjo Pythonovega **tolmača**, po eno vrstico naenkrat. V nadaljevanju bomo potrebovali več kot le eno vrstico kode, zato naredi naslednje:

*   Zapri tolmač
*   Odpri poljuben urejevalnik programske kode
*   Ustvari novo python datoteko in vanjo napiši nekaj kode
*   Zaženi!

Za izhod iz tolmača, vnesi ukaz exit() ga izvedi:

    >>> exit()
    $
    

Zdaj si ponovno v običajni ukazni vrstici.

Odpri urejevalnik, ki si ga izbrala v poglavju [urejevalniki programske kode][2]. Ustvari novo datoteko in vanjo prepiši sledečo kodo:

 [2]: ../code_editor/README.md

    python
    print('Hello, Django girls!')
    

> **Opomba** Verjetno si že opazila eno izmed najbolj kul stvari pri urejevalnikih programske kode: barve! V Pythonovi konzoli so imeli vsi ukazi enako barvo, zdaj pa nam urejevalnik funkcijo `print` obarva z drugačno barvo kot preostalo kodo. Tako obarvanje nam lahko zelo pomaga. Barve nas recimo opozorijo na napake, že ko pišemo kodo. Velikokrat se recimo zgodi, da se zatipkamo, pozabimo napisati kakšen obvezen ukaz (v nadaljevanju bomo pri funkcijah spoznali `def`) in podobno. Barve so vsekakor eden izmed razlogov, zakaj uporabljamo urejevalnike. :)

Z urejevalnikom se lahko malce spoznaš, tako da vanj prepišeš nekaj kode od prej.

Datoteko bomo zdaj shranili in ji dali pametno ime. Poimenuj jo recimo **python_intro.py**in jo shrani na namizje. Datoteko lahko seveda poimenuješ povsem poljubno, važno je le, da se ime konča z **.py**. Končnica **.py** operacijskemu sistemu pove, da je našo datoteko potrebno zagnati s Pythonom.

Zdaj lahko datoteko zaženeš! Za začetek uporabi svoje znanje ukazne vrstice in **spremeni imenik** v namizje.

Na Mac-u, ukaz zgleda približno takole:

    $ cd /Users/<tvoje_ime>/Desktop
    

Na Linux-u tako:

    $ cd /home/<tvoje_ime>/Desktop
    

Na Windows-u pa tako:

    > cd C:\Users\<tvoje_ime>\Desktop
    

Če se ti kje zatakne, povprašaj za pomoč mentorja.

S pomočjo Python-a našo datoteko izvršimo takole:

    $ python3 python_intro.py
    Hello, Django girls!
    

Odlično! Pravkar si zagnala svoj prvi program.

Zdaj se lahko spoznamo z enim izmed bistvenih programerskih orodij:

## If...elif...else

V programu se velikokrat pojavi koda, za katero želimo, da se izvede le, ko je izpolnjen nek pogoj. V Pythonu nam to omogoča **if stavek**.

Kodo, ki je v datoteki **python_intro.py** zamenjaj s tole:

    python
    if 3 > 2:
    

Če ta program shraniš in zaženeš, boš dobila napako:

    $ python3 python_intro.py
    File "python_intro.py", line 2
             ^
    SyntaxError: unexpected EOF while parsing
    

Težava je v tem, da nismo povedali, kaj naj se zgodi, če je pogoj `3 > 2` resničen (enak `True`). Naredimo zdaj program, ki bo izpisal "It works!". Spremeni kodo v datoteki **python_intro.py**:

    python
    if 3 > 2:
        print('It works!')
    

Si opazila, da smo vrstico po if stavku zamaknili? To moraš narediti vedno, zato da Python ve, kaj pognati, če je pogoj resničen. Narediš lahko le en presledek, vendar je koda bolj pregledna, če jih narediš več. S tipko `tab` recimo narediš 4 presledke.

Datoteko shrani in ponovno poženi:

    $ python3 python_intro.py
    It works!
    

### Kaj pa, če pogoj ni resničen?

Dosedaj smo se pogovarjali le o kodi, ki se izvede, če pogoj velja. Če pa pogoj ni resničen ali drugačen, si lahko pomagamo s stavkoma `elif` in `else`:

    python
    if 5 > 2:
        print('5 is indeed greater than 2')
    else:
        print('5 is not greater than 2')
    

Zgornji program bo izpisal:

    $ python3 python_intro.py
    5 is indeed greater than 2
    

Če bi bilo število 2 večje kot 5, bi se izvedel drugi print. Preprosto, kajne? Poglejmo si še `elif`:

    python
    name = 'Sonja'
    if name == 'Ola':
        print('Hey Ola!')
    elif name == 'Sonja':
        print('Hey Sonja!')
    else:
        print('Hey anonymous!')
    

program izpiše:

    $ python3 python_intro.py
    Hey Sonja!
    

`elif` torej doda še dodaten pogoj, ki se preveri, če je prejšnji pogoj neresničen.

Po začetnem `if` stavku, lahko dodaš lahko poljubno število `elif` stavkov. Recimo:

    python
    volume = 57
    if volume < 20:
        print("It's kinda quiet.")
    elif 20 <= volume < 40:
        print("It's nice for background music")
    elif 40 <= volume < 60:
        print("Perfect, I can hear all the details")
    elif 60 <= volume < 80:
        print("Nice for parties")
    elif 80 <= volume < 100:
        print("A bit loud!")
    else:
        print("My ears are hurting! :(")
    

Python začne po vrsti preverjati pogoje, se ustavi, ko pride do resničnega in izvede ustrezno kodo, ki temu pogoju sledi:

    $ python3 python_intro.py
    Perfect, I can hear all the details
    

### Povzetek

V zadnjih treh podpoglavjih smo se naučili:

*   **primerjanja** - v Python-u lahko neke vrednosti primerjamo s pomočjo operatorjev `>`, `>=`, `==`, `<=`, `<`, `and` in `or`
*   **Boolean** - to je objekt, ki ima lahko le vrednosti `True` in `False`
*   **Shranjevanje** - kodo lahko shranimo v datoteko in si s tem olajšamo zaganjanje obsežnih programov.
*   **if...elif...else** - stavki, ki omogočajo izvajanje kode le, ko je izpolnjen nek pogoj.

Čas je za zadnje podpoglavje!

## Funkcije

Se spominjaš funkcije `len()`? No, dobra novica - kmalu boš znala funkcijo narediti sama!

Funkcija je zaporedje ukazov, ki jih Python izvede, ko mu podamo ime funkcije. Vsaka funkcija se začne z besedo `def`, ima svoje ime in določene argumente. Začnimo z nečim preprostim. Kodo v datoteki **python_intro.py** zamenjaj s sledečo:

    python
    def hi():
        print('Hi there!')
        print('How are you?')
    
    hi()
    

Super, naredila si svojo prvo funkcijo!

Verjetno se sprašuješ, zakaj smo na koncu datoteke napisali ime funkcije. To smo naredili zato, ker Python prebere celo datoteko in nato izvede vso kodo. S stavkom def torej funkcijo le definiramo, s klicem hi(), pa zahtevamo, da naj jo Python izvede.

Poženi zdaj ta programček in si oglej rezultat:

    $ python3 python_intro.py
    Hi there!
    How are you?
    

Odlično! Dodajmo naši funkciji še argumente. Spodobilo bi se, da bi naša funkcija pozdravu dodala še ime, saj je to precej bolj vljudno:

    python
    def hi(name):
    

Kot vidiš, smo funkciji dodali argument `name`:

    python
    def hi(name):
        if name == 'Ola':
            print('Hi Ola!')
        elif name == 'Sonja':
            print('Hi Sonja!')
        else:
            print('Hi anonymous!')
    
    hi()
    

Ne pozabi: Funkcija `print`, ki sledi `if` stavku v zgornji kodi, je zamaknjena. S tem Pythonu povemo, da je ta koda znotraj if stavka in se izvede le, ko je izpolnjen nek pogoj. Zaženi zdaj program:

    $ python3 python_intro.py
    Traceback (most recent call last):
    File "python_intro.py", line 10, in <module>
      hi()
    TypeError: hi() missing 1 required positional argument: 'name'
    

Dobimo napako. Na srečo nam Python dokaj natančno pove, v čem je težava. Pove nam, da naša funkcija `hi()` potrebuje argument, mi pa smo ga pozabili dodati, ko smo funkcijo klicali. Popravimo to napako:

    python
    hi("Ola")
    

Program ponovno poženi:

    $ python3 python_intro.py
    Hi Ola!
    

Kaj pa, če za argument damo kakšno drugo ime?

    python
    hi("Sonja")
    

Poženi:

    $ python3 python_intro.py
    Hi Sonja!
    

Kaj misliš, da se bo zgodilo, če funkciji podaš kakšno drugo ime (ne Ola ali Sonja)? Poskusi in videla boš, če si razmišljala pravilno. Izpisati bi moralo tole:

    Hi anonymous!
    

Funkcije so zelo uporabna stvar, saj nam lahko, če jih pravilno uporabimo, precej zmanjšajo količino kode. Če ne bi uporabili funkcije, bi v našem primeru morali vsakič, ko dobimo ime osebe, sami vedno znova napisati tisti print stavek. Točno to je glavna moč funkcij - preprečijo ponavljanje iste oziroma podobne kode.

Poskusimo našo funkcijo še malo nadgraditi. Človeških imen je malce več kot dve in pisati if oziroma elif stavek za vsako ime posebej, bi bilo malce zamudno.

    python
    def hi(name):
        print('Hi ' + name + '!')
    
    hi("Rachel")
    

Poženi program:

    $ python3 python_intro.py
    Hi Rachel!
    

Čestitke! Pisanje funkcij zdaj obvladaš! :)

## Zanke

Prišli smo do zadnjega dela tega poglavja.

Kot smo že omenili, programerji ne maramo večkrat pisati podobne kode. Konec koncev je smisel programiranja ravno to, da računalnik naredi čimveč sam. Pri pisanju krajše kode, nam pomagajo zanke.

Se še spomniš seznamov? Naredimo seznam deklet:

    python
    girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
    

Vsako izmed njih želimo pozdraviti po imenu. Uporabili bomo zanko, znotraj nje pa že napisano funkcijo `hi`:

    python
    for name in girls:
    

Tako kot ~~~ if~~~ stavek, moramo tudi ~~~ for~~~ zanko zamakniti za vsaj en presledek.

Tole je celotna koda:

    python
    def hi(name):
        print('Hi ' + name + '!')
    
    girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
    for name in girls:
        hi(name)
        print('Next girl')
    

Ko program zaženemo, dobimo nekaj takega:

    $ python3 python_intro.py
    Hi Rachel!
    Next girl
    Hi Monica!
    Next girl
    Hi Phoebe!
    Next girl
    Hi Ola!
    Next girl
    Hi You!
    Next girl
    

Koda, ki je znotraj `for` zanke, se torej res ponovi za vsak element seznama `girls`.

`for` zanko pa lahko narediš tudi s pomočjo funkcije `range`:

    for i in range(1, 6):
        print(i)
    

Rezultat:

    1
    2
    3
    4
    5
    

`range` je funkcija, ki ustvari seznam zaporednih števil (do posamičnega števila lahko dostopamo preko spremenljivke i).

Iz zgornjega primera se vidi tudi, da druga številka, ki jo podamo funkciji range, ni vključena v seznam števil. `range(1, 6)` torej naredi seznam števil od (vključno) 1 do (vključno) 5. Na številko 6 lahko torej gledamo kot na mejo.

## Povzetek

To je to. **Obvladaš!** Lahko si ponosna nase, saj je bilo to poglavje kar zahtevno. Veseli smo, predelala že tako velik del tega vodiča!

Predlagamo, da si pred nadaljevanjem spočiješ oči od vse te kode. Malce se pretegni, sprehodi naokrog, nato pa nadaljuj z naslednjim poglavjem. :)

![Mafin][3]

 [3]: images/cupcake.png