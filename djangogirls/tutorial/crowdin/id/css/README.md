# CSS - membuat halaman web menjadi lebih menarik!

Blog yang kita buat masih terlihat jelek, kan? Sekarang waktunya untuk mempercantik tampilannya! Kita akan menggunakan CSS untuk itu.

## Apa itu CSS?

Cascading Style Sheets (CSS) adalah bahasa yang digunakan untuk mengatur tampilan dan pengaturan dari sebuah situs web yang ditulis dalam bahasa markup (seperti HTML). Anggap saja CSS sebagai make-up untuk halaman web kita.

Tetapi kita tidak ingin mulai lagi dari awal, kan? Sekali lagi, kita akan memanfaatkan program yang telah dibuat dan dirilis secara gratis di Internet oleh programmer lain. Kamu tahu? Mengulangi hal sama adalah hal yang tidak menarik.

## Mari kita gunakan Bootstrap!

Bootstrap adalah salah satu framework untuk HTML dan CSS yang paling populer dalam membuat halaman web yang menarik: http://getbootstrap.com/

Bootstrap dibuat oleh programmer yang bekerja untuk Twitter dan sekarang dikembangkan oleh relawan dari seluruh dunia.

## Memasang Bootstrap

Untuk memasang Bootstrap, kamu perlu menambahkan kode berikut ke tag `<head>` di file `.html` (`blog/templates/blog/post_list.html`):

    html
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    

Dua baris di atas tidak menambahkan file apa pun ke proyek Django yang kita buat. Baris tersebut hanya menunjuk file yang ada di Internet. Sekarang, buka website yang telah kita buat dan tekan tombol refresh. Inilah halaman web kita!

![Figure 14.1][1]

 [1]: images/bootstrap1.png

Langsung berubah menjadi lebih indah!

## Static files di Django

Mari kita bahas apa itu **static files**. Yang dimaksud dengan static files adalah semua berkas yang kontennya tidak akan berubah karena adanya permintaan dari pengguna. Contoh static files adalah CSS dan gambar.

### Dimana menyimpan static files untuk Django

Seperti yang anda lihat ketika kita menjalankan `collectstatic` pada server, Django sudah tahu di mana untuk menemukan static files untuk membuat "admin" app. Sekarang kita hanya butuh menambahkan beberapa static files untuk app kita, `blog`.

Kita melakukan itu dengan cara membuat folder bernama `static` didalam blog app:

    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    └── mysite
    

Django akan otomatis menemukan semua folder bernama "static" di dalam semua folder app mu. dan akan dapat di gunakan kontennya sebagai static files.

## File CSS pertama mu!

Mari sekarang buat sebuah file CSS, untuk menambah style ke dalam halaman web mu. Buat sebuah folder bernama `css` di dalam folder `static`. Kemudian buat sebuah file bernama `blog.css` di dalam folder `css`. Ready?

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css
    

Saatnya menulis CSS! Buka file `blog/static/css/blog.css` kedalam teks editor mu.

Kita tidak akan pergi terlalu jauh dalam mengkustomisasi dan belajar tentang CSS di sini, karena cukup mudah dan Anda dapat mempelajari sendiri setelah workshop ini. Kami merekomendasikan untuk melakukan ini [Codeacademy HTML & CSS kursus][2] untuk mempelajari segala sesuatu yang perlu Anda ketahui tentang membuat website anda supaya lebih cantik dengan menggunakan CSS.

 [2]: http://www.codecademy.com/tracks/web

Tapi, mari kita coba. Mungkin kita bisa coba mengubah warna Headernya? Untuk memahami warna, komputer menggunakan kode khusus. Biasanya dimulai dengan `#<0> dan diikuti dengan 6 digiti (A-F) dan angka (0-9). Kamu dapat menemukan contoh kodenya pada link berikut ini: http://www.colorpicker.com/. Kamu juga bisa menggunakan <a href="http://www.w3schools.com/cssref/css_colornames.asp">standar warna<0>, seperti <code>red<code> dan <1>green<1>.</p>

<p>Dalam berkas <code>blog/static/css/blog.css` kamu harus ditambahkan kode seperti berikut:

    css
    h1 a {
        color: #FCA205;
    }
    

`h1 a` adalah selector dalam CSS. Ini berarti bahwa kita menerapkan style keseluruh elemen `a` yang berada didalam elemen `h1`( contoh. ketika kita mempunyai kode seperti berikut: `<h1><a href="">link</a></h1>`). Pada contoh kali ini, kita memberitahukan untuk melakukan perubahan warna menjadi `#FCA205`, yang dimana warna tersebut adalah Jingga. Tentu saja, kamu bisa menempatkan warna mu sendiri disini!

Dalam berkas CSS kita menentukan styles untuk elemen yang berada pada berkas HTML. Elemen tersebut diidentifikasikan berdasarkan nama elemen(misal `a`, `h1`, `body`), atribut `class` atau atribut `id`. Class dan id adalah nama-nama elemen yang kamu berikan sendiri. Class-class mendefinisikan kelompok-kelompok elemen, dan id menunjuk pada elemen khusus. Sebagai contoh, tag berikut ini dapat diidentifikasikan dengan CSS dengan menggunakan nama tag `a`, kelas `external_link`, atau id `link_ke_alamat_wiki`:

    html
    <a href="http://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page">
    

Baca lebih lanjut tentang [CSS Selectors di w3schools][3].

 [3]: http://www.w3schools.com/cssref/css_selectors.asp

Kemudian kita juga perlu memberitahu template HTML kita bahwa kita menambahkan beberapa berkas CSS. Buka file `blog/templates/blog/post_list.html` dan tambahkan baris ini di paling awal :

    html
    {% load staticfiles %}
    

Kita baru saja memuat file statis disini :). Then, between the `<head>` and `</head>`, after the links to the Bootstrap CSS files (the browser reads the files in the order they're given, so code in our file may override code in Bootstrap files), add this line:

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

![Figure 14.2][4]

 [4]: images/color2.png

Nice work! Maybe we would also like to give our website a little air and increase the margin on the left side? Let's try this!

    css
    body {
        padding-left: 15px;
    }
    

Add this to your CSS, save the file and see how it works!

![Figure 14.3][5]

 [5]: images/margin2.png

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