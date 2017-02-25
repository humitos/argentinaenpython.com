# HTML 入門

テンプレートとは何でしょうか？

A template is a file that we can re-use to present different information in a consistent format - for example, you could use a template to help you write a letter, because although each letter might contain a different message and be addressed to a different person, they will share the same format.

A Django template's format is described in a language called HTML (that's the HTML we mentioned in the first chapter **How the Internet works**).

## HTMLとは？

HTML is a simple code that is interpreted by your web browser - such as Chrome, Firefox or Safari - to display a webpage for the user.

HTML stands for "HyperText Markup Language". **HyperText** means it's a type of text that supports hyperlinks between pages. **Markup** means we have taken a document and marked it up with code to tell something (in this case, a browser) how to interpret the page. HTML code is built with **tags**, each one starting with `<` and ending with `>`. These tags represent markup **elements**.

## 最初のテンプレート

Creating a template means creating a template file. Everything is a file, right? You have probably noticed this already.

Templates are saved in `blog/templates/blog` directory. So first create a directory called `templates` inside your blog directory. Then create another directory called `blog` inside your templates directory:

    blog
    └───templates
        └───blog
    

(You might wonder why we need two directories both called `blog` - as you will discover later, this is simply a useful naming convention that makes life easier when things start to get more complicated.)

And now create a `post_list.html` file (just leave it blank for now) inside the `blog/templates/blog` directory.

あなたのウェブサイトを見てみてください: http://127.0.0.1:8000/

> `TemplateDoesNotExists`エラーが発生する場合、サーバーを再起動してください。 コマンドラインで、Ctrl+C（CtrlとCを同時）を押してサーバーを停止し、`python manage.py runserver`コマンドで起動します。

![図 11.1][1]

 [1]: images/step1.png

No error anymore! Congratulations :) However, your website isn't actually publishing anything except an empty page, because your template is empty too. We need to fix that.

Add the following to your template file:

    html
    <html>
        <p>Hi there!</p>
        <p>It works!</p>
    </html>
    

それではあなたのウェブサイトを見てみてください: http://127.0.0.1:8000/

![図 11.2][2]

 [2]: images/step3.png

It worked! Nice work there :)

*   The most basic tag, `<html>`, is always the beginning of any webpage and `</html>` is always the end. As you can see, the whole content of the website goes between the beginning tag `<html>` and closing tag `</html>`
*   `<p>` is a tag for paragraph elements; `</p>` closes each paragraph

## Head と body

それぞれのHTMLページは**head**と**body**という要素によって2つにわけられています。.

*   **head**は文書についての情報を含む要素で、画面には表示されません。

*   **body**はWebページの一部として表示されるすべてを含む要素です。

`<head>`でページの設定をブラウザに伝え、`<body>`でページの内容を伝えます。

例えば、以下のように`<head>`にタイトル要素を入れることができます：

    html
    <html>
        <head>
            <title>ブログ</title>
        </head>
        <body>
            <p>こんにちは！</p>
        </body>
    </html>w
    

ファイルを保存し、ページを更新してください。

![図 11.3][3]

 [3]: images/step4.png

Notice how the browser has understood that "Ola's blog" is the title of your page? It has interpreted `<title>Ola's blog</title>` and placed the text in the title bar of your browser (it will also be used for bookmarks and so on).

Probably you have also noticed that each opening tag is matched by a *closing tag*, with a `/`, and that elements are *nested* (i.e. you can't close a particular tag until all the ones that were inside it have been closed too).

It's like putting things into boxes. You have one big box, `<html></html>`; inside it there is `<body></body>`, and that contains still smaller boxes: `<p></p>`.

You need to follow these rules of *closing* tags, and of *nesting* elements - if you don't, the browser may not be able to interpret them properly and your page will display incorrectly.

## テンプレートのカスタマイズ

You can now have a little fun and try to customize your template! Here are a few useful tags for that:

*   `<h1>A heading</h1>` - for your most important heading
*   `<h2>A sub-heading</h2>` for a heading at the next level
*   `<h3>A sub-sub-heading</h3>` ... and so on, up to `<h6>`
*   `<em>text</em>` emphasizes your text
*   `<strong>text</strong>` strongly emphasizes your text
*   `<br />` goes to another line (you can't put anything inside br)
*   `<a href="http://djangogirls.org">link</a>` creates a link
*   `<ul><li>first item</li><li>second item</li></ul>` makes a list, just like this one!
*   `<div></div>` defines a section of the page

テンプレートの例：

    html
    <html>
        <head>
            <title>Django Girlsのブログ</title>
        </head>
        <body>
            <div>
                <h1><a href="">Django Girlsのブログ</a></h1>
            </div>
    
            <div>
                <p>公開日: 2014/06/14, 12:14</p>
                <h2><a href="">最初の投稿</a></h2>
                <p> こんにちは！ よろしくお願いします！ </p>
            </div>
    
            <div>
                <p>公開日: 2014/06/14, 12:14</p>
                <h2><a href="">2番目の投稿</a></h2>
                <p> こんにちは！ よろしくお願いします！ </p>
            </div>
        </body>
    </html>
    

ここで3つの `div` セクションを作成しました。

*   最初の`div`要素には、ブログのタイトル（見出しとリンク）が含まれています。
*   Another two `div` elements contain our blogposts with a published date, `h2` with a post title that is clickable and two `p`s (paragraph) of text, one for the date and one for our blogpost.

It gives us this effect:

![図 11.4][4]

 [4]: images/step6.png

Yaaay! But so far, our template only ever displays exactly **the same information** - whereas earlier we were talking about templates as allowing us to display **different** information in the **same format**.

What we really want to do is display real posts added in our Django admin - and that's where we're going next.

## One more thing: deploy!

It'd be good to see all this out and live on the Internet, right? Let's do another PythonAnywhere deploy:

### Commit, and push your code up to Github

First off, let's see what files have changed since we last deployed (run these commands locally, not on PythonAnywhere):

    $ git status
    

Make sure you're in the `djangogirls` directory and let's tell `git` to include all the changes within this directory:

    $ git add -A .
    

> **Note** `-A` (short for "all") means that `git` will also recognize if you've deleted files (by default, it only recognizes new/modified files). Also remember (from chapter 3) that `.` means the current directory.

Before we upload all the files, let's check what `git` will be uploading (all the files that `git` will upload should now appear in green):

    $ git status
    

We're almost there, now it's time to tell it to save this change in its history. We're going to give it a "commit message" where we describe what we've changed. You can type anything you'd like at this stage, but it's helpful to type something descriptive so that you can remember what you've done in the future.

    $ git commit -m "Changed the HTML for the site."
    

> **Note** Make sure you use double quotes around the commit message.

Once we've done that, we upload (push) our changes up to Github:

    git push
    

### Pull your new code down to PythonAnywhere, and reload your web app

*   Open up the [PythonAnywhere consoles page][5] and go to your **Bash console** (or start a new one). Then, run:

 [5]: https://www.pythonanywhere.com/consoles/

    $ cd ~/my-first-blog
    $ source myvenv/bin/activate
    (myvenv)$ git pull
    [...]
    (myvenv)$ python manage.py collectstatic
    [...]
    

And watch your code get downloaded. If you want to check that it's arrived, you can hop over to the **Files tab** and view your code on PythonAnywhere.

*   Finally, hop on over to the [Web tab][6] and hit **Reload** on your web app.

 [6]: https://www.pythonanywhere.com/web_app_setup/

Your update should be live! Go ahead and refresh your website in the browser. Changes should be visible :)