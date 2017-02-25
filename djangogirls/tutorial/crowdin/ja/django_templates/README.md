# Djangoテンプレート

何かデータを表示しましょう！Djangoはそれをビルトインの テンプレートタグ で実現できます。

## テンプレートタグとは？

HTMLではブラウザがpythonを認識できないのでpythonのコードは書けません。HTMLはより静的でpythonは動的です。

Djangoテンプレートタグ はHTMLにPyhtonのようなコードを埋め込むことができて、動的なウェブサイトがより早く簡単に作れます!

## ブログ一覧テンプレート

前の章で、posts変数でテンプレートに記事のリストを渡しました。今からHTMLで表示をしてみましょう。

Djangoテンプレートで変数を表示する為には、変数の名前を二重括弧で括ります:

    html
    {{ posts }}
    

れをblog/templates/blog/post_list.htmlに書いてみて下さい。 ２つめと３つ目の<div>
</div>タグをまるごと {{posts}} に置き換えて下さい。 ファイルを保存してページをリロードしますと：

![図 13.1][1]

 [1]: images/step1.png

見たとおり、このようになります。

    [<Post: My second post>, <Post: My first post>]
    

Djangoはオブジェクトのリストと認識します。 Introduction to Pythonを思い出して下さい。 ループを使ってリストを表示しましたよね。 Djangoテンプレートではこう書きます:

    {% for post in posts %}
        {{ post }}
    {% endfor %}
    

これをブログのテンプレートで使ってみましょう。

![図 13.2][2]

 [2]: images/step2.png

動きましたね。 しかし、Introduction to HTMLで作った静的な記事のような表示です。HTMLとテンプレートタグを混ぜてみましょう。 bodyタグの中を次のように書いてください: bodyはこのようにします。

    html
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
    

{% for %}と{% endfor %}の間にリストの中のオブジェクトごとに表示したい内容を書くとオブジェクトの数だけ繰り返し書かれます。ページをリロードしてみましょう。

![図 13.3][3]

 [3]: images/step3.png

post 変数がさっきと違って、{{ post.title }} や {{ post.text }} になっていることに気づきましたか？ Post モデルで定義したそれぞれのフィールドにアクセスしています。 |linebreaks はPostのテキスト中の改行を段落に変換するフィルタに通すという意味です。

## もう一つ...

PythonAnywhereでデプロイして、インターネットでウェブサイトを公開できます。おさらいしましょう。もう一度PythonAnywhereでdeployしてみましょう。もう一度そのステップをおさらいします。

*   まず、GitHubでコードをpushします。

    $ git status
    [...]
    $ git add -A .
    $ git status
    [...]
    $ git commit -m "Modified templates to display posts from database."
    [...]
    $ git push
    

*   そしたら、Pythonanywhereに戻って、Bashコンソール（か、新しいコンソール）に入って、動かしましょう：

    $ cd my-first-blog
    $ git pull
    [...]
    

*   最後にブラウザのタブを開いてアプリをリロードします。更新が反映されています！

おめでとう！これができたら、Django adminとして新しい投稿を追加しましょう。（published_dateを忘れないで！）それから、投稿したものがそこに見えるか、リロードしましょう。

動くのが楽しくなってきたでしょう？少しパソコンから離れて、休憩しましょう：）

![図 13.4][4]

 [4]: images/donut.png