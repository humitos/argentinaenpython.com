# מבצוע!

> **הערה:** הפרק הבא יחסית קשה. תתמידי ותסיימי אותו; מבצוע (מלשון מבצע, להפוך משהו למבצעי - באנגלית deployment) הוא חלק חשוב בתהליך בניית אתרים. פרק זה מופיע באמצע המדריך בכוונה, כדי שהחונכת שלך תוכל לעזור לך עם החלקים הקצת יותר טריקיים בהעלאת האתר שלך לאוויר. כך שאם יגמר לך הזמן, עדיין תוכלי לסיים את כל העסק בכוחות עצמך.

עד עכשיו האתר שלך היה זמין במחשב שלך בלבד, והגיע הזמן למבצע אותו! מבצוע הוא תהליך הפרסום של האפליקציה שלך באינטרנט, כך שגם אנשי םאחרים יוכלו לראות אותה ולהשתמש בה :).

כמו שכבר למדת, אתר אינטרנט חייב להימצא על שרת. יש המון ספקי שרתים באינטרנט. אנחנו נשתמש באחד שיחסית פשוט למבצוע: [PythonAnywhere][1]. PythonAnywhere הוא תשתית חינמית עבור אפליקציות קטנות שאין להן יותר מדי מבקרים, והוא בהחלט יספיק לנו לבינתיים.

 [1]: http://pythonanywhere.com/

השירות החיצוני האחר שנשתמש בו הוא [GitHub][2], שהוא שירות אחסון קוד. יש גם כל מני שירותים אחרים, אבל כמעט לכל המתכנתים בימינו יש חשבון GitHub, אז עכשיו גם לך יהיה!

 [2]: http://www.github.com

אנחנו נשתמש ב-GitHub בתור קרש קפיצה, ממנו נעביר את הקוד שלנו ל-PythonAnywhere.

# Git

Git היא תוכנת version control (ובעברית, בקרת גרסאות), שמתכנתים רבים משתמשים בה. התוכנה הזו יודעת לעקוב אחרי שינויים בקבצים לאורך זמן, כך שתמיד אפשר לעבור לגרסה אחרת מאוחר יותר. זה קצת כמו track changes ב-Microsoft Word, אבל הרבה יותר חזק.

## התקנת Git

> **הערה:** אם כבר התקנת git, אין צורך לעשות זאת שוב - את יכולה לדלג על החלק הבא ולהתחיל לעבוד על ה-repository שלך.

{% include "deploy/install_git.md" %}

## מתחילים את ה-Git Repository

Git עוקב אחרי שינויים בקבוצה מסוימת של קבצים שנקראת repository (או בקיצור, repo. עברית זה כנראה משהו כמו "מאגר"). בואי נייצר אחד בשביל הפרויקט שלנו. פתחי טרמינל והריצי את הפקודות הבאות בתיקייה של `djangogirls`:

> **הערה:** בדקי מה התיקייה הנוכחית שלך עם `pwd` (בלינוקס או במק) או `cd` (בווינדוס) לפני שאת מייצרת את ה - repository. את אמורה להיות בתיקייה `djangogirls`.

    $ git init
    Initialized empty Git repository in ~/djangogirls/.git/
    $ git config --global user.name "Your Name"
    $ git config --global user.email you@example.com
    

אתחול של git repository הוא משהו שצריך לעשות פעם אחת פר פרויקט (ואת שם המשתמש והאימייל לא תצטרכי להזין יותר לעולם).

Git יעקוב רק אחרי שינויים של קבצים בתיקייה הזו, אבל יש גם קבצים מסוימים שהיינו רוצים שהוא יתעלם מהם. אנחנו עושים זאת על ידי יצירת קובץ בשם `.gitignore` בתיקייה הראשית. פתחי את עורך הקוד שלך וצרי קובץ חדש עם השורות הבאות:

    *.pyc
    __pycache__
    myvenv
    db.sqlite3
    .DS_Store
    

לבסוף, תשמרי אותו בתור.gitignore בתיקייה הראשית של הפרויקט.

> **הערה:** הנקודה בתחילת שם הקובץ חשובה! אם יש לך איזושהי בעיה לשמור את הקובץ (במק, למשל, אי-אפשר לייצר קבצים שמתחילים ב-. באמצעות ה-finder), תנסי לעשות Save As בעורך הקוד, זה בדרך-כלל עובד.

זה רעיון טוב להריץ `git status` לפני שמריצים `git add`, או בכל פעם שמשהו משתנה ולא בטוחים מה קורה. זה ימנע הפתעות לא נעימות, כמו תוספות של קבצים לא קשורים. הפקודה `git status` מחזירה דיווח על אודות הקבצים שאנחנו לא עוקבים אחריהם (untracked), שהשתנו (modified) ושסימנו לשמור בפעם הבאה (staged), באיזה ענף אנחנו נמצאים, ועוד כל מיני דברים מעניינים. הפלט שלה צריך להיות משהו כזה:

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
    

ולבסוף נשמור את השינויים. עברי ל - console והריצי את הפקודות הבאות:

    $ git add -A .
    $ git commit -m "My Django Girls app, first commit"
     [...]
     13 files changed, 200 insertions(+)
     create mode 100644 .gitignore
     [...]
     create mode 100644 mysite/wsgi.py
    

## Pushing our code to GitHub

היכנסי ל [Github.com][2] ופתחי משתמש חדש (אם כבר עשית זאת בהכנה לסדנא זה מעולה!)

לאחר מכן, צרי repository חדש ותני לו את השם "my-first-blog". Leave the "initialise with a README" tickbox un-checked, leave the .gitignore option blank (we've done that manually) and leave the License as None.

![][3]

 [3]: images/new_github_repo.png

> **Note** The name `my-first-blog` is important -- you could choose something else, but it's going to occur lots of times in the instructions below, and you'd have to substitute it each time. It's probably easier to just stick with the name `my-first-blog`.

במסך הבא תוכלי לראות את ה - clone URL (כתובת להעתקה) של ה - repository שלך. בחרי בגרסת ה - "HTTPS", העתיקי אותה ובקרוב נעתיק אותה ל terminal:

![][4]

 [4]: images/github_get_repo_url_screenshot.png

כעת אנחנו צריכים לחבר בין ה - repo על המחשב שלך לזאת שנמצאת ב - GitHub.

הקלידי את הפקודות הבאות ב - console שלך (החליפי את `<your-github-username>` בשם המשתמש שבחרת כשיצרת את החשבון ב - GitHub, בלי סוגריים משולשים):

    $ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
    $ git push -u origin master
    

הכניסי את שם המשתמש והסיסמא ל - GitHub ולאחר מכן תראי משהו כזה:

    Username for 'https://github.com': hjwp
    Password for 'https://hjwp@github.com':
    Counting objects: 6, done.
    Writing objects: 100% (6/6), 200 bytes | 0 bytes/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/hjwp/my-first-blog.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.
    

<!--TODO: maybe do ssh keys installs in install party, and point ppl who dont have it to an extention -->

הקוד שלך נמצא כעת ב - GitHub. תבדקי את זה! את תראי שהוא בחברה טובה - [Django][5], [Django Girls Tutorial][6] ופרוייקטי קוד פתוח רבים אחרים גם נמאצים שם :)

 [5]: https://github.com/django/django
 [6]: https://github.com/DjangoGirls/tutorial

# Setting up our blog on PythonAnywhere

> **הערה** יתכן שכבר יצרת חשבון ב - PythonAnywhere במהלך תהליך ההתקנה - אם כן, אין צורך לעשות זאת שוב.

{% include "deploy/signup_pythonanywhere.md" %}

## Pulling our code down on PythonAnywhere

When you've signed up for PythonAnywhere, you'll be taken to your dashboard or "Consoles" page. Choose the option to start a "Bash" console -- that's the PythonAnywhere version of a console, just like the one on your computer.

> **Note** PythonAnywhere is based on Linux, so if you're on Windows, the console will look a little different from the one on your computer.

Let's pull down our code from GitHub and onto PythonAnywhere by creating a "clone" of our repo. Type the following into the console on PythonAnywhere (don't forget to use your GitHub username in place of `<your-github-username>`):

    $ git clone https://github.com/<your-github-username>/my-first-blog.git
    

This will pull down a copy of your code onto PythonAnywhere. Check it out by typing `tree my-first-blog`:

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
    

### Creating a virtualenv on PythonAnywhere

Just like you did on your own computer, you can create a virtualenv on PythonAnywhere. In the Bash console, type:

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
    

> **Note** The `pip install` step can take a couple of minutes. Patience, patience! But if it takes more than 5 minutes, something is wrong. Ask your coach.

<!--TODO: think about using requirements.txt instead of pip install.-->

### Collecting static files.

Were you wondering what the "whitenoise" thing was? It's a tool for serving so-called "static files". Static files are the files that don't regularly change or don't run programming code, such as HTML or CSS files. They work differently on servers compared to on our own computer and we need a tool like "whitenoise" to serve them.

We'll find out a bit more about static files later in the tutorial, when we edit the CSS for our site.

For now we just need to run an extra command called `collectstatic`, on the server. It tells Django to gather up all the static files it needs on the server. At the moment these are mostly files that make the admin site look pretty.

    (mvenv) $ python manage.py collectstatic
    
    You have requested to collect static files at the destination
    location as specified in your settings:
    
        /home/edith/my-first-blog/static
    
    This will overwrite existing files!
    Are you sure you want to do this?
    
    Type 'yes' to continue, or 'no' to cancel: yes
    

Type "yes", and away it goes! Don't you love making computers print out pages and pages of impenetrable text? I always make little noises to accompany it. Brp, brp brp...

    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/actions.min.js'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/inlines.min.js'
    [...]
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/changelists.css'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/base.css'
    62 static files copied to '/home/edith/my-first-blog/static'.
    

### Creating the database on PythonAnywhere

Here's another thing that's different between your own computer and the server: it uses a different database. So the user accounts and posts can be different on the server and on your computer.

We can initialise the database on the server just like we did the one on your own computer, with `migrate` and `createsuperuser`:

    (mvenv) $ python manage.py migrate
    Operations to perform:
    [...]
      Applying sessions.0001_initial... OK
    
    
    (mvenv) $ python manage.py createsuperuser
    

## Publishing our blog as a web app

Now our code is on PythonAnywhere, our virtualenv is ready, the static files are collected, and the database is initialised. We're ready to publish it as a web app!

Click back to the PythonAnywhere dashboard by clicking on its logo, and go click on the **Web** tab. Finally, hit **Add a new web app**.

After confirming your domain name, choose **manual configuration** (NB *not* the "Django" option) in the dialog. Next choose **Python 3.4**, and click Next to finish the wizard.

> **Note** Make sure you choose the "Manual configuration" option, not the "Django" one. We're too cool for the default PythonAnywhere Django setup ;-)

### Setting the virtualenv

You'll be taken to the PythonAnywhere config screen for your webapp, which is where you'll need to go whenever you want to make changes to the app on the server.

![][7]

 [7]: images/pythonanywhere_web_tab_virtualenv.png

In the "Virtualenv" section, click the red text that says "Enter the path to a virtualenv", and enter: `/home/<your-username>/my-first-blog/myvenv/`. Click the blue box with the check mark to save the path before moving on.

> **Note** Substitute your own username as appropriate. If you make a mistake, PythonAnywhere will show you a little warning.

### Configuring the WSGI file

Django works using the "WSGI protocol", a standard for serving websites using Python, which PythonAnywhere supports. The way we configure PythonAnywhere to recognise our Django blog is by editing a WSGI configuration file.

Click on the "WSGI configuration file" link (in the "Code" section near the top of the page -- it'll be named something like `/var/www/<your-username>_pythonanywhere_com_wsgi.py`), and you'll be taken to an editor.

Delete all the contents and replace them with something like this:

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
    

> **Note** Don't forget to substitute in your own username where it says `<your-username>`

This file's job is to tell PythonAnywhere where our web app lives and what the Django settings file's name is. It also sets up the "whitenoise" static files tool.

Hit **Save** and then go back to the **Web** tab.

We're all done! Hit the big green **Reload** button and you'll be able to go view your application. You'll find a link to it at the top of the page.

## Debugging tips

If you see an error when you try to visit your site, the first place to look for some debugging info is in your **error log**. You'll find a link to this on the PythonAnywhere [Web tab][8]. See if there are any error messages in there; the most recent ones are at the bottom. Common problems include:

 [8]: https://www.pythonanywhere.com/web_app_setup/

*   Forgetting one of the steps we did in the console: creating the virtualenv, activating it, installing Django into it, running collectstatic, migrating the database.

*   Making a mistake in the virtualenv path on the Web tab -- there will usually be a little red error message on there, if there is a problem.

*   Making a mistake in the WSGI configuration file -- did you get the path to your my-first-blog folder right?

*   Did you pick the same version of Python for your virtualenv as you did for your web app? Both should be 3.4.

*   There are some [general debugging tips on the PythonAnywhere wiki][9].

 [9]: https://www.pythonanywhere.com/wiki/DebuggingImportError

And remember, your coach is here to help!

# את באוויר!

בדף הבית של האתר צריך להיות כתוב "Welcome to Django", בדיוק כמו במחשב שלך. Try adding `/admin/` to the end of the URL, and you'll be taken to the admin site. Log in with the username and password, and you'll see you can add new Posts on the server.

Give yourself a *HUGE* pat on the back! Server deployments are one of the trickiest parts of web development and it often takes people several days before they get them working. But you've got your site live, on the real Internet, just like that!