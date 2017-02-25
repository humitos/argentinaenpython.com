# Django obrazci

Naš zadnji korak je ustvariti enostaven način za dodajanje in urejanje vnosov. `Admin` v Django je odličen, ampak težko prilagodljiv. `Obrazci` nam omogočajo poljubno oblikovanje našega vmesnika - naredimo lahko skoraj vse, kar želimo!

Z obrazci Django lahko definiramo povsem nov obrazec ali pa ustvarimo `ModelForm`, ki vnos v obrazec shrani v model.

To pa je naravnost to, kar želimo storiti: ustvarili bomo obrazec za našo objavo - `Post`.

Kot vsi ključni deli ogrodja Django so tudi obrazci v svoji datoteki: `forms.py`.

V imeniku `Blog` ustvarimo datoteko s tem imenom.

    blog
       └── forms.py
    

Oprite datoteko in vtipkajte sledečo kodo:

    python
    from django import forms
    
    from .models import Post
    
    class PostForm(forms.ModelForm):
    
        class Meta:
            model = Post
            fields = ('title', 'text',)
    

Najprej uvozimo obrazce Django (`from django import forms`) in nato pričakovano naš model za `Post` (`from .models import Post`).

Kot ste najbrž že uganili je `PostForm` ime našega obrazca. Django mora vedeti, da je ta obrazec `ModelForm` (Django v ozadju izvede nekaj čarovnije) - za to skrbi `forms.ModelForm`.

Nato definiramo `class Meta`, kjer določimo model, ki bo podlaga za naš obrazec (`model = Post`).

Na koncu še določimo polje oziroma polja, ki jih bodo v našem obrazcu. Mi želimo imeti le `title` in `text` - `author` bo oseba, ki je trenutno prijavljena (ti!), datum, torej `created_date`, pa naj bo samodejno nastavljen na datum, ko smo napisali objavo (kar v naši kodi). Drži?

To je vse! Edino kar nam sedaj še preostane je, da obrazec uporabimo v *view* in ga prikažemo v predlogi.

Ponovno bomo ustvarili: povezavo do strani, URL, view in predlogo.

## Povezava do strani z obrazcem

Čas je da odpremo `blog/templates/blog/base.html`. Dodali bomo elemnt `div`, ki ga bomo poimenovali `page-header`:

    html
    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    

Našo funkcijo view bomo poimenovali `post_new`.

Vaša datoteka html sedaj izgleda tako:

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
                <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
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
    </html>
    

Sedaj ste shranili in osvežili stran na naslovu http://127.0.0.1:8000 in ponovno se je pojavila dobro znana `NoReverseMatch`.

## URL

Odprite `blog/urls.py` in dodajte to vrstico:

    python
        url(r'^post/new/$', views.post_new, name='post_new'),
    

Vaša koda je seda:

    python
    from django.conf.urls import include, url
    from . import views
    
    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
        url(r'^post/new/$', views.post_new, name='post_new'),
    ]
    

Če osvežite stran, se vam pojavi `AttributeError`, ker še nismo implementirali `post_new`. Dajmo to popravit.

## post_new view

Odprite datoteko `blog/views.py` in vpišite spodnje vrstice skupaj z vrsticami `from`:

    python
    from .forms import PostForm
    

in našo funkcijo *view*:

    python
    def post_new(request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    

Če želite ustvariti nov obrazec `Post`, moramo zagnati `PostForm()` in ga posredovati predlogi. K tej funkciji *view* se bomo še vrnili, ampak zaenkrat na hitro narediti predlogo za obrazec.

## Predloga

Ustvariti v imeniku `blog/templates/blog` ustvarite datoteko `post_edit.html`. Da bo obrazec deloval, moramo narediti naslednje:

*   prikazati moramo obrazec. To lahko storimo tako, da dodamo `{% raw %}{{ form.as_p }}{% endraw %}`.
*   zgornjo vrstico je potrebno oviti s HTML oznako za obrazec: `<form method="POST">...</form>`
*   potrebujemo še gumb `Shrani`. Za to uporabimo kar gumb HTML `<button type="submit">Save</button>`
*   in za konec še pred oznako `<form ...>` dodamo `{% raw %}{% csrf_token %}{% endraw %}`. S tem zavarujemo naš obrazec! Django vas bo opozoril, če tega ne boste dodali:

![CSFR Forbidden page][1]

 [1]: images/csrf2.png

Poglejmo si ponovno kako izgleda datoteka HTML `post_edit.htm<0>:</p>

<pre><code>html
{% extends 'blog/base.html' %}

{% block content %}
    <h1>New post</h1>
    <form method="POST" class="post-form">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-default">Save</button>
    </form>
{% endblock %}
`</pre> 
Osvežite stran! To! Vaš obrazec se pravilno prikaže!

![New form][2]

Samo trenutek! Kaj se zgodi, če v polja `title` in `text` vnesete besedilo in pritisnete gumb za shranjevanje?

Nič! Vrne nas na isto stran, našega besedila pa ni nikjer... in nikjer ni nove objave. Kje se je zalomilo?

Odgovor: nikjer. Potrebno bo dopolniti funkcijo *view*.

## Shranjevanje obrazca

Ponovno odprite `blog/views.py`. Naša funkcija `post_new` bi morala izgledati tako:

    python
    def post_new(request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    

Ko pošljemo obrazec, nas funkcija preusmeri nazaj na isto funkcijo, le da je v `request` več podatkov, natančneje v `request.POST` (ime ni povezano z objavo v blogu, post, ampak nakazuje na podatke, ki so posredovani z metodo post, torej "objavljanjem" podatkov). Če ste bili pozorni, ste opazili, da smo v naši HTML datoteki v definicijo obrazca `<form>` vključili spremenljivko `method="POST"`? Vsa polja obrazca so sedaj v `request.POST`. Ne preimenujte `post` (edina druga dovoljena `metoda` je `GET` - žal nimamo časa, da bi se poglobili v razlike).

Naša funkcija *view* mora torej razrešiti dve različni situaciji. Situacija ena: ko prvič obiščemo spletno stran in želimo dobiti prazen obrazec. Situacija dve: kot ponovno kličemo funkcijo *view* s podatki obrazca, ki smo jih vnesli. Da bi naša funkcija pravilno razrešila obe situacijo moramo dodati pogoj (uporabili bomo `if`).

    python
    if request.method == "POST":
        [...]
    else:
        form = PostForm()
    

Zapolnimo pikice `[...]`. Če je uporabljena `metoda` `POST`, želimo ustvariti `PostFomr` s podatki obrazca. Drži? To bomo sedaj storili:

    python
    form = PostForm(request.POST)
    

Mala malica! Sedaj se bomo prepričali, da je obrazec pravilen (vsa zahtevana polja so nastavljena in vsi podatki so pravilni). To storimo s `form.is_valid()`.

Preverimo, ali je obrazec veljaven. Če je, lahko shranimo podatke!

    python
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
    

Opravka imamo z dvema zadevama: obrazec shranimo z `form.save`, dodamo avtorja (ker v `PostForm` nimamo polja `author` in je to polje obvezno!). `commit=False` pomeni, da še ne želimo takoj shraniti model `Post` - najprej želimo dodati avtorja. Največkrat boste uporabili `form.save()` brez `commit=False`. Tukaj pa bomo uporabili prav to. Metoda `post.save()` ohrani spremembe (dodan avtor). Rezultat je nova objava!

Finally, it would be awesome if we can immediatelly go to `post_detail` page for newly created blog post, right? To do that we need one more import:

    python
    from django.shortcuts import redirect
    

Add it at the very beginning of your file. And now we can say: go to `post_detail` page for a newly created post.

    python
    return redirect('blog.views.post_detail', pk=post.pk)
    

`blog.views.post_detail` is the name of the view we want to go to. Remember that this *view* requires a `pk` variable? To pass it to the views we use `pk=post.pk`, where `post` is the newly created blog post!

Ok, we talked a lot, but we probably want to see what the whole *view* looks like now, right?

    python
    def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    

Let's see if it works. Go to the page http://127.0.0.1:8000/post/new/, add a `title` and `text`, save it... and voilà! The new blog post is added and we are redirected to `post_detail` page!

You might have noticed that we are setting publish date before saving the post. Later on, we will introduce a *publish button* in **Django Girls Tutorial: Extensions**.

That is awesome!

## Form validation

Now, we will show you how cool Django forms are. A blog post needs to have `title` and `text` fields. In our `Post` model we did not say (as opposed to `published_date`) that these fields are not required, so Django, by default, expects them to be set.

Try to save the form without `title` and `text`. Guess, what will happen!

![Form validation][3]

Django is taking care of validating that all the fields in our form are correct. Isn't it awesome?

> As we have recently used the Django admin interface the system currently thinks we are logged in. There are a few situations that could lead to us being logged out (closing the browser, restarting the DB etc.). If you find that you are getting errors creating a post referring to a lack of a logged in user, head to the admin page http://127.0.0.1:8000/admin and log in again. This will fix the issue temporarily. There is a permanent fix awaiting you in the **Homework: add security to your website!** chapter after the main tutorial.

![Logged in error][4]

## Edit form

Now we know how to add a new form. But what if we want to edit an existing one? It is very similar to what we just did. Let's create some important things quickly (if you don't understand something, you should ask your coach or look at the previous chapters, since we covered all these steps already).

Open `blog/templates/blog/post_detail.html` and add this line:

    python
    <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    

so that the template will look like:

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        <div class="post">
            {% if post.published_date %}
                <div class="date">
                    {{ post.published_date }}
                </div>
            {% endif %}
            <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
            <h1>{{ post.title }}</h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endblock %}
    

In `blog/urls.py` we add this line:

    python
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    

We will reuse the template `blog/templates/blog/post_edit.html`, so the last missing thing is a *view*.

Let's open a `blog/views.py` and add at the very end of the file:

    python
    def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    

This looks almost exactly the same as our `post_new` view, right? But not entirely. First thing: we pass an extra `pk` parameter from urls. Next: we get the `Post` model we want to edit with `get_object_or_404(Post, pk=pk)` and then, when we create a form we pass this post as an `instance` both when we save the form:

    python
    form = PostForm(request.POST, instance=post)
    

and when we just opened a form with this post to edit:

    python
    form = PostForm(instance=post)
    

Ok, let's test if it works! Let's go to `post_detail` page. There should be an edit button in the top-right corner:

![Edit button][5]

When you click it you will see the form with our blog post:

![Edit form][6]

Feel free to change the title or the text and save changes!

Congratulations! Your application is getting more and more complete!

If you need more information about Django forms you should read the documentation: https://docs.djangoproject.com/en/1.8/topics/forms/

## Security

Being able to create new posts just by clicking a link is awesome! But, right now, anyone that visits your site will be able to post a new blog post and that's probably not something you want. Let's make it so the button shows up for you but not far anyone else.

In `blog/templates/blog/base.html`, find our `page-header` `div` and the anchor tag you put in there earlier. It should look like this:

    html
    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    

We're going to add another `{% if %}` tag to this which will make the link only show up for users that are logged into the admin. Right now, that's just you! Change the `<a>` tag to look like this:

    html
    {% if user.is_authenticated %}
        <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    {% endif %}
    

This `{% if %}` will cause the link to only be sent to the browser if the user requesting the page is logged in. This doesn't protect the creation of new posts completely, but it's a good first step. We'll cover more security in the extension lessons.

Since you're likely logged in, if you refresh the page, you won't see anything different. Load the page in a new browser or an incognito window, though, and you'll see that the link doesn't show up!

## One more thing: deploy time!

Let's see if all this works on PythonAnywhere. Time for another deploy!

*   First, commit your new code, and push it up to Github

    $ git status
    $ git add -A .
    $ git status
    $ git commit -m "Added views to create/edit blog post inside the site."
    $ git push
    

*   Then, in a [PythonAnywhere Bash console][7]:

    $ cd my-first-blog
    $ source myvenv/bin/activate
    (myvenv)$ git pull
    [...]
    (myvenv)$ python manage.py collectstatic
    [...]
    

*   Finally, hop on over to the [Web tab][8] and hit **Reload**.

And that should be it! Congrats :)

 [2]: images/new_form2.png
 [3]: images/form_validation2.png
 [4]: images/post_create_error.png
 [5]: images/edit_button2.png
 [6]: images/edit_form2.png
 [7]: https://www.pythonanywhere.com/consoles/
 [8]: https://www.pythonanywhere.com/web_app_setup/