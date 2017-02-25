# CSS - jadikan ia cantik!

Blog kita masih kelihatan hodoh, betul? Masa untuk menjadikannya cantik! Kami akan menggunakan CSS untuk itu.

## Apakah CSS?

Cascading Style Sheets (CSS) ialah bahasa yang digunakan untuk menggambarkan rupa dan format sesebuah laman sesawang yang ditulis dalam bahasa penanda (seperti HTML). Anggap ia sebagai mekap bagi laman web anda;).

Tetapi kita tidak mahu bermula dari awal, betul? Kita akan, sekali lagi, menggunakan sesuatu yang telah pun dilakukan oleh pengaturcara-pengaturcara lain dan dikeluarkan di Internet secara percuma. You know, reinventing the wheel is no fun.

## Mari kita gunakan Bootstrap!

Bootstrap adalah salah satu rangka HTML dan CSS paling popular untuk membangunkan Laman web yang cantik: http://getbootstrap.com/

Ia telah ditulis oleh pengaturcara yang telah bekerja untuk Twitter dan kini dibangunkan oleh sukarelawan dari seluruh dunia.

## Memasang Bootstrap

Untuk memasang Bootstrap, anda perlu menambah ini di `< head >` dalam fail `.html` (`blog/templates/blog/post_list.html`):

    html
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    

Ini tidak menambah sebarang fail ke dalam projek. Ia hanya menghala ke fail yang wujud di internet. Sekarang, buka laman web anda dan me-refresh halaman. Ini dia!

![Figure 14.1][1]

 [1]: images/bootstrap1.png

Kelihatan lebih cantik!

## Fail Statik dalam Django

Akhir sekali, kita akan melihat dengan lebih dekat kepada **fail-fail statik**. Fail-fail statik adalah semua CSS dan imej--fail yang tidak dinamik, oleh itu, kandungan mereka tidak bergantung kepada konteks permintaan dan akan sama bagi setiap pengguna anda.

### Di mana fail-fail statik diletakkan dalam Django

Seperti yang anda lihat, apabila kita larikan `collectstatic` pada pelayan, Django sudah tahu di mana untuk mencari fail-fail statik untuk aplikasi terbina dalam "admin". Sekarang kita hanya perlu menambah beberapa fail statik untuk aplikasi kita sendiri, `blog`.

Kita melaksanakannya dengan mencipta folder yang dipanggil `statik` di dalam aplikasi blog ini:

    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    └── mysite
    

Django secara automatik akan mencari mana-mana folder yang dipanggil "statik" di dalam mana-mana folder aplikasi anda, dan ia akan dapat menggunakan kandungannya sebagai fail-fail statik.

## Fail CSS anda yang pertama!

Mari kita mencipta fail CSS sekarang, untuk menambah gaya yang tersendiri untuk laman web anda. Cipta satu direktori baru yang dipanggil `css` dalam direktori `statik`. Kemudian cipta fail baru yang dipanggil `blog.css` di dalam direktori `css`. Ready?

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css
    

Masa untuk menulis beberapa CSS! Buka fail `blog/static/css/blog.css` dalam Penyunting kod anda.

Kita tidak akan membincangkan dengan lanjut mengenai menyesuaikan dan mempelajari tentang CSS di sini, kerana ianya cukup mudah dan anda juga boleh belajar sendiri selepas bengkel ini. Kami mengesyorkan melakukan aktiviti ini [Codeacademy HTML & CSS Course][2] untuk mengetahui segala-galanya yang anda perlu tahu tentang membuat laman web anda lebih cantik dengan CSS.

 [2]: http://www.codecademy.com/tracks/web

Tetapi mari kita lakukan sekurang-kurangnya sedikit. Mungkin kita boleh menukar warna header? Untuk memahami warna, komputer menggunakan kod khas. Ia bermula dengan `#` dan diikuti dengan 6 huruf (A-F) dan nombor (0-9). Anda boleh mencari kod warna sebagai contoh di sini: http://www.colorpicker.com/. Anda juga boleh menggunakan [warna-warna yang telah ditetapkan][3], seperti `red` dan `green`.

 [3]: http://www.w3schools.com/cssref/css_colornames.asp

Dalam fail `blog/static/css/blog.css`, anda perlu menambah kod berikut:

    css
    h1 a {
        color: #FCA205;
    }
    

`h1 a` adalah Pilihan CSS. Ini bermakna kita sedang menggunakan gaya tersebut kepada mana-mana unsur `a` dalam elemen `h1` (contohnya apabila kita mempunyai kod seperti: `< h1 >< a href = "" > link < /a >< / h1 >`). Dalam kes ini, kita sedang memberitahunya untuk menukar warna kepada `#FCA205`, iaitu warna oren. Sudah tentu, anda boleh meletakkan warna anda sendiri di sini!

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