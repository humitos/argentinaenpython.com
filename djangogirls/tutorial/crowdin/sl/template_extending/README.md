# Razširitev predloge

Še ena lepa stvar, ki jo Django omogoča, je **razširjanje predlog**. Kaj je razširjanje predlog? Razširjanje predlog pomeni, da lahko, na več straneh svoje spletne strani, uporabiš isti del HTML dokumenta.

Na tak način se izognete kopiranju kode v vse datoteke v katerih uporabljate podobne informacije/postavitev. Ko želite kaj spremeniti, to storite samo enkrat!

## Osnovna predloga

Osnovna predloga je najbolj temeljna predloga, iz katere boš kasneje naredila vse ostale strani na svoji spletni strani.

V `blog/templates` ustvari datoteko `base.html`:

    blog
    └───templates
        └───blog
                base.html
                post_list.html
    

Nato jo odpri in vanjo prekopiraj celotno vsebino datoteke `post_list.html`:

    html
    {% load staticfiles %}
    <html>
        <head>
            <title>Django Girls blog</title>
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
            <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
            <link rel="stylesheet" href="{% static 'css/blog.css' %}">
        </head>
        <body>
            <div class="page-header">
                <h1><a href="/">Django Girls Blog</a></h1>
            </div>
    
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
        </body>
    </html>
    

V datoteki `base.html` zamenjaj vsebino značke `<body>` (vse med `<body>` in `</body>`) s temle:

    html
    <body>
        <div class="page-header">
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>
        <div class="content container">
            <div class="row">
                <div class="col-md-8">
                {% block content %}
                {% endblock %}
                </div>
            </div>
        </div>
    </body>
    

Dejansko si vse, kar je med `{% for post in posts %}{% endfor %}`, zamenjala s tole kratko kodo:

    html
    {% block content %}
    {% endblock %}
    

Kaj točno si s tem dosegla? Uporabila si ukaz `block`, ki omogoča vstavljanje HTML kode med ukaza block in endblock. Kodo dobiš iz predlog, ki razširjajo predlogo `base.html`. Ne skrbi, kmalu si bomo to pogledali še na primeru.

Shrani spremembe in ponovno odpri `blog/templates/blog/post_list.html`. Izbriši vso kodo, ki ni v znački body in še `<div class="page-header"></div>`. Datoteka zdaj zgleda takole:

    html
    {% for post in posts %}
        <div class="post">
            <div class="date">
                {{ post.published_date }}
            </div>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
    

Na začetek dodaj:

    {% extends 'blog/base.html' %}
    

{% raw %}To pomeni, da ta predloga razširja predlogo `base.html`. Za konec daj vso kodo (razen pravkar dodane vrstice) med ukaza `{% block content %}` in `{% endblock content %}`. Takole:{% endraw %}

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        {% for post in posts %}
            <div class="post">
                <div class="date">
                    {{ post.published_date }}
                </div>
                <h1><a href="">{{ post.title }}</a></h1>
                <p>{{ post.text|linebreaks }}</p>
            </div>
        {% endfor %}
    {% endblock content %}
    

Končano! Poglej svojo stran in preveri, če vse deluje kot mora :)

> Če se ti je pojavila napaka `TemplateDoesNotExists`, ki reče, da predloga `blog/base.html` ne obstaja in imaš v ukazni vrstici zagnan server, server zaustavi (pritisni Ctrl+C) in ga ponovno zaženi s pomočjo ukaza `python manage.py runserver`.