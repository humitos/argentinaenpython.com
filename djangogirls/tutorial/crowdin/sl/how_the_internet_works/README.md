# Kako deluje internet

> To poglavje je povzetek predavanja "How the internet works" Jessice McKellar (http://web.mit.edu/jesstess/www/).

Prepričani smo, da vsakodnevno uporabljaš internet. Ampak ali pravzaprav veš, kaj se zgodi, ko vpišeš naslov, kot je http://djnagogirls.org v svoj brskalnik in pritisneš `enter`?

Si vedela, da je spletna stran zgolj množica datotek, shranjenih na trdem disku ? Povsem enako kot tvoje slike, glasba in filmi. Posebnost datotek, ki sestavljajo spletno stran, je le, da vsebujejo programsko kodo, ki ji rečemo HTML.

Če še nisi nikoli programirala, se to morda sliši malce nenavadno, vendar pa spletni brskalniki (kot so Chrome, Safari, Firefox ipd.), programsko kodo HTML obožujejo. Narejeni so namreč tako, da to kodo razumejo. Razbrati znajo napisane ukaze, ki jih koda vsebuje, in po njihovih navodilih prikazati spletno stran.

Kot vsako datoteko, moramo tudi HTML datoteke shraniti na trdi disk računalnika. Računalnikom, na katerih so shranjene spletne strani, rečemo *strežniki*. Strežniki nimajo ekrana, miške in tipkovnice, saj je njihov glavni namen shraniti podatki in omogočiti, da si z njimi lahko postrežemo. Od tod pride tudi pride njihovo ime *strežniki* -- *postrežejo* nam podatke.

Super, ampak kakšno ima pravzaprav to povezavo s tem, kako deluje internet?

Narisali smo ti sliko! Internet deluje nekako tako:

![Figure 1.1][1]

 [1]: images/internet_1.png

Nenavadno, kajne? Internet je pravzaprav omrežje povezanih računalnikov (prej omenjenih *strežnikov*). Na milijone računalnikov! Ogromna mreža kablov, razpredena po celem svetu! Obiščeš lahko spletno stran Cable Map (http://submarinecablemap.com). Tam boš videla, kako zapletena mreža je internet. Tule je slika iz njihove spletne strani:

![Figure 1.2][2]

 [2]: images/internet_3.png

Fascinantno! Vendar pa jasno tvoj računalnik ne more biti s kabli povezan z vsemi strežniki, ki so povezani na internet. Zato se, da lahko vseeno dostopaš do neke spletne strani, prošnja za povezavo z določenim strežnikom (recimo s tistim, na katerem je shranjena spletna stran http://djangogirls.org), pošlje preko večih ostalih strežnikov, ki jo posredujejo naprej, dokler ne pride do pravega.

Nekako tako:

![Figure 1.3][3]

 [3]: images/internet_2.png

Lahko ti predstavljaš, da s tem, ko vpišeš http://djangogirls.org, pošlješ pismo, na katerem piše, "Dragi strežnik Django Girls, rada bi videla spletno stran djangogirls.org. Pošlji mi jo, prosim!"

To pismo gre na najbližjo pošto, od tod gre na pošto, ki je še nekoliko bližje želenemu naslovu in tako nadaljuje, dokler ne pride do želenega naslova. Edina razlika, če primerjamo to pošiljanje s pošiljanjem v internetu je, da v internetu dejansko pošljemo več pisem (*podatkovnih paketov*) na isto pošto (strežnik). Ta pisma pa gredo lahko do končnega naslova (strežnika) skozi povsem različne pošte (*omrežne usmerjevalnike*). 

![Figure 1.4][4]

 [4]: images/internet_4.png

Ubistvu je vse skupaj zelo preprosto. Pošlješ pismo in čakaš na odgovor. Seveda je pismo v našem primeru podatkovni paket, vendar je ideja povsem enaka!

Namesto običajnega naslova, ki vsebuje naslov ulice, poštno številko in ime države, v računalništvu uporabljamo IP naslov, ki predstavlja naslov računalnika. Tvoj računalnik bo, ko vidi naslov djangogirls.org, s pomočjo sistema DNS (Domain Name System), ta naslov pretvoril v IP. To deluje podobno kot, zdaj že precej zastareli, telefonski imeniki. V njih poiščeš ime osebe in s tem pridobiš njen nalov in številko.

Ko pošlješ pismo, mora to, da uspešno pride na cilj, imeti naslov, znamko,... Napisati pa ga moraš jasno v jeziku, ki ga naslovnik razume. Enako velja za *podatkovne pakete*, ki jih računalnik pošlje, da lahko vidi spletno stran. Za to se uporablja protokol HTTP (Hypertext Transfer Protocol).

Povzemimo vso zgodbo. Če želiš imeti svojo spletno stran, moraš torej datoteke, iz katerih je sestavljena, naložiti na poseben računalnik, ki se mu reče *strežnik*. Ko *strežnik* dobi neko *prošnjo* (v pismu), kot odgovor pošlje spletno stran (v drugem pismu).

Glede na to, da je to vodič o orodju Django, te verjetno zanima, kaj v napisani zgodbi počne Django. Ko strežnik pošlje odgovor na prošnjo, ta odgovor ni nujno vedno enak za vsakega uporabnika. Veliko bolje je, če je ta prošnja (pismo) spreminja glede na to, komu je poslana. To bi znalo priti prav zlasti takrat, ko je odgovor namenjen nekomu, ki si mu odgovor poslal nedolgo nazaj. To zveni smiselno, kajne? Django nam bo pomagal delati tovrstna zanimiva pisma, ki se spreminjajo glede na naslovnika :).

Dovolj dogovorjenja, čas je, da začnemo z delom!