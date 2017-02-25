# Deploy!

> **補足** このチャプターはちょっと難しいことが沢山書かれています。 頑張って最後までやりきってください。デプロイはウェブサイトを開発するプロセスの上で、とても重要な部分ですが、躓きやすいポイントも多く含まれています。 チュートリアルの途中にこのチャプターを入れています。そういった躓きやすい箇所はメンターに質問して、あなたが作っているウェブサイトをオンラインでみれるようにしてください。 言い換えれば、もし時間切れでワークショップ内でチュートリアルを終わらせることができなかったとしても、この後のチュートリアルはきっと自分で終わらせることができるでしょう。

今、あなたのウェブサイトはあなたのコンピュータでのみ見る事ができます。ではこれをデプロイする方法を学びましょう。 デプロイとは、あなたが作っているアプリケーションをインターネットで公開することです。あなた以外の人もウェブサイトを見ることができるようになりますよ。

これまでに学んだとおり、ウェブサイトはサーバーに置かれています。 インターネットにはたくさんの利用可能なサーバープロバイダがあります。 私たちは比較的シンプルにデプロイするプロセスを使いましょう。 PythonAnywhere は、多くの人がアクセスするものではない小さいアプリケーションを無料で公開できますので今のあなたには最適でしょう。

使用するその他の外部サービスは [GitHub][1] コードのホスティング サービスです。 他にも色々ありますが、ほとんどのプログラマはGitHubのアカウントを持っています。そしてあなたも今そうなります。

 [1]: http://www.github.com

私達はPythonAnywhereから私たちのコードを転送する方法にGIｔHubを利用します。

# Git

Gitはたくさんのプログラマが利用する「ヴァージョン管理システム」です。 このソフトウェアはファイルの変更を長期にわたって追跡し、あなたは特定のバージョンを後で思い出す事が可能です。 Microsoft Wordに少し変更を追跡する特徴があります、しかしもっと強力です。

## Gitのインストール

> **特徴：**もし、あなたが既にそのインストールをやっている場合は再度行う必要はありません。-あなたは次のセクションにスキップしてあなたのGitリポジトリの作成を開始します。

{% include "deploy/install_git.md" %}

## Starting our Git repository

Gitはリポジトリ（または略して「レポ」）と呼ばれる特定のファイルに変更をセットし追跡します。 私たちのプロジェクトを開始しましょう。 あなたのコンソールを開き、`djangogirls` ディレクトリでこれらのコマンドを実行します。

> **備考：**リポジトリを初期化する前に `pwd` (OSX/Linux) または `cd` (Windows) コマンドで現在の作業ディレクトリを確認してください。 `Djangogirls` フォルダーにする必要があります。

    $ git init
    Initialized empty Git repository in ~/djangogirls/.git/
    $ git config --global user.name "Your Name"
    $ git config --global user.email you@example.com
    

我々 だけのプロジェクトごとに 1 回行う必要があるものは、git リポジトリを初期化する事 (とユーザー名を入力し直して、再びこれまでメールする必要はありません)。

Git のすべてのファイルおよびこのディレクトリ内のフォルダーの変更を追跡しますが、無視するいくつかのファイルがあります。 ベース ディレクトリの `.gitignore` という名前のファイルを作成することによってこれを行います。 あなたのエディターを開き、次の内容で新しいファイルを作成します。

    *.pyc
    __pycache__
    myvenv
    db.sqlite3
    .DS_Store
    

`.Gitignore` トップレベルの"djangogirls"フォルダーとして保存します。

> **備考：**ファイル名の先頭のドットは重要です! もしそのファイルを作るのが難しいなら、（Macをお使いの型はFinderからどっとで始まるファイルが作られていません。）そういう時はエディタでSave Asから作成すれば問題ありません。

`Git に追加` する前に、またはあなたは自分が何が変わったのかわからない見つけるたびに `git status` コマンドを使用することをお勧めします。 これは間違ったファイルを追加またはコミットなど思いもかけない事を止めるのを助けます。 `Git status` コマンドは、untracked/modifed/staged filesおよび多くについての情報を返します。 出力はこのようになります。：

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
    

最終的に我々 は、変更内容を保存します。本体に移動し、これらのコマンドを実行します。

    $ git add -A .
    $ git commit -m "My Django Girls app, first commit"
     [...]
     13 files changed, 200 insertions(+)
     create mode 100644 .gitignore
     [...]
     create mode 100644 mysite/wsgi.py
    

## Pushing our code to GitHub

新しい、無料のアカウント [GitHub.com][1] とサインに行きます。(あなたはすでにワーク ショップ準備をしました、素晴らしい!)

そして、新しいリポジトリに "my-first-blog"の名前で新しいリポジトリを作成します。 「Readme ファイルで初期化」tickbox の解除にチェックを残す、(我々 は手動でそれをやった) .gitignore オプションの空白のままに、None としてライセンスを残します。

![][2]

 [2]: images/new_github_repo.png

> **備考：** `my-first-blog`の名前が重要です --あなたは他の何かを選ぶこともできた、しかしそれは以下の指示の時間の多くが発生するたびにそれを置き換える必要があります。 `my-first-blog`の名前にしておくことは簡単でしょう。.

次の画面では、あなたの repo のクローンの URL が表示されます。"HTTPS"のバージョンを選択してコピーし端末にそれを貼り付けます。

![][3]

 [3]: images/github_get_repo_url_screenshot.png

今私たちはGitリポジトリをGitHubのコンピュータにフックする必要があります。

本体 ( `< あなた github 名 >` GitHub のアカウントを作成したときに入力したユーザー名） に、次を入力します。

    $ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
    $ git push -u origin master
    

あなたのGit Hubのユーザー名とパスワードを入力してください。そしてあなたはこのように見るべきです。

    Username for 'https://github.com': hjwp
    Password for 'https://hjwp@github.com':
    Counting objects: 6, done.
    Writing objects: 100% (6/6), 200 bytes | 0 bytes/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/hjwp/my-first-blog.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.
    

<!--TODO: maybe do ssh keys installs in install party, and point ppl who dont have it to an extention -->

コードは GitHub 上で公開されます。 それをチェックしにいってください。 あなたは良い会社を見つけるでしょう。[Django][4]、[Django Girls Tutorial][5]、および他の多くの偉大なオープン ソース ソフトウェア プロジェクトは GitHub 上でコード:) ホストを見つけること

 [4]: https://github.com/django/django
 [5]: https://github.com/DjangoGirls/tutorial

# Setting up our blog on PythonAnywhere

> **備考：**あなたがすでにPythonAnywhereのアカウントを以前に作成しインストールの手順をふんでいたら、再びそれを行う必要はありません。

{% include "deploy/signup_pythonanywhere.md" %}

## Pulling our code down on PythonAnywhere

PythonAnywhere のサインアップしているときダッシュ ボードまたは「コンソール」ページが表示されます。 ” Bash”コンソールを始めるためにオプションを選択してください。-それは、コンソール（ちょうどあなたのコンピュータのもののような）のPythonAnywhereバージョンです。

> **備考：**PythonAnywhere は Linux に基づきますので、Windows の場合は、あなたのコンピュータ上で進行中のものと少し違って見えるでしょう。

私たちのレポにクローンを作ることによって、GitHubとPythonAnywhere上から私たちのコードをpull downしましょう。 PythonAnywhere のコンソールに、次を入力 (GitHub ユーザー名 `< あなた github 名 >` の代わりを使用することを忘れないでください)。

    $ git clone https://github.com/<your-github-username>/my-first-blog.git
    

これは、PythonAnywhere にあなたのコードのコピーをおろします。タイピングによってそれをチェックします`tree my-first-blog`

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

同じように、自分のコンピューターにした PythonAnywhere の仮想環境を作成できます。Bash のコンソールでは、次の内容を入力します。

    $ virtualenv --python=python3.4 myvenv
    Running virtualenv with interpreter /usr/bin/python3.4
    [...]
    Installing setuptools, pip...done.
    
    $ source myvenv/bin/activate
    
    (mvenv) $  pip install django whitenoise
    Collecting django
    [...]
    Successfully installed django-1.8.2 whitenoise-2.0
    

> **備考：**`pip をインストール` ステップが数分をかかります。 忍耐、忍耐! しかし、何かが間違っている場合は、5 分以上かかります。 その時はコーチに確認してください。

<!--TODO: think about using requirements.txt instead of pip install.-->

### 静的ファイルを収集

あなたは、「whitenoise」ものが何であるかについて疑問に思っていましたか？ いわゆる「静的ファイル」を提供するためのツールです。 静的ファイルは、変更しないでください定期的に、HTML や CSS ファイルなど、プログラミング コードを実行しないでください。 彼らは我々 自身のコンピューター上と比較してサーバーで異なる動作し、それらを提供する「whitenoise」のようなツールが必要です。

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
    

### PythonAnywhereにデータベース生成

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

![][6]

 [6]: images/pythonanywhere_web_tab_virtualenv.png

In the "Virtualenv" section, click the red text that says "Enter the path to a virtualenv", and enter: `/home/<your-username>/my-first-blog/myvenv/`. Click the blue box with the check mark to save the path before moving on.

> **Note** Substitute your own username as appropriate. If you make a mistake, PythonAnywhere will show you a little warning.

### Configuring the WSGI file

Django works using the "WSGI protocol", a standard for serving websites using Python, which PythonAnywhere supports. The way we configure PythonAnywhere to recognise our Django blog is by editing a WSGI configuration file.

Click on the "WSGI configuration file" link (in the "Code" section near the top of the page -- it'll be named something like `/var/www/<your-username>_pythonanywhere_com_wsgi.py`), and you'll be taken to an editor.

すべての内容を削除し、下の内容を書いてください。

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
    

> **注意**`<your-username>`にあなたのusernameを入れることを忘れないように気をつけてください。

This file's job is to tell PythonAnywhere where our web app lives and what the Django settings file's name is. It also sets up the "whitenoise" static files tool.

**セーブ(save)**を押して**Web**タブを押します。

We're all done! Hit the big green **Reload** button and you'll be able to go view your application. You'll find a link to it at the top of the page.

## デバッギングのヒント

If you see an error when you try to visit your site, the first place to look for some debugging info is in your **error log**. You'll find a link to this on the PythonAnywhere [Web tab][7]. See if there are any error messages in there; the most recent ones are at the bottom. Common problems include:

 [7]: https://www.pythonanywhere.com/web_app_setup/

*   Forgetting one of the steps we did in the console: creating the virtualenv, activating it, installing Django into it, running collectstatic, migrating the database.

*   Making a mistake in the virtualenv path on the Web tab -- there will usually be a little red error message on there, if there is a problem.

*   Making a mistake in the WSGI configuration file -- did you get the path to your my-first-blog folder right?

*   Did you pick the same version of Python for your virtualenv as you did for your web app? Both should be 3.4.

*   There are some [general debugging tips on the PythonAnywhere wiki][8].

 [8]: https://www.pythonanywhere.com/wiki/DebuggingImportError

覚えてください。あなたのコーチたちはあなたのためにここにいます。

# You are live!

The default page for your site should say "Welcome to Django", just like it does on your local computer. Try adding `/admin/` to the end of the URL, and you'll be taken to the admin site. Log in with the username and password, and you'll see you can add new Posts on the server.

Give yourself a *HUGE* pat on the back! Server deployments are one of the trickiest parts of web development and it often takes people several days before they get them working. But you've got your site live, on the real Internet, just like that!