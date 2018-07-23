# Django admin

記事の追加や編集、削除するにはdjango adminを使います。

Blog/admin.pyファイルをエディタで開いて、内容をこのように変えて下さい：

    python
    from django.contrib import admin
    from .models import Post
    
    admin.site.register(Post)
    

前章でpostモデルをimportするのを見ました。 Adminページ(管理画面)のモデルを作るために、モデルを登録する必要があります。`admin.site.register(Post)`の部分です。.

OKです、Postモデルについて見ていきましょう。 Web サーバーを実行するコンソールで `python manage.py runserver` を実行してください。 ブラウザーに移動し、次のアドレスを入力してください。 http://127.0.0.1:8000/admin/ このようなログイン ページが表示されます。

![ログインページ][1]

 [1]: images/login_page2.png

ログインには、*superuser*というサイトにすべての制御を持っているユーザーを作成する必要があります。 コマンドラインに戻り、`python manage.py createsuperuser` と入力し、enter キーを押します。 プロンプトが表示されたら、ユーザー名 (小文字、スペースなし)、電子メール アドレス、およびパスワードを入力します。 入力しているパスワードを見ることはできませんが心配しないでください - それについては補完されています。 パスワードを入力したら`enter`を押して終わりです。 出力はこのようになります (ユーザー名と電子メールはあなたが入力したもの)。

    (myvenv) ~/djangogirls$ python manage.py createsuperuser
    Username: admin
    Email address: admin@admin.com
    Password:
    Password (again):
    Superuser created successfully.
    

ブラウザーに戻ります。あなたが先ほど作ったスーパー ユーザーの内容でログインします。 Djangoの管理画面のダッシュ ボードを見ることができます。

![Django admin][2]

 [2]: images/django_admin3.png

記事に移動し、それを少し試してみる。幾つかのブログ記事を追加します。内容について心配しないでください - 時間短縮で、このチュートリアルのテキストをコピー＆ペーストしてみてください。

少なくとも 2 つまたは 3 つの記事 (すべてではない) は 同じ日付あることを確認します。それは後で参考になります。

![Django admin][3]

 [3]: images/edit_post3.png

のマニュアルを確認する必要がありますDjango adminについてもっと知りたい時は、Djangoのドキュメントを見ると良いでしょう。こちらはバージョン1.8のものです。（お使いの環境に合わせたバージョンを参照ください） https://docs.djangoproject.com/en/1.8/ref/contrib/admin/

ここでおそらく、コーヒーか紅茶か何かを食べてリフレッシュする時間をとりましょう。 初めてDjango modelを作成しました。