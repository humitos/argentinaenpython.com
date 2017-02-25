# Django 範本 (templates)

是時候顯示一些資料了！為此，Django 提供我們一些有用的內建**範本標籤 (template tags)**。

## 範本標籤是什麼？

你知道，在 HTML 中，你不能真的寫 Python 程式碼，因為瀏覽器不能理解它。他們只知道 HTML。我們瞭解 HTML 是相當靜態的而 Python 是較動態的。

**Django 範本標籤** 允許我們將像 Python 這樣的內容轉換成 HTML，所以我們可以更快更容易的建立動態網站。Yikes！

## 顯示文章清單範本

在前一章中我們在 `posts` 變數中給我們的範本文章清單，現在我們將在 HTML 中顯示它。

若要刊載 Django 範本中的變數，我們把變數放在兩個雙大括弧裡面，像這樣︰

    html
    {{ posts }}
    

在你的 `blog/templates/blog/post_list.html` 範本中，試試這個。 將第二個 `<div>` 到第三個 `</div>` 之間的內容，用 `{{ posts }}` 代替。 存檔，並更新網頁 (refresh) 以查看結果︰

![圖 13.1][1]

 [1]: images/step1.png

如你所看到的，我們得到是這樣︰

    [<Post: My second post>, <Post: My first post>]
    

這表示 Django 瞭解它是物件清單。 還記得在 **Python 簡介** 中我們可以如何顯示清單嗎？ 是的，用迴圈 (loop)！ 在 Django 範本中你這樣做︰

    html
    {% for post in posts %}
        {{ post }}
    {% endfor %}
    

在你的範本中試試這些。

![圖 13.2][2]

 [2]: images/step2.png

成功了！ 但我們希望它能展現像我們在 **HTML 簡介** 章節中建立的靜態文章那樣。 你可以混合使用 HTML 和範本標籤。 我們的 `body` 將像這樣︰

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
    

{% raw %}你放在 `{% for %}` 和 `{% endfor %}` 之間的程式碼將重複清單中的每個物件。更新你的網頁︰{% endraw %}

![圖 13.3][3]

 [3]: images/step3.png

你有沒有注意到我們使用的符號稍有不同，這次是 `{{ post.title }}` 或 `{{ post.text }}`？ 我們存取定義在我們 `Post` 模型中每個欄位的資料。 此外，`|linebreaks` 經由輸送文章至一個篩檢程式來把分行符號轉換為段落。

## 還有一件事

看看是否你的網站仍將會在公共的網際網路上運作是一件不錯的事，對吧？讓我們試著再次部署到 PythonAnywhere 上。這裡是一個概括的步驟...

*   首先，推送你的代碼到 Github

    $ git status
    [...]
    $ git add -A .
    $ git status
    [...]
    $ git commit -m "Modified templates to display posts from database."
    [...]
    $ git push
    

*   然後，登錄 [PythonAnywhere][4] 並到你的 **Bash 主控台**（或啟動一個新的），然後，執行︰

 [4]: https://www.pythonanywhere.com/consoles/

    $ cd my-first-blog
    $ git pull
    [...]
    

*   最後，跳到 [Web 選項tab][5] 並點選在你網站應用程式 (web app) 上的 **Reload**，你的更新應該完成了！

 [5]: https://www.pythonanywhere.com/web_app_setup/

恭喜！現在試著在你的 Django 管理介面中新增文章（記得要加入 published_date！），然後，更新網頁以查看是否有顯示出來。

神奇吧？我們很自豪！離開你的電腦，你應該休息一下。:)

![圖 13.4][6]

 [6]: images/donut.png