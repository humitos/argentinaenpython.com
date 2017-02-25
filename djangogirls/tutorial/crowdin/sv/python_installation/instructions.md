> This section is based on a tutorial by Geek Girls Carrots (http://django.carrots.pl/)

Django är skrivet i Python. Vi behöver Python för att göra något i Django. Vi börjar med att installera det! Vi vill att du installerar Python 3.4, så om du har en tidigare version måste du uppgradera.

### Windows

Du kan ladda ner Python för Windows från hemsidan https://www.python.org/downloads/release/python-343/. Efter att du laddar ner ***.msi**-filen kör du den (dubbelklicka på den) och följ instruktionerna. Det är viktigt att du kommer ihåg sökvägen (mappen) som du installerar Python i. Den kommer behövas senare!

One thing to watch out for: on the second screen of the installation wizard, marked "Customize", make sure you scroll down and choose the "Add python.exe to the Path" option, as shown here:

![Don't forget to add Python to the Path](../python_installation/images/add_python_to_windows_path.png)

### Linux

Troligen har du redan Python installerat. För att kolla om det är installerat (och vilken version), öppna en terminal och skriv in följande kommando:

    $ python3 --version
    Python 3.4.3
    

If you don't have Python installed, or if you want a different version, you can install it as follows:

#### Debian or Ubuntu

Skriv in följande kommando i terminalen:

    $ sudo apt-get install python3.4
    

#### Fedora (up to 21)

Kör detta kommando i terminalen:

    $ sudo yum install python3.4
    

#### Fedora (22+)

Kör detta kommando i terminalen:

    $ sudo dnf install python3.4
    

### OS X

You need to go to the website https://www.python.org/downloads/release/python-343/ and download the Python installer:

  * Download the *Mac OS X 64-bit/32-bit installer* file,
  * Double click *python-3.4.3-macosx10.6.pkg* to run the installer.

Verifiera installationen genom att öppna terminalen och köra `python3`-kommandot:

    $ python3 --version
    Python 3.4.3
    

* * *

If you have any doubts, or if something went wrong and you have no idea what to do next - please ask your coach! Sometimes things don't go smoothly and it's better to ask for help from someone with more experience.