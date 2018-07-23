# Form Django

Hal penting terakhir yang akan kita lakukan adalah bagaimana membuat agar user dapat menambah dan mengedit post blog dengan mudah. `Admin` django sudah bagus, tapi sedikit sulit untuk meng-customize dan membuatnya lebih cantik. Dengan `form` kita memiliki keleluasaan besar atas antar muka kita. Hampir segala yang kita bayangkan dapat kita terapkan!

Bagusnya form django adalah bahwa kita dapat mendefinisikannya dengan mudah atau dengan membuat sebuah `ModelForm` yang akan memberikan keluaran form tersebut ke dalam model terkait.

Ini benar-benar merupakan hal yang kita ingin lakukan. Kita akan membuat sebuah form yang kita tujukan untuk model `Post` kita.

Sama seperti tiap bagian penting dari Django, form memiliki file sendiri, yaitu forms.py.

Kita perlu membuat sebuah file dengan nama tersebut di dalam directory `blog`.

    blog
       └── forms.py
    

Oke, mari kita buka file itu, lalu ketik kode berikut:

    python
    from django import forms
    
    from .models import Post
    
    class PostForm(forms.ModelForm):
    
        class Meta:
            model = Post
            fields = ('title', 'text',)
    

Pertama, kita perlu mengimport form Django (</code>form django import forms</code>) dan model `Post` kita (`from .models import Post</0>).</p>

<p><code>PostForm`, sebagaimana yang barangkali anda duga, adalah nama form kita. Kita perlu memberitahu django bahwa form ini adalah sebuah `ModelForm` (Sehingga nanti django akan melakukan beberapa pekerjaan ajaib untuk kita). `form.ModelForm` itu yang bertanggungjawab untuk perkerjaan tersebut.

Selanjutnya, kita memiliki `class Meta` dimana kita memberitahu django model yang mana yang harus digunakan untuk menciptakan form ini (`model=post`).

Akhirnya, kita dapat menyatakan field-field mana yang akan muncul di dalam form kita. Dalam skenario ini kita hanya ingin menampilkan </code>title</code> dan `text`. Sementara `penulis` pastilah orang yang pada saat itu login dan `created_date</0> semestinya akan diset otomatis pada saat kita membuat postingan (Di dalam kode), ya kan?</p>

<p>Begitulah caranya! Yang kita perlu lakukan sekarang adalah menggunakan <em>view</em> dan menampilkannya di dalam sebuah template.</p>

<p>Sekali lagi, kita akan membuat sebuah link menuju halaman tersebut, sebuah URL, sebuah view dan sebuah template.</p>

<h2>Mengarahkan link menuju sebuah halaman dengan Form</h2>

<p>Sekarang saatnya membuka <code>blog/templates/base.html`. Kita akan menambahkan sebuah link di dalam `div` yang diberi nama `page-header`:

    html
    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    

Perhatikan bahwa kita ingin memanggil view baru kita `post_view`.

Setelah menambahkan baris tersebut, file html anda akan tampak seperti ini:

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
    

Setelah disimpan dan merefresh halaman http://127.0.0.1:8000 anda pasti akan melihat tampilan error yang sudah familiar: `NoReverseMatch`, betul?

## URL

Kita buka `blog/urls.py` dan tambahkan baris:

    python
        url(r'^post/new/$', views.post_new, name='post_new'),
    

Dan kode terakhir akan tampak seperti ini:

    python
    from django.conf.urls import include, url
    from . import views
    
    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
        url(r'^post/new/$', views.post_new, name='post_new'),
    ]
    

Setelah merefresh website, kita akan melihat `AttributeError`, karena kita belum memiliki view `post_view`. Mari tambahkan sekarang.

## view post_view

Sekarang kita buka file `blog/views.py` dan tambahkan baris-baris berikut dengan sisa dari baris-baris `rows`: 

    python
    from .forms import PostForm
    

dan *view* kita:

    python
    def post_new(request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    

Untuk membuat sebuah form `post` baru, kita perlu memanggil `PostForm` dan mengirimkannya ke dalam template tersebut. Kita akan kembali ke *view* ini, tapi untuk saat ini, mari kita buat secara cepat sebuah template untuk form tersebut.

## Template

Kita perlu membuat sebuah file </code>post_edit.html</code> di dalam direktori `blog/templates/blog</0>. Untuk membuat sebuah form agar berjalan, kita perlu beberapa hal:</p>

<ul>
<li>kita harus menampilkan form tersebut. Kita dapat melakukannya dengan bentuk <code>{% raw %}{{ form.as_p }}{% endraw %}`.</li> 
*   baris di atas tersebut perlu diletakkan di dalam tag form HTML: `<form method="POST">...</form>`
*   kita perlu sebuah tombol `Save`. Kita lakukan hal itu dengan sebuah tombol HTML: `<button type="submit">Save</button>`
*   dan akhirnya persis setelah tag pembuka `<form ...>` kita perlu menambahkan `{% raw %}{% csrf_token %}{% endraw %}`. Ini sangat penting, karena akan menjadikan form anda aman! Django akan sedikit protes jika anda lupa akan hal ini ketika anda mencoba untuk menyimpan form tersebut:</ul> 
![Halaman terlarang CSFR][1]

Oke, mari kita lihat kode HTML di dalam `post_edit.hrml` seharusnya tampak:

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        <h1>New post</h1>
        <form method="POST" class="post-form">{% csrf_token %}
            {{ form.as_p }}
            <button type="submit" class="save btn btn-default">Save</button>
        </form>
    {% endblock %}
    

Saatnya merefresh web kita! Wow...! Form anda tampil!

![Form Baru][2]

Tapi, tunggu sebentar. Ketika anda mengetik sesuatu di pada field `title` dan `text` lalu mencoba menyimpannya, apa yang terjadi?

Tidak terjadi apa-apa! Kita akan tetap pada halaman yang sama dan teks kita hilang dan tidak ada posting baru ditambahkan. Lalu, apa yang salah?

Jawabnya: tidak ada yang salah. Kita hanya perlu bekerja sedikit lagi pada *view kita*.

## Menyimpan Form

Buka `blog/views.py` sekali lagi. Saat ini yang kita punya di dalam `post_view` adalah:

    python
    def post_new(request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    

Ketika kita melakukan submit form tersebut, kita dibawa kembali kepada view yang sama, tapi kali ini kita punya lebih banyak data dalam `request`, lebih spesifik di dalam `request.POST` (Selebihnya tidak ada hubungannya dengan sebuah post blog, itu terkait dengan kenyataan bahwa kita sedang memposting data). Ingat bahwa di dalam file HTML definisi `<form>` kita memiliki variabel `method="POST"`? Semua field dari from tersebut kini dalam `request.POST`. Anda tidak boleh merename `POST` apapun namanya (satu-satunya nilai valed dari `method` adalah `GET`, akan tetapi kami tidak punya cukup waktu untuk menjelaskan perbedaannya).

Sehingga di dalam *view* kita, kita menghadapi dua masalah berbeda untuk ditangani. Pertama: ketika kita mangakses halaman tersebut untuk pertama kali, kita menginginkan form kosong. Kedua: Ketika kita kembali ke *view* tersebut, form akan terisi dengan data yang baru saja kita ketik. Sehingga kita perlu menambahkan sebuah kondisi (akan kita gunakan `if` untuk keperluan tersebut).

    python
    if request.method == "POST":
        [...]
    else:
        form = PostForm()
    

Kini saatnya untuk mengisi titik-titik `[...]` itu. Jika `method` nilainya `POST` maka kita ingin membentuk `PostForm` dengan data dari form tersebut, benar begitu ? Kita akan melakukan hal itu dengan:

    python
    form = PostForm(request.POST)
    

Mudah! Hal berikutnya yang harus dikerjakan adalah mengecek apakah form tersebut benar (semua field yang dibutuhkan telah diset dan tidak ada lagi nilai yang salah akan disimpan). Kita lakukan hal itu dengan `form.is_valid()`..

Kita cek apakah form tersebut valid dan jika ya, kita dapat menyimpannya!

    python
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
    

Pada dasarnya, kita memiliki dua hal disini: kita menyimpan form tersebut dengan `form.save` dan menambahkan author (karena belum ada field `author` di dalam `PostForm` dan field ini diperlukan). `commit=False` artinya bahwa kita tidak ingin menyimpan model `Post` dulu, kita ingin menambah author dulu. Anda hampir akan selalu menggunakan `form.save` tanpa `commit=False`, akan tetapi dalam kasus ini, kita perlu menambahkannya dulu. `post.save()` akan menyimpan perubahan (menambahkan author) dan post blog baru tercipta!

Akhirnya, akan sangat bagus jika kita dapat segera menuju halaman `post_detail` yang berisi post blog yang baru tersebut, betul? Untuk melakukan hal itu kita perlu melakukan satu import lagi:

    python
    from django.shortcuts import redirect
    

Tambahkan itu pada awal baris file anda. Dan sekarang kita dapat berkata: pergilah ke halaman `post_detail` untuk menampilkan post yang baru dibuat tersebut.

    python
    return redirect('blog.views.post_detail', pk=post.pk)
    

`blog.views.post_detail` adalah nama dari view yang ingin kita tuju. Ingat bahwa *view* ini memerlukan sebuah variabel `pk`? Untuk mengirimkannya ke view kita gunakan `pk=post.pk`, dimana `post` merupakan post blog yang baru saja dibuat.

Oke, kita telah berbicara banyak, tetapi kita mungkin ingin melihat seperti apa penampilan seluruh *view* sekarang. Benar begitu ?

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
    

Mari lihat, apakah dapat berjalan. Buka alamat http://127.0.0.1:8000/post/new/, tambahkan sebuah `title` dan `text`, lalu simpan. Dan viola! Blog post baru telah ditambahkan dan diarahkan ke halaman `post_detail`!

Mungkin anda telah memperhatikan bahwa kita menentukan nilai publish date sebelum menyimpan post. Kelak kita akan memperkenalkan sebuah *publish button* dalam ** jango Girls Tutorial: Extensions**.

Sejauh ini bagus !

## Validasi Form

Sekarang, akan kami perlihatkan betapa hebatnya form django itu. Sebuah post blog perlu memiliki field `title` dan `text`. Dalam model `Post` kita, kita tidak berkata (seperti kebalikan dari `published_date`) bahwa field-field ini tidak diperlukan, sehingga secara default django berharap bahwa field-field tersebut nilainya harus diset.

Cobalah menyimpan form tanpa `title` dan `text`. Tebak apa yang akan terjadi!

![Validasi Form][3]

Django memperhatikan validasi apakah semua field dalam form kita benar. Bukankah itu hebat?

> Sebagaimana kita telah menggunakan interface admin Django, sistem saat ini berfikir bahwa kita dalam kondisi login. Ada situasi tertentu yang akan membawa kita logout (menutup browser merestart database dan lain sebagianya). Jika anda mengalami error ketika membuat sebuah post terkait masalah user yang belum login, bukalah halaman admin http://127.0.0.1:8000/admin dan login lagi. Ini sementara akan menyelesaikan permasalahan. Ada penyelesain permanen yang menanti anda pada bab **Homework: add security to your website!** setelah tutorial utama.

![Login Error][4]

## Form Edit

Kini kita tahu bagaimana menambah form baru. Tetapi, bagaimana jika kita ingin mengedit yang sudah ada ? Caranya sangat mirip dengan yang telah barusaja kita lakukan. Mari kita buat beberapa hal penting secara cepat (jika anda tidak tahu sesuatu, anda harus bertanya kepada pelatih anda atau lihat bab-bab sebelumnya karena semua langkah telah kami ajarkan).

Buka `blog/templates/blog/post_detail.html` dan tambahkan baris ini:

    python
    <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    

Sehingga template itu tampak seperti:

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
    

Dalam `blog/urls.py` kita tambah baris ini:

    python
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    

Kita akan menggunakan kembali template `blog/templates/blog/post_edit.html`, sehingga sesuatu yang belum adalah sebuah *view*.

Mari buka sebuah `blog/views.py` dan tambahkan di bagian paling akhir dari file tersebut:

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
    

Ini tampak hampir sama persis dengan view `post_new` kita, benar ? Tetapi tidak seluruhnya sama persis. Hal pertama: kita lewatkan sebuah parameter tambahan `pk` dari url. Berikutnya: kita mendapatkan model `Post` yang ingin kita edit dengan `get_object_or_404(Post,pk=pk)` dan kemudian, dan ketika kita membuat sebuah form kita lewatkan post ini sebagai `instance` keduanya ketika kita menyimpan form:

    python
    form = PostForm(request.POST, instance=post)
    

dan ketika kita baru saja membuka sebuah form dengan post untuk diedit:

    python
    form = PostForm(instance=post)
    

Oke, mari kita uji apakah bekerja!

![Tombol Edit][5]

Ketika anda mengkliknya, anda aka melihat form tersebut berisi post blog kita:

![Form Edit][6]

Anda bebas mengganti judul atau isinya dan menyimpan perubahannya.

Selamat! Aplikasi anda makin lama makin lengkap!

Apabila anda menginginkan lebih banyak informasi tentang form Django anda harus membaca dokumentasinya di https://docs.djangoproject.com/en/1.8/topics/forms/

## Keamanan

Telah berhasil membuat post baru hanya dengan melakukan klik pada sebuah link itu hebat! Tapi, sekarang seseorang yang mengunjungi website anda akan dapat memposting postingan baru dan itu mungkin bukan hal yang anda inginkan! Tetapi, sekarang seseorang yang mengunjungi website anda akan dapat mengirim sebuah postingan baru dan ini mungkin bukan sesuatu yang anda kehendaki. Mari kita buat agar tombol tersebut terlihat bagi anda dan bukan bagi orang lain.

Dalam `blog/templates/blog/base.html`, temukan `div` dari `page-header` kita dan anchor tag yang anda letakkan sebelumnya. Tampilannya seharusnya seperti ini:

    html
    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    

Kita akan menambahkan sebuah tag 0>{% if %}</code> lagi ke dalamnya yang menyebabkan link itu hanya akan muncul bagi user yang login sebagai admin. Saat ini, hanya anda! Ubah tag 0><a></code> agar menjadi ini:

    html
    {% if user.is_authenticated %}
        <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    {% endif %}
    

`{% if %}` ini akan menyebabkan link tersebut dikirim ke browser hanya jika user yang bersangkutan login. Ini tidak melindungi adanya penulisan post baru seluruhnya, tapi cukup bagus untuk langkah awal. Kita akan mempelajari masalah keamanan lebih jauh pada pelajaran tentang extension.

Karena kelihatannya anda dalam keadaan login, jika anda merefresh halaman itu, anda mungkin tidak akan melihat perubahan apapun. Buka halaman tersebut dangan browser baru atau dengan jendela baru maka anda tidak akan melihat link tersebut!

## Satu hal lagi: saatnya melakukan deploy!

Mari kita lihat apakah itu semua dapat berjalan di PythonAnywhere. Saatnya melakukan deploy lagi!

*   Pertama, lakukan commit kode baru anda dan kirim ke GitHub

    $ git status
    $ git add -A .
    $ git status
    $ git commit -m "Added views to create/edit blog post inside the site."
    $ git push
    

*   Kemudian dalam konsol Bash [PythonAnywhere][7]:

    $ cd my-first-blog
    $ source myvenv/bin/activate
    (myvenv)$ git pull
    [...]
    (myvenv)$ python manage.py collectstatic
    [...]
    

*   Yang terakhir, cari [Web tab][8] dan klik **Reload**.

Dan seharusnya dapa berjalan! Selamat :)

 [1]: images/csrf2.png
 [2]: images/new_form2.png
 [3]: images/form_validation2.png
 [4]: images/post_create_error.png
 [5]: images/edit_button2.png
 [6]: images/edit_form2.png
 [7]: https://www.pythonanywhere.com/consoles/
 [8]: https://www.pythonanywhere.com/web_app_setup/