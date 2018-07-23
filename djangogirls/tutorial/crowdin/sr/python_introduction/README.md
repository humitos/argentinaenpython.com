# Uvod u Python

> Part of this chapter is based on tutorials by Geek Girls Carrots (http://django.carrots.pl/).

Hajde da pišemo nešto koda!

## Python prompt

Da biste se počeli igrati u Python-u, moramo otvoriti *komandnu liniju* na našem računaru. Trebalo bi da već znate kako se to radi - naučili ste u poglavlju [Uvod u komandnu liniju][1].

 [1]: ../intro_to_command_line/README.md

Kada budete spremni, ispratiti sledeće instrukcije.

Želimo da otvorimo Python konzolu, tako da ćemo otkucati `python` na Windows-u ili `python3 ` na Mac-u ili Linux-u i pritisnuti `enter`.

    $ python3
    Python 3.4.3 (...)
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    

## Vaša prva Python komanda!

Nakon pokretanja Python komange, prompt se menja u `>>>`. To za nas znači da sada možemo koristiti samo komande u Python jeziku. Ne morate uneti `>>>` - Python to radi za vas.

Ako želite da izađete iz Python konzole, možete u bilo komtrenutku otkucati `exit()` ili korsititi prečicu `Ctrl + Z` za Windows, odnosno `Ctrl + D` za Mac/Linux. Onda nećete više videti `>>>`.

Trenutno ne želimo izaći iz Python konzole. Želimo da naučimo više o njoj. Hajde da počnemo sa nečim veoma jednostavnim. Na primer, probajte otkucati neke matematičke izraze, poput `2 + 3` i pritisnite `enter`.

    >>> 2 + 3
    5
    

Lepo! Vidite kako se pojavio rezultat? Python zna matematiku! Možete isprobati i druge komande, kao: - `4 * 5` - `5 - 1` - `40 / 2`

Zabavljajte se sa ovim malo i onda se vratite ovde :).

Kao što vidite, Python je odličan kalkulator. Ako se pitate šta još može da radi...

## Stringovi

Šta je sa vašim imenom? Ukucajte vaše ime između navodnika kao u primeru:

    >>> "Ola"
    'Ola'
    

Upravo ste kreirali vaš prvi string! To je niz karaktera koji može biti obrađen od strane računara. String mora uvek počinjati i završavati se sa istim karaketerom. To može biti jedan navodnik (`'`) ili dvostruki (`"`) navodnici (nema razlike!). Navodnici govore Python-u da je ono što je unutar njih string.

Stringovi mogu biti povezani međusobno. Probajte ovo:

    >>> "Hi there " + "Ola"
    'Hi there Ola'
    

Možete i pomnožiti string nekim brojem:

    >>> "Ola" * 3
    'OlaOlaOla'
    

Ako treba da stavite navodnik unutar stringa, to možete uraditi na dva načina.

Koristeći dvostruke navodnike:

    >>> "Runnin' down the hill"
    "Runnin' down the hill"
    

ili eskejpovanjem navodnika korišćenjem ubrnute kose crte (backslash) (``):

    >>> 'Runnin\' down the hill'
    "Runnin' down the hill"
    

Lepo, zar ne? Da biste videli vaše ime sa svim velikim slovima, dovoljno je da ukucate:

    >>> "Ola".upper()
    'OLA'
    

Potrebno je samo da upotrebite **funkciju ** `upper` nad vašim stringom! Funkcije (poput `upper()`) jeste sekvenca instrukcija koju Python može da izvrši nad datim objektom (`"Ola"`) kada je pozovete.

Ako želite da saznate broj slova koja se nalaze u vašem imenu, postoji funkcija i za to!

    >>> len("Ola")
    3
    

Da li se pitate zašto nekada pozivate dunkciju sa `.` na kraju stringa (poput `"Ola".upper()`), a nekada prvo pozovete funkciju i string stavite u zagrade? U nekim slučajevima funkcija pripada objektima, poput `upper()`, i može se primeniti samo na stringovima. U ovom slučaju funkciju zovemo **metoda**. U nekim drugim situacijama funkcije ne pripadaju ničemu konkretnom i mogu se koristiti na raznim tipovima objekata, poput `len()`. Zato smo proslediti `"Ola"` kao parametar funkciji `len`.

### Kratak pregled

OK, dosta o stringovima. Do sada ste naučili o:

*   **promptu** - kucanje komandi (koda) u Python prompt rezultira odgovorima u Python-u
*   **brojevi i stringovi** - u Python-u se brojevi korsite za matematiku, a stringovi za tekstualne objekte
*   **operatori** - kao što su + u *, kombinuju vrednosti proizvodeći nove
*   **funkcije** - kao što su upper() i len(), primenjuju akcije nad objektima.

Ovo su osnove svakog programskog jezika koga ćete učiti. Spremni za nešto teže? Sigurni smo da jeste!

## Greške

Hajde da probamo nešto novo. Da li možemo dobiti dužinu broja na isti način kao što smo to radili za vaše ime? Otkucajte `len(304023)` i pritisnitet `enter`:

    >>> len(304023)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: object of type 'int' has no len()
    

Dobili smo našu prvu grešku! Kaže da objekti tipa "int" (integeri, celi brojevi) nemaju dužinu. Šta možemo sada uraditi? Možda da napišemo naš broj kao string? Stringovi imaju dužinu, zar ne?

    >>> len(str(304023))
    6
    

Radi! Koristili smo funkciju `str` unutar funkcije `len`. `str()` konvertuje sve u stringove.

*   Funkcija `str` konvertuje stvari **stringove**
*   Funkcija `int` konvertuje stvari u **integere**

> Važno: možemokonvertovati brojeve u tekst, ali ne možemo nužno tekst u brojeve - šta bi recimo `int('hello')` bilo?

## Varijable

Jako bitan koncept u programiranju su varijable. Varijabla je ništa više nego naziv za nešto što ćemo moći koristiti kasnije. Programeri koriste varijable da čuvaju podatke, učine svoj kod čitljivijim i kako ne bi morali stalno pamtiti šta je koja stvar.

Hajde da, na primer, želimo kreirati novu varijablu koju ćemo zvati `naziv`:

    >>> ime= "Ola"
    

Vidite? Jednostavno je! Kažemo samo da je ime jednako Ola.

Kao što ste primetili, vaš program nije ništa vratio, kao što je ranije bio slučaj. Kako onda možemo znati da ta varijabla zaista postoji? Jednostavno unesite `ime` i pritisnite `enter`:

    >>> ime
    'Ola'
    

Jej! Vaša prva varijabla :)! Uvek možete promeniti na šta se ona odnosi:

    >>> ime= "Sonja"
    >>> ime
    'Sonja'
    

Možete ih koristiti i unutar funkcija:

    >>> len(ime)
    5
    

Strava, zar ne? Naravno, varijable mogu biti bilo šta, znači i brojevi! Probajte sledeće:

    >>> a = 4
    >>> b = 6
    >>> a * b
    24
    

Šta se dešava ako iskoristimo pogrešno ime? Da li možete pogoditi? Hajde da probamo!

    >>> city = "Tokyo"
    >>> ctiy
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'ctiy' is not defined
    

Greška! Kao što možete videti, Python ima drugačije tipove grešaka i ova se zove **NameError**. Python će vam dati grešku ako probate koristiti varijablu koja nije još uvek definisana. Ako kasnije naiđete na ovu grešku, proverite da li ste u vašem kodu pogrešno napisali neki naziv.

Poigrajte se malo sa ovim i vidite šta je sve moguće raditi!

## Print funkcija

Probajte ovo:

    >>> ime= 'Maria'
    >>> ime
    'Maria'
    >>> print(ime)
    Maria
    

Kada samo otkucate `ime`, Python interpreter odgovara sa string *reprezentacijom* varijable "ime", a do su slova M-a-r-i-a, okružena jednostrukim navodnicima. Kada napišemo `print(ime)`, Python će "odštampati" sadržaj varijable na ekran, bez navodnika, što je urednije.

Kao što ćete videte kasnije, `print()` se koristi i kada želimo da odštampano nešto unutar funkcija, ili kada želimo da odštampano nešto preko više linija.

## Liste

Pored stringova i integera, Python koristi još mnogo različitih tipova objekata. Sada ćemo da prikažemo **liste**. Liste su upravo ono što mislite da jesu: objekti koji su liste drugih objekata :)

Hajde da napravimo listu:

    >>> []
    []
    

Da, ovo je prazna lista. Nije nešto korisnika, zar ne? Hajde da kreiramo listu brojeva za lutriju. Ne želimo da se ponavljamo više puta, pa ćemo je staviti u varijablu:

    >>> lutrija= [3, 42, 12, 19, 30, 59]
    

Dobro, sada imamo listu! Šta da radimo sa njom? Hajde da vidimo koliko ima brojeva u listi. Da li imate ideju koja bi se funkcija mogla koristiti za to? To već znate!

    >>> len(lutrija)
    6
    

Da! `len()` nam može dati broj objekata u listu. Korisno, zar ne? Možda bismo je sada mogli sortirati:

    >>> lutrija.sort()
    

Ovo ništa ne vraća, nego samo manje raspored u kom se brojevi pojavljuju u listi. Hajde da opet odštampano ovu listu i vidimo šta će se desiti:

    >>> print(lutrija)
    [3, 12, 19, 30, 42, 59]
    

Kao što možete videti, brojevi su sortirani od najmanje do najveće vrednosti. Čestitamo!

Možda želimo da obrnemo ovaj raspored? Hajde da uradimo to!

    >>> lutrija.reverse()
    >>> print(lutrija)
    [59, 42, 30, 19, 12, 3]
    

Jednostavno, zar ne? Ako želite nešto dodati u vašu listu, tomožete uraditi unosom sledeće komande:

    >>> lutrija.append(199)
    >>> print(lutrija)
    [59, 42, 30, 19, 12, 3, 199]
    

Ako želite da prikažete samo prvi broj, možete to uraditi koristeći **indekse**. Indeks je broj koji pokazuje gde se u listi nalazi neki element. Programeri više vole da počnu brojati od 0, tako da prvi objekat u listi ima indeks 0, sledeći 1 itd. Probajte ovo:

    >>> print(lutrija[0])
    59
    >>> print(lutrija[1])
    42
    

Možete videti da možete pristupiti različitim objektima u listi koristeći naziv liste i indeks objekta koga navodite unutar uglastih zagrada.

Ako želite da izbrišete nešto iz liste moraćete koristiti **indekse** kao što smo naučili i **del** naredbu (del je skraćeno za delete). Hajde da damo primer i time demonstriramo ono što smo upravo naučili; izbrisaćemo prvi element naše liste.

    >>> print(lutrija)
    [59, 42, 30, 19, 12, 3, 199]
    >>> print(lutrija[0])
    59
    >>> del lutrija[0]
    >>> print(lutrija)
    [42, 30, 19, 12, 3, 199]
    

Ovo odlično radi!

Za malo dodatne zabave, isprobajte neke druge indekse: 6, 7, 1000, -1, -6 ili -1000. Da li možete pogoditi rezultat pre nego što isprobate komande. Da li rezultati imaju smisla?

Možete naći listu svih dostupnihh metoda listi u sledećem poglavlju Python dokumentacije: https://docs.python.org/3/tutorial/datastructures.html

## Rečnici

Rečnici su slični listama, ali vrednostima pristupate traženjem po ključu umesto indeksu. Ključ može biti bilo koji ključ ili broj. Sintaksa za definisanje praznog rečnika je:

    >>> {}
    {}
    

Ovo pokazuje da smo napravili prazan rečnik. Jej!

Probajte sada napisati sledeće komande (takođe, zamenite informacije vašim):

    >>> ucesnik= {'ime': 'Ola', 'zemlja': 'Poljska', 'omiljeni_brojevi': [7, 42, 92]}
    

Sa ovom komandom, upravo ste kreirali varijablu sa nazivom `ucesnik` sa tri para ključ-vrednost:

*   Ključ `ime` pokazuje na vrednost `'Ola'` (što je `string` objekat),
*   `zemlja` pokazuje na vrednost `'Poljska'` (još jedan`string`),
*   i `omiljeni_brojevi` pokazuje na `[7, 42, 92]` (`listu` sa brojevima unutar nje).

Sintaksa za proveru sadržaja pojedinim ključeva je sledeća:

    >>> print(ucesnik['ime'])
    Ola
    

Vidite, slično je listama. Ali ne treba da pamptite indekse - samo nazive.

Šta se dešava ako pitamo Python za vrednost ključa koja ne postoji? Možete li pogoditi. Hajde da isprobamo i vidimo!

    >>> ucesnik['godine']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'godine'
    

Pogledajte, još jedna greška! Ovo je**KeyError**. Python je uslužan i govori nam da ključ `'godine'` ne postoji za dati rečnik.

Kada treba koristiti rečnik, a kada listu? Pa, to jeste dobro pitanje o kome treba razmišljati. Samo smislite neki odgovor pre nego što pogledate sledeću liniju.

*   Da li vam treba uređena sekvrenca elemenata? Koristite listu.
*   Da li vam je potrebno da pridružite vrednosti ključevima, tako da ih kasnije možete efikasno (po ključu) tražiti? Koristite rečnik.

Rečnici su, popu listi, *promenljivi*, što znači da se mogu menjati nakon što se kreiraju. Možete dodati nove parove ključ/vrednost u rečnik nakon što ga kreirate, kao na primer:

    >>> ucesnik['omiljeni_jezik'] = 'Python'
    

Kao i kod listi, `len()` metodu možete koristiti nad rečnicima, a ona vraća broj ključ-vrednost parova u rečniku:

    >>> len(ucesnik)
    4
    

Nadamo se ovo do sada ima smisla. :) Da li ste spremni za malo zabave nad rečnicima? Pređite na sledeću liniju za neke fanrastične stvari.

Možete koristiti `del` komandu za brisanje elemenata iz rečnika. Recimo, ako želite da obrišete element koji odgovara ključu `'omiljeni_brojevi'`, samo otkucajte sledeću komandu:

    >>> del ucesnik['omiljeni_brojevi']
    >>> ucesnik
    {'zemlja': 'Poljska', 'omiljeni jezik': 'Python', 'ime': 'Ola'}
    

Kao što možete videti iz rezultata, ključ-vrednost par koji odgovara ključu 'omiljeni_brojevi' je izbrisan.

Možete i promeniti vrednost koja je dodeljena već postojećem ključu u rečniku. Otkucajte:

    >>> ucesnik['zemlja'] = 'Nemacka'
    >>> ucesnik
    {'zemlja': 'Nemacka', 'omiljeni_jezik': 'Python', 'ime': 'Ola'}
    

Vrednost za ključ `'zemlja'` je promenjena od `Poljska` na `Nemacka`. :) Uzbudljivo? Jeee! Upravo ste naučili još jednu strava stvar.

### Kratak pregled

Strava! Sada znate puno o programiranju. U ovom delu ste naučili o:

*   **greškama** - znate kako da čitate i razumete greške koje se prikazuju kada Python ne razume komandu koju ste mu dali
*   **varijablama** - nazivima objekata koji vam dozvoljavaju da kodirate lakše i učinite vaš kod čitljivijim
*   **listama** - listama objekata koji se čuvaju u određenom poretku
*   **rečnicima** - objektima koji čuvaju kluč-vrednost parove

Uzbuđeni zbog sledećeg dela? :)

## Poređenje stvari

Poređenje stvari je bitan deo programiranja. Šta je najlakše za poređenje? Brojevi, naravno. Hajde da vidimo kako ovo radi:

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
    

Dali smo Python-u neke brojeve da poredi. Kao što vidite, Python može porediti ne samo brojeve, nego i rezultate metoda. Strava, zar ne?

Da li se pitate zašto smo stavili dva znaka jednakosti `==` jedan pored drugog kako bismo ispitali da li su dva broja jednaka? Jedan znak `=` koristimo da varijablama dodelimo vrednost. Uvek, **uvek**, morate staviti dva `==` ako želite proveriti da li su neke dve stvari međusobno jdnake. Takođe možemo reći i da su dve stvari međusobno različite. Za to koristimo simbol `!=`, kao što je prikazano u primeru gore.

Dajmo Python-u još dva zadatka:

    >>> 6 >= 12 / 2
    True
    >>> 3 <= 2
    False
    

`>` i`<` su jednostavni, ali šta `>=` i`<=` znače? Čitajte ih na sledeći način:

*   x `>` y znači: x je veće od y
*   x `<` y znači: x je manje od y
*   x `<=` y znači: x je manje ili jednako y
*   x `>=` y znači: x je veće ili jednako y

Strava! Hoćete još jedan? Probajte ovo:

    >>> 6 > 2 and 2 < 3
    True
    >>> 3 > 2 and 2 < 1
    False
    >>> 3 > 2 or 2 < 1
    True
    

Možete dati Python-u kolliko god želite brojeva da poredi i uvek će vam dati odgovor? Prilično pametno, zar ne?

*   **and** - ako koristite `and` operator, oba poređenja moraju biti True da bi cela komanda bila True
*   **or** - ako koristite `or` operator, samo jedno poređenje mora biti True da bi cela komanda bila True

Da li ste nekada čuli za izraz "porediti jabuke i kruške"? Hajde da isprobamo ekvivalent tome u Python-u:

    >>> 1 > 'django'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unorderable types: int() > str()
    

Ovde možete videti da baš kao u izreci, Python ne može porediti broj (`int`) i string (`str`). Umesto toga, pokazuje **TypeError** i kaže nam da se dva tipa ne mogu porediti međusobno.

## Boolean

Slučajno, upravo ste naučili o jednom novom tipu objekata u Python-u. Zove se **Boolean** - i veroavtno je najjednostavniji tip od svih.

Imamo samo dva Boolean objekta: - True - False

Da bi Python ovo razumeo, morate uvek pisati 'True' (prvo slovo je veliko, sva ostala su mala). **true, True, tRUE ne rade - samo je True korektno.** (Naravno, isto važi i za 'False'.)

Booleani takođe mogu biti varijable! Pogledajte:

    >>> a = True
    >>> a
    True
    

Možete uraditi i sledeće:

    >>> a = 2 > 5
    >>> a
    False
    

Provežbajte i zabavite se malo sa Booleanima pokuševajući izvršiti sledeće komande:

*   `True and True`
*   `False and True`
*   `True or 1 == 1`
*   `1 != 2`

Čestitamo! Booleani su jedna od najinteresantnijih mogućnosti u programiranju i upravo ste naučili kako da ih koristite!

# Sačuvajte!

Do sada smo sav kod pisali u interpreteru, što nas ograničava na unos samo jedne linije u jednom trenutku. Obični programi se čuvaju u fajlovima i izvržavaju od strane **interpretera** programskog jezika ili **kompajlera**. Do sada smo naše programe izvršavali kao jednu liniju u jedinici vremena u Python **interpreteru**. Za naredne zadatake će nam trebati više od jedne linije koda, tako da bi na brzinu trebalo da:

*   Zatvorite Python interpreter
*   Otvorite editor koda po vašem izboru
*   Snimite neki kod u novi python fajl
*   Pokrenite ga!

Da biste izašli iz Python interpretera koga smo koristili, samo unesite ~~~exit()~~~ funkciju:

    >>> exit()
    $
    

Ovo će vas vratiti na komand prompt.

Ranije smo odabrali editor koda iz [editori koda][2] sekcije. Sada treba da otvorimo tah editor i unesemo neki kod u novi fajl:

 [2]: ../code_editor/README.md

    python
    print('Hello, Django girls!')
    

> **Napomena**Mogli ste primetiti jednu od najboljih stvari vezanih za editore koda: boje! U Python konzoli je sve bilo iste boje, a sada možete primetiti da je `print` funkcija drugačije boje nego string. Ovo se naziva "naglašavanje sintakse" i jako je korisno za kodiranje. Boja će vam dati naznaku šta određena stvar predstavlja, poput nezatvorenih stringova ili grešku u kucanju rezervisane reči (kao što je `def` za funkciju, kao što ćemo dole videti). Ovo je jeda od razloga zašto koristimo editore koda :)

Očigledno, sada ste već iskusni Python developer, pa slobodno napišite nešto koda od onoga što ste naučili danas.

Sada treba da sačuvamo fajl i damo mu neko opisno ime. Hajde da fajl nazovemo **python_intro.py** i snimimo ga na desktop. Fajl možemo nazvati kako god želimo, ali je bitno da osiguramo da se fajl završava na **.py**. Ekstenzija **.py** govori operativnom sistemu da je u pitanju **izvršivi python fajl** te da ga Python može pokrenuti.

With the file saved, it's time to run it! Using the skills you've learned in the command line section, use the terminal to **change directories** to the desktop.

On a Mac, the command will look something like this:

    $ cd /Users/<your_name>/Desktop
    

On Linux, it will be like this (the word "Desktop" might be translated to your language):

    $ cd /home/<your_name>/Desktop
    

And on windows, it will be like this:

    > cd C:\Users\<your_name>\Desktop
    

If you get stuck, just ask for help.

Now use Python to execute the code in the file like this:

    $ python3 python_intro.py
    Hello, Django girls!
    

Alright! You just ran your first Python program that was saved to a file. Feel awesome?

You can now move on to an essential tool in programming:

## If...elif...else

Lots of things in code should only be executed when given conditions are met. That's why Python has something called **if statements**.

Replace the code in your **python_intro.py** file with this:

    python
    if 3 > 2:
    

If we saved this and ran it, we'd see an error like this:

    $ python3 python_intro.py
    File "python_intro.py", line 2
             ^
    SyntaxError: unexpected EOF while parsing
    

Python expects us to give further instructions to it which are executed if the condition `3 > 2` turns out to be true (or `True` for that matter). Let’s try to make Python print “It works!”. Change your code in your **python_intro.py** file to this:

    python
    if 3 > 2:
        print('It works!')
    

Notice how we've indented the next line of code by 4 spaces? We need to do this so Python knows what code to run if the result is true. You can do one space, but nearly all Python programmers do 4 to make things look neat. A single `tab` will also count as 4 spaces.

Save it and give it another run:

    $ python3 python_intro.py
    It works!
    

### What if a condition isn't True?

In previous examples, code was executed only when the conditions were True. But Python also has `elif` and `else` statements:

    python
    if 5 > 2:
        print('5 is indeed greater than 2')
    else:
        print('5 is not greater than 2')
    

When this is run it will print out:

    $ python3 python_intro.py
    5 is indeed greater than 2
    

If 2 were a greater number than 5, then the second command would be executed. Easy, right? Let's see how `elif` works:

    python
    name = 'Sonja'
    if name == 'Ola':
        print('Hey Ola!')
    elif name == 'Sonja':
        print('Hey Sonja!')
    else:
        print('Hey anonymous!')
    

and executed:

    $ python3 python_intro.py
    Hey Sonja!
    

See what happened there? `elif` lets you add extra conditions that run if the previous conditions fail.

You can add as many `elif` statements as you like after your initial `if` statement. For example:

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
    

Python runs through each test in sequence and prints:

    $ python3 python_intro.py
    Perfect, I can hear all the details
    

### Kratak pregled

In the last three exercises you learned about:

*   **comparing things** - in Python you can compare things by using `>`, `>=`, `==`, `<=`, `<` and the `and`, `or` operators
*   **Boolean** - a type of object that can only have one of two values: `True` or `False`
*   **Saving files** - storing code in files so you can execute larger programs.
*   **if...elif...else** - statements that allow you to execute code only when certain conditions are met.

Time for the last part of this chapter!

## Your own functions!

Remember functions like `len()` that you can execute in Python? Well, good news - you will learn how to write your own functions now!

A function is a sequence of instructions that Python should execute. Each function in Python starts with the keyword `def`, is given a name, and can have some parameters. Let's start with an easy one. Replace the code in **python_intro.py** with the following:

    python
    def hi():
        print('Hi there!')
        print('How are you?')
    
    hi()
    

Okay, our first function is ready!

You may wonder why we've written the name of the function at the bottom of the file. This is because Python reads the file and executes it from top to bottom. So in order to use our function, we have to re-write it at the bottom.

Let's run this now and see what happens:

    $ python3 python_intro.py
    Hi there!
    How are you?
    

That was easy! Let's build our first function with parameters. We will use the previous example - a function that says 'hi' to the person running it - with a name:

    python
    def hi(name):
    

As you can see, we now gave our function a parameter that we called `name`:

    python
    def hi(name):
        if name == 'Ola':
            print('Hi Ola!')
        elif name == 'Sonja':
            print('Hi Sonja!')
        else:
            print('Hi anonymous!')
    
    hi()
    

Remember: The `print` function is indented four spaces within the `if` statement. This is because the function runs when the condition is met. Let's see how it works now:

    $ python3 python_intro.py
    Traceback (most recent call last):
    File "python_intro.py", line 10, in <module>
      hi()
    TypeError: hi() missing 1 required positional argument: 'name'
    

Oops, an error. Luckily, Python gives us a pretty useful error message. It tells us that the function `hi()` (the one we defined) has one required argument (called `name`) and that we forgot to pass it when calling the function. Let's fix it at the bottom of the file:

    python
    hi("Ola")
    

And run it again:

    $ python3 python_intro.py
    Hi Ola!
    

And if we change the name?

    python
    hi("Sonja")
    

And run it:

    $ python3 python_intro.py
    Hi Sonja!
    

Now, what do you think will happen if you write another name in there? (Not Ola or Sonja) Give it a try and see if you're right. It should print out this:

    Hi anonymous!
    

This is awesome, right? This way you don't have to repeat yourself every time you want to change the name of the person the function is supposed to greet. And that's exactly why we need functions - you never want to repeat your code!

Let's do something smarter -- there are more names than two, and writing a condition for each would be hard, right?

    python
    def hi(name):
        print('Hi ' + name + '!')
    
    hi("Rachel")
    

Let's call the code now:

    $ python3 python_intro.py
    Hi Rachel!
    

Congratulations! You just learned how to write functions! :)

## Loops

This is the last part already. That was quick, right? :)

Programmers don't like to repeat themselves. Programming is all about automating things, so we don't want to greet every person by their name manually, right? That's where loops come in handy.

Still remember lists? Let's do a list of girls:

    python
    girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
    

We want to greet all of them by their name. We have the `hi` function to do that, so let's use it in a loop:

    python
    for name in girls:
    

The ~~~ for~~~ statement behaves similarly to the ~~~ if~~~ statement; code below both of these need to be indented four spaces.

Here is the full code that will be in the file:

    python
    def hi(name):
        print('Hi ' + name + '!')
    
    girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
    for name in girls:
        hi(name)
        print('Next girl')
    

And when we run it:

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
    

As you can see, everything you put inside a `for` statement with an indent will be repeated for every element of the list `girls`.

You can also use `for` on numbers using the `range` function:

    for i in range(1, 6):
        print(i)
    

Which would print:

    1
    2
    3
    4
    5
    

`range` is a function that creates a list of numbers following one after the other (these numbers are provided by you as parameters).

Note that the second of these two numbers is not included in the list that is output by Python (meaning `range(1, 6)` counts from 1 to 5, but does not include the number 6). That is because "range" is half-open, and with that we mean it includes the first value, but not the last.

## Kratak pregled

That's it. **You totally rock!** This was a tricky chapter, so you should feel proud of yourself. We're definitely proud of you for making it this far!

You might want to briefly do something else - stretch, walk around for a bit, rest your eyes - before going on to the next chapter. :)

![Cupcake][3]

 [3]: images/cupcake.png