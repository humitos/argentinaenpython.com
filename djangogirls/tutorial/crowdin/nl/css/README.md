# CSS - Maak het mooi!

Ons blog ziet er nogsteeds nogal lelijk uit, toch? Tijd om hem mooi te maken! Hiervoor zullen we CSS gebruiken.

## Wat is CSS?

Cascading Style Sheets (CSS) is een taal die wordt gebruikt om het uiterlijk en de opmaak te beschrijven van een website die in een markup language (zoals HTML) geschreven is. Zie het als make-up voor onze webpagina ;).

Maar we willen niet helemaal opnieuw beginnen, toch? Wij zullen, nogmaals, iets gebruiken dat al gedaan is door programmeurs en gratis vrijgegeven op het Internet. Zo leuk is het namelijk niet om het wiel opnieuw uit te vinden.

## Laten we gebruik maken van Bootstrap!

Bootstrap is een van de meest populaire HTML en CSS frameworks voor het ontwikkelen van mooie websites: http://getbootstrap.com/

Het is geschreven door programmeurs die voor Twitter werkten en wordt tegenwoordig ontwikkeld door vrijwilligers van over de hele wereld.

## Bootstrap installeren

Om Bootstrap te installeren, voeg je deze regels toe aan de `< head >` in je `Html`-bestand (`blog/templates/blog/post_list.html`):

    HTML < link rel = de href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"stylesheet"" >< link rel = de href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"stylesheet"" >
    

Dit voegt geen bestanden aan je project. Het verwijst alleen naar bestanden die bestaan op het internet. Probeer het maar eens: Open je website en vernieuw de pagina. Dit is het resultaat!

![Figure 14.1][1]

 [1]: images/bootstrap1.png

Dit ziet er al een stuk beter uit!

## Statische bestanden in Django

Ten slotte zullen we een kijkje nemen naar de dingen die we **statische bestanden** hebben genoemd. Statische bestanden zijn al je CSS en plaatjes -- bestanden die niet dynamisch zijn, dus hun inhoud hangt niet af van de request context en zal hetzelfde zijn voor elke gebruiker.

### Waar zet je statische bestanden in Django

Zoals u gezien hebt hebben we ` collectstatic ` op de server uitgevoerd, Django weet al waar de statische bestanden voor de ingebouwde "admin" app te vinden zijn. Nu moeten we enkel statische files voor onze eigen applicatie toevoegen, ` blog `.

We doen dit door een folder met de naam `static` aan te maken binnenin de blog applicatie:

    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    └── mysite
    

Django zal automatisch folders genaamd "static" terugvinden binnen elk van uw applicaties, en zal de inhoud hiervan gebruiken als statische bestanden.

## Uw eerste CSS bestand!

Laten we een CSS bestand aanmaken om uw eigen stijl toe te voegen aan de web-pagina. Maak een nieuwe map aan genaamd: `css` binnen uw `static` map. Maak daarna een nieuw bestand genaamd: `blog.css` aan binnen deze `css` map. Ready?

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css
    

Tijd om wat CSS te schrijven! Open het `blog/static/css/blog.css` bestand in uw code verwerker.

We gaan hier niet te diep ingaan op het leren en aanpassen van CSS omdat het best gemakkelijk is om te leren, je kan het zelf leren na deze workshop. We raden het aan om deze [Codeacademy HTML & CSS course][2] te volgen om alles te leren wat u moet weten over het mooi maken van websites met CSS.

 [2]: http://www.codecademy.com/tracks/web

Maar laat ons op z'n minst een beetje doen. Misschien kunnen we de kleur van onze hoofding veranderen? Om kleuren te begrijpen gebruiken computer speciale codes. Deze beginnen met een `#` waar 6 letters (A-F) en nummers (0-9) op volgen. U kan voorbeelden van kleurcodes hier terugvinden: http://www.colorpicker.com/. Men kan ook voorgedefinieerde kleuren gebruiken zoals `red` en `green`.

In uw `blog/static/css/blog.css` zou u de volgende code moeten toevoegen:

    css
    h1 a {
        color: #FCA205;
    }
    

`h1 a` is een CSS Selector. Dit betekent dat we onze stijl toepassen op elk `a` element in een `h1` element (b.v. waneer we iets zoals dit in onze code hebben: `<h1><a href="">link</a></h1>`). In dit geval vertellen we het zijn kleur te veranderen naar `#FCA205`, wat oranje is. Uiteraard kan u uw eigen kleur hier zetten!

In een CSS bestand bepalen we de stijl voor de elementen in het HTML bestand. De elementen worden geïdentificeerd door de element naam (b.v. `a`, `h1`, `body`), het attribuut `class` of het attribuut `id`. Class en id zijn namen die u zelf geeft aan het element. Een class definieert een groep van elementen, en id's verwijzen naar specifieke elementen. Bijvoorbeeld, de volgende tag kan geïdentificeerd worden door CSS door gebruik te maken van de tag naam `a`, de class `external_link`, of het id `link_to_wiki_page`:

    html
    <a href="http://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page">
    

Lees over [CSS Selectors in w3schools][3].

 [3]: http://www.w3schools.com/cssref/css_selectors.asp

Als volgende moeten we ons HTML template vertellen dat we CSS hebben toegevoegd. Open het `blog/templates/blog/post_list.html` bestand en voeg deze lijn toe aan het begin ervan:

    html
    {% load staticfiles %}
    

We zijn gewoon statische bestanden aan het laden hier :). Dan, tussen de `<head>` en `</head>`, na de links naar de Bootsrap CSS bestanden (de browser leest de bestanden in de volgorde waarin ze zijn gegeven, dus onze code kan code in Boostrap bestanden overschrijven), voeg deze lijn toe:

    html
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    

We hebben net aan onze template verteld waar onze CSS staat.

Uw bestand zou er nu zo uit moeten zien:

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
    

Ok, sla het bestand op en vernieuw de site!

![Figure 14.2][4]

 [4]: images/color2.png

Goed werk! Misschien moeten we onze site een beetje ruimte geven en de marge aan de linker kant groter maken? Laten we dit proberen!

    css
    body {
        padding-left: 15px;
    }
    

Voeg dit aan uw CSS toe, en kijk hoe het werkt!

![Figure 14.3][5]

 [5]: images/margin2.png

Misschien kunnen we het lettertype in onze hoofding aanpassen? Plak dit in uw `<head>` in het `blog/templates/blog/post_list.html` bestand:

    html
    <link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
    

Deze lijn zal een lettertype genaamd *Lobster* van Google Fonts (https://www.google.com/fonts) importeren.

Now add the line `font-family: 'Lobster';` in the CSS file `blog/static/css/blog.css` inside the `h1 a` declaration block (the code between the braces `{` and `}`) and refresh the page:

    css
    h1 a {
        color: #FCA205;
        font-family: 'Lobster';
    }
    

![Figure 14.3][6]

 [6]: images/font.png

Great!

As mentioned above, CSS has a concept of classes, which basically allows you to name a part of the HTML code and apply styles only to this part, not affecting others. It's super helpful if you have two divs, but they're doing something very different (like your header and your post), so you don't want them to look the same.

Go ahead and name some parts of the HTML code. Add a class called `page-header` to your `div` that contains your header, like this:

    html
    <div class="page-header">
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>
    

And now add a class `post` to your `div` containing a blog post.

    html
    <div class="post">
        <p>published: {{ post.published_date }}</p>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
    

We will now add declaration blocks to different selectors. Selectors starting with `.` relate to classes. There are many great tutorials and explanations about CSS on the Web to help you understand the following code. For now, just copy and paste it into your `blog/static/css/blog.css` file:

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
    

Then surround the HTML code which displays the posts with declarations of classes. Replace this:

    html
    {% for post in posts %}
        <div class="post">
            <p>published: {{ post.published_date }}</p>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
    

in the `blog/templates/blog/post_list.html` with this:

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
    

Save those files and refresh your website.

![Figure 14.4][7]

 [7]: images/final.png

Woohoo! Looks awesome, right? The code we just pasted is not really so hard to understand and you should be able to understand most of it just by reading it.

Don't be afraid to tinker with this CSS a little bit and try to change some things. If you break something, don't worry, you can always undo it!

Anyway, we really recommend taking this free online [Codeacademy HTML & CSS course][2] as some post-workshop homework to learn everything you need to know about making your websites prettier with CSS.

Ready for the next chapter?! :)