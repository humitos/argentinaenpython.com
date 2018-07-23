# Osnove dela z ukazno vrstico

Dobro ti gre! Naučila si se že kar nekaj uporabnih stvari. Še malo, pa boš napisala svoj prvi program!

**Najprej pa te moramo seznaniti z zelo uporabnim in zabavnim orodjem: ukazno vrstico!**

Nadaljni koraki te bodo seznanili z uporabo črnega okna, ki ga uporablja vsak pravi heker. Sprva deluje malce nenavadno, vendar je dejansko zgolj program, v katerega vpisuješ ustrezne ukaze.

> 

## Kaj je ukazna vrstica?

Okno, ki mu rečemo **ukazna vrstica** ali **ukazna lupina**, je program, ki omogoča raznovrstno delo z datotekami na računalniku, kot je brisanje, pregledovanje, urejanje in dodajanje. Podobno kot Explorer v operacijskem sistemu Windows in Finder v operacijskem sistemu OSX, le da nima grafičnega vmesnika. Angleška imena za ukazno vrstico, ki si jih morda že slišala so recimo: *cmd*, *CLI*, *prompt*, *console* in *terminal*.

## Zagon ukazne vrstice

Delo z ukazno vrstico bomo začeli z zagonom le-te.

### Windows

Pritisni Start → Vsi programi → Pripomočki → Ukazna vrstica.

### Mac OS X

Applications → Utilities → Terminal.

### Linux

Verjetno se nahaja v Applications → Accessories → Terminal, vendar je to odvisno od tega, katero verzijo Linuxa imaš naloženo. Če je tam ni, pogooglaj :)

## Ukazna vrstica

Pred sabo imaš torej odprto črno ali belo okno, ki čaka, da vanj vpišeš ustrezne ukaze.

Če uporabljaš operacijski sistem Mac ali Linux, se prva vrstica v ukazni lupini verjetno začne takole:

    $
    

Na operacijskem sistemu Windows pa tako:

    >
    

Vsak ukaz se bo začel s tem znakom in presledkom, vendar tebi tega ne bo treba pisati vsakič znova. To bo zate naredil tvoj računalnik :)

> Manjša opomba: tvoja vrstica se verjetno začne nekako tako `C:\Users\Ana>` ali tako `Anas-MacBook-Air:~ ana$` še pred prej opisanim znakom. To je povsem pravilno. V vodiču ta del spuščamo, saj je tako bolj pregledno.

## Tvoj prvi ukaz :)

Začnimo z nečim preprostim. Vpiši sledeči ukaz:

    $ whoami
    

ali

    > whoami
    

Nato pritisni `enter`. Rezultat je približno tak:

    $ whoami
    ana
    

Kot si opazila, je računalnik izpisal tvoje ime. Super! :)

> Priporočamo, da vse ukaze prepišeš, ne kopiraš, saj si jih boš tako bolj zapomnila.

## Osnove

Vsak operacijski sistem ima malce različen nabor ukazov v ukazni vrstici, zato se vedno prepričaj, da spremljaš navodila za svoj operacijski sistem.

### Trenutni imenik

Če želimo delati z datotekami, bi bilo za začetek uporabno vedeti, v katerem direktoriju se nahajamo. Vpiši sledeči ukaz in pritisni `enter`:

    $ pwd
    /Users/ana
    

Na operacijskem sistemu Windows:

    > cd
    C:\Uporabniki\ana
    

Nekaj podobnega si verjetno dobila tudi ti. Ko odpreš ukazno vrstico, je tvoj imenik običajno enak domačemu imeniku prijavljenega uporabnika.

> Opomba: 'pwd' pomeni 'print working directory'.

* * *

### Izpis datotek in imenikov

Bi rada izpisala vse imenike in datoteke, ki so v tvojem trenutnem imeniku? To narediš takole:

    $ ls
    Applications
    Desktop
    Downloads
    Music
    ...
    

Windows:

    > dir
     Directory of C:\Uporabniki\ana
    05/08/2014 07:28 PM <DIR>      Aplikacije
    05/08/2014 07:28 PM <DIR>      Namizje
    05/08/2014 07:28 PM <DIR>      Prenosi
    05/08/2014 07:28 PM <DIR>      Glasba
    ...
    

* * *

### Sprememba imenika

Premaknimo se v imenik Namizje:

    $ cd Desktop
    

Windows:

    > cd Namizje
    

Preveri, če si se res premaknila:

    $ pwd
    /Users/ana/Desktop
    

Windows:

    > cd
    C:\Uporabniki\ana\Namizje
    

Deluje! Super!

> UPORABEN namig: če vpišeš `cd N` in pritisneš `tab`, ukazna vrstica samo dopolni preostanek imena. To ne bo delovalo, če je v imeniku več kot ena datoteka, ki se začne z "N". Pritisni `tab` dvakrat, če želiš, da se ti izpišejo vse možnosti.

* * *

### Ustvarjanje imenika

Kako pa bi ustvarili nov imenik? Recimo takole:

    $ mkdir vaja
    

Windows:

    > mkdir vaja
    

Ta ukaz bo naredil nov imenik z imenom `vaja` znotraj našega trenutnaga imenika. To lahko preveriš tako, da vpišeš ukaz `ls` oziroma `dir`, ali pa greš pogledat v imenik s pomočjo programa Finder oziroma Explorer! Poskusi :)

> UPORABEN namig: Če nočeš vedno znova vpisovati istega ukaza, lahko s pomočje pritiskanja puščic `gor` in `dol` na tipkovnici, pregledaš nedavno uporabljene ukaze.

* * *

### Vaja!

Zate imamo majhen izziv: v novo ustvarjenem imeniku `vaja` ustvari imenik z imenom `test`. Uporabi ukaza `cd` in `mkdir`.

#### Rešitev:

    $ cd vaja
    $ mkdir test
    $ ls
    test
    

Windows:

    > cd vaja
    > mkdir test
    > dir
    05/08/2014 07:28 PM <DIR>      test
    

Čestitke! :)

* * *

### Čistka :)

Ustvarjenih imenikov ne potrebujemo več, zato jim odstranimo.

Za začetek se pomaknimo nazaj v nadrejeni imenik:

    $ cd ..
    

Windows:

    > cd ..
    

Z ukazom `..`, ki sledi ukazu `cd`, se torej premaknemo iz trenutnega imenika v nadrejei imenik (to je imenik, ki naš trenutno imenik vsebuje).

Preverimo našo lokacijo:

    $ pwd
    /Users/ana/Desktop
    

Windows:

    > cd
    C:\Uporabniki\ana\Namizje
    

Pripravljeni smo za odstranitev imenika `vaja`:

> **Pozor**: Odstranjevanje datotek in imenikov s pomočjo ukazov `del`, `rmdir` in `rm` je nepreklicno, kar pomeni, da z njimi datoteke oziroma imenike *izbrišemo za vedno*! Pri uporabi omenjenih ukazov bodi zato zelo previdna.

    $ rm -r vaja
    

Windows:

    > rmdir /S vaja
    vaja, Are you sure <Y/N>? Y
    

Končano! Preverimo imenik:

    $ ls
    

Windows:

    > dir
    

### Izhod

Zaenkrat smo se naučili dovolj, zato lahko ukazno vrstico zapremo. Naredimo to kot pravi hekerji! :)

    $ exit
    

Windows:

    > exit
    

Super! :)

## Povzetek

Tu je še povzetek nekaterih uporabnih ukazov:

| Ukaz (Windows) | Ukaz (Mac OS/ Linux) | Opis                                                   | Primer                                            |
| -------------- | -------------------- | ------------------------------------------------------ | ------------------------------------------------- |
| exit           | exit                 | zapri okno                                             | **exit**                                          |
| cd             | cd                   | spremeni imenik                                        | **cd test**                                       |
| dir            | ls                   | izpiši imenike/datoteke, vsebovane v trenutnem imeniku | **dir**                                           |
| copy           | cp                   | kopiraj datoteko                                       | **copy c:\test\test.txt c:\windows\test.txt** |
| move           | mv                   | premakni datoteko                                      | **move c:\test\test.txt c:\windows\test.txt** |
| mkdir          | mkdir                | ustvari nov imenik                                     | **mkdir testniimenik**                            |
| del            | rm                   | izbriši imenik/datoteko                                | **del c:\test\test.txt**                        |

To je le nekaj osnovnih ukazov za ukazno vrstico. Drugih danes ne boš potrebovala.

Če ti je bilo to poglavje zanimivo in bi rada izvedela še kaj več, imaš na strani [ss64.com][1] seznam vseh ukazov za vse operacijske sisteme.

 [1]: http://ss64.com

## Pripravljena?

Začnimo s programskim jezikom Python!