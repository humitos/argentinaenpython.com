# Deploy (Publikasikan)

> **Catatan** Bab berikut mungkin terasa agak sulit untuk dipahami. Lanjutkan sampai selesai; proses deploy merupakan proses yang penting pada proses pengembangan website. Bab ini sengaja diletakkan di bagian tengah tutorial ini dengan harapan agar pendamping anda, kalau ada, dapat membantu anda menjadikan website anda online, dengan sedikit trik. Ini artinya, anda masih dapat menyelesaikan sendiri tutorial ini kalau-kalau anda tak lagi punya cukup waktu.

Sejauh ini, website anda hanya bisa berjalan pada komputer anda sendiri, sekarang anda akan belajar bagaimana mendeploynya. Proses deploy adalah proses mempublikasikan aplikasi anda di Internet agar orang lain dapat membuka dan melihat aplikasi anda :).

Sebagaimana yang telah anda pelajari, sebuah website haruslah diletakkan pada server. Ada banyak penyedia server di Internet. Kita akan menggunakan salah satu, yang proses deploymennya relatif mudah: [PythonAnywhere][1]. PythonAnywhere sifatnya gratis untuk aplikasi kecil yang pengunjungnya tidak terlalu banyak sehingga saya pikir cukup untuk sementara.

 [1]: http://pythonanywhere.com/

Layanan eksternal lain akan menggunakan [GitHub][2], yang merupakan sebuah layanan hosting kode program. Ada beberapa yang lain, akan tetapi hampir semua programmer saat ini memiliki akun di GitHub, anda berikutnya.

 [2]: http://www.github.com

Kita akan menggunakan GitHub sebagai batu loncatan untuk mentransfer kode program kita dari dan ke PyThonAnywhere.

# Git

Git adalah suatu "sistem kontrol versi" yang digunakan oleh banyak sekali programmer. Software ini dapat mencatat perubahan file dari waktu ke waktu sehingga anda dapat mencari versi tertentu di kemudian hari. Ini mirip dengan fitur "track changes" pada Microsoft Word, tapi jauh lebih baik.

## Menginstal Git

> **Catatan** Jika anda sudah melakukan instalasi, anda tidak perlu melakukannya lagi, lompat saja ke pembahasan selanjutnya dan mulai membuat repositori Git anda.

{% include "deploy/install_git.md" %}

## Memulai repositori Git kita

Git mencatat perubahan atas file-file yang disebut repositori kode (atau disingkat "repo" saja). Mari kita mulai untuk proyek kita. Buka konsole dan jalankan perintah ini dalam direktori`djangogirl`:

> **Catatan** Cek direktori kerja saat ini dengan perintah `pwd` (OSX/Linux) atau `cd` (Windows) sebelum melakukan inisialisasi repositori. Anda harus berada di dalam folder `djangogirl`.

    $ git init
    Initialized empty Git repository in ~/djangogirls/.git/
    $ git config --global user.name "Nama Anda"
    $ git config --global user.email anda@contoh.com
     
    

Melakukan inisialisasi repositori Git hanya perlu dilakukan sekali untuk tiap proyek (dan selanjutnya anda tidak harus mendaftarkan namauser dan email lagi).

Git akan mencatat perubahan atas semua file dan folder yang ada dalam direktori ini, tetapi ada beberapa file yang ingin kita abaikan. Kita melakukan ini dengan cara membuat sebuah file yang diberi nama `.fitignore`, dalam direktori utama. Jalankan program editor anda kemudian buat sebuah file baru dengan isi :

    *.pyc
    __pycache__
    myvenv
    db.sqlite3
    .DS_Store
    

Dan simpanlah dengan nama `.gitignore` pada folder "djangogirls" terluar.

> **Catatan** Titik di depan nama file sangat penting! Jika anda mengalami kesulitan membuat nama file semacam ini (Karena Macs tidak suka jika anda membuat nama file yang diawali dengan titik lewat Finder, ini contoh kasus), maka pilih fitur "Save As" pada editor anda, biasanya pasti bisa.

Sebaiknya cek status dulu dengan perintah `git status` sebelum melakukan `git add` atau kapanpun anda ingin memastikan apa yang telah berubah. Ini agar anda tidak kaget, misalnya ada file yang tidak diinginkan ikut ditambahkan atau telah terjadi proses commit. Perintah `git satatus` tersebut akan memberikan informasi atas beberapa file yang tidak terlacak/termodifikasi/ditampilkan dan banyak informasi lain. Keluarannya kira-kira seperti ini:

    $ git status
    On branch master
    
    Initial commit
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
    
            .gitignore
            blog/
            manage.py
            mysite/
    
    nothing added to commit but untracked files present (use "git add" to track)
    

Dan akhirnya kita simpan perubahan kita. Buka konsole dan jalankan perintah-perintah berikut:

    $ git add -A .
    $ git commit -m "My Django Girls app, first commit"
     [...]
     13 files changed, 200 insertions(+)
     create mode 100644 .gitignore
     [...]
     create mode 100644 mysite/wsgi.py
    

## Memasukkan kode kita ke GitHub

Buka [GitHub.com][2] lalu buatlah akun sebagai free user. (Apabila pernah anda lakukan sebelumnya pada persiapan workshop, ini bagus!)

Kemudian buat sebuah repositori baru, beri nama "my-first-blog". Tickbox "initialise with a README" jangan anda centang, biarkan opsi .gitignore kosong (kita telah melakukannya secara manual) dan biarkan License tetap None.

![][3]

 [3]: images/new_github_repo.png

> **Catatan** Nama `my-first-blog` sangat penting, tentu anda bisa saja memilih nama lain, akan tetapi nama tersebut akan selalu muncul lagi dan anda tentu akan repot harus selalu menggantinya. Jadi tak usah sulit-sulit, pakai saja nama `my-first-blog`.

Pada layar selanjutnya, akan diperlihatkan kepada anda clone URL repositori anda. Pilih versi "HTTPS", copylah dan nanti akan kita paste di terminal:

![][4]

 [4]: images/github_get_repo_url_screenshot.png

Sekarang kita perlu menghubungkan repositori dalam komputer anda ke dalam GitHub.

Ketik perintah berikut ini pada konsol (Gantilah ` <your-github-username >` dengan nama user sesuai akun GitHub yang telah anda buat, tetapi tanpa tanda kurung sudut):

    $ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
    $ git push -u origin master
    

Masukkan username dan password GitHub anda dan seharusnya anda akan melihat yang seperti ini:

    Username for 'https://github.com': hjwp
    Password for 'https://hjwp@github.com':
    Counting objects: 6, done.
    
    Writing objects: 100% (6/6), 200 bytes | 0 bytes/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/hjwp/my-first-blog.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.
    

<!--TODO: maybe do ssh keys installs in install party, and point ppl who dont have it to an extention -->

Kode anda kini ada dalam GitHub. Silahkan anda cek! Akan anda dapati bahwa kode anda ada dalam perusahaan yang bagus - [Django][5], [Django Girls Tutorial][6], dan ada banyak lagi proyek software opensource yang menyimpan kode programnya di GitHub :)

 [5]: https://github.com/django/django
 [6]: https://github.com/DjangoGirls/tutorial

# Menyeting blog kita di PythonAnywhere

> **Catatan** Anda mungkin sudah membuat akun di PythonAnywhere pada proses install sebelumnya. Jika ya, maka anda tidak perlu melakukannya lagi.

{% include "deploy/signup_pythonanywhere.md" %}

## Menarik kembali kode kita dari PythonAnywhere

Ketika anda sudah mendaftar di PythonAnywhere, anda akan dibawa ke halaman dashboard atau "konsol" anda. Pilih opsi tersebut untuk memulai konsole "Bash", yang mana merupakan konsole versi PythonAnywhere, hampir sama seperti yang ada dalam komputer anda.

> **Catatan** PythonAnywhere berbasis Linux, sehingga jika anda menggunakan Windows, tampilan konsol agak sedikit lain dibandingkan yang ada di komputer anda.

Mari kita tarik kembali kode kita dari GitHub dan memasukkan ke PythonAnywhere dengan cara membuat "clone" dari repo kita. Ketik perintah berikut di dalam konsol PythonAnywhere (jangan lupa gunakan username GitHub anda pada `<username--github-anda>`):

    $ git clone https://github.com/<username-github-anda>/my-first-blog.git
    

Ini akan menarik kembali salinan kode anda ke dalam PythonAnywhere. Bisa di cek dengan perintah `tree my-first-blog`:

    $ tree my-first-blog
    my-first-blog/
    ├── blog
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
    

### Membuat virtualenv pada PythonAnywhere

Sama persis dengan yang telah anda lakukan pada komputer anda, anda dapat menciptakan virtualenv pada PythonAnywhere. Pada konsol Bash ketik:

    $ cd my-first-blog
    
    $ virtualenv --python=python3.4 myvenv
    Running virtualenv with interpreter /usr/bin/python3.4
    [...]
    Installing setuptools, pip...done.
    
    $ source myvenv/bin/activate
    
    (mvenv) $  pip install django whitenoise
    Collecting django
    [...]
    Successfully installed django-1.8.2 whitenoise-2.0
    

> **Catatan** Proses `pip install` dapat berlangsung beberapa menit. Sabar, sabar! Tapi jika lebih dari 5 menit, berarti ada yang salah. Tanya kawan anda.

<!--TODO: think about using requirements.txt instead of pip install.-->

### Mengumpulkan file-file statis.

Pernahkan anda bertanya apa itu "whitenoise"? Itu adalah sebuah tool untuk menangani apa yang disebut dengan "file statis". File statis adalah file yang tidak sering berubah atau file yang tidak menjalankan kode program, misalnya file HTML atau CSS. File-file tersebut pada server kerjanya berbeda dibandingkan dengan pada komputer kita dan kita memerlukan tool seperti "whitenoise" untuk menanganinya.

Kita akan lebih memahami lagi nanti tentang file statis Kita akan lebih paham lagi apa itu file statis pada tutorial berikutmya, yaitu ketika kita mengedit CSS untuk website kita.

Tapi sekarang kita hanya perlu menjalankan perintah tambahan yang disebut `collecstatic` pada server. Perintah itu akan membuat django mengumpulkan seluruh file statis pada server. Sejauh ini, file-file inilah yang membuat website pada sisi admin tampak lebih cantik.

    (mvenv) $ python manage.py collectstatic
    
    You have requested to collect static files at the destination
    location as specified in your settings:
    
        /home/edith/my-first-blog/static
    
    This will overwrite existing files!
    Are you sure you want to do this?
    
    Type 'yes' to continue, or 'no' to cancel: yes
    

Ketik "yes" dan biarkan prosesnya berjalan ! Bukankah anda suka ketika komputer menampilkan tulisan banyak halaman tanpa bisa di ganggu ? Saya biasanya menunggunya dengan berdengan ria...na na na ....

    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/actions.min.js'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/inlines.min.js'
    [...]
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/changelists.css'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/base.css'
    62 static files copied to '/home/edith/my-first-blog/static'.
    

### Membuat database di PythonAnywhere

Ada hal lain yang berbeda antara komputer anda dan server: databasenya lain. Akibatnya akun user dan postingian mungkin berbeda antara di server dengan yang ada di komputer anda.

Kita dapat memulai bekerja dengan database di server dengan cara yang sama persis ketika anda lakukan di komputer anda sendiri:

    (mvenv) $ python manage.py migrate
    Operations to perform:
    [...]
      Applying sessions.0001_initial... OK
    
    
    (mvenv) $ python manage.py createsuperuser
    

## Mempublikasikan blog kita sebagai sebuah aplikasi web

Kini kode program kita sudah ada di PythonAnywhere, virtualenv kita sudah siap, file static sudah dikumpulkan dan database sudah dibuat. Kita siap untuk mempublikasikannya sebagai sebuah aplikasi berbasis web!

Klik back pada dashboard PythonAnywhere, klik pada logonya kemudian klik pada tab **Web**. Yang terkhir, klik **Add a new web app**.

Setelah nama domain anda disetujui, pilih **manual configuration** (NB *bukan* pilihan "Django") pada dialog itu. Selanjutnya pilih **Python 3.4** dan klik next untuk mengakhiri wizard.

> **Catatan** Pastikan anda memilih opsi "Manual configuration", jangan memilih opsi "Dango". Terlalu mudah jika memilih setingan default Django pada PythonAnywhere.

### Melakukan setting virtualenv

Anda akan dibawa ke dalam layar konfigurasi PythonAnywhere untuk aplikasi web anda dan ini merupakan tampilan darimana ada dapat memulai mengubah apapun atas aplikasi wen anda di server.

![][7]

 [7]: images/pythonanywhere_web_tab_virtualenv.png

Pada seksi "Virtualenv", klik teks merah yang berbunyi "Enter the path to a virtualenv" lalu tekan enter: `/home/<namauser-anda>/my-first-blog/myvenv/`. Klik kotak biru yang ada tanda centangnya untuk menyimpan path sebelum anda melanjutkan.

> **Catatan** Gantilah nama user anda seperlunya. Jika anda berbuat kesalahan, PythonAnywhere akan menampilkan peringatan.

### Menkonfigurasi file WSGI

Django bekerja menggunakan "protokol WSGI", protokol standar website yang menggunakan python, yang dalam hal ini juga didukung oleh PythonAnywhere. Tatacara kita untuk menkonfigurasi PythonAnywhere agar mengenali blog Django kita, dilakukan dengan mengedit suatu file konfigurasi WSGI.

Klik pada link "WSGI configuration file" (pada seksi "Code" dekat bagian atas halaman, yang akan diberi nama semacam `/var/www/<username-anda>_pythonanywhere_com_wsgi.py`), dan anda akan dibawa ke dalam sebuah teks editor.

Hapus semua isinya dan ganti dengan yang berikut:

    python
    import os
    import sys
    
    path = '/home/<your-username>/my-first-blog'  # use your own username here
    if path not in sys.path:
        sys.path.append(path)
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    
    from django.core.wsgi import get_wsgi_application
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(get_wsgi_application())
    

> **Catatan** Jangan lupa untuk mengganti username anda sendiri jika anda menemui `<your-username>`

File ini berfungsi untuk memberi tahu PythonAnywhere di mana aplikasi web kita akan ditempatkan dan apa nama file-file setting Django. Ini juga akan mengeset tool file statis "whitenoise".

Klik **Save** dan kembalilah ke tab **Web**.

Selesai! Klik tombol hijau besar dengan label **Reload** dan anda akan dapat melihat aplikasi anda. Nda akan menemukan sebuah link yang mengarah kepadanya di bagian atas halaman.

## Tip Debugging (Mencari bug atau error)

Jika anda melihat ada error pada saat anda membuka website anda, lokasi pertama-tama untuk mencari informasi debugging adalah pada **error log**. Anda akan menemukan sebuah link yang mengarah ke sana pada tab [Web tab][8] PythonAnywhere. Lihat apakah ada pesan error di sana, yang terbaru ada di bagian bawah. Masalah-masalah yang umum dijumpai meliputi:

 [8]: https://www.pythonanywhere.com/web_app_setup/

*   Melewati step yang telah kita lakukan di konsole: membuat virtualenv, mengaktifkannya, menginstal django di dalmnya, menjalankan collectstatic maupun melakukan migrasi database.

*   Melakukan kesalahan pada path virtualenv pada tab Web. Disana biasanya akan ada pesan error merah jika ada kesalahan.

*   Melakukan kesalahan pada file konfigurasi WSGI. Bukankah anda telah mendapatkan path mengarah pada folder my-first-blog?

*   Apakah anda memilih versi python yang sama untuk virtualenv dengan python apliksi web anda? Keduanya harus versi 3.4.

*   Ada tips debugging umum di wiki PythonAnywhere..

Dan ingat, pendamping anda siap di sini untuk membantu ada!

# Website anda kini hidup!

Halaman default website anda seharusnya berbunyi: "Welcome to Django", persis sama dengan yang di komputer lokal anda. Coba tambahkan `/admin/` di akhir URL, maka anda akan masuk pada admin website. Lakukan Log in dengan username dan password yang sesuai dan anda akan dapat membuat posting baru di server.

Tepuk tangan! Pada proses pengembangan website, proses deploy ke dalam server adalah sebuah proses yang perlu sedikit trik dan seseorang biasanya perlu beberapa hari usaha sampai berhasil. Tapi kini anda sudah berhasil membuat website anda hidup dalam Internet sesungguhnya, itu sangat bagus!