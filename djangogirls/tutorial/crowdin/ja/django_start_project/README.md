# あなたの最初のDjangoプロジェクト！

> このチャプターの一部はGeek Girls Carrots (http://django.carrots.pl/) のチュートリアルに基づいています。
> 
> このチャプターの一部はCreative Commons Attribution-ShareAlike 4.0 International License のライセンスによる django-marcador tutorial に基づいています。 このdjango-marcador tutorialはMarkus Zapke-Gründemann らが著作権を保有しています。 

ここからは、シンプルなブログを作っていきますよ！

最初のステップは、Djangoのプロジェクトを新しく作成します。 基本的に、Djangoのスクリプトを実行しDjangoプロジェクトの骨格を作ります。 スクリプトは、これから使う沢山のファイルやディレクトリを自動生成します。

Djangoでは、ファイルやディレクトリの名前がとても重要です。 作成されたファイルの名前は変えるべきではありません。 ファイルを移動させるのもいいアイディアとはいえません。 Djangoでは、重要なファイルを決められたファイル構成で作成しておくことが必要です。 

> virtualenv（仮想環境）を実行しているでしょうか。 コンソールに(myvenv)という括弧が表示されていなければ、virtualenvを実行してください。 チャプターDjango installationのWorking with virtualenv で、仮想環境を実行する方法を説明しました。 覚えていますか？次のコマンドを入力ですよ。: Windowsでは、myvenv\Scripts\activate, Mac OS / Linuxでは、 myvenv/bin/activate でしたね。

MacOS とLinuxの場合はコンソールで以下のコマンドを実行します。最後のピリオド(ドット) . を忘れないで下さい

    (myvenv) ~/djangogirls$ django-admin startproject mysite .
    

Windowsの場合はこちらです。最後のピリオド(ドット) . を忘れないで下さい。

    (myvenv) C:\Users\Name\djangogirls> django-admin startproject mysite .
    

> コマンドの最後にピリオド (.) があることを確認してくださいね。これば、現在の作業ディレクトリにDjangoをインストールするということを示すので、とても重要なのです。(ピリオドは簡略表記です)
> 
> Note: 上記のコマンドを入力するときは、django-admin または django-admin.py 開始部分のみを入力することを忘れないで下さい。 "(myvenv) ~/djangogirls$ "と"(myvenv) C:\Users\Name\djangogirls"は、あなたの環境のコマンド・ラインで入力を求めてい例です。

django-admin.py は、必要なディレクトリとファイルを作成するスクリプトです。次のようなファイル構造が作成されましたね。:

    djangogirls
    ├───manage.py
    └───mysite
            settings.py
            urls.py
            wsgi.py
            __init__.py
    

`manage.py` is a script that helps with management of the site. With it we will be able to start a web server on our computer without installing anything else, amongst other things.

The `settings.py` file contains the configuration of your website.

Remember when we talked about a mail carrier checking where to deliver a letter? `urls.py` file contains a list of patterns used by `urlresolver`.

Let's ignore the other files for now as we won't change them. The only thing to remember is not to delete them by accident!

## 設定変更

Let's make some changes in `mysite/settings.py`. Open the file using the code editor you installed earlier.

It would be nice to have the correct time on our website. Go to the [wikipedia timezones list][1] and copy your relevant time zone (TZ). (eg. `Europe/Berlin` )

 [1]: http://en.wikipedia.org/wiki/List_of_tz_database_time_zones

In settings.py, find the line that contains `TIME_ZONE` and modify it to choose your own timezone:

    python
    TIME_ZONE = 'Europe/Berlin'
    

Modifying "Europe/Berlin" as appropriate

We'll also need to add a path for static files (we'll find out all about static files and CSS later in the tutorial). Go down to the *end* of the file, and just underneath the `STATIC_URL` entry, add a new one called `STATIC_ROOT`:

    python
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    

## データベース設定

There's a lot of different database software that can store data for your site. We'll use the default one, `sqlite3`.

This is already set up in this part of your `mysite/settings.py` file:

    python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    

To create a database for our blog, let's run the following in the console: `python manage.py migrate` (we need to be in the `djangogirls` directory that contains the `manage.py` file). If that goes well, you should see something like this:

    (myvenv) ~/djangogirls$ python manage.py migrate
    Operations to perform:
      Synchronize unmigrated apps: messages, staticfiles
      Apply all migrations: contenttypes, sessions, admin, auth
    Synchronizing apps without migrations:
       Creating tables...
          Running deferred SQL...
       Installing custom SQL...
    Running migrations:
      Rendering model states... DONE
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying sessions.0001_initial... OK
    

And we're done! Time to start the web server and see if our website is working!

You need to be in the directory that contains the `manage.py` file (the `djangogirls` directory). In the console, we can start the web server by running `python manage.py runserver`:

    (myvenv) ~/djangogirls$ python manage.py runserver
    

If you are on Windows and this fails with `UnicodeDecodeError`, use this command instead:

    (myvenv) ~/djangogirls$ python manage.py runserver 0:8000
    

Now all you need to do is check that your website is running. Open your browser (Firefox, Chrome, Safari, Internet Explorer or whatever you use) and enter the address:

    http://127.0.0.1:8000/
    

The web server will take over your command prompt until you stop it. To type more commands whilst it is running open a new terminal window and activate your virtualenv. To stop the web server, switch back to the window in which it's running and pressing CTRL+C - Control and C buttons together (on Windows, you might have to press Ctrl+Break).

Congratulations! You've just created your first website and run it using a web server! Isn't that awesome?

![It worked!][2]

 [2]: images/it_worked2.png

Ready for the next step? It's time to create some content!