# Hur Internet fungerar

> Detta kapitlet är inspirerat av Jessica McKellars föredrag "How the Internet Works" (http://web.mit.edu/jesstess/www/).

We bet you use the Internet every day. But do you actually know what happens when you type an address like http://djangogirls.org into your browser and press `enter`?

Det första du måste förstå är att en hemsida bara är ett gäng filer sparade på en hårddisk. Precis som dina filmklipp, musik och bilder. Men det finns en sak som är unikt för hemsidor: de innehåller programkod som kallas HTML.

If you're not familiar with programming it can be hard to grasp HTML at first, but your web browsers (like Chrome, Safari, Firefox, etc.) love it. Web browsers are designed to understand this code, follow its instructions, and present these files that your website is made of, exactly the way you want.

Precis som med alla filer måste vi lagra HTML-filer någonstans på en hårddisk. För Internet använder vi speciella kraftfulla datorer som kallas *servrar*. De har ingen skärm, mus eller tangentbord, för deras huvudsyfte är att lagra data och göra den åtkomlig. Det är därför de kallas *servrar* -- för de *serverar* din information.

Okej, men du vill säkert veta hur Internet ser ut, eller hur?

Vi har ritat en bild åt dig! Så här ser det ut:

![Figur 1.1][1]

 [1]: images/internet_1.png

Visst ser det stökigt ut? Egentligen är det ett nätverk av anslutna datorer (ovan nämnda *servers*). Hundratusentals datorer! Många, många mil av kabel runt världen! You can visit a Submarine Cable Map website (http://submarinecablemap.com) to see how complicated the net is. Här är en skärmdump från hemsidan:

![Figur 1.2][2]

 [2]: images/internet_3.png

Visst är det fascinerande? Men självklart går det inte att ha en kabel mellan varje dator som är ansluten till Internet. Så får att nå en dator (till exempel den där http://djangogirls.org finns sparad) måste vi skicka en begäran genom många olika datorer.

Så här ser det ut:

![Figur 1.3][3]

 [3]: images/internet_2.png

Tänk dig att, när du skriver http://djangogirls.org, skickar du ett brev där det står: "Hej Django Girls, Jag vill se hemsidan djangogirls.org. Snälla skicka den till mig!"

Ditt brev går till postkontoret närmast dig. Then it goes to another that is a bit nearer to your addressee, then to another, and another until it is delivered at its destination. The only unique thing is that if you send many letters (*data packets*) to the same place, they could go through totally different post offices (*routers*). This depends on how they are distributed at each office.

![Figur 1.4][4]

 [4]: images/internet_4.png

Ja, så simpelt är det. Du skickar meddelanden och förväntar dig ett svar. Istället för papper och penna använder du såklart bytes av data, men idén är den samma!

Istället för adresser med gatunamn, stad, postkod och land, använder vi IP-adresser. Först frågar din dator en DNS (Domain Name System) om att översätta djangogirls.org till en IP-adress. It works a little bit like old-fashioned phonebooks where you could look up the name of the person you want to contact and find their phone number and address.

När du skickar ett brev behövs några olika saker för att det ska komma fram ordentligt: en adress, frimärke osv. Och så måste du använda ett språk som mottagaren förstår, eller hur? The same applies to the *data packets* you send to see a website. We use a protocol called HTTP (Hypertext Transfer Protocol).

So, basically, when you have a website, you need to have a *server* (machine) where it lives. When the *server* receives an incoming *request* (in a letter), it sends back your website (in another letter).

Eftersom detta är en tutorial för Django, kommer du säkert fråga vad Django gör. När du skickar ett svar, vill du inte alltid skicka samma sak till alla. Det är mycket bättre om dina brev är personliga till personen som precis har skrivit till dig, eller hur? Django hjälper dig att skapa dessa personliga, intressanta brev :).

Nog med prat, dags att skapa något!