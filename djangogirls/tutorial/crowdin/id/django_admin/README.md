# Admin Django

Untuk menambah, mengedit dan menghapus post yang baru saja kita buat modelnya, akan kita gunakan admin Django.

Mari buka file `blog/admin` dan gantilah isinya dengan ini:

    python
    from django.contrib import admin
    from .models import Post
    
    admin.site.register(Post)
    

Sebagaimana dapat anda lihat, kita mengimport (meng Include) model Post yang telah didefinisikan di bab sebelumnya. Agar model kita tampil pada halaman admin, kita perlu mendaftarkan model tersebut dengan `admin.site.register(Post)`.

Oke, saatnya kita lihat model Post kita. Ingat untuk menjalankan `python manage.py runserver` di konsol untuk menjalankan web server. Bukalah browser dan ketik alamat http://127.0.0.1:8000/admin/ dan anda akan melihat halaman login seperti ini:

![Login page][1]

 [1]: images/login_page2.png

To log in, you need to create a *superuser* - a user which has control over everything on the site. Go back to the command-line and type `python manage.py createsuperuser`, and press enter. When prompted, type your username (lowercase, no spaces), email address, and password. Don't worry that you can't see the password you're typing in - that's how it's supposed to be. Just type it in and press `enter` to continue. The output should look like this (where username and email should be your own ones):

    (myvenv) ~/djangogirls$ python manage.py createsuperuser
    Username: admin
    Email address: admin@admin.com
    Password:
    Password (again):
    Superuser created successfully.
    

Return to your browser. Log in with the superuser's credentials you chose; you should see the Django admin dashboard.

![Admin Django][2]

 [2]: images/django_admin3.png

Go to Posts and experiment a little bit with it. Add five or six blog posts. Don't worry about the content - you can simply copy-paste some text from this tutorial to save time :).

Make sure that at least two or three posts (but not all) have the publish date set. It will be helpful later.

![Admin Django][3]

 [3]: images/edit_post3.png

If you want to know more about Django admin, you should check Django's documentation: https://docs.djangoproject.com/en/1.8/ref/contrib/admin/

This is probably a good moment to grab a coffee (or tea) or something to eat to re-energise yourself. You created your first Django model - you deserve a little timeout!