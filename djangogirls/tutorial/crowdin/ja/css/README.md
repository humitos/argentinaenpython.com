# CSS - make it pretty!

ブログは作ったものの、まだなんかダサいですよね。かわいくしましょう！　そのためにはCSSを使います。

## CSSとは？

Cascading Style Sheets (CSS)とは、マークアップ言語（HTMLなど）で書かれたWebサイトの見た目や書式を記述するのに使われる言語です。私達のWebページにとってのメイクだと思ってください (*＾∀ﾟ)b

でも、またゼロから始めたくはないですよね。 すでにプログラマたちが作ってネットに無料で公開しているものを使いましょう。 すでにあるものをイチから作り直すなんて、車輪を再発明するみたいで楽しくないじゃないですか。

## Let's use Bootstrap!

Bootstrapは、きれいなWebサイトを作るためのHTMLとCSSのフレームワークとして、とっても有名です。

もともとTwitterで働いていたプログラマ達が作ったもので、今では世界中のボランティアの人たちによって開発されています。

## Bootstrapのインストール

Bootstrapをインストールするには、`.html`ファイル（`blog/templates/blog/post_list.html`）の中の`<head>`タグの中にこれを書き加えます：

    html
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    

このコードは、プロジェクトに何のファイルも追加しません。ネット上にあるファイルを指定しているだけです。では、そのまま、あなたのWebサイトを開いて、ページを再読み込みしてみてください。こんな感じ！

![図 14.1][1]

 [1]: images/bootstrap1.png

これだけでずいぶん見た目が良くなりましたね！

## Static files in Django

最後に、**静的ファイル**と呼ばれるものを詳しく見ていきましょう。 静的ファイルとは、CSSファイルや画像ファイルなど、サーバーへのリクエストが行われる環境に依存しない、動的に変わることがないファイルのことです。どのユーザーに対しても内容が同じになります。

### 静的ファイルはプロジェクトのどこに置けばいいの？

`collectstatic`コマンドをサーバー上で実行したときに見たとおり、Djangoは、組み込まれている "admin" アプリのための静的ファイルをどこで探せばいいのか、すでに知っています。私たちがやることは、`blog`アプリのための静的ファイルを追加することだけです。.

そのために、blogアプリの中に`static`というフォルダを作ります。

    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    └── mysite
    

Djangoは、全てのアプリのフォルダ内の、"static"と名づけられた全てのフォルダを自動的に探して、静的ファイルとしてその内容を使うことができます。

## Your first CSS file!

では、いよいよ、CSSファイルを作って、あなたのWebページにあなただけのスタイルを設定していきます。 `static`ディレクトリの中に`css`というディレクトリを作成しましょう。 そして、その`css`ディレクトリの中に`blog.css`という新規ファイルを作ります。 Ready?

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css
    

ついにCSSを書くときが来ました！　コードエディタで`blog/static/css/blog.css`ファイルを開きましょう。

ここでは、CSSについての学習やカスタマイズには、深くは踏み込みません。というのも、結構簡単なので、このワークショップのあと自分で学べるでしょうから。 CSSでWebサイトをさらにかわいくするために必要なことが学ぶのには、[ Codeacademy HTML & CSS course][2] が本当にオススメです。

 [2]: http://www.codecademy.com/tracks/web

ただ、せめて少しはここでやってみましょう。 ヘッダーの色を変えてみるのもいいかもしれませんね。 色を理解するために、コンピュータは特殊なコードを使います。 コードは、`#`で始まり、それにA〜Fのアルファベットや0〜9の数字が6つ続きます。 カラーコードのサンプルはこのサイトで確認できます：http://www.colorpicker.com/ `red`や`green`といった[定義済みの色][3]を利用することもできます。.

 [3]: http://www.w3schools.com/cssref/css_colornames.asp

`blog/static/css/blog.css`ファイルに、次のコードを追加しましょう。

    css
    h1 a {
        color: #FCA205;
    }
    

`h1 a`はCSSセレクタと呼ばれるものです。 `h1`要素の中にある`a`要素（例えばこんなコード：`<h1><a href="">link</a></h1>`）に、スタイルを適用しますよ、という意味です。 この場合、その要素を`#FCA205`に、つまりオレンジ色にしようとしています。 もちろん、あなたの好きな色に変えられます！

CSSファイルには、HTMLファイルの各要素のスタイルを指定していきます。 要素は、要素名（例えば、`a`、`h1`、`body`とか）や`class`属性、`id`属性で識別されます。 classやidは、あなたが自分で要素につけることができる名前です。 classは要素のグループを定義して、idは特定の要素を指定します。 例えば、次のタグは、タグ名`a`、class名`external_link`、id名` link_to_wiki_page`、どれを使ってもCSSによって識別されます。

    html
    <a href="http://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page">
    

CSSセレクタについては[CSS Selectors in w3schools][4]を見てください。.

 [4]: http://www.w3schools.com/cssref/css_selectors.asp

さて、CSSを追加したこともHTMLテンプレートに教えないといけません。`blog/templates/blog/post_list.html`を開いて、先頭にこの行を追加しましょう：

    html
    {% load staticfiles %}
    

これで静的ファイルを読み込みます(^_^) そして、Bootstrap CSSファイルへのリンクの後ろにある、`<head>`と`</head>`の間に、このコードを追加しましょう（ブラウザは受け取った順にファイルを読み込むので、私たちのCSSファイルのコードがBootstrapファイルのコードで上書きされてしまうのです）：

    html
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    

このようにCSSファイルがどこにあるか示します。

ファイルは次のようになっているはずです:

    html
    {% load staticfiles %}
    <html>
        <head>
            <title>Django Girls blog</title>
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
            <link rel="stylesheet" href="{% static 'css/blog.css' %}">
        </head>
        <body>
            <div>
                <h1><a href="/">Django Girls Blog</a></h1>
            </div>
    
            {% for post in posts %}
                <div>
                    <p>published: {{ post.published_date }}</p>
                    <h1><a href="">{{ post.title }}</a></h1>
                    <p>{{ post.text|linebreaks }}</p>
                </div>
            {% endfor %}
        </body>
    </html>
    

保存して、サイトを更新してください。

![図 14.2][5]

 [5]: images/color2.png

素晴らしいですね！あとは、左サイドの余白幅を少し広げて、余裕を持たせてあげたらもっと良くなると思いませんか？やってみましょう。

    css
    body {
        padding-left: 15px;
    }
    

これをCSSに追加して、保存して。さぁ見てみましょう！

![図 14.3][6]

 [6]: images/margin2.png

ヘッダーのフォントを変えてみませんか？ファイル `blog/templates/blog/post_list.html` の`<head>` タグの中に次の一行を貼り付けましょう。

    html
    <link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
    

この行ではGoogle Fonts (https://www.google.com/fonts) から Lobster と呼ばれるフォントを読み込んでいます。

`blog/static/css/blog.css` ファイルを開いて、 `h1 a`というのブロック中に `font-family: 'Lobster';`という行を追加してみましょう　（コードは`{` と `}`で囲まれています）。そしてページを更新します：

    css
    h1 a {
        color: #FCA205;
        font-family: 'Lobster';
    }
    

![図 14.3][7]

 [7]: images/font.png

素晴らしいです！

上に示したように、CSSはHTMLコードの一部に名前をつけて、他に影響を与えずにこの部分にだけスタイルを適用するといった、クラスの概念を持っています。 あなたが2つのdiv要素を持っていた場合これは非情に便利でしょう。しかし、見出しと投稿のように、これらの要素は通常全く違う事を行います。そのため、あなたはこれらを区別して扱いたくなるでしょう。

先に進んで、HTMLコードの一部に名前をつけましょう。ヘッダーに含まれる`div` 要素に、`page-header` というクラス名をつけましょう：

    html
    <div class="page-header">
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>
    

さらにブログ投稿を含む`div` 要素に`post` というクラス名をつけましょう。

    html
    <div class="post">
        <p>published: {{ post.published_date }}</p>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
    

そして、別のセレクタに宣言ブロックを追加します。 `.`で始まるセレクタはクラスに関連します。 Web上にはCSSに関する非常に多くのチュートリアルが存在し、それらは以下に示すコードを理解する手助けになるはずです。 今のところは、`blog/static/css/blog.css`のファイルに以下の内容をコピー＆ペーストしましょう：

    css
    .page-header {
        background-color: #ff9400;
        margin-top: 0;
        padding: 20px 20px 20px 40px;
    }
    
    .page-header h1, .page-header h1 a, .page-header h1 a:visited, .page-header h1 a:active {
        color: #ffffff;
        font-size: 36pt;
        text-decoration: none;
    }
    
    .content {
        margin-left: 40px;
    }
    
    h1, h2, h3, h4 {
        font-family: 'Lobster', cursive;
    }
    
    .date {
        float: right;
        color: #828282;
    }
    
    .save {
        float: right;
    }
    
    .post-form textarea, .post-form input {
        width: 100%;
    }
    
    .top-menu, .top-menu:hover, .top-menu:visited {
        color: #ffffff;
        float: right;
        font-size: 26pt;
        margin-right: 20px;
    }
    
    .post {
        margin-bottom: 70px;
    }
    
    .post h1 a, .post h1 a:visited {
        color: #000000;
    }
    

そして、これをクラス宣言で投稿を表示しているHTMLコードで囲みます。 <0>blog/templates/blog/post_list.html</0> 中のこの部分を

    html
    {% for post in posts %}
        <div class="post">
            <p>published: {{ post.published_date }}</p>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
    

これで置き換えて下さい：

    html
    <div class="content container">
        <div class="row">
            <div class="col-md-8">
                {% for post in posts %}
                    <div class="post">
                        <div class="date">
                            {{ post.published_date }}
                        </div>
                        <h1><a href="">{{ post.title }}</a></h1>
                        <p>{{ post.text|linebreaks }}</p>
                    </div>
                {% endfor %}
            </div>
        </div>
    </div>
    

それらのファイルを保存してWebサイトを更新してみましょう。

![図 14.4][8]

 [8]: images/final.png

やったー！ほら凄いでしょ？この貼り付けたコードを理解するのはそんなに難しいことじゃありません。実際に読んでみることで、そのほとんどを理解することができるでしょう。

CSSをいじることを恐れないで下さい！たとえ何かを壊してしまっても、すぐに元に戻すことができます。

美しいWebサイトを作るために必要な全てのことを学ぶために、この無料のオンライン講座を受講することをおすすめします：[Codeacademy HTML & CSS course][2] （※英語サイトです）

さて、次の章にいく準備はできましたか？^皿^