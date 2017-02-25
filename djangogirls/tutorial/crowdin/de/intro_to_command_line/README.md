# Einführung in die Konsole/Kommandozeile

Uuh, aufregend, oder?! In ein paar Minuten wirst du deine erste Zeile Code schreiben :)

**Erstmal stellen wir dir deine neuen Freundin vor: Die Konsole!**

Im Folgenden zeigen wir dir, wie du das schwarze Fenster benutzt, das alle Hackerinnen nutzen. Es sieht vielleicht erstmal etwas unheimlich aus, aber es ist nur ein Programm, das darauf wartet Anweisungen von dir zu bekommen.

> **Hinweis** Bitte beachte, dass wir in dem gesamten Buch die Begriffe "Verzeichnis" und "Ordner" wechselnd gebrauchen aber sie stehen für ein und dasselbe.

## Was ist die die Konsole?

Das Fenster, welches gewöhnlich die **Kommandokonsole** oder **Kommandoleisten-Interface** genannt wird, ist eine Text basierte Applikation zum Betrachten, Bearbeiten und Manipulieren von Dateien auf deinem Computer. Ähnlich wie Windows Explorer oder Finder auf dem Mac aber ohne das grafische Interface. Andere Bezeichnungen dafür sind: *cmd*, *CLI*, *prompt*, *Eingabeaufforderung*, *Kommandozeile*, <0>Konsole</0>, <0>Terminal</0>..

## Öffnen der Konsolenanwendung

Um mit unserem Tutorial zu starten musst du als erstes das Kommandozeilenprogramm starten.

### Windows

Geh ins Start Menü → Alle Programme → Zubehör → Eingabeaufforderung.

### Mac OS X

Programme → Zubehör → Terminal.

### Linux

Wahrscheinlich ist es unter Programme → Zubehör → Terminal, aber das ist von deinem System abhängig. Wenn es nicht da ist google einfach schnell danach :)

## Eingabeaufforderung (Prompt)

Du solltest nun ein weißes oder schwarzes Fenster sehen, das auf deine Anweisungen wartet.

Auf einem Mac oder Linux, siehst du wahrscheinlich `$`, also so:

    $
    

Auf Windows siehst du ein `>` Zeichen, also das hier:

    >
    

Vor jedem Kommando wird dieses Zeichen und ein Leerzeichen vorangestellt, aber du musst das nicht hinschreiben. Dein Computer macht das für dich :)

> Ein kleiner Hinweis: falls du etwas in der Art wie `C:\Users\ola>` oder `Olas-MacBook-Air:~ ola$` sehen solltest, ist das auch 100%ig korrekt. In diesem Tutorial werden wir das Ganze auf das einfachste Minimum herunterbrechen.

## Dein erstes Kommando (YAY!)

Fangen wir mit etwas einfachem an. Schreibe folgenden Befehl:

    $ whoami
    

oder

    > whoami
    

Und dann betätige `Enter`. Dies ist unser Ergebnis:

    $ whoami
    olasitarska
    

Wie du sehen kannst, hat der Computer gerade deinen Benutzernamen ausgegeben. Toll, was?:)

> Versuche jeden Befehl abzuschreiben und nicht zu kopieren und einzufügen. Auf diese Weise wirst du dir mehr merken!

## Grundlagen

Jedes Betriebssystem hat einen geringfügig anderen Bestand an Befehlen für die Kommandozeile, beachte daher die Anweisungen für dein Betriebssystem. Lass uns das ausprobieren.

### Derzeitiges Verzeichnis

Es wäre schön zu sehen, wo wir uns befinden, oder? Lass uns nachsehen. Gibt diesen Befehl in die Konsole ein und bestätige ihn mit `enter`:

    $ pwd
    /Users/olasitarska
    

Wenn du Windows benützt, schreibe folgendes:

    > cd
    C:\Users\olasitarska
    

Du wirst wahrscheinlich etwas Ähnliches auf deinem Gerät sehen. Wenn du die Konsole öffnest, befindest du dich normalerweise im Heimverzeichnis deines Benutzers.

> Hinweis: 'pwd' steht für 'print working directory' (zeige derzeitiges Arbeitsverzeichnis).

* * *

### Anzeigen von Dateien und Unterordnern

Nun, was befindet sich in deinem Verzeichnis? Es wäre toll das herauszufinden. Lass uns mal schauen:

    $ ls
    Anwendungen
    Desktop
    Downloads
    Musik
    ...
    

Windows:

    > dir  Directory of C:\Users\olasitarska 05/08/2014 07:28 PM <DIR> Applications 05/08/2014 07:28 PM <DIR> Desktop 05/08/2014 07:28 PM <DIR> Downloads 05/08/2014 07:28 PM <DIR> Music ...
    

* * *

### Wechseln des Verzeichnisses

Lass uns jetzt zu unserem Desktop-Verzeichnis wechseln:

    $ cd Desktop
    

Windows:

    > cd Desktop
    

Schau, ob das Wechseln des Verzeichnisses funktioniert hat:

    $ pwd
    /Users/olasitarska/Desktop
    

Windows:

    > cd
    C:\Users\olasitarska\Desktop
    

Hier ist es!

> Profi-Tipp: wenn du `cd D` tippst und dann `tab` auf deiner Tastatur drückst, wird die Kommandozeile automatisch den Rest des Namens vervollständigen, wodurch du schneller navigieren kannst. Wenn es mehr als einen Ordner gibt, dessen Name mit "D" beginnt, drücke die `tab`-Taste zweimal um eine Liste der Möglichkeiten anzuzeigen.

* * *

### Erstellen eines Verzeichnisses

Wie wärs damit ein Probeverzeichnis auf deinem Desktop zu erstellen? So kannst du das tun:

    $ mkdir practice
    

Windows:

    > mkdir practice
    

Dieser kleine Befehl erstellt einen Ordner mit dem Namen `practice` auf deinem Desktop. Du kannst nun überprüfen ob er wirklich dort ist indem du auf deinem Desktop nachschaust oder indem du den Befehl `ls` or `dir` ausführst! Versuch es :)

> Profi-Tipp: wenn du dieselben Befehle nicht immer wieder und wieder schreiben willst, verwende die `Pfeil aufwärts`- und `Pfeil abwärts`-Tasten deiner Tastatur um durch die zuletzt verwendeten Befehle zu blättern.

* * *

### Übung!

Eine kleine Herausforderung für dich: erstelle in deinem neu erstellten `practice`-Ordner ein Verzeichnis namens `test`. Verwende dazu die `cd` und `mkdir`-Kommandos.

#### Lösung:

    $ cd practice $ mkdir test $ ls test
    

Windows:

    > cd practice 
    > mkdir test 
    > dir 
    05/08/2014 07:28 PM <DIR>   test
    

Glückwunsch! :)

* * *

### Aufräumen

Wir wollen kein Chaos hinterlassen, also lass uns das bislang Geschaffene wieder löschen.

Zuerst müssen wir zurück zum Desktop wechseln:

    $ cd ..
    

Windows:

    > cd ..
    

Durch Verwendung von `..` mit dem `cd` Kommando wechselst du dein aktuelles Verzeichnis zum übergeordneten Verzeichnis (dies ist das Verzeichnis, dass das aktuelle Verzeichnis enthält).

Schau wo du gerade bist:

    $ pwd
    /Users/olasitarska/Desktop
    

Windows:

    > cd
    C:\Users\olasitarska\Desktop
    

Jetzt ist es an der Zeit dein `practice` Verzeichnis zu löschen:

> **Achtung**: Wenn du Daten mit `del`, `rmdir` oder `rm` löschst, kannst du das nicht mehr rückgängig machen, das bedeutet *die gelöschten Dateien sind für immer weg*! Sei also sehr vorsichtig mit diesem Befehl.

    $ rm -r practice
    

Windows:

    > rmdir /S practice 
    practice, Are you sure <Y/N>? Y
    

Geschafft! Lass uns schauen ob es wirklich gelöscht ist:

    $ ls
    

Windows:

    > dir
    

### Beenden

Das wärs fürs erste. Du kannst nun beruhigt deine Konsole schließen. Lass es uns wie die Hacker machen, okay?:)

    $ exit
    

Windows:

    > exit
    

Cool, was? :)

## Zusammenfassung

Hier ist eine Zusammenfassung einiger nützlicher Kommandos:

| Befehl (Windows) | Befehl (Mac OS / Linux) | Beschreibung                   | Beispiel                                          |
| ---------------- | ----------------------- | ------------------------------ | ------------------------------------------------- |
| exit             | exit                    | Fenster schließen              | **exit**                                          |
| cd               | cd                      | Verzeichnis wechseln           | **cd test**                                       |
| dir              | ls                      | zeige Unterordner/Dateien      | **dir**                                           |
| copy             | cp                      | Datei kopieren                 | **copy c:\test\test.txt c:\windows\test.txt** |
| move             | mv                      | Datei verschieben              | **move c:\test\test.txt c:\windows\test.txt** |
| mkdir            | mkdir                   | erstelle ein neues Verzeichnis | **mkdir testdirectory**                           |
| del              | rm                      | lösche einen Ordner/eine Datei | **del c:\test\test.txt**                        |

Das sind nur sehr wenige der Befehle, welche du in deiner Konsole verwenden kannst, aber du wirst heute nicht mehr brauchen.

Falls du neugierig bist, findest du auf [ss64.com][1] eine vollständige Übersicht über alle Kommandozeilen-Befehle für alle Betriebssysteme.

 [1]: http://ss64.com

## Fertig?

Lass uns mit Python anfangen!