# Django views - time to create!

それでは前の章の続きをやりましょう。確かビューの作成がまだだったので、エラーになっていましたね。

私たちは*view*にアプリケーションのロジックを置きます。 それは前に作成した `モデル` から情報を取得し、それを `テンプレート` に引き渡します。 テンプレートは次の章で作成します。 Viewsは、**Python 入門** の章で書いたものよりも、少し複雑なだけですよ。

ビューは、`views.py` ファイルに記述します。私たちの場合 *ビュー* を `blog/views.py` に書くことになります。

## blog/views.py

OK それでは早速そのファイル（blog/views.py)を開いてみましょう。

    python
    from django.shortcuts import render
    
    # Create your views here.
    

まだ何もないですね。最も単純な*ビュー*は、このように見る事ができます。

    python
    def post_list(request):
        return render(request, 'blog/post_list.html', {})
    

よく見てみましょう。まず` post_list` というメソッド( def から始まる部分のことです)を、記述しています。この` post_list` は`(request)`を引数にとり`render`メソッドを`return`しています。`render`メソッドは<0>blog/post_list.html</0> というテンプレートファイルを使って、引数で受け取った<0>(request)</0>の内容を出力しています。.

ファイルを保存したら、どんな風に表示されるか、ブラウザで http://127.0.0.1:8000/ を確認してみましょう。

今度は別のエラーです。何と書いてあるか読んでみましょう。

![エラー][1]

 [1]: images/error.png

簡単です: *TemplateDoesNotExist*。テンプレートが無いだけです。それでは次の章でテンプレートを作成してみましょう!

> Djangoのビューについてもっと知りたいのなら、英語で書かれていますが、オフィシャルドキュメントを是非読んでみてください https://docs.djangoproject.com/en/1.8/topics/http/views/