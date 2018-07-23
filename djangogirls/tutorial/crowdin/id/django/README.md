# Apa itu Django ?

Django (*/ˈdʒæŋɡoʊ/ jang-goh*) adalah sebuah aplikasi web framework gratis dan open source, ditulis dengan bahasa Python. Sebuah framework web adalah sebuah set komponen-komponen yang dapat membantu anda untuk mengembangkan website dengan lebih cepat dan mudah.

Ketika anda sedang membangun sebuah website, anda akan selalu berurusan dengan hal-hal serupa misalnya bagaimana menangani autentikasi user (sign up, sign in dan sign out), panel pengelolaan website, form-form, bagaimana mengupload file dan sebagianya.

Untung bagi anda bahwa para pengembang website sebelumnya juga menghadapi permasalahan serupa. Hal ini mendorong mereka untuk membuat team dan menciptakan sebuah framework (Django salah satunya) yang memberi anda komponen siap-pakai yang dapat anda gunakan.

Framework lahir untuk meringankan beban kerja anda pada saat anda membangun sebuah website.

## Mengapa anda memerlukan sebuah framework?

Untuk mengerti sebenarnya django itu untuk apa, kita perlu melihat pada server lebih dekat. Hal pertama yang harus di ketahui adalah bahwa anda ingin agar si server melayani anda menampilkan halaman web.

Bayangkanlah sebuah mailbox/kotak surat (port), yang selalu dimonitor untuk mengetahui apakah ada surat masuk (request). Ini dikerjakan oleh server. Web server membaca surat tersebut dan mengirim respon menggunakan halaman web. Akan tetapi, ketika anda ingin mengirimkan sesuatu, anda perlu menyiapkan isinya. Dan django akan membantu anda membuat isinya.

## Apa yang terjadi ketika seseorang membuka halaman web di server anda ?

Pada saat request masuk pada sebuah web server, request itu akan diserahkan kepada django dan django akan memproses apa diminta. Yang pertamakali dilakukan adalah mengambil alamat halaman web kemudian memikirkan apa yang harus dikerjakan selanjutnya. Bagian ini dikerjakan oleh **urlresolver** Django (Ingat bahwa suatu alamat website disebut URL: Universal Resource Locater. Sehingga kita bisa mengerti maksud apa itu *urlresolver*). Sederhana saja, django mengambil beberapa pola dan untuk mencocokkan dengan alamat URL tersebut. Django mengecek pola dari atas sampai bawah dan jika ada yang cocok maka django akan mengirimkan request itu ke fungsi terkait (Yang kita namakan dengan *view*).

Bayangkanlah ada petugas pengantar surat membawa sebuah surat. Ia menelusuri jalan dan mengecek tiap nomor rumah apakah cocok dengan alamat pada surat. Jika cocok, ia akan mengantarkan ke sana. Begitulah cara kerja urlresolver!

Pada fungsi *view* inilah terjadi proses yang menarik dimana kita dapat melihat ke dalam database untuk mendapat suatu informasi. Munkin si user ingin mengubah data? Seperti sebuah surat yang mengatakan "Tolong ubah diskripsi pekerjaan saya." *view* dapat mengecek apakah anda boleh melakukan pekerjaan itu, setelah itu baru mengupdate diskripsi pekerjaan itu untuk anda lalu mengirim pesan balasan: "Sudah saya kerjakan !". Kemudian *view* tersebut membuat suatu respon dan Django dapat mengirim kepada si user dari web browser.

Tentu saja diskripsi tadi agak disederhanakan, toh sejauh ini anda tak perlu tahu segala sesuatu yang sangat teknis dulu. Mengerti yang umum-umum dulu sudah cukup.

Jadi, kita tidak akan belajar segala sesuatunya langsung secara detail, tetapi kita akan membuat sesuatu dengan django dan hal-hal penting lainnya sambil berjalan!