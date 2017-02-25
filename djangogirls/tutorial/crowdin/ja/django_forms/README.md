# Djangoのフォーム

自分のwebサイトで最終的にやりたいことは、ブログポストを追加したり編集したりすることをいいやり方で作ることです。 Djanogo adminはかなりいいですが、カスタマイズや上手く作るのはより難しいです。 フォームによってインターフェイス上でものすごい力を持っています。 - 私たちが想像する処理がほとんど行うことができます!

Djangoのフォームでよいところは、フォームをスクラッチで定義できたり、モデルからフォームを生成できるところです。

これはまさに私たちがやりたいことです：Postモデルを作ります。

Djangoのフォームの重要な部分は`forms.py`ファイルで持ちます。.

これは`blog`ディレクトリの下にforms. pyの名前で作る必要があります。

    blog
       └── forms.py
    

forms. pyファイルを開き、次のコードをタイプしてください。

    from django import forms
    
    from .models import Post
    
    class PostForm(forms.ModelForm):
    
        class Meta:
            model = Post
            fields = ('title', 'text',)
    

Djangoのフォームクラスをインポートする必要があります。それが`rom django import forms`の部分です。そして`from .models import Post`はポストモデルをインポートしています。).

PostFormとは何かと思うかもしれません。これはフォームを作る時に定義する名前です。 Djangoでいう、このフォームはModelForm(Djangoは私たちにマジックをする）です。`forms.ModelForm`はPostFormの引数です。

次に`class Meta`ですが、Postモデルを使う時、このフォーム`model = Post`を使います。).

最後にフォームのフィールドに何を置くか書きます。 このシナリオで、私たちは`title` と `text`の部分でタイトルと本文を公開します。 `author`は現在ログインしている人（あなた）です。 `created_date` は自動的に記事ポストを書いた時間が設定されます。

そしてそうです！今私たちが ビューで必要なのは、フォームを使うことです。テンプレートがあるので、それを示します。

もう一度ファイルを作ります。：ページへのリンク、URL、ビューとテンプレートです。

## フォームにおけるページへのリンク

`blog/templates/blog/base.html`を開いてみましょう。ページヘッダというdivのリンクに次の内容を追加しましょう。

    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    

`post_new`という新しいビューを作ります。.

行を追加すると、このような html ファイルになります。

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
    

Htmlファイルを保存して、ページをリロードします。 `NoReverseMatch` エラーが表示されます?

## URL

blog/urls.pyを開き、次の内容を追加します。

        url(r'^post/new/$', views.post_new, name='post_new'),
    

次に、このような内容を追加します。

    from django.conf.urls import include, url
    from . from django.conf.urls import include, url
    from . import views
    
    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
        url(r'^post/new/$', views.post_new, name='post_new'),
    ]
    

サイトをリロードした後、`AttributeError`が出ます。`post_new`ビューの実装がないからです。ファイルに追加してみましょう。

## post_new view

blog/views.pyを開きます。fromの行の後に次の内容を追加してみましょう。

    from .forms import PostForm
    

その後にビューを追加します。

    def post_new(request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    

Postフォームを新しく作るには、PostFormを呼び出し、それをテンプレートに渡す必要があります。 ビューに戻り、いまからフォームのテンプレートを作りましょう。

## テンプレート

blog/templates/blogディレクトリにpost_edit.htmlファイルを作りましょう。フォームを動かすにはいくつかやることがあります。

*   フォームを表示するには、例えば単純に{% raw %}{{ form.as_p }}{% endraw %}でできます。.
*   上記の行は HTML フォーム タグでラップする必要があります: `<form method="POST">...</form>`
*   `保存` のボタンが必要です。HTML ボタンで行う: `<button type="submit">Save</button>`
*   最後に`<form ...>` タグを開いて、 `{% raw %}{% csrf_token %}{% endraw %}`を追加する必要があります。 フォームを安全に保護できるのでこれは非常に重要です! Djangoはフォームを保存した際にこれを忘れると、アラートが出るでしょう。

![CSFR Forbidden page][1]

 [1]: images/csrf2.png

OK,そうしたらどのようにHTMLで`post_edit.html`表すか見て下さい：

    {% extends 'blog/base.html' %}
    
    {% block content %}
        <h1>New post</h1>
        
    {% endblock %}
    

更新をしてみましょう。やった！フォームが表示されます。

![New form][2]

 [2]: images/new_form2.png

ちょっと待ってみて下さい。`title` and `text` フィールドに何か入力して保存するとどうなりますか？

何もない!我々 は再び同じページと私たちのテキストはあの新しい記事は追加されません。なぜこうなってしまったのか？

答えは: ないからです。ビュー で、もう少し作業を行う必要があります。.

## Formをsaveする

`Blog/views.py` をもう一度開きます。現在は `post_new` ビューはこうなっています。

    def post_new(request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    

フォームを送信する時、同じビューに戻るが、リクエストにデータがあると、POSTされます。（ブログポストとは関係ない、データをポストしている） HTMLファイル formの定義はPOSTメソッドを使うのを覚えていますか？ フォームの全てのフィールドがPOSTリクエストです。 POST の名前を他の名前に変更することはできません (それを変更する唯一の方法は method に GET を指定することですが、それがなぜ間違いであるかを話す時間がありません)

そのため view では2つの状況をハンドルするようにします。 1つ目は初回アクセス時で空のフォームが欲しい時です。 2つ目はフォームの入力を終えて全てのフォームのデータともに view に戻る時です。 それでは [...] の部分を埋めていきます。

    python
    if request.method == "POST":
        [...]
    else:
        form = PostForm()
    

Method が POST の場合、フォームから送られたデータを用いて PostForm を作成するために次のようにします:

    python
    form = PostForm(request.POST)
    

簡単ですね! 次にフォームの値が正しいかどうかをチェックします（すべての必須フィールドが設定され、全く誤った値が保存されていないことを）。 form.is_valid() を使うことでチェックできます。.

フォームをチェックして、フォームの値が有効であれば保存できます。

    python
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
    

基本的にここでは2つのことを行います。まず form.save でフォームを保存することと author を追加することです(まだ PostForm 内に author フィールドがありませんし、このフィールドは必須です)。 commit=False は Post モデルをまだセーブしません。ではauthorを追加します。commit=False を指定せず form.save() を実行します。 そしてこのケースではそれが必要です。 post.save() は変更(authorの追加) を保存し、新しいブログ記事を作成します。

最後に、新しく作成された記事の post_detail ページを表示できれば良いですよね? そのために次のインポートを追加します:

    python
    from django.shortcuts import redirect
    

それをファイルの先頭に追加します。これでようやく、新しく作成されたポストのための post_detail ページに移動する処理を書けます。

    python
    return redirect('blog.views.post_detail', pk=post.pk)
    

blog.views.post_detail は新しく作成されたポストのために post_detail ページに移動するためのビューです。 この view では pk 変数が必須であることを覚えていますか? post では新しいブログ記事が作成されます。

OK, たくさんのことを説明しました。全体の view は以下のようになります。

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
    

では動作確認してみます。 http://127.0.0.1:8000/post/new/ に行き、 title と text を追加し、保存します...。 できあがり! 新しいブログ記事が追加され、post_detail にリダイレクトされます！

おそらくあなたは日付が設定されていないことに気づいたことでしょう。それについては Django Girls Tutorial: Extensions 内の publish button をみてください。.

素晴らしい！

## フォームのバリデーション(検証)

ここではDjangoのフォームのクールなところを紹介します。 ブログのポストは title と text のフィールドが必要です。 Post モデルでは、これらのフィールドがなくてもよいとは書いておらず(デフォルトの値が設定されている published_date とは対照的に)、Djangoではその場合、それらのフィールドには何らかの値が設定されないとエラーが起こるようになっています。

title と text を入力せずに保存してみましょう。何が起こるでしょうか?

![フォームのバリデーション(検証)][3]

 [3]: images/form_validation2.png

Djangoはフォームのすべてのフィールドが正しいことを検証してくれます。気が利くでしょう?

> ここでは現在、Djangoの管理画面と同様に、ログイン状態で操作しています。 いくつかの状況ではログアウト状態になることがあります(ブラウザを閉じる、DBを再起動するなど..)。 ポストの作成時にログインユーザがわからないことでエラーが発生した場合、管理画面に移動し再度ログインすることで、 その問題は一時的に解決します。 メインチュートリアルの後 Homework: add security to your website! の章に恒久的な対策がありますので宿題として取り組んでみてください。

![Logged in error][4]

 [4]: images/post_create_error.png

## フォームの編集

今、私たちは新しいフォームを追加する方法を知っています。 しかし既存のデータを編集するためはどうすれば良いのでしょうか? それは先ほど行ったことと非常に似ています。 すぐにいくつかの重要なものを作成してみましょう。（もしわからない場合、コーチに尋ねるか、もしくはすでに手順をカバーしているので、前の章を見てください）

blog/templates/blog/post_detail.html を開いて次の行を追加します:

    python
    <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    

テンプレートは次のようになります:

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
    

blog/urls.py には次の行を追加します:

    python
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    

テンプレート blog/templates/blog/post_edit.html を再利用します。そしてviewを追加します。.

blog/views.py を開いて次をファイルの最後に追加します:

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
    

post_view とほとんど同じに見えますか? しかし完全に同じではありません。 まずURLから pk パラメータを渡します。次に Post モデルを get_object_or_404(Post, pk=pk) で取得します。 その後フォームを保存する際、この記事をインスタンスとしてフォームを作成します。

    python
    form = PostForm(request.POST, instance=post)
    

そしてこの記事でフォームを開き編集します。

    python
    form = PostForm(instance=post)
    

Ok, 動作確認しましょう。 post_detail ページにいきます。そこの右上に [編集] ボタンがあるはずです:

![Edit button][5]

 [5]: images/edit_button2.png

クリックするとブログの記事にフォームが表示されます:

![フォームの編集][6]

 [6]: images/edit_form2.png

あとはお気軽にタイトルやテキストを変更して保存してください。

おめでとう！アプリケーションが完成しました。

Djangoのフォームについての詳細を知りたい場合、Django Projectのドキュメントを読んでください: https://docs.djangoproject.com/en/1.8/topics/forms/

## Security

Being able to create new posts just by clicking a link is awesome! But, right now, anyone that visits your site will be able to post a new blog post and that's probably not something you want. Let's make it so the button shows up for you but not far anyone else.

In `blog/templates/blog/base.html`, find our `page-header` `div` and the anchor tag you put in there earlier. It should look like this:

    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    

We're going to add another `{% if %}` tag to this which will make the link only show up for users that are logged into the admin. Right now, that's just you! Change the `<a>` tag to look like this:

    html
    {% if user.is_authenticated %}
        <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    {% endif %}
    

This `{% if %}` will cause the link to only be sent to the browser if the user requesting the page is logged in. This doesn't protect the creation of new posts completely, but it's a good first step. We'll cover more security in the extension lessons.

Since you're likely logged in, if you refresh the page, you won't see anything different. Load the page in a new browser or an incognito window, though, and you'll see that the link doesn't show up!

## もう一つ: deployの時間です!

ではPythonAnywhere上で動作するかを確認しましょう。再度デプロイします。

*   なおデプロイ方法を忘れてしまった場合は章の最後 Deploy をチェックしてください: 

    $ git status
    $ git add -A .
    $ git status
    $ git commit -m "Added views to create/edit blog post inside the site."
    $ git push
    

*   そうすると、PythonAnywhereのbashコンソールで見ると：

    $ cd my-first-blog
    $ source myvenv/bin/activate
    (myvenv)$ git pull
    [...]
    (myvenv)$ python manage.py collectstatic
    [...]
    

*   最後に、Webタブに行って、リロードします。.

そしてdeployします! おめでとうございます :)