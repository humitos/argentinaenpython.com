# Διαχείριση μέσω Django admin

Για να προσθέσετε, να επεξεργαστείτε ή και να διαγράψετε τις δημοσιεύσεις που μόλις αναπτύξαμε, θα χρησιμοποιούμε το διαχειριστικό σύστημα του Django γνωστό ως Django admin.

Ανοίξτε το αρχείο `blog/admin.py` και αντικαταστήστε το περιεχόμενό του με το παρακάτω:

    python
    from django.contrib import admin
    from .models import Post
    
    admin.site.register(Post)
    

Με τον παραπάνω κώδικα, εισάγουμε το μοντέλο Post (δηλαδή τον πίνακα της βάσης με όνομα Post) όπως ορίστηκε από το προηγούμενο κεφάλαιο. Για να είναι διαθέσιμο στο σύστημα διαχείρισης του Django, πρέπει να "εγγράψουμε" (register) το μοντέλο Post, `admin.site.register(Post)`..

Εντάξη λοιπόν αγαπητοί κύριοι και κυρίες, ας ρίξουμε μια ματία στο Post μοντέλο μας. Θυμηθείτε ότι πρέπει πρώτα να πληκτρολογήσουμε `python manage.py runserver` στην κονσόλα μας ώστε να ξεκινήσει ο σερβερ μας. Πηγαίνετε στον αγαπημένο σας browser και πληκτρολογήστε τη διεύθυνση http://127.0.0.1:8000/admin/. Θα δείτε την σελίδα εισόδου του Django admin:

![Login page][1]

 [1]: images/login_page2.png

Για την είσοδο σας, πρέπει να δημιουργήσετε έναν *superuser* - έναν χρήστη δηλαδή που έχει τα πλήρη δικαιώματα επεξεργασίας στην ιστοσελίδα που κατασκευάζουμε παρέα. Go back to the command-line and type `python manage.py createsuperuser`, and press enter. When prompted, type your username (lowercase, no spaces), email address, and password. Don't worry that you can't see the password you're typing in - that's how it's supposed to be. Just type it in and press `enter` to continue. The output should look like this (where username and email should be your own ones):

    (myvenv) ~/djangogirls$ python manage.py createsuperuser
    Username: admin
    Email address: admin@admin.com
    Password:
    Password (again):
    Superuser created successfully.
    

Return to your browser. Log in with the superuser's credentials you chose; you should see the Django admin dashboard.

![Διαχείριση μέσω Django admin][2]

 [2]: images/django_admin3.png

Go to Posts and experiment a little bit with it. Add five or six blog posts. Don't worry about the content - you can simply copy-paste some text from this tutorial to save time :).

Make sure that at least two or three posts (but not all) have the publish date set. It will be helpful later.

![Διαχείριση μέσω Django admin][3]

 [3]: images/edit_post3.png

If you want to know more about Django admin, you should check Django's documentation: https://docs.djangoproject.com/en/1.8/ref/contrib/admin/

This is probably a good moment to grab a coffee (or tea) or something to eat to re-energise yourself. You created your first Django model - you deserve a little timeout!