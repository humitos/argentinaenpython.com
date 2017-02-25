> Ova sekcija je bazirana na tutorialu napravljedn od strane Geek Girl Carrots (http://django.carrots.pl/)

Django je napisan u Python-u. Potreban nam je Python da bismo bilo šta uradili u Djangu. Počnimo sa njegovom instalacijom! Želeli bismo da instalirate Python 3.4, pa bi trebalo da nadogradite stariju verziju ukoliko je već imate instaliranu.

### Windows

Python za Windows možete skinuti sa veb-sajta https://www.python.org/downloads/release/python-343/. Nakon što skinete ***.msi** fajl, pokrenite ga (dvokliknite na njega) i ispratite instrukcije. Bitno je zapamptiti putanju (direktorijum) gde ste instalirale Python. Trebaće nam kasnije!

Jedna stvar na koju treba obratiti pažnju: na drugom prozor instalacionog mađioničara, markirajte "Customize", odskrolujte dole i izaberite opciju "Add python.exe tp the path", kao što je prikazano ovde:

![Nemojte zaboraviti da dodate Python na Path](../python_installation/images/add_python_to_windows_path.png)

### Linux

Velika je verovatnoća da već imate instaliran Python. Možete to proveriti (kao i verziju koju imate) ako otvorite konzolu i ukucate sledeću komandu:

    $ python3 --version
    Python 3.4.3
    

Ako nemate instaliran Python, ili imate neku drugu verziju, instalacija se vrši na sledeći način:

#### Debian ili Ubuntu

Ukucajte ovu komandu u konzolu:

    $ sudo apt-get install python3.4
    

#### Fedora (do verzije 21)

Unesite sledeću komandu u konzolu:

    $ sudo yum install python3.4
    

#### Fedora (22+)

Unesite sledeću komandu u konzolu:

    $ sudo dnf install python3.4
    

### OS X

Idite na veb-sajt https://www.python.org/downloads/release/python-343/ i skinite instalacioni fajl Python-a:

  * Skinite *Mac OS X 64-bit/32-bit instalacioni fajl*,
  * Dvokliknite na *python-3.4.3-macosx10.6.pkg* da biste pokrenuli instalaciju.

Uverite se da je instalacija uspešno prošla utvaranjem *terminala* i pokretanjem `pyhon3` komande:

    $ python3 --version
    Python 3.4.3
    

* * *

Ako imate bilo kakvih sumnji ili ako nešto nije prošlo kako treba - molim vas, pitajte vašeg coach-a! Ponekad stvari ne prođu glatkoi bolje je potražiti pomoć od nekog iskusnijeg.