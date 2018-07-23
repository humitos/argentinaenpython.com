# Django urls

最初のウェブページを立てましょう、あなたのブログです。始めに、djangoのURLについて少し学びましょう。

## URLとは？

URLとは、Webアドレスです。 サイトのURLは、ブラウザのアドレスバーで見ることができます。（そう、127. 0. 0. 1: 8000 や http://djangogirls. com がURLです。） そう、127.0.0.1:8000 や http://djangogirls.com がURLです。

![URL][1]

 [1]: images/url.png

インターネット上のすべてのページには、独自のURLが必要です。 それによって、これから作るアプリケーションが、URLを指定してアクセスしてきたユーザに、何を見せたらいいのかわかるのです。 DjangoではURL_conf（URL設定）と呼ばれるものを使います。 これは、指定されたURLに合わせてDjangoがどのviewを返したらいいか判断する仕組みのことです。

## How do URLs work in Django?

mysite/urls.pyを開いて、中身をみてみると：

    python
    from django.conf.urls import include, url
    from django.contrib import admin
    
    urlpatterns = [
        # Examples:
        # url(r'^$', 'mysite.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),
    
        url(r'^admin/', include(admin.site.urls)),
    ]
    

ご覧のとおり、Djangoは既にこのようなものを置いてくれています。

#で始まっている行はコメント行です。これはPythonによって実行されない行です。とっても便利でしょう？

前の章で訪れたadminのURLについてはすでに書いてありますね。

    python
        url(r'^admin/', include(admin.site.urls)),
    

admin/で始まる全てのURLについて、Djangoが返すべきviewをこの行で指定しています。 今回の場合、adminで始まるURLをたくさん作ることになりますが、その全てをこの小さいファイルに書くようなことはしません。この方がきれいで読みやすいですし。

## 正規表現

どのやってDjangoはビューにURLをマッチするのかと思うかもしれません。 そうです、この部分はひとひねりしています。 Djangoはregex、正規表現を使います。Regexは多くの（本当に多くの）検索パターンのルールを持っています。 理解するのは簡単では無いですが、今は心配しないで下さい。 将来、それらを正確に理解できるでしょう。今回は必要なものだけ使っています。

どのようにパターンが作られるかを理解したいなら、こちらのプロセスの例があります。すなわち、 探し求めているパターンを表現する限定したルールのサブセットだけを理解したい場合は：

    ^ は何らかの文章で始まる
    $は何らかの文章の最後にマッチする
    \dは数字にマッチする
    +は1回以上の繰り返しにマッチ
    () はパターンをくくる
    

URLの定義においては何でも文字通り扱われます。

このようなウェブサイトのアドレスを想像してみてください：http://www.mysite.com/post/12345/ この12345の部分がポストした記事の番号です。

すべてのポストした記事の数を分けて記述することは非常に面倒です。 正規表現でURLにマッチした、記事の番号を取り出すことがパターンで 作れます。 １つずつそれが何を示しているか紐解いてみましょう。

*   ^post/　これはpost/で始まるURL（^のすぐ後）全て扱えます。 `^`)
*   (\d+)は１つか複数の数字を示します。取り出したい番号のことです。
*   /は別の記号が続くのを示します。
*   $は/で終わる後に示します。URLの終わりを示します。

## あなたの初めてDjango url!

さあ最初のURLを作りましょう！'http://127.0.0.1:8000/'はブログの入口ページなので、投稿したブログポストのリストを表示したいです。

mysite/urls.py ファイルは簡潔なままにしておきたいので、mysite/urls.pyではblogアプリからURLをインポートするだけにしましょう。

コメントされた行（#で始まる行）を消して、入口ページのURL（'`'）にはblog.urls`をインポートするように書いてください。`''`).

Mysite/urls.pyファイルはこのようになります：

    python
    from django.conf.urls import include, url
    from django.contrib import admin
    
    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'', include('blog.urls')),
    ]
    

これでDjangoは'http://127.0.0.1:8000/'に来たリクエストは`blog.urls`へリダイレクトするようになり、それ以降はそちらを参照するようになります。

Pythonで正規表現を書く時は、常にrの後に文字を書きます。 これは文字列がPythonで意味しない特別な文字であり、正規表現では意味する文字を含むというヒントになります。

## blog.urls

新しくblogs/urls.pyという空のファイルを作って下さい。そして最初の2行を以下のように書きます：

    python
    from django.conf.urls import url
    from . import views
    

これはDjangoのメソッドと、blogアプリの全てのビュー（といっても、今は一つもありません。すぐに作りますけど！）をインポートするという意味です。

その後、最初のURLパターンを追加します。

    python
    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
    ]
    

これは^$というパターンのURLをpost_listというビューに割り当てたことを意味します。 ^$ とは何を意味しているのでしょうか。それは正規表現のマジックです:）分解してみましょう： 正規表現での^は「文字列の開始」を意味します。ここからパターンマッチを始めます。 $は「文字列の終端」を意味していて、ここでパターンマッチを終わります。 この2つの記号を並べたパターンがマッチするのは、そう、空の文字列です。といっても、DjangoのURL名前解決では'http://127.0.0.1:8000/'は除いてパターンマッチするので、このパターンは'http://127.0.0.1:8000/'自体を意味します。つまり、'http://127.0.0.1:8000/'というURLにアクセスしてきたユーザに対して`views.post_list`を返すように指定していることになります。

The last part `name='post_list'` is the name of the URL that will be used to identify the view. This can be the same as the name of the view but it can also be something completely different. We will be using the named URLs later in the project so it is important to name each URL in the app. We should also try to keep the names of URLs unique and easy to remember.

Django URLconfについて知りたい場合は、公式のドキュメントを見て下さい： https://docs.djangoproject.com/en/1.8/topics/http/urls/

![エラー][2]

 [2]: images/error1.png

どう見ても「うまく動いた」感じはしませんね。でも心配しないで、これはただのエラーページで、怖がるものではありません。むしろ、結構便利なものなんですよ：

'post_list'というアトリビュートがない、と書いてあるのが見えますね。 Post_list と聞いて、何か思い出しませんか？ そう、さっきこのURLに、ビューのpost_listを割り当てたのでした。 でも、ビュー をまだ作ってないんですから、このエラーが出るのは当然ですよね。 なにもおかしいことはしていません。次の章ではビューを作っていきましょう。

> Django URLconfについて知りたい場合は、公式のドキュメントを見て下さい： https://docs.djangoproject.com/en/1.8/topics/http/urls/