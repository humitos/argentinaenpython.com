# CSS - gör det tjusigt!

Vår blogg är fortfarande ganska ful, va? Dags att göra det snyggt! Vi använder CSS för det.

## Vad är CSS?

Cascading Style Sheets (CSS) är ett språk som används för att beskriva utseende och formattering av en webbsida skriven i ett markupspråk (som HTML). Tänk make-up för vår webbsida ;).

Men vi vill inte börja om från början igen, eller hur? Vi kommer, än en gång, att använda något som redan har skapats av programmerare och släppts fritt på Internet. Du vet, att återuppfinna hjulet är inte så kul.

## Låt oss använda Bootstrap!

Bootstrap är ett av de mest populära HTML- och CSS-ramverken för att bygga snygga webbsidor: http://getbootstrap.com/

Det skapades av programmerare som arbetade på Twitter och utvecklas nu av frivilliga från hela världen.

## Installera Bootstrap

För att installera Bootstrap behöver du lägga till detta i `<head>` i din `.html`-fil (`blog/templates/blog/post_list.html`):

    html
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    

Detta lägger inte till några filer i ditt projekt. Det bara pekar på filer som finns på Internet. Öppna nu webbsidan och ladda om. Här är den!

![Figur 14.1][1]

 [1]: images/bootstrap1.png

Det ser redan bättre ut!

## Statiska filer i Django

Äntligen ska vi nu ta en närmare titt på dessa saker vi kallat **statiska filer**. Statiska filer är alla dina CSS-filer och bilder -- filer som inte är dynamiska, så deras innehåll beror inte på request kontexten och kommer därför vara likadana för alla användare.

### Vart ska vi lägga statiska filer för Django

Som du såg när vi körde `collectstatic` på servern, vet Django redan var den ska hitta statiska filer för den inbyggda "admin" appen. Nu behöver vi bara lägga till några statiska filer för vår egen app, `blog`.

Vi gör det genom att skapa en mapp kallad `static` i vår blogg app:

    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    └── mysite
    

Django kommer automatiskt att hinna alla mappar kallade "static" i någon av dina app-mappar, och kommer kunna använda dess innehåll som statiska filer.

## Din första CSS-fil!

Nu ska vi skapa en CSS-fil, för att lägga till din egen stil till din webbsida. Skapa en ny mapp kallad `css` i din `static`-mapp. Skapa sen en ny fil som du kallar `blog.css` inne i `css`-mappen. Redo?

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css
    

Dags att skriva lite CSS! Öppna upp filen `blog/static/css/blog.css` i din kod-editor.

Vi kommer inte gå in allt för djupt i anpassningar och att lära sig CSS här, eftersom det är ganska enkelt och du kan lära dig det på egen hand efter denna workshop. Vi rekommenderar verkligen att ta [Codeacademys HTML & CSS kurs][2] för att lära dig allt du behöver veta om att göra dina webbsidor snyggare med CSS.

 [2]: http://www.codecademy.com/tracks/web

Men låt oss göra åtminstone lite grann. Kanske vi kan ändra färgen på headern? För att förstå färger använder datorer speciella koder. De börjar med `#` följt av 6 bokstäver (A-F) och siffror (0-9). Du kan hitta färgkoder som exempel här: http://www.colorpicker.com/. Du kan också använda [fördefinierade färger][3], som `red` och `green`.

 [3]: http://www.w3schools.com/cssref/css_colornames.asp

Lägg till följande i filen `blog/static/css/blog.css`:

    css
    h1 a {
        color: #FCA205;
    }
    

`h1 a` är en CSS Selector. Det betyder att vi applicerar vår stil till alla `a`-element inuti `h1`-element (tex när vi i koden har något i stil med `<h1><a href="">link</a></h1>`). I detta fall säger vi åt den att ändra sin färg till `#FCA205`, vilket är orange. Du kan såklart välja din egen färg här!

I en CSS-fil bestämmer vi stilar för element i HTML-filen. Elementen identifieras med deras elementnamn (tex `a`, `h1`, `body`), med `class`-attributet eller med `id`-attributet. Class och id är namn du själv ger elementet. Class definierar grupper av element, medan id pekar på specifika element. Till exempel, följande tagg kan identifieras i CSS genom dess elementnamn `a`, dess class-attribut `external_link` eller genom dess id `link_to_wiki_page`:

    html
    <a href="http://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page">
    

Läs om [CSS Selektorer hos w3schools][4].

 [4]: http://www.w3schools.com/cssref/css_selectors.asp

Sen måste vi också berätta för vår HTML-mall att vi har lagt till lite CSS. Öppna filen `blog/templates/blog/post_list.html` och lägg till denna rad i början av den:

    html
    {% load staticfiles %}
    

Här läser vi bara in static files :). Sen, mellan `<head>` och `</head>`, efter länkarna till Bootstraps CSS-filer (webbläsaren läser in filerna i den ordning de angivits, så kod i vår fil kan skriva över kod i Bootstraps filer), lägg till följande rad:

    html
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    

Vi berättade just för vår mall var CSS-filen finns.

Filen ska nu se ut såhär:

    html
    {% load staticfiles %}
    <html>
        <head>
            <title>Django Girls blog</title>
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
            <link rel="stylesheet" href="{% static 'css/blog.css' %}">
        </head>
        <body>
            <div>
                <h1><a href="/">Django Girls Blog</a></h1>
            </div>
    
            {% for post in posts %}
                <div>
                    <p>published: {{ post.published_date }}</p>
                    <h1><a href="">{{ post.title }}</a></h1>
                    <p>{{ post.text|linebreaks }}</p>
                </div>
            {% endfor %}
        </body>
    </html>
    

OK, spara filen och ladda om sidan!

![Figur 14.2][5]

 [5]: images/color2.png

Bra jobbat! Kanske skulle vi också vilja ge vår webbsida lite mer luft och öka marginalen på vänstersidan? Låt oss prova!

    css
    body {
        padding-left: 15px;
    }
    

Lägg till detta i CSS-filen, spara filen och se hur det fungerar!

![Figur 14.3][6]

 [6]: images/margin2.png

Vi kanske kan anpassa typsnittet i headern? Kopiera detta till `<head>` i filen `blog/templates/blog/post_list.html`:

    html
    <link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
    

Den här raden kommer importera ett typsnitt kallat *Lobster* från Google Fonts (https://www.google.com/fonts).

Lägg nu till raden `font-family: 'Lobster';` i CSS-filen `blog/static/css/blog.css` innanför deklarations-blocket för `h1 a` (koden mellan måsvingarna, `{` och `}`) och ladda om sidan:

    css
    h1 a {
        color: #FCA205;
        font-family: 'Lobster';
    }
    

![Figur 14.3][7]

 [7]: images/font.png

Toppen!

Som vi nämnde ovan, CSS har ett koncept av klasser, som i princip låter dig namnge en del av HTML-koden och applicera stilar bara till den delen, utan att påverka något annat. Det är superbra om du har två divar, men de används till helt olika saker (som din header och ett inlägg), så du vill inte att de ska se likadana ut.

Nu kan vi börja namnge delar av vår HTML. Lägg till en klass `page-header` till den `div` som innehåller din header, såhär:

    html
    <div class="page-header">
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>
    

Och lägg till klassen `post` till den `div` som innehåller en blogg-post.

    html
    <div class="post">
        <p>published: {{ post.published_date }}</p>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
    

Vi kommer nu lägga till deklarations-block till olika selektorer. Selektorer som börjar med `.` avser klasser. Det finns mängder av bra guider och förklaringar om CSS på webben som kan hjälpa dig förstå följande kod. Men för stunden, kopiera den bara till filen `blog/static/css/blog.css`:

    css
    .page-header {
        background-color: #ff9400;
        margin-top: 0;
        padding: 20px 20px 20px 40px;
    }
    
    .page-header h1, .page-header h1 a, .page-header h1 a:visited, .page-header h1 a:active {
        color: #ffffff;
        font-size: 36pt;
        text-decoration: none;
    }
    
    .content {
        margin-left: 40px;
    }
    
    h1, h2, h3, h4 {
        font-family: 'Lobster', cursive;
    }
    
    .date {
        float: right;
        color: #828282;
    }
    
    .save {
        float: right;
    }
    
    .post-form textarea, .post-form input {
        width: 100%;
    }
    
    .top-menu, .top-menu:hover, .top-menu:visited {
        color: #ffffff;
        float: right;
        font-size: 26pt;
        margin-right: 20px;
    }
    
    .post {
        margin-bottom: 70px;
    }
    
    .post h1 a, .post h1 a:visited {
        color: #000000;
    }
    

Sen omger vi HTML-koden som visar inlägg med deklarationer av klasser. Ersätt detta:

    html
    {% for post in posts %}
        <div class="post">
            <p>published: {{ post.published_date }}</p>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
    

i filen `blog/templates/blog/post_list.html` med detta:

    html
    <div class="content container">
        <div class="row">
            <div class="col-md-8">
                {% for post in posts %}
                    <div class="post">
                        <div class="date">
                            {{ post.published_date }}
                        </div>
                        <h1><a href="">{{ post.title }}</a></h1>
                        <p>{{ post.text|linebreaks }}</p>
                    </div>
                {% endfor %}
            </div>
        </div>
    </div>
    

Spara filerna och ladda om sidan.

![Figur 14.4][8]

 [8]: images/final.png

Woohoo! Ser awesome ut, eller hur? Koden du just klistrat in är egentligen inte så svår att förstå och du bör kunna förstå det mesta genom att bara läsa den.

Var inte rädd för att mixtra med denna CSS lite och försöka ändra på saker. Om du har sönder något, oroa dig inte, du kan alltid ångra tillbaka det!

Hursomhelst, vi rekommenderar verkligen att du tar denna gratis [HTML & CSS kurs på Codeacademy][2] som en efter-workshop-läxa för att lära dig allt du behöver veta för att göra webbsidor snyggare med CSS.

Redo för nästa kapitel?! :)