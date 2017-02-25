# DjangoのORMとクエリセット

この章では、Djangoのデータベース接続方法と、データストアについて学びます。やってみましょう！

## クエリセットとは？

クエリセットが何かと言うと、モデルが提供しているオブジェクトのリストのことです。クエリセットは、データベースからデータを読み込んだり、抽出したり、言われた通りにやってくれます。

実際に動かしてみるのが一番わかりやすいので、試してみましょう。

## Django shell

コンソール画面を開いて、次のコマンドを入力してみましょう。

    (myvenv) ~/djangogirls$ python manage.py shell
    

次のような表示に切り替わるでしょう。

    (InteractiveConsole)
    >>>
    

今、Djangoのインタラクティブコンソールが起動しています。Pythonプロンプトしかないように見えますが、ちゃんとDjangoも動いています。勿論このコンソール画面では、Pythonのコマンドは何でも使えます。

### All objects

最初に、ポストデータを全部表示させてみましょう。次のコマンドで、ポストのデータを全部表示させることが出来ます。

    >>> Post.objects.all()
    Traceback (most recent call last):
          File "<console>", line 1, in <module>
    NameError: name 'Post' is not defined
    

ごめんなさい、エラーになってしまいましたね。Postがないというエラーです。その通りなんです。最初にインポートをしなくてはならないのに、忘れていました。

    >>> from blog.models import Post
    

こんな風に書くだけで、blog.modelsからPostモデルをインポート出来ます。それでは、もう一度試してみましょう。

    >>> Post.objects.all()
    [<Post: my post title>, <Post: another post title>]
    

さっきDjangoの管理画面から作ったポストのリストが表示されました。だけど、次はこのコンソール画面から、新たにポストを作ってみたいですよね。それはどうすればいいのでしょうか。

### Create object

データベースに、新しいPostを作成するには、次のようにします。

    >>> Post.objects.create(author=me, title='Sample title', text='Test')
    

いい感じなのですが、1つだけマズイことをしているんです。authorに me を渡していますが、これは User モデルのインスタンスでないといけませんよね。それは、どうやればいいと思います？

そうです、さっきと同じです。Userモデルも先にインポートしておきましょう。

    >>> from django.contrib.auth.models import User
    

どんなユーザが、データベースに登録されてましたっけ？覗いてみましょうか。

    >>> User.objects.all()
    [<User: ola>]
    

作成しておいたスーパーユーザがいますね。このユーザを使ってみましょう。

    me = User.objects.get(username='ola')
    

Ola というユーザ名の User モデルのインスタンスを、取り出せたでしょう？よかった！勿論、他のユーザ名のユーザを取り出しても構いません。

さあ、遂にコンソール画面から、最初のポストを作成出来ますね。

    >>> Post.objects.create(author=me, title='Sample title', text='Test')
    

どうでしょうか？ちゃんと出来ているか、確認しておきましょうね。

    >>> Post.objects.all()
    [<Post: my post title>, <Post: another post title>, <Post: Sample title>]
    

There it is, one more post in the list!

### Add more posts

この先の楽しみの為にも、もう2〜3個、記事を作っておきましょう。そうすれば、もっとよくこの章を理解出来ると思います。

### Filter objects

クエリセットの大部分は、フィルタ機能だと言えるでしょう。 ユーザolaさんのポストを全部確認してみましょうか。 全部のポストを取り出すのではなく、olaさんのポストだけを取り出したい場合は、Post.objects.all() の all を filter に変更します。 クエリセットの結果として、カッコの中に、blogの内容が一覧で表示されました。 以下の例だと、 author が me と等しいものだけが抽出されています。 Djangoでの表し方は、`author=me`となります。 このようになりますね。

    >>> Post.objects.filter(author=me)
    [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]
    

もしかすると title フィールドに title という単語が含まれているポストだけを取り出したくなるかもしれませんね。

    >>> Post.objects.filter(title__contains='title')
    [<Post: Sample title>, <Post: 4th title of post>]
    

> **Note** title と contains の間に、アンダーバーが2個続いていますが、 これはDjangoのORMの構文です。フィールド名のtitleと、照合タイプのcontainsを、2つのアンダーバーで連結させています。 もしアンダーバーが1個だけだと、title_contains というフィールド名だと判断されてしまい、エラーになります。("FieldError: Cannot resolve keyword title_contains")

また、公開済みの全ポストを取り出すことも出来ます。全てのポストの中から、既に公開済みのポストを取り出してみましょう。それには、 published_date を指定します。

> > > from django.utils import timezone Post.objects.filter(published_date__lte=timezone.now()) []

Unfortunately, the post we added from the Python console is not published yet. We can change that! First get an instance of a post we want to publish:

    >>> post = Post.objects.get(title="Sample title")
    

And then publish it with our `publish` method!

    >>> post.publish()
    

Now try to get list of published posts again (press the up arrow button 3 times and hit `enter`):

    >>> Post.objects.filter(published_date__lte=timezone.now())
    [<Post: Sample title>]
    

### Ordering objects

QuerySets also allow you to order the list of objects. Let's try to order them by `created_date` field:

    >>> Post.objects.order_by('created_date')
    [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]
    

We can also reverse the ordering by adding `-` at the beginning:

    >>> Post.objects.order_by('-created_date')
    [<Post: 4th title of post>,  <Post: My 3rd post!>, <Post: Post number 2>, <Post: Sample title>]
    

### Chaining QuerySets

You can also combine QuerySets by **chaining** them together:

    >>> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    

This is really powerful and lets you write quite complex queries.

Cool! You're now ready for the next part! To close the shell, type this:

    >>> exit()
    $