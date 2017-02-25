# Kaj je Django?

Django (*džango*) je brezplačno odprtokodno ogrodje, narejeno v programskem jeziku Python. Ogrodje je skupek že napisanih programov, ki ti pomagajo spletne strani graditi hitreje in lažje.

Kot si opazila, obstajajo določeni gradniki, ki jih ima vsaka spletna stran: sistem za registriranje, plošča za upravljanje spletne strani, kontaktni obrazec, sistem za nalaganje datotek in podobno.

Na našo srečo so se našli ljudje, ki so to ugotovili in so skupaj razvili ogrodja (kot je Django), ki nam nudijo že narejene določene komponente spletne strani.

Ogrodja nas torej rešujejo pred ponovnim odkrivanjem stvari, ki so že dolgo znane oziroma narejene. To jasno precej pospeši postopek razvoja spletnih strani.

## Zakaj potrebujemo ogrodja?

Da bi res dobro razumeli, kaj pravzaprav je Django, si podrobneje oglejmo spletni strežnik. Prva stvar, ki jo mora strežnik vedeti je, da od njega želiš podatke o spletni strani.

Predstavljaj si nabiralnik, ki čaka na prejeta pisma. Točno to počno spletni strežniki. Preberejo pismo in pošljejo odgovor v obliki spletne strani. Ta spletna stran pa mora jasno imeti neko vsebino. Pri ustvarjanju le-te, ti bo pomagal Django.

## Kaj se zgodi, ko nekdo od našega strežnika zahteva spletno stran?

Ko strežnik dobi prošnjo po spletni strani, jo preda Djangu, ta pa poskuša ugotoviti, kaj točno ta prošnja od njega hoče. Najprej pogleda naslov spletne strani in poskuša na podlagi le-tega ugotoviti, kaj se od njega zahteva. Za to je odgovoren del Djanga, ki mu rečemo **razreševalec url naslovov** (naslovu spletne strani se dostikrat reče tudi URL naslov - Uniform Resource Locator). To opravilo je dokaj preprosto - v seznamu poznanih naslovov poskuša najti trenuten URL. Če ga najde, zahtevo posreduje funkciji, ki je odgovorna za prikaz dela spletne strani s tem naslovom (rečemo ji *view*).

Predstavljaj si poštarja, ko dostavlja pismo. Ko hodi po ulici, da bi ga dostavil, mora za vsak naslov preveriti, če je isti, kot tisti na pismu. Ko najde pravi naslov, pismo tam odloži. Django deluje povsem enako!

V funkciji *view* se dogaja tisto, kar nas najbolj zanima: iskanje želenih podatkov v bazi podatkov. Recimo, da želi uporabnik spremeniti svoje podatke, ki jih imamo shranjene v bazi. Funkcija *view* najprej preveri, če je to uporabniku sploh dovoljeno, nato pa, če mu je, nazaj pošlje odgovor, da so bili podatki uspešno spremenjeni. Django ta odgovor le še posreduje brskalniku našega uporabnika.

Zgornji opis je resda malce poenostavljen, vendar pa povzame vse tisto, kar moraš zaenkrat vedeti.

Zdaj vemo dovolj, da se lahko začnemo ukvarjati z razvijanjem aplikacije. Vse ostale pomembne stvari bomo povedali sproti.