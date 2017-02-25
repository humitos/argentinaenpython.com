# Die Domain

Heroku hat die eine Domain bereitgestellt aber sie ist sehr lang, schwer zu merken und einfach nur eklig. Es wäre doch toll einen Domainnamen zu haben der kürzer und einfacher zu merken wäre, oder?

In diesem Kapitel werden wir die beibringen wie man eine Domain kauft und sie mit Heroku verknüpft!

## Wo registriert man eine Domain?

Eine typische Domain kostet in etwa 15 $ pro Jahr. Es gibt günstigerer und teurere Varianten, je nach Provider. Es gibt viele Firmen von denen du Domains kaufen kannst: eine einfache [Google-Suche][1] wird dir hunderte Vorschläge zeigen.

 [1]: https://www.google.com/search?q=register%20domain

Unser Favorit ist [I want my name][2]. Die werben mit "einfachem Domainmanagement" und es ist wirklich simpel.

 [2]: https://iwantmyname.com/

## Wie registriert man eine Domain auf IWantMyName?

Gehe auf [iwantmyname][3] und tippe eine Domain, die du haben möchtest in das Suchfeld.

 [3]: http://iwantmyname.com

![][4]

 [4]: images/1.png

Du solltest jetzt eine Liste mit all den verfügbaren Domains sehen, die du in das Suchfeld eingegeben hast. Wir du sehen kannst, zeigt dir ein smiley an wenn eine Domain verfügbar ist und ein trauriges Gesicht wenn sie bereits vergeben ist.

![][5]

 [5]: images/2.png

Wir haben beschlossen, `djangogirls.in` zu kaufen:

![][6]

 [6]: images/3.png

Gehe zur Kasse. Du solltest dich jetzt bei IwantMyName anmelden wenn du nicht bereits ein Konto dort hast. Danach gib deine Kreditkarten Informationen ein und kaufe deine Domain!

Im Anschluss klicke auf `Domains` im Menu und wähle deine neu gekaufte Domain aus. Dann suche und klicke auf den `manage DNS records` Link:

![][7]

 [7]: images/4.png

Jetzt musst du dieses Formular finden:

![][8]

 [8]: images/5.png

Fülle es mit den folgenden Details aus: - Hostname: www - Type: CNAME - Value: your domain from Heroku (for example djangogirls.herokuapp.com) - TTL: 3600

![][9]

 [9]: images/6.png

Klicke auf "Hinzufügen" und speichere die Änderungen am unteren Ende.

Es kann einige Stunden dauern bevor deine Domain lauffähig ist, also übe dich in Geduld!

## Konfigurieren der Domain in Heroku

Du musst Heroku angeben, dass du deine eigene Domain benutzen möchtest.

Gehe zum [Heroku Dashboard][10] logge dich mit deinem Heroku Konto ein und wähle deine App aus. Dann gehe in das Einstellungsmenu und füge deine Domain in der `Domains` Sektion ein und speichere deine Änderungen.

 [10]: https://dashboard.heroku.com/apps

Das wars!