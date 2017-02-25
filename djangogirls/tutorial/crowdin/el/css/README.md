# CSS - κάνε τα πράγματα όμορφα!

Το blog μας φαίνεται ακόμα αρκετά άσχημο, έτσι δεν είναι; Ωρα να το κάνουμε όμορφο! Γι'αυτή τη δουλειά θα χρησιμοποιούμε τη CSS.

## Τι είναι η CSS;

Η CSS (Cascading Style Sheets-Διαδοχικά Φύλλα Στυλ) είναι μια γλώσσα που χρησιμοποιείται για να περιγράψει την εμφάνιση και μορφοποίηση μιας ιστοσελίδας που έχει συνταχθεί σε γλώσσα σήμανσης (όπως η HTML). Δες το σαν μακιγιάζ για την ιστοσελίδα μας ;).

Αλλά δεν θέλουμε να ξεκινήσουμε από το μηδέν, πάλι, σωστά; Θα χρησιμοποιούμε, για ακόμη μια φορά, κάτι που έχει ήδη δημιουργηθεί από άλλους προγραμματιστές παλαιότερα και διατείθεται στο διαδίκτυο για δωρεάν χρήση. Όπως ξέρουμε, δεν είναι πολύ ευχάριστο να επανεφευρίσκεις τον τροχό από την αρχή.

## Ας χρησιμοποιήσουμε το Bootstrap!

Το Bootstrap είναι μια από τις πιο δημοφιλή εργαλειοθήκες (framework) HTML / CSS που αποσκοπούν στην εύκολη και γρήγορη ανάπτυξη καλαίσθητων ιστοσελίδων: http://getbootstrap.com/

Γράφτηκε αρχικά από προγραμματιστές που εργάστηκαν για το Twitter, και σήμερα συνεχίζει να αναπτύσεται από εθελοντές από όλο τον κόσμο.

## Εγκατάσταση του Bootstrap

Για να εγκαταστήσεις το Bootstrap, πρέπει να προσθέσεις τις παρακάτω γραμμές μέσα στο `<head>` που βρίσκεται στο αρχείο `.html` (`blog/templates/blog/post_list.html`):

    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    

Αυτό δεν προσθέτει καινούργια αρχεία στο project σου. Συνδέει μόνο αρχεία που υπάρχουν ήδη στο διαθέσιμα στο Διαδίκτυο. Εμπρος λοιπόν, άνοιξε ξανά ή ανανέωσε τη σελίδα σου. Ιδού!

![Figure 14.1][1]

 [1]: images/bootstrap1.png

Δείχνει ήδη πολύ καλύτερο!

## Στατικά αρχεία στο Django

Τέλος, ας ρίξουμε μια πιο προσεκτική ματιά στα λεγόμενα **στατικά αρχεία**. Στατικά αρχεία είναι όλη η CSS και εικόνες σας -- αρχεία που δεν είναι δυναμικά, έτσι το περιεχόμενό τους δεν αλλάζει ανάλογα με διαφορετικές συνθήκες και είναι πάντα το ίδιο για κάθε χρήστη.

### Πού βρίσκονται τα στατικά αρχεία στο Django

Όπως είδες όταν τρέξαμε `collectstatic` στον server, το Django ξέρει ήδη πού να βρει τα στατικά αρχεία από το ενσωματωμένο "admin" app. Τώρα μένει απλώς να προσθέσουμε μερικά στατικά αρχεία για το δικό μας app, `blog`.

Για να το κάνουμε αυτό πρέπει να δημιουργήσουμε ένα φάκελο με το όνομα `static` μέσα στο φάκελο του app blog:

    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    └── mysite
    

To Django θα βρει αυτόματα οποιουσδήποτε φακέλους με το όνομα "static" μέσα σε οποιουσδήποτε φακέλους των apps σας και θα είναι σε θέση να χρησιμοποιήσει τα περιεχόμενά τους ως στατικά αρχεία.

## Το πρώτο CSS αρχείο σας!

Ας δημιουργήσουμε ένα CSS αρχείο τώρα, για να προσθέσετε το δικό σας στυλ στην ιστοσελίδα σας. Δημιουργήστε έναν νέο κατάλογο που ονομάζεται `css` μέσα στο `static` κατάλογο. Στη συνέχεια, δημιουργήστε ένα νέο αρχείο που ονομάζεται `blog.css` μέσα σε αυτόν τον κατάλογο `css`. Είστε έτοιμη;

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css
    

Ώρα να γράψουμε λίγη CSS! Άνοιξε το αρχείο `blog/static/css/blog.css` στον επεξεργαστή.

Δε θα αφιερώσουμε πολύ χρόνο εδώ στο πώς μπορούμε να προσαρμόσουμε και να μάθουμε τη CSS, επειδή είναι αρκετά απλή και μπορείς να τη μάθεις μόνη σου μετά από αυτό το σεμινάριο. Συστήνουμε να χρησιμοποιήσεις το πρόγραμμα εκμάθησης [Codeacademy HTML & CSS course][2] για να μάθεις όλα όσα χρειάζονται για το πώς να κάνεις τις σελίδες σου όμορφες με τη CSS.

 [2]: http://www.codecademy.com/tracks/web

Αλλά ας δοκιμάσουμε μερικά πράγματα. Ίσως θα μπορούσαμε να αλλάξουμε το χρώμα του τίτλου της σελίδας μας; Για να καταλάβουν τα χρώματα, οι υπολογιστές χρησιμοποιούν ειδικούς κώδικες. Οι κώδικες αυτοί ξεκινούν με το σύμβολο `#` και ακολουθούντα από 6 λατινικά γράμματα (A-F) και αριθμούς (0-9). Μπορείς να βρεις αυτούς τους χρωματικούς κώδικες για παράδειγμα εδώ: http://www.colorpicker.com/. Μπορείς επίσης να χρησιμοποιήσεις [προκαθορισμένα χρώματα][3] με το αγγλικό όνομά τους, όπως το `red` (κόκκινο) και το `green` (πράσινο).

 [3]: http://www.w3schools.com/cssref/css_colornames.asp

Στο αρχείο `blog/static/css/blog.css` πρέπει να προσθέσεις τον παρακάτω κώδικα:

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