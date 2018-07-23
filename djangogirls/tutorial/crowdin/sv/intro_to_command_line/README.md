# Introduktion till kommandotolken

Visst är det spännande!?! Inom bara några minuter kommer du skriva din första rad kod :)

**Låt oss introducera dig till din första nya vän: kommandotolken!**

De följande stegen kommer att visa dig hur du använder det svarta fönstret som alla hackers använder. Det kan se lite läskigt ut i början, men egentligen är det bara ett fönster som väntar på instruktioner från dig.

> **Note** Please note that throughout this book we use the terms 'directory' and 'folder' interchangably but they are one and the same thing.

## Vad är kommandotolken?

The window, which is usually called the **command line** or **command-line interface**, is a text-based application for viewing, handling, and manipulating files on your computer. Much like Windows Explorer or Finder on Mac, but without the graphical interface. Andra namn på kommandotolken är: *cmd*, *CLI*, *prompt*, *konsol* eller *terminal*.

## Öppna kommandotolken

För att börja experimentera måste vi först öppna kommandotolken.

### Windows

Gå till Startmenyn → Alla program → Tillbehör → Kommandotolken.

### Mac OS X

Program → Verktygsprogram → Terminal.

### Linux

Det är antagligen under Applikationer → Tillbehör → Terminal, men det beror på ditt system. Om du inte hittar det, försök googla det :)

## Prompt

Nu borde du sen ett vitt eller svart fönster som väntar på dina kommandon.

Om du använder Mac eller Linux ser du antagligen `$`, precis såhär:

    $
    

På Windows är det ett `>`, såhär:

    >
    

Varje kommando kommer att ha detta tecken framför sig och ett mellanslag, men du behöver inte skriva det. Din dator skriver det åt dig :)

> Just a small note: in your case there may be something like `C:\Users\ola>` or `Olas-MacBook-Air:~ ola$` before the prompt sign and that's 100% correct. I denna tutorial kommer vi förenkla det så mycket som möjligt.

## Ditt första kommando (WOHO!)

Vi börjar med något enkelt. Skriv in detta kommandot:

    $ whoami
    

eller

    > whoami
    

And then hit `enter`. This is our result:

    $ whoami
    olasitarska
    

As you can see, the computer has just printed your username. Neat, huh?:)

> Try to type each command, do not copy-paste. You'll remember more this way!

## Grunderna

Varje operativsystem har lite olika kommandon för terminalen, så följ instruktionerna för ditt operativsystem. Nu kör vi!

### Aktuell katalog

It'd be nice to know where are we now, right? Let's see. Type this command and hit `enter`:

    $ pwd
    /Users/olasitarska
    

Om du använder Windows:

    > cd
    C:\Users\olasitarska
    

You'll probably see something similar on your machine. Once you open the command line you usually start at your user's home directory.

> Notis: 'pwd' står för 'print working directory', alltså 'skriv ut nuvarande mapp'.

* * *

### Lista filer och mappar

Så vad finns här? Det hade varit kul att se. Vi testar:

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

### Ändra aktuell katalog

Now, let's go to our Desktop directory:

    $ cd Desktop
    

Windows:

    > cd Desktop
    

Testa om det verkligen fungerande:

    $ pwd
    /Users/olasitarska/Desktop
    

Windows:

    > cd
    C:\Users\olasitarska\Desktop
    

Det fungerade!

> Tips: om du skriver `cd D` och sen trycker på `tabb` på tangentbordet, kommer konsolen automatiskt fylla i resten av namnet så att du kan navigera snabbare. Om det finns fler än en mappar som börjar med "D" kan du trycka på `tabb` två gånger för att få en lista med alternativ.

* * *

### Skapa katalog

How about creating a practice directory on your desktop? You can do it this way:

    $ mkdir practice
    

Windows:

    > mkdir practice
    

This little command will create a folder with the name `practice` on your desktop. You can check if it's there just by looking on your Desktop or by running a `ls` or `dir` command! Testa! :)

> Tips: Om du inte vill skriva samma kommandon om och om igen, testa att trycka på `uppåtpilen` och `nedåtpilen` för att bläddra bland kommandon som du nyligen har använt.

* * *

### Övning!

Small challenge for you: in your newly created `practice` directory create a directory called `test`. Use `cd` and `mkdir` commands.

#### Lösning:

    $ cd practice
    $ mkdir test
    $ ls
    test
    

Windows:

    > cd practice
    > mkdir test
    > dir
    05/08/2014 07:28 PM <DIR>      test
    

Grattis! :)

* * *

### Städa upp

Vi vill inte lämna det stökigt, så låt oss ta bort allt som vi har gjort hittills.

Först måste vi tillbaka till skrivbordet:

    $ cd ..
    

Windows:

    > cd ..
    

Using `..` with the `cd` command will change your current directory to the parent directory (this is the directory that contains your current directory).

Kolla var du är:

    $ pwd
    /Users/olasitarska/Desktop
    

Windows:

    > cd
    C:\Users\olasitarska\Desktop
    

Now time to delete the `practice` directory:

> **Varning**: Att ta bort filer med `del`, `rmdir` eller `rm` är oåterkalleligt, alltså är *raderade filer borta för alltid*! Så var väldigt försiktig med detta kommandot.

    $ rm -r practice
    

Windows:

    > rmdir /S practice
    practice, Are you sure <Y/N>? Y
    

Klart! För att vara säker på att den verkligen är raderad kan vi kolla med:

    $ ls
    

Windows:

    > dir
    

### Exit

That's it for now! You can safely close the command line now. Let's do it the hacker way, alright?:)

    $ exit
    

Windows:

    > exit
    

Coolt, eller hur? :)

## Sammanfattning

Här är en sammanfattning med några användbara kommandon:

| Kommando (Windows) | Kommando (Mac OS / Linux) | Beskrivning            | Exempel                                           |
| ------------------ | ------------------------- | ---------------------- | ------------------------------------------------- |
| exit               | exit                      | stäng fönstret         | **exit**                                          |
| cd                 | cd                        | ändra mapp             | **cd test**                                       |
| dir                | ls                        | lista kataloger/filer  | **dir**                                           |
| copy               | cp                        | kopiera fil            | **copy c:\test\test.txt c:\windows\test.txt** |
| move               | mv                        | flytta fil             | **move c:\test\test.txt c:\windows\test.txt** |
| mkdir              | mkdir                     | skapa en ny katalog    | **mkdir testkatalog**                             |
| del                | rm                        | ta bort en katalog/fil | **del c:\test\test.txt**                        |

These are just a very few of the commands you can run in your command line, but you're not going to use anything more than that today.

Om du är nyfiken så innehåller [ss64.com][1] en komplett lista med kommandon för alla operativsystem.

 [1]: http://ss64.com

## Redo?

Nu dyker vi ner i Python!