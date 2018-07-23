# Cum funcționează Internetul

> Acest capitol este inspirat de prelegerea „Cum funcționează Internetul” ținută de Jessica McKellar (http://web.mit.edu/jesstess/www/).

We bet you use the Internet every day. But do you actually know what happens when you type an address like http://djangogirls.org into your browser and press `enter`?

Primul lucru pe care trebuie să-l știi este că un website este o grămadă de fișiere salvate pe un hard disk. Just like your movies, music, or pictures. Totuși, paginile web au ceva special: conțin un cod numit HTML.

If you're not familiar with programming it can be hard to grasp HTML at first, but your web browsers (like Chrome, Safari, Firefox, etc.) love it. Web browsers are designed to understand this code, follow its instructions, and present these files that your website is made of, exactly the way you want.

Ca orice fișier, și cele care conțin HTML trebuie stocate undeva, pe un hard disk. În cazul internetului, folosim computere speciale foarte puternice numite *servere*. Ele nu au monitor, mouse sau tastatură pentru că principalul lor scop e să stocheze și să livreze date. De aia se și numesc *servere* -- pentru că ne *servesc* date.

OK, dar probabil vrei să știi cum arată Internetul, așa-i?

Ți-am desenat o schemă! Arată așa:

![Figura 1.1][1]

 [1]: images/internet_1.png

Cam haos, nu? De fapt, este o rețea de computere conectate (*serverele* mai sus menționate). Sute de mii de computere! Mulți, mulți kilometri de cabluri în toată lumea! You can visit a Submarine Cable Map website (http://submarinecablemap.com) to see how complicated the net is. Uite un screenshot de pe site:

![Figura 1.2][2]

 [2]: images/internet_3.png

E fascinant, nu-i așa? Dar, evident, nu e posibil să existe un cablu care să unească toate computerele conectate la Internet. Așa că, pentru a ajunge la un computer (de exemplu la cel pe care e salvat http://djangogirls.org) trebuie să transmitem o cerere prin multe, multe alte computere.

Arată așa:

![Figura 1.3][3]

 [3]: images/internet_2.png

Imaginează-ți că atunci când tastezi http://djangogirls.org, trimiți o scrisoare care zice: „Dragă Django Girls, vreau să văd siteul djangogirls.org. Vă rog să mi-l trimiteți!”

Scrisoarea ta ajunge la oficiul poștal cel mai apropiat. Then it goes to another that is a bit nearer to your addressee, then to another, and another until it is delivered at its destination. The only unique thing is that if you send many letters (*data packets*) to the same place, they could go through totally different post offices (*routers*). This depends on how they are distributed at each office.

![Figura 1.4][4]

 [4]: images/internet_4.png

Da, e atât de simplu. Trimiți mesaje și aștepți răspunsuri. Desigur, în loc de hârtie și pix folosești biți de date, dar ideea e aceeași!

În loc de adrese cu numele străzii, oraș, cod și numele țării, folosim adrese IP. Computerul tău cere de la DNS (Domain Name System) să traducă djangogirls.org într-o adresă IP. It works a little bit like old-fashioned phonebooks where you could look up the name of the person you want to contact and find their phone number and address.

Când trimiți o scrisoare, trebuie să aibă anumite elemente ca să fie expediată corect: adresă, timbru etc. De asemeni, folosești un limbaj pe care destinatarul îl înțelege, nu? The same applies to the *data packets* you send to see a website. We use a protocol called HTTP (Hypertext Transfer Protocol).

So, basically, when you have a website, you need to have a *server* (machine) where it lives. When the *server* receives an incoming *request* (in a letter), it sends back your website (in another letter).

Din moment ce acesta e un tutorial Django, poate vă întrebați ce face Django. Când trimiți un răspuns, nu vrei întotdeauna să trimiți același lucru tuturor. E mult mai bine dacă scrisorile tale sunt personalizate special pentru persoana care tocmai ți-a scris, nu? Django te ajută să creezi aceste scrisori personalizate și interesante :).

Gata cu vorba, e timpul să creăm!