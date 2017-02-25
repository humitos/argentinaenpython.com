> Sebagian dari bagian ini diambil dari tutorial yang ditulis oleh Geek Girl Carrots (http://django.carrots.pl/).
> 
> Sebagian dari bagian ini didasarkan pada [django-marcador tutorial](http://django-marcador.keimlink.de/) dengan lisensi yang dinamakan <0>django-marcador tutorial</0> <0>django-marcador tutorial</0>. The django-marcador tutorial is copyrighted by Markus Zapke-Gründemann et al.

## Virtual Environment

Sebelum kita menginstal django kami akan mengajari anda untuk menginstall tool yang sangat penting yang akan menjaga lingkungan pengembangan anda teratur di komputer anda. Dimungkinkan untuk melewati bagian ini, tapi sangat dianjurkan untuk tidak melewatinya. Dimulai dengan setup sebaik mungkin akan menghindarkan anda dari banyak kesulitan di masa yang akan datang.

Karena itu, mari membuat sebuah **virtual environment** (juga disebut *virtualenv*). Virtualenv akan memisahkan setup Python/Django untuk tiap proyek. Ini artinya bahwa suatu perubahan yang anda buat pada sebuah website, tidak akan mempengaruhi website lain yang juga sedang anda kembangkan. Jelas bukan ?

Yang perlu anda kerjakan adalah menemukan sebuah direktory dimana anda ingin menciptakan `virtualenv`, yaitu home directory anda, ini sebagai misal. Pada windows mungkin akan tampak seperti ini `C:\Users\Name` (dimana `Name` adalah nama login anda).

Karena tutorial ini akan menggunakan sebuah direktory baru yaitu `djangogirls`, dari home direktory anda:

    mkdir djangogirls
    cd djangogirls
    

Kita akan membuat sebuah virtualenv dengan nama `myenv`. Bentuk perintah umumnya seperti ini:

    python3 -m venv myvenv
    

### Windows

Untuk membuat sebuah `virtualenv` baru, anda perlu membuka konsol (kami sudah menjelaskan kepada anda pada bab sebelumnya, ingat kan ?) dan mengetikan `C:\Python34\python -m venv myvenv`. It will look like this:

    C:\Users\Name\djangogirls> C:\Python34\python -m venv myvenv
    

Dimana `C:\Python34\python` adalah direktory dimana anda menginstal python dan `myvenv` adalah nama dari `virtualenv` anda. Anda boleh menggunakan nama yang lain, tapi harus menggunakan huruf kecil dan tanpa spasi, karakter khusus ataupun tanda petik. Baik juga menentukan nama yang pendek saja, sebab anda akan selalu merujuk nama itu.

### Linux dan OS X

Menciptakan sebuah `virtualenv` baik di Linux maupun di OS X dapat dilakukan dengan mudah: `python3 -m venv myvenv`. Tampak seperti ini:

    ~/djangogirls$ python3 -m venv myvenv
    

`myvenv` adalah nama dari `virtualenv` anda. Anda dapat menggunakan nama lain akan tetapi tetap gunakan huruf kecil dan tanpa spasi. Sebaiknya gunakan nama yang pendek saja, sebab anda akan selalu merujuk nama itu.

> **CATATAN:** Ketika anda menciptakan virtual environment on Ubuntu 14.04 seperti di bawah ini, akan terjadi error sebagai berikut:
> 
>     Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1
>     
> 
> Untuk mengatasi hal ini, gunakan perintah `virtualenv`.
> 
>     ~/djangogirls$ sudo apt-get install python-virtualenv
>     ~/djangogirls$ virtualenv --python=python3.4 myvenv
>     

## Bekerja Dengan Virtualenv

Perintah di atas akan meciptakan sebuah direktori dengan nama `myvenv` (atau nama apa saja yang anda pilih) yang berisi virtual environment kita (jelasnya berisi banyak file dan direktori).

#### Windows

Aktifkan virtual environment anda dengan menjalankan:

    C:\Users\Name\djangogirls> myvenv\Scripts\activate
    

#### Linux dan OS X

Aktifkan virtual environment anda dengan menjalankan:

    ~/djangogirls$ source myvenv/bin/activate
    

Ingat untuk mengganti `myvenv` dengan nama pilihan anda `virtualenv` name!

> **CATATAN:** kadang-kadang `source` tidak tersedia. Kalau anda menghadapi masalah tersebut coba ini:
> 
>     ~/djangogirls$ . myvenv/bin/activate
>     

Anda akan tahu kalau `virtualenv` telah berjalan jika anda melihat prompt di konsole anda seperti ini:

    (myvenv) C:\Users\Name\djangogirls>
    

Atau:

    (myvenv) ~/djangogirls$
    

Perhatikan bahwa awalah `(myvenv)` muncul!

Ketika anda bekerja dalam sebuah virtual environment, `python` akan otomatis mengacu pada versi yang benar sehingga anda dapat menggunakan perintah `python` bukannya `python3`.

Oke, kita telah memiliki semua dipendensi penting pada tempatnya. Pada akhirnya kita dapat mengintal django.

## Menginstall Django

Sekarang anda telah mempunyai `virtualenv`, anda bisa menginstall Django menggunakan `pip`. Jalankan Kode berikut pada console anda `pip install djanggo==1.8`(catatan, gunakan 2 tanda sama dengan: `==`).

    (myvenv) ~$ pip install django==1.8
    Downloading/unpacking django==1.8
    Installing collected packages: django
    Successfully installed django
    Cleaning up...
    

Di Windows

> Jika anda mengalami error saat memanggil pip pada windows platform silahkan cek apakah path project anda terdapat spasi, aksen atau spesial karakter (contoh: `C:\Users\User Name\djangogirls`). Jika ada karakter seperti itu mohon untuk menghapus spasi, aksen atau karakter spesial tersebut (saran : `C:\djangogirls`). Setelah anda melakukanya silahkan jalankan command lagi.

Di Linux

> Jika anda mengalami error saat memanggil pip pada Ubuntu 12.04 silahkan jalankan code berikut `python -m pip install -U --force-reinstall pip` untuk memperbaiki instalasi pip pada cirtualenv.

Itu dia! Akhirnya sekarang anda telah membuat aplikasi Django!