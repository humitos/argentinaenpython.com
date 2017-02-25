# HTML 簡介

你可能會問什麼是範本 (template)？

範本 (template) 是一個檔案，它讓我們可以重複使用一致的格式來呈現不同的資訊 -- 例如：你可以使用範本 (template) 來幫你寫一封信，因為雖然每封信件可能包含不同的訊息，及發送給不同的人，但他們將會共用相同的格式。

我們使用 HTML 語言來描述 Django 的範本。（HTML 也就是我們在第一章**網際網路如何運作**中提到的 HTML 語言。）).

## 什麼是 HTML？

HTML 是一種簡單的程式碼，由你的網路瀏覽器 -- 如 Chrome、Firefox、或 Safari -- 轉譯後，顯示一個網頁給使用者。

HTML 代表 "超文字標記語言 (HyperText Markup Language)"。 **超文字 (HyperText)** 是指它是一種支援網頁之間的超連結的文字。 **標記 (Markup)** 意味著我們接收文件並標示上程式碼來告訴某個東西（在這裡是指瀏覽器）如何解譯成網頁。 HTML 程式碼是由**標記 (tags)** 構成，每一程式碼以 `<` 開始，且以 `>` 結束。 這些標籤 (tags) 表示標記 (markup) **元素 (elements)**。.

## 你第一個範本 (template)！

建立一個範本 (template) 是指建立一個範本檔 (template file)，一切都是一個檔，對吧？你可能已經注意到這點了。

範本 (templates) 儲存在 `blog/templates/blog` 目錄中。 所以，先建立一個名稱為 `templates` 目錄 在你的 blog 目錄裡。 然後建立另一個稱為 `blog` 的目錄在你的 templates 目錄裡：

    blog
    └───templates
        └───blog
    

(你可能會疑惑為什麼我們需要兩個都叫 `blog` 的目錄 -- 之後你將會發現，這是簡單有用的命名常規，當事情開始變得更加複雜時，它讓我們生活更容易。)

現在，在 `blog/templates/blog` 目錄裡面，建立一個 `post_list.html` 檔（現在讓它保留空白） 。

看看你的網站現在是什麼樣子：http://127.0.0.1:8000/

> 如果你仍然有錯誤 `TemplateDoesNotExists`，試著重新開啟你的伺服器。 到命令列，按 Ctrl+C （Control 和C 按鈕一起按）停止伺服器運作，再執行 `python manage.py runserver` 命令重新啟動伺服器。

![圖 11.1][1]

 [1]: images/step1.png

再也沒有錯誤了！恭喜 :) 然而，您的網站實際上沒有發佈任何東西除了一空白網頁，因為你的範本 (template) 也是空白，我們需要修復這個問題。

加入以下內容到你的範本檔 (template file) 中：

    html
    <html>
        <p>Hi there!</p>
        <p>It works!</p>
    </html>
    

你的網站現在看起來怎麼樣？鍵入網址去看看：http://127.0.0.1:8000/。

![圖 11.2][2]

 [2]: images/step3.png

它可以運作 了挨！非常好 :)。

*   最基本的標籤 `<html>` 永遠是所有網頁的開始，而 `</html>` 是永遠是所有網頁的結尾。 正如你可看到的，整個網站的內容是在開始標籤 `<html>` 和結束標籤 `</html>` 之間。
*   `<p>` 是一種用於段落元素的標籤；`</p>` 結束每個段落。

## Head & body

每個 HTML 頁面也分為兩個元素︰**head** 和 **body**。.

*   **head** 是一個元素，它包含不顯示在螢幕上的有關於文件的資訊。

*   **body** 是一個元素。它包含一切顯示在網頁的東西。

我們使用 `<head>` 告訴瀏覽器有關網頁的設定，和 `<body>` 來告訴它網頁上究竟有什麼。

例如：你可以把網頁標題元素放入 `<head>` 裡面，像這樣：

    html
    <html>
        <head>
           <title>Ola's blog</title>
        </head>
        <body>
            <p>Hi there!</p>
            <p>It works!</p>
        </body>
    </html>
    

存檔並更新你的網頁。

![圖 11.3][3]

 [3]: images/step4.png

注意瀏覽器如何瞭解 "Ola's blog" 是你的網頁的標題？ 它已經轉譯 `<title>Ola's blog</title>` 並把文字內容放在你的瀏覽器的標題列上（它將被用於書籤 (bookmarks)，.. 等等）。

你可能也注意到每個開始標籤都搭配一個 `/` 和 *結束標籤 (closing tag)*，且元素是*嵌套的 (nested)*(即是你必需結束特定標籤內所有標籤後，才能結束這個特定標籤）。

這就像把東西放進盒子裡。 你有一個大箱子 `<html></html>`，在它裡面有 `<body></body>`，並包含了更小的箱子：`<p></p>` 。.

你必需遵循這些 *結束 (closing)* 標籤 (tags) 和 *嵌套 (nesting)* 元素 ( elements) 規則 -- 如果你不這樣做，瀏覽器可能不能正確地解譯他們，且您的頁面將不會被正確顯示。

## 自訂您的範本 (template)

現在，你可以有點樂趣和試著自訂您的範本！這裡是幾個有用的標籤︰

*   `<h1>A heading</h1>` -- 是你最重要的標題。
*   `<h2>A sub-heading</h2>` 為下一級標題。
*   `<h3>A sub-sub-heading</h3>` ... 等等，到 `<h6>`。
*   `<em>text</em>` 強調文字。
*   `<strong>text</strong>` 強烈強調你的文字。
*   `<br />` 跳至另一行（你不能放任何東西在 br 裡面。
*   `<a href="http://djangogirls.org">link</a>` 建一個連結。
*   `<ul><li>first item</li><li>second item</li></ul>` 製作一個清單，就像這個一樣。
*   `<div></div>` 定義網頁的一個區域。

下面是一個完整範本的示例︰

    html
    <html>
        <head>
            <title>Django Girls blog</title>
        </head>
        <body>
            <div>
                <h1><a href="">Django Girls Blog</a></h1>
            </div>
    
            <div>
                <p>published: 14.06.2014, 12:14</p>
                <h2><a href="">My first post</a></h2>
                <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut
    fermentum massa justo sit amet risus.</p>
            </div>
    
            <div>
                <p>published: 14.06.2014, 12:14</p>
                <h2><a href="">My second post</a></h2>
                <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut
    f.</p>
            </div>
        </body>
    </html>
    

我們已經建立三個 `div` 區域在這裡。

*   第一個 `div` 元素包含我們的部落格的標題 -- 這是一個標題和連結。
*   另外兩個 `div` 元素包含我們的部落格文章和它的發佈日期、`h2` 是可點擊的文章標題、和兩個 `p` （段落）的文章，一個是日期，而一個是我們的部落格。

它給了我們這樣的效果：

![圖 11.4][4]

 [4]: images/step6.png

Yaaay! 但到目前為止，我們的範本 (template) 只顯示**相同資訊** -- 而我們之前談到範本允許我們顯示**不同資訊**在相同**相同格式**上。.

我們真正想要做的是顯示我們在 Django 管理頁面新增的文章 -- 這是我們接下來要做的事。

## 還有一件事：部署！

看到這一切在網際網路上是一件很美好的事，對吧？讓我們做另一個 PythonAnywhere 部署：

### 提交和推送程式碼到 Github

首先，讓我們看看自上次部署後我們修改了那些檔案（執行這些命令在你電腦上，不是在 PythonAnywhere）：

    $ git status
    

請確認你在 `djangogirls` 目錄中，並告訴 `git` 去收錄這目錄內所有更改過的檔案。

    $ git add -A .
    

> **注意** `-A` ("all"的縮寫) 是指 `git` 將也會辨認是否你已經刪除檔案（在預設情況下，它只能識別新增／修改的檔案）。 此外，記得（在第３章）`.` 是指目前的目錄。

在我們上傳的所有檔之前，讓我們檢查 `git` 將上傳那些檔案（所有 `git` 將上傳的檔案現在都應以綠色顯示）：

    $ git status
    

我們差不多完成工作了，現在是時候告訴它把這次改變儲存在它的歷史紀錄中。 我們將給它 "提交訊息"，在裡面我們描述我們已經做了什麼改變。 在這階段，你可以鍵入任何你想要的東西，但鍵入一些描述性的東西更有幫助的，如此，在將來你能想起你做了什麼。

    $ git commit -m "Changed the HTML for the site."
    

> **注意** 確認在提交消息前後使用雙引號。

假如我們完成這些，我們可以上傳（推送）我們的修改到 Github 上：

    git push
    

### 拉取我們新的程式碼到 PythonAnywhere 上，並重新載入你的網站應用程式 (web app)

*   打開 [PythonAnywhere 主控台頁面][5]，並到你的 **Bash 主控台 (console)**（或者啟動一個新的）。然後，執行：

 [5]: https://www.pythonanywhere.com/consoles/

    $ cd ~/my-first-blog
    $ source myvenv/bin/activate
    (myvenv)$ git pull
    [...]
    (myvenv)$ python manage.py collectstatic
    [...]
    

同時注視你的程式碼被下載，假如你想要確認程式碼已經下載，你可以跳到 **Files 選項** 並在 PythonAnywhere 上查看你的程式碼。

*   最後，跳到 [Web 選項][6] 並在你的網站應用程式 (web app) 上，點選 **Reload** 。

 [6]: https://www.pythonanywhere.com/web_app_setup/

你的更新應該上線了！在瀏覽器重新載入 (refresh) 你的網頁，你應該可看到它改變了 :)