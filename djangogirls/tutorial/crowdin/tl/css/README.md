# CSS - gawin nating maganda!

Pangit pa ang ating kasalukuyang blog, hindi ba? Oras na para pagandahin ito! Gagamitin natin ang CSS para riyan.

## Ano ang CSS?

Ang Cascading Style Sheets (CSS) ay isang lenggwahe na ginagamit para ilarawan ang itsura at porma ng mga websites na gumagamit ng markup language tulad ng HTML. Kung ihahambing sa tao, para itong kolorete na nagbibigay-buhay o aliwalas sa mukha.

Pero hindi naman natin gustong gumawa na lang mula sa wala, hindi ba? Muli, tayo ay gagamit ng mga nasimulan na noon ng ibang mga programmers at ibinihagi sa Internet ng libre. Hindi praktikal o masaya ang gumawa ng bagay na nagawa naman na ng iba.

## Gamitin natin ang Bootstrap!

Ang Bootstrap ay isa sa mga pinakasikat na balangkas ng HTML at CSS para sa pagbuo ng mga magagandang websites: http://getbootstrap.com/

Ito ay sinulat ng mga programmers na nagtrabaho sa Twitter at ito ay patuloy na boluntaryong inaalagaan sa buong mundo ng mga indibidwal.

## Install Bootstrap

Para mailagay ang Bootstrap sa iyong proyekto, kailangan mong ilagay ito sa `<head>` ng iyong `.html` file (`blog/templates/blog/post_list.html`):

    html
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    

Wala naman itong maidadagdag na kahit anong file sa iyong proyekto. Gumagawa lamang ito ng panuro sa mga files ng bootstrap na nakalagay na sa Internet noon pa. Tara na, buksan mo na ang iyong website at i-refresh (Ctrl + F5 o F5) ang pahina. Ayan na!

![Figure 14.1][1]

 [1]: images/bootstrap1.png

Gumaganda na siya!

## Static Files sa Django

Finally we will take a closer look at these things we've been calling **static files**. Static files are all your CSS and images -- files that are not dynamic, so their content doesn't depend on the request context and will be the same for every user.

### Where to put static files for Django

As you saw when we ran `collectstatic` on the server, Django already knows where to find the static files for the built-in "admin" app. Now we just need to add some static files for our own app, `blog`.

We do that by creating a folder called `static` inside the blog app:

    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    └── mysite
    

Django will automatically find any folders called "static" inside any of your apps' folders, and it will be able to use their contents as static files.

## Ang iyong unang CSS file!

Gumawa na tayo ng CSS file ngayon, upang mailagay mo naman ang iyong estilo sa iyong magiging web-page. Gumawa ng bagong directory na `css` sa loob ng iyong `static` directory. Pagkatapos, gumawa ka ng bagong file na `blog.css` sa loob nitong `css` directory mo. Handa ka na ba?

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css
    

Time to write some CSS! Open up the `blog/static/css/blog.css` file in your code editor.

Hindi na natin susuyurin ng husto o lalaliman ang usapan sa pag-eestilo ng mga web-page at pag-aaral ng CSS dito, dahil madali naman itong aralin at kayang kaya mo na ito pagkatapos ng ating ginagawa rito. Talagang nirerekomenda namin na subukan mo rin ang [Codeacademy HTML & CSS course][2] upang matutunan mo lahat ng kailangan mong malaman tungkol sa pagpapaganda ng mga websites gamit ang CSS.

 [2]: http://www.codecademy.com/tracks/web

Pero gumawa naman tayo kahit kaunti lang. Siguro maaari nating baguhin ang kulay ng header? Para maunawaan ang mga kulay, ang kompyuter ay sumusunod sa mga special codes o mga numero at letra na nagsisimbolo ng kulay. Nagsisimula ito sa simbolong `#` at sinusundan ng 6 na titik (A-F) at numero (0-9). Halimbawa, maaari kang pumili ng iyong gustong kulay rito: http://www.colorpicker.com/. You may also use [predefined colors][3], such as `red` and `green`.

 [3]: http://www.w3schools.com/cssref/css_colornames.asp

In your `blog/static/css/blog.css` file you should add the following code:

    css
    h1 a {
        color: #FCA205;
    }
    

`h1 a` is a CSS Selector. This means we're applying our styles to any `a` element inside of an `h1` element (e.g. when we have in code something like: `<h1><a href="">link</a></h1>`). In this case, we're telling it to change its color to `#FCA205`, which is orange. Of course, you can put your own color here!

In a CSS file we determine styles for elements in the HTML file. The elements are identified by the element name (i.e. `a`, `h1`, `body`), the attribute `class` or the attribute `id`. Class and id are names you give the element by yourself. Classes define groups of elements, and ids point to specific elements. For example, the following tag may be identified by CSS using the tag name `a`, the class `external_link`, or the id `link_to_wiki_page`:

    html
    <a href="http://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page">
    

Read about [CSS Selectors in w3schools][4].

 [4]: http://www.w3schools.com/cssref/css_selectors.asp

Then, we need to also tell our HTML template that we added some CSS. Open the `blog/templates/blog/post_list.html` file and add this line at the very beginning of it:

    html
    {% load staticfiles %}
    

We're just loading static files here :). Then, between the `<head>` and `</head>`, after the links to the Bootstrap CSS files (the browser reads the files in the order they're given, so code in our file may override code in Bootstrap files), add this line:

    html
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    

We just told our template where our CSS file is located.

Your file should now look like this:

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
    

OK, save the file and refresh the site!

![Figure 14.2][5]

 [5]: images/color2.png

Nice work! Maybe we would also like to give our website a little air and increase the margin on the left side? Let's try this!

    css
    body {
        padding-left: 15px;
    }
    

Add this to your CSS, save the file and see how it works!

![Figure 14.3][6]

 [6]: images/margin2.png

Maybe we can customize the font in our header? Paste this into your `<head>` in `blog/templates/blog/post_list.html` file:

    html
    <link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
    

This line will import a font called *Lobster* from Google Fonts (https://www.google.com/fonts).

Now add the line `font-family: 'Lobster';` in the CSS file `blog/static/css/blog.css` inside the `h1 a` declaration block (the code between the braces `{` and `}`) and refresh the page:

    css
    h1 a {
        color: #FCA205;
        font-family: 'Lobster';
    }
    

![Figure 14.3][7]

 [7]: images/font.png

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

![Figure 14.4][8]

 [8]: images/final.png

Woohoo! Looks awesome, right? The code we just pasted is not really so hard to understand and you should be able to understand most of it just by reading it.

Don't be afraid to tinker with this CSS a little bit and try to change some things. If you break something, don't worry, you can always undo it!

Anyway, we really recommend taking this free online [Codeacademy HTML & CSS course][2] as some post-workshop homework to learn everything you need to know about making your websites prettier with CSS.

Ready for the next chapter?! :)