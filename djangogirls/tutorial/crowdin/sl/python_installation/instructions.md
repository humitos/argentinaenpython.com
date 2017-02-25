> To poglavje temelji na vodiču, ki so ga naredile Geek Girls Carrots (http://django.carrots.pl/)

Orodje Django je napisano v programskem jeziku Python. Vse kar bomo počeli je, da bomo programirali v Pythonu in pri tem uporabljali Django kot pomagalo, da bo vse skupaj šlo hitreje. Za začetek ga namestimo! Namestiti želimo Python 3.4, zato tudi, če že imaš starejšo različico, Python nadgradi na različico 3.4.

### Windows

Python za Windows lahko preneseš iz spletne strani https://www.python.org/downloads/release/python-343/. Ko se datoteka ***.msi** uspešno prenese, jo zaženi (nanjo dvakrat pritisni) in sledi navodilom. Pomembno je, da si zapomniš lokacijo (nadrejeni imenik), v katero je Python namesti. Kasneje jo bomo potrebovali!

Pozorna bodi na opisani korak: v drugem koraku namestitvenega menija izberi "Customize", se pomakne dol in izberi možnost "Add python.exe to the Path", kot je tudi prikazano na spodnji sliki:

![Ne pozabi dodati Pythona v Path](../python_installation/images/add_python_to_windows_path.png)

### Linux

Python je na tvojem računalniku verjetno že nameščen. To preveriš tako, da odpreš ukazno vrstico in vpišeš sledeči ukaz:

    $ python3 --version
    Python 3.4.3
    

Če slučajno še ni nameščen, to narediš takole:

#### Debian ali Ubuntu

Vpiši sledeči ukaz:

    $ sudo apt-get install python3.4
    

#### Fedora (verzija 21 ali starejša)

Vpiši sledeči ukaz:

    $ sudo yum install python3.4
    

#### Fedora (22+)

Vpiši sledeči ukaz:

    $ sudo dnf install python3.4
    

### OS X

Pojdi na spletno stran https://www.python.org/downloads/release/python-343/ in nato:

  * Prenesi datoteko *Mac OS X 64-bit/32-bit*,
  * Dvakrat pritisni na preneseno datoteko *python-3.4.3-macosx10.6.pkg*, da pričneš namestitevo proceduro.

Uspešno namestitev lahko preveriš tako, da odpreš aplikacijo *Terminal* in vpišeš ukaz `python3`:

    $ python3 --version
    Python 3.4.3
    

* * *

Če imaš težave ali pa če česa ne razumeš, za pomoč prosi svojega mentorja! Namestitev se včasih lahko zakomplicira zato je bolje, da za pomoč prosiš nekoga z več izkušnjami.