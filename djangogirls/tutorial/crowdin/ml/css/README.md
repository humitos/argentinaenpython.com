# CSS - ഭംഗിയാക്കൂ!

നമ്മുടെ ഭ്ലോഗ് ഇപ്പോഴും കാണാന്‍ വലിയ ഭംഗിയില്ല, അല്ലേ? അത് ഭംഗിയാക്കാന്‍ സമയമായി! അതിനു വേണ്ടി നമുക്കു CSS ഉപയോഗിക്കാം.

## എന്താണ് CSS?

HTML പോലെയുള്ള മാര്‍ക്കപ്പ് ഭാഷ ഉപയോഗിച്ച് നിര്‍മിച്ചിട്ടുള്ള ഒരു വെബ്സൈറ്റിന്റെ രൂപവും ഫോര്‍മാറ്റിംഗും വിവരിക്കാന്‍ ഉപയോഗിക്കുന്ന ഒരു ഭാഷയാണ് Cascading Style Sheets അഥവാ CSS. നമ്മുടെ വെബ്പേജിനു വേണ്ടിയുള്ള ഒരു മേക്കപ്പ് കിറ്റ് എന്ന് പരിഗണിച്ചാല്‍ മതി ;).

പക്ഷെ നമുക്ക് വീണ്ടും പൂജ്യത്തില്‍ നിന്നും തുടങ്ങണ്ടല്ലോ, അല്ലേ? അതുകോണ്ട് നമുക്ക് ഇതിനു വേണ്ടി ഒരിക്കല്‍ കൂടി പ്രോഗ്രാമര്‍മാര്‍ മുന്‍ബേ നിര്‍മ്മിച്ചു ഇന്റെര്‍നെറ്റില്‍ സൌജന്യമായി റിലീസ് ചെയ്തിറ്റുള്ള ഒരു സംഭവം ഉപയോഗിക്കാം. ചക്രത്തെ ഒരു തവണ കൂടി കണ്ടുപടിച്ചിട്ട് കാര്യമൊന്നും ഇല്ലല്ലോ.

## നമുക്ക് Bootstrap ഉപയോഗിക്കാം!

ഭംഗിയുള്ള വെബ്സൈറ്റുകള്‍ നിര്‍മിക്കാന്‍ ഉപയോഗിക്കുന്ന ഏറ്റവും ജനപ്രിയം നേടിയ HTML-ഉം CSS-ഉം അടങ്ങുന്ന ഒരു ഫ്രെയിംവര്‍ക്ക് (ചട്ടക്കൂട്) ആണ് Bootstrap: http://getbootstrap.com/

അത് ആദ്യമായി നിര്‍മിച്ചത് ട്വിറ്ററിനു വേണ്ടി ജോലി ചെയ്തിരുന്ന ഒരു കൂട്ടം പ്രൊഗ്രാമ്മര്‍മാര്‍ ആയിരുന്നു. എന്നാല്‍ ഇന്ന് അത് നിര്‍മിച്ചുകൊണ്ടിരിക്കുന്നത് ലോകത്തിന്റെ എല്ലാ ഭാഗത്തുനിന്നുമുള്ള സന്നദ്ധ സേവകരാണ്.

## Bootstrap ഇന്‍സ്റ്റാള്‍ ചെയ്യാം

Bootstrap ഇന്‍സ്റ്റാള്‍ ചെയ്യുന്നതിനായി താഴെ കൊടുത്തിറ്റുള്ളത് നിങ്ങളുടെ `.html` (`blog/templates/blog/post_list.html`) ഫൈലിലെ `<head>`-ല്‍ ചേര്‍ക്കുക:

    html <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"> <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    

ഇത് നിങ്ങളുടെ പ്രൊജക്റ്റിലോട്ട് ഒരു ഫൈലും ചേര്‍ക്കില്ല. മറിച്ച് ഇത് ഇന്റെര്‍നെറ്റിലുള്ള ഒരു കൂട്ടം ഫൈലുകളിലോട്ട് ചൂണ്ടുകയുള്ളു. ചെല്ലൂ, നിങ്ങളുടെ വെബ്സൈറ്റ് തുറന്ന് റിഫ്രെഷ് ചെയ്യൂ. അതാ!

![Figure 14.1][1]

 [1]: images/bootstrap1.png

ഇപ്പോള്‍ തന്നെ ഒന്നു ഭംഗി കൂടിയില്ലേ!

## Django-യിലെ static ഫൈലുകള്‍

ഒടുവില്‍ നമ്മള്‍ **static ഫൈലുകള്‍** എന്നു വിളിച്ചുകൊണ്ടിരിക്കുന്ന ഈ വസ്തുക്കളെ ഒന്നു പരിഷോധിക്കാം. നിങ്ങളുടെ എല്ലാ CSS-ഉം ചിത്രങ്ങളുമാണ് static ഫൈലുകള്‍ - അതായത് ഒരിക്കലും മാറാത്ത ഫൈലുകള്‍. അതിനാല്‍ തന്നെ അവയില്‍ അടങ്ങിയിട്ടുള്ളത് ഒരിക്കലും വരുന്ന റിക്വസ്റ്റിനെ ആശ്രയിച്ചായിരിക്കില്ല. അവ ഏതൊരു ഉപഭോക്താവിനും ഒന്നു തന്നെ ആയിരിക്കും.

### Django-യിലെ static ഫൈലുകള്‍ എവിടെ വെക്കണം

നമ്മള്‍ നേരത്തെ സെര്‍വറില്‍ `collectstatic` റണ്‍ ചെയ്തപ്പോള്‍ നിങ്ങള്‍ ശ്രദ്ധിച്ചില്ലേ, Django-യ്ക് മുന്‍കൂട്ടി അറിയാമായിരുന്നു നമ്മുടെ പ്രൊജക്ട്ടില്‍ അടങ്ങിയിട്ടുള്ള "admin" ആപ്പിന്റെ static ഫൈലുകള്‍ കിട്ടാന്‍ എവിടെ ചെന്നു തപ്പണമെന്ന്. ഇനി നമുക്ക് നമ്മുടെ `blog` ആപ്പിലോട്ട് കുറച്ച് static ഫൈലുകള്‍ ചേര്‍ക്കാം..

അത് ചെയ്യാനായി നമുക്ക് blog ആപ്പിനകത്ത് ഒരു `static` എന്ന് പേരുള്ള ഫോള്‍ഡര്‍ നിര്‍മിക്കാം:

    djangogirls
    ├── blog
    │   ├── migrations 
    │   └── static
    └── mysite
    

നമ്മുടെ എല്ലാ ആപ്പിനും അകത്തുള്ള "static" എന്ന പേരിലുള്ള ഫോള്‍ഡറുകള്‍ തന്നെത്താന്‍ കണ്ടുപിടിക്കുവാനും, അവയില്‍ അടങ്ങിയിട്ടുള്ളവ static ഫൈലുകളായി ഉപയോഗിക്കുവാനും Django-യ്ക് കഴിയും.

## നമ്മുടെ ആദ്യത്തെ CSS ഫൈല്‍!

നമ്മുടെ വെബ് പേജിനു നമ്മുടെ സ്വന്തം സ്ടൈല്‍ കൊടുക്കാനായി നമുക്കൊരു CSS ഫൈല്‍ നിര്‍മിക്കാം. `css` എന്ന് പേരുള്ള ഒരു പുതിയ ടയറക്ട്റി നിങ്ങളുടെ `static` ടയറക്ട്റിക്കകത്ത് നിര്‍മിക്കൂ. എന്നിട്ട് `blog.css` എന്ന് പേരുള്ള ഒരു പുതിയ ഫൈല്‍ ഈ `css` ടയറക്ടറിക്കകത്ത് നിര്‍മിക്കൂ. Ready?

    djangogirls
     └─── blog
          └─── static
               └─── css
                    └─── blog.css
    

കുറച്ച് CSS എഴുതാന്‍ നേരമായി! നിങ്ങളുടെ ടെക്സ്ട് എഡിറ്ററില്‍ `blog/static/css/blog.css` എന്ന ഫൈല്‍ തുറക്കൂ.

ഇപ്പോള്‍ നമ്മള്‍ CSS-നെക്കുറിച്ച് ആഴത്തില്‍ പടിക്കുവാനോ അതില്‍ നിര്‍ദ്ദേശാനുസരണം ഭേദഗതി വരുത്തുവാനോ പോകുന്നില്ല. കാരണം അത് എളുപ്പമാണ്. ഈ വര്‍ക്ക്ഷോപ്പിനു ഷേശം നിങ്ങള്‍ക്കതിനെക്കുറിച്ച് സ്വന്തമായി പടിക്കാം. നിങ്ങളുടെ വെബ്സൈറ്റുകളെ CSS ഉപയോഗിച്ച് ഭംഗിപ്പെടുത്തുന്നതിനെക്കുറിച്ച് കൂടുതല്‍ പഠിക്കാനായി ഞങ്ങള്‍ [Codeacademy HTML & CSS course][2] ശക്തമായി നിര്‍ദേശിക്കുന്നു.

 [2]: http://www.codecademy.com/tracks/web

എന്നാലും നമുക്ക് കുറച്ചൊന്ന് ചെയ്തു നോക്കാം. നമ്മുടെ ഹെഡറിന്റെ നിറമൊന്നു മാറ്റി നോക്കാം? നിറങ്ങളെ മനസ്സിലാക്കുവാനായി കംബ്യൂട്ടറുകള്‍ പ്രത്യേക കോഡുകള്‍ ഉപയോഗിക്കും. അവ `#`-ല്‍ തുടങ്ങി 6 അക്ശരങ്ങളെക്കൊണ്ട് തുടര്‍ന്ന് അവസാനിക്കുന്നു. ആ 6 അക്ശരങ്ങളില്‍ A-F വരെയുള്ള ഏതെങ്കിലും ആല്‍ഫബറ്റുകളോ 0-9 വരെയുള്ള ഏതെങ്കിലും അക്കങ്ങളോ അടങ്ങാം. ഉദാഹരണത്തിനായി ചില നിറങ്ങളുടെ കോഡുകള്‍ ഇവിടെ കാണാം: http://www.colorpicker.com/. നേരിട്ട് നിറങ്ങളുടെ പേരുകള്‍ ഉപയോഗിച്ചാലും തെറ്റില്ല. ഉദാഹരണത്തിന് `red` എന്നോ `green` എന്നോ ഉപയോഗിക്കാം.

നിങ്ങളുടെ `blog/static/css/blog.css` ഫൈലില്‍ താഴെ കാണിച്ചിട്ടുള്ള കോട് ചേര്‍ക്കുക:

    css
    h1 a {
         color: #FCA205;
    }
    

`h1 a`-നെ ഒരു CSS Selector എന്നണ് വിളിക്കുക. ഇതിന്റെ അര്‍തഥം നമ്മുടെ സ്റ്റൈലുകള്‍ ഏതൊരു `h1` എലമെന്റ്റിനു കീഴില്‍ വരുന്ന എല്ലാ `a` എലമെന്റ്റുകളുടെ മുകളിലും ചെലുത്തും എന്നാണ്. (ഉദാ. നമ്മുടെ കോടില്‍ ഇങ്ങനെ ഉണ്ടെങ്കില്‍: `<h1><a href="">link</a></h1>`). ഈ അവസരത്തില്‍, അതിന്റെ നിറം `#FCA205` അഥവാ ഓറഞ്ജ് ആക്കി മാറ്റുവാനാണ് നാം നിര്‍ദേശിക്കുന്നത്. നിങ്ങള്‍ക്ക് ഇഷ്ടമുള്ള നിറം ഉപയൊഗിക്കാം ഇവിടെ!

ഒരു HTML ഫൈലിലുള്ള എലമെന്റ്സിന്റെ സ്ടൈലിനെയാണ് നമ്മള്‍ ഒരു CSS ഫൈലില്‍ നിര്‍ണയിക്കുന്നത്. എലമെന്റ്സിനെ തിരിച്ചറിയുന്നത് അവയുടെ പേര് (ഉദാ. `a`, `h1`, `body`), അല്ലെങ്കില്‍ അവയുടെ ആട്രിബ്യൂട്ട് `class`-ഓ, അല്ലെങ്കില്‍ അവയുടെ ആട്രിബ്യൂട്ട് `id`-യോ ഉപയോഗിച്ചാണ്. Class-ഉം id-യും നിങ്ങള്‍ തന്നെ എലമെന്റ്സിനു കൊടുക്കുന്ന പേരുകളാണ്. ഒരു class ഒരു കൂട്ടം എലമെന്റ്സിനെ വര്‍ണ്ണിക്കുവാന്‍ ഉപയോഗിക്കുന്നതാണ്. എന്നാല്‍ ഒരു id ഒരു പ്രത്യേഗ എലമെന്റിനെയാണ് സൂജിപ്പിക്കുന്നത്. ഉദാഹരണത്തിനായി CSS-ല്‍ താഴെ കൊടുത്തിട്ടുള്ള ട്ടാഗ് തിരിച്ചറിയാന്‍ ആ ട്ടാഗിന്റെ പേരായ `a`-ഓ, അതിന്റെ class-ആയ `external_link`-ഓ, അതിന്റെ id-ആയ `link_to_wiki_page`-ഓ ഉപയോഗിക്കാം:

    html
    <a href="http://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page">
    

[w3schools-ല്‍ CSS-നെ][3] കുറിച്ച് വായിക്കൂ.

 [3]: http://www.w3schools.com/cssref/css_selectors.asp

ഇതിനെല്ലാം ശേഷം നമ്മള്‍ CSS ചേര്‍ത്തിറ്റുണ്ട് എന്ന കാര്യം നമ്മുടെ HTML ടെംപ്ലയ്റ്റിനോട് പറയണം. അതിനായി `blog/templates/blog/post_list.html` എന്ന ഫൈല്‍ തുറന്നതിനു ശേഷം താഴെ കൊടുത്തിട്ടുളള വരി അതിന്റെ ഏറ്റവും മുകളില്‍ ചേര്‍ക്കുക:

    html
    {% load staticfiles %}
    

ഇങ്ങനെയാണ് നമ്മള്‍ static ഫൈലുകള്‍ ലോഡ് ചെയ്യുക :). അതിനു ശേഷം, `<head>`-നും `</head>`-നും ഇടയില്‍, Bootstrap CSS ഫൈലുകളുടെ ലിങ്കുകള്‍ക്ക് ശേഷം (കാരണം ബ്രൌസര്‍ ലിങ്കുകള്‍ യഥാ ക്രമത്തിലാണ് വായിക്കുക. അതിനാല്‍ നമ്മുടെ ഫൈലിലെ കോട് ഒരുപക്ഷേ Bootstrap ഫൈലുകളിലെ കോടിനെ നിഷ്‌ഫലമാക്കിയേക്കാം), താഴെയുളള വരി ചേര്‍ക്കുക:

    html
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    

നമ്മുടെ CSS ഫൈല്‍ എവിടെയാണെന്ന് നമ്മുടെ ടെംപ്ലൈറ്റിനോട് നാം പറഞ്ഞുകൊടുത്ത് കഴിഞ്ഞു.

നമ്മുടെ ഫൈല്‍ കണ്ടാല്‍ താഴെ കൊടുത്തിട്ടുളളത് പോലെ ഇരിക്കണം:

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
    

ഫൈല്‍ സേവ് ചെയത് സൈറ്റ് റിഫ്രഷ് ചെയ്യൂ!

![Figure 14.2][4]

 [4]: images/color2.png

അടിപൊളി! നമ്മുടെ വെബ്സൈറ്റിന് എടതു ഭാഗത്തെ മാര്‍ജിന്‍ കൂട്ടി ഇത്തിരി വിസ്താരം നല്‍കാം? ശ്രമിക്കാം!

    css
    body {
         padding-left: 15px;
    }
    

ഇത് നിങ്ങളുടെ CSS-ലോട്ട് ചേര്‍ക്കൂ, ഫൈല്‍ സേവ് ചെയ്യൂ എന്നിട്ട് വ്യത്യാസം കാണൂ!

![Figure 14.3][5]

 [5]: images/margin2.png

നമ്മുടെ ഹെഡറിന്റെ ഫോണ്ടില്‍ ഒരു ഭേതഗതി വരുത്തി നോക്കിയാലോ? നിങ്ങളുടെ `blog/templates/blog/post_list.html` എന്ന ഫൈലിലെ `<head>`-ലോട്ട് താഴെയുള്ളത് പേസ്റ്റ് ചെയ്യൂ:

    html
    <link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
    

Google Fonts (https://www.google.com/fonts) -ല്‍ നിന്നും *Lobster* എന്ന ഫോണ്ടിനെയാണ് ഈ വരി ഇംപോര്‍ട്ട് ചെയ്യുക.

ഇനി `blog/static/css/blog.css` എന്ന ഫൈലിലെ `h1 a`-ന്റെ ഉള്ളിലുള്ള ഡിക്ലറെശന്‍ ബ്ളോക്കിലോട്ട് ( `{`-ന്റെയും `}`-ന്റെയും ഇടയിലുള്ളത്) ഈ വരി ചേര്‍ക്കൂ: `font-family: 'Lobster';` എന്നിട്ട് പേജ് റിഫ്രഷ് ചെയ്യൂ:

    css
    h1 a {
        color: #FCA205;
        font-family: 'Lobster';
    }
    

![Figure 14.3][6]

 [6]: images/font.png

ഉഷാര്‍!

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