# Kako internet radi

> Ovo poglavlje je inspirisano govorom "Kako internet radi" koji je održala Jessica McKellar (http://web.mit.edu/jesstess/www/).

Sigurni smo da internet koristite svakog dana. Ali da li zaista znate šta se dešava kada upišete adresu poput http://djangogirls.org u vaš brauzer i pritisnete `enter`?

Prva stvar koju treba da shvatite je da je svaki veb-sajt samo gomila fajlova na hard disku. Baš kao i vaši filmovi, muzika ili slike. Međutim, jedna stvar je jedinstvena za veb-sajtove: svi uključuju kompjuterski kod zvan HTML.

Ako niste upoznate sa programiranjem, u početku može biti teško razumeti HTML, ali ga vaši brauzeri (poput Chrome-a, Safari-a, Firefox-a itd.) vole. Brauzeri su dizajnirani tako da razumeju ovaj kod, prate njegova uputsva i prikazuju ove fajlove od kojih se vaš veb-sajt sastoji, baš na način kako želite.

Kao i sa svakim fajlom, HTML fajlove treba čuvati negde na hard disku. Za internet se koriste posebni, jaki kompjuteri koje zovemo *serveri*. Oni nemaju ekran, miš ili tastaturu, pošto im je glavna namera čuvanje podataka koje će servirati. Zato se i zovu *serveri* -- zato što vas *služe* podacima.

OK, ali želite da znate kako internet izgleda, zar ne?

Nacrtali smo vam sliku! Izgleda ovako:

![Slika 1.1][1]

 [1]: images/internet_1.png

Potpuni nered, zar ne? Zapravo, to je mreža povezanih mašina koje smo gore zvali *serverima*. Stotine hiljada mašina! Mnogo, mnogo kilometara kabla širom sveta! Možete posetiti Submarine Cable Map veb-sajt (http://submarinecablemap.com) da vidite koliko je ova mreža komplikovana. Evo jedne slike ekrana sa tog veb-sajta:

![Slika 1.2][2]

 [2]: images/internet_3.png

Fascinantno, zar ne? Ali, očigledno, nije moguće imati žicu izmeću svih mašina povezanih na internet. Dakle, da bi se došlo do mašine (na primer, one gde se čuva http://djangogirls.org), potrebno je da prosledimo zahtev preko puno, puno, različitih mašina.

To izgleda ovako:

![Slika 1.3][3]

 [3]: images/internet_2.png

Zamislite da kada ukucate http://djangogirls.org, pošaljete pismo gde piše: "Dragi Django Girls, želim da vidim djangogirls.org veb-sajt. Molim vas, pošali te mi ga!"

Vaše pismo ide do pošte najbliže vama. Zatim ide do još jedne koja je malo bliža primaocu, zatim do još jedne, i još jedne dok ne bude dostavljno na svoju destinaciju. Jedina jedinstvena stvar je da kada šaljete mnogo pisama (*pakete podataka*) na isto mesto, oni idu kroz skroz različite pošte (*rutere*). Ovo zavisi od načina na koji se isporučuju u svakoj pošti.

![Slika 1.4][4]

 [4]: images/internet_4.png

Da, zaista je tako jednostavno. Pošaljete poruke i očekujete neki odgovor. Naravno, umesto papira i olovke, koriste se bajtovi podataka, ali ideja je ista!

Umesto adrese koja se sastoji od naziva ulice, grada, poštanskog broja i naziva zemlje, koristimo IP adrese. Vaš računar prvo pita DNS (Domain Name System) da prevede djangogirls.org u IP adresu. Pvo je pomalo nalik na stare telefonske imenike gde ste mogli po imenu osobe koju želite da kontaktirate naći njen broj telefona i adresu.

Kada pošaljete pismo, ono ima određene osobine koje omogućavaju ispravnu isporuku: adresu, markicu itd. Koristite i jezik koji primalac razume, zar ne? Isto važi i za *pakete podataka* koje šaljete da biste videli neki veb-sajt. Koristimo jedan protokol koji se zove HTTP (Hypertext Transfer Protocol).

Praktično, kada imate veb-sajt, potrebno je da imate *server* (mašinu) gde on živi. Kada *server* primi dolazeći *zahtev* (u pismu), šelje ga nazad veb-sajtu (u drugom pismu).

Pošto je ovo Django tutorial, pitaćete šta Django radi. Kada pošaljete odgovor, ne želite uvek poslati istu stvar svakome. Mnogo je bolje ako vaša pisma specijalno prilagođena svakoj osobno onoj koja vam je baš pisala, zar ne? Django vam pomaže pri kreiranju ovakvih, personalizovanih, interesantnih pisama :).

Dosta priče, vreme je da stvaramo!