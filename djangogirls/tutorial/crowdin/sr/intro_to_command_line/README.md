# Uvod u interfejs komandne linije

Uzbudljivo je, zar ne?! Pisaćete svoju prvu liniju koda za samo nekoliko minuta :)

**Upoznaćemo vas sa vašim novim prijateljem: komandnom linijom!**

Naredni koraci će vam pokazati kako da koristite onaj crni prozor koji svi hakeri koriste. Možda će delovati pomalo strašno u početku, ali je to zapravo jedan program koji čeka vaše komande.

> **Napomena** Obratite pažnju na to da ćemokrozovu knjigu koristite termine "direktorijum" i "folder" naizmenično, ali su oni zapravo jedna te ista stvar.

## Šta je komandna linija?

Prozor koji se obično naziva ** komandna linija** ili **interfejs komandne linije** je tekstualno bazirana aplikacija za pregled, rukovanje i manipulaciju fajlovima na vašem kompjuteru. Poput Windows Explorer-a ili Finder-a na Mac-u, ali bez grafičkog interfejsa. Drugi nazivi za komandnu liniju su: *cmd*, *CLI*, *prompt*, *konzola* ili *terminal*.

## Otvorite interfejs komandne linije

Da bismo započeli eksperimentisanje, moramo prvo otvoriti naš interfejs komandne linije.

### Windows

Idite na Start menu → All Programs → Accessories → Command Prompt.

### Mac OS X

Applications → Utilities → Terminal.

### Linux

Verovatno je pod Applications → Accessories → Terminal, ali možda zavisi od vašeg sistema. Ako nije tamo, izguglajte :)

## Prompt

Trebalo bi da vidite beli ili crni prozor koji čeka vaše komande.

Ako koristite Mac ili Linux, verovatno vidite `$`, poput ovoga:

    $
    

Na Windows-u imate znak `>`, poput ovoga:

    >
    

Svaka komanda će imate prefiks koji se sastoji od ovog znaka i jednog razmaka, ali ih ne morate kucate. Vaš računar će to uraditi za vas :)

> Samo mala napomena: ako vidite nešto poput `C:\Users\ola>` ili `Olas-MacBook-Air:~ ola$` pre tog znaka, sve je 100% korektno. U ovom tutorialu ćemo ga maksimalno pojednostaviti.

## Vaša prva komanda (YAY!)

Počnimo od nečeg jednostavnog. Otkucajte komandu:

    $ whoami
    

ili

    > whoami
    

I pritisnite `enter`. Ovo je naš rezultat:

    $ whoami
    olasitarska
    

Kao što vidite, računar je jednostavno ispisao vaše korisničko ime. Strava, zar ne?:)

> Probajte da otkucate komandu, ne da je prekopirate. Tako ćete više toga zapamptiti!

## Osnove

Svaki operativni sistem ima malo drugačiji skup komandi za komandnu liniju, te budite sigurni da pratite instrukcije za vaš operativni sistem. Probajmo sledeće:

### Trenutni direktorijum

Bilo bi lepo znati gde smo sada, zar ne? Pogledajmo. Ukucajte sledeću komandu i pritisnite `enter`:

    $ pwd
    /Users/olasitarska
    

Ako koristite Windows:

    > cd
    C:\Users\olasitarska
    

Verovatno ćete videti nešto slično na vašoj mašini. Kada otvorite komandnu liniju, obično počinjete na home direktorijimu vašeg naloga.

> Napomena 'pwd' znači 'print working directory'.

* * *

### Izlistavanje fajlova i direktorijuma

Šta je sve unutra? Bilo bi interesantno otkriti. Pogledajmo:

    $ ls
    Applications
    Desktop
    Downloads
    Music
    ...
    

Windows:

    > dir
     Directory of C:\Users\olasitarska
    05/08/2014 07:28 PM <DIR>      Applications
    05/08/2014 07:28 PM <DIR>      Desktop
    05/08/2014 07:28 PM <DIR>      Downloads
    05/08/2014 07:28 PM <DIR>      Music
    ...
    

* * *

### Promena tekućeg direktorijuma

Hajdemo sada na Desktop direktorijum:

    $ cd Desktop
    

Windows:

    > cd Desktop
    

Proverimo da li se stvarno promenio:

    $ pwd
    /Users/olasitarska/Desktop
    

Windows:

    > cd
    C:\Users\olasitarska\Desktop
    

Tu je!

> PRO saver: Ako ukucate `cd D` i zatim pritisnete `tab` na vašoj tastaturi, komandna linija će automatski popuniti ostatak naziva tako da možete brže navigirati. Ako postoji više foldera koji počinju slovom "D", pritisnite `tab` dugme dva puta da biste dobili listu opcija.

* * *

### Kreiranje direktorijuma

Šta kažete na to da napravimo direktorijum vežbe radi na vašem desktop-u? Možete to učiniti na sledeći način:

    $ mkdir vezba
    

Windows:

    > mkdir vezba
    

Ova mala komanda kreira folder sa nazivom `vezba` na vašem desktop-u. Možete proveriti da li je zaista tamo ako pogledate vaš desktop ili pokrenete komandu `ls` ili `dir`! Probajte:)

> PRO saver> Ako ne želite da kucate istu komandu ponovo i ponovo, pritisnite `strelicu na gore` i `strelicu na dole` na vašoj tastaturi da biste se kretali kroz skoro unete komande.

* * *

### Vežba!

Mali izazov za vas: u vašem novokreiranom `vezba` direktorijumu napravite direktorijum koji se zove `test`. Koristite `cd` i `mkdir` komande.

#### Rešenje:

    $ cd practice
    $ mkdir test
    $ ls
    test
    

Windows:

    > cd practice
    > mkdir test
    > dir
    05/08/2014 07:28 PM <DIR>      test
    

Čestitamo! :)

* * *

### Čišćenje

Ne želimo da ostavimo haos, pa hajde da izbrišemo sve što smo uradili do ove tačke.

Najpre treba da se vratimo na desktop:

    $ cd ..
    

Windows:

    > cd ..
    

Koristeći `..` sa `cd` komandom zamenjujemo trenutni direktorijum sa roditeljskim (to je onaj koji sadrži trenutni).

Pogledajmo gde smo:

    $ pwd
    /Users/olasitarska/Desktop
    

Windows:

    > cd
    C:\Users\olasitarska\Desktop
    

Sada je vreme da izbrišemo `vezva` direktorijum:

> **Pažnja**: Brisanje fajlova korišćenje `del`, `rmdir` ili`rm` se ne može poništiti, što znači da su *izbrisani fajlovi zauvek izgubljeni*! Dakle, budite jako korisni kada koristite ovu komandu.

    $ rm -r vezba
    

Windows:

    > rmdir /S vezba
    vezba, Are you sure <Y/N>? Y
    

Gotovo! Da bismo bili sigurni da je stvarno izbrisano, proverimo sledeće:

    $ ls
    

Windows:

    > dir
    

### Izlazak

To je to za sada! Možete bezbedno zatvoriti komandnu liniju sadad. Hajde da to uradimo na hakerski način :)

    $ exit
    

Windows:

    > exit
    

Cool, zar ne? :)

## Kratak pregled

Evo pregleda nekih korisnih komandi:

| Komande (Windows) | Komande (Mac OS / Linux) | Opis                            | Primer                                            |
| ----------------- | ------------------------ | ------------------------------- | ------------------------------------------------- |
| exit              | exit                     | zatvara prozor                  | **exit**                                          |
| cd                | cd                       | menja direktorijum              | **cd test**                                       |
| dir               | ls                       | izlistava direktorijume/fajlove | **dir**                                           |
| copy              | cp                       | kopira fajl                     | **copy c:\test\test.txt c:\windows\test.txt** |
| move              | mv                       | premešta fajl                   | **move c:\test\test.txt c:\windows\test.txt** |
| mkdir             | mkdir                    | pravi novi direktorijum         | **mkdir testdirectory**                           |
| del               | rm                       | briše direktorijum/fajl         | **del c:\test\test.txt**                        |

Ovo je samo mali broj komandi koje možete koristiti u vašoj komandnoj liniji, ali danas nećete koristiti ništa više dodatno.

Ako vas zanima, [ss64.com][1] sadrži kompletan pregled svih komandi za sve operativne sisteme.

 [1]: http://ss64.com

## Spremni?

Hajde da se bacimo na Python!