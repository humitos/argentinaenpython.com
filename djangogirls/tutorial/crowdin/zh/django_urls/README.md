# Django urls

我們將要建立我們的第一個網頁： 你的部落格的首頁！但首先，讓我們先瞭解一點 Django 的 url。

## 什麼是 URL？

URL 只是一個 web 位址。 每次您訪問網站 你可以都看到 URL， -- 它是在您的瀏覽器的網址列中（是的！ `127.0.0.1:8000` 是‘一個 URL！ 同時 `Https://djangogirls.com` 也是一個網址）：

![Url][1]

 [1]: images/url.png

在網際網路上每個網頁都需要有它自己的 URL。 這樣你的應用程式才知道它應該顯示什內給打開 URL 的使用者。 在 Django，我們使用叫做 `URLconf` (URL configuration)。 URLconf 是一套模式 (patterns)，Django 將用它試著去找尋和它接收到 URL 相匹配的正確 view。

## 在 Django 上 URLs 如何運作？

在你選擇的程式碼編輯器上，打開 `mysite/urls.py` 檔，看看它長什麼樣子：

    python
    from django.conf.urls import include, url
    from django.contrib import admin
    
    urlpatterns = [
        # Examples:
        # url(r'^$', 'mysite.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')), 
    
        url(r'^admin/', include(admin.site.urls)),
    ]
    

正如你所看到的，Django 已經為我們放一些東西在裡面了。

以 `#` 開頭的行是注釋 -- 它意味著 Python 不會執行這些行，很方便，對吧？

前一章節提到的 admin URL 已經在這裡：

    python
        url(r'^admin/', include(admin.site.urls)),
    

這意味著對於每個以 `admin/` 開頭的 URL，Django 將會為它找到相應的 *view*。 在這個程式，我們包含了許多的 admin URLs 進來，所以這些 URLs 不會塞滿這個小檔案 -- 這樣程式更易讀也更清潔。

## Regex

你想知道 Django 如何將 URLs 匹配到 views 嗎？ 喔，這一部分比較棘手。 Django 使用 `regex`，是 "正規表示法" ("regular expressions") 的簡稱。 正規表示法有很多（很多！）的規則，這些規則形成一個搜尋模式。‘ 由於正規表示法是一個進階的主題，我們將不會在這裡詳細地討論它如何運行。

如果你還想瞭解我們如何建立模式 (patterns)，下面是一個過程的示範 -- 我們將只需要有限規則的子集合就能表達我們正在尋找的模式了，即：

    ^ 表示文字的開始
    $ 表示文字的結尾
    \d 表示數字
    + 表示前一個項目必需重複一次
    () 表示取得部份的模式 (pattern)
    

在 url 定義之外的東西將被接受。

現在想像你有這樣的一個網站位址：`http://www.mysite.com/post/12345/`，其中 `12345` 是你文章 (post) 的編號。

為所有個別編號的文章撰寫單獨的 views將會很令人惱火。 使用正規表示法，我們可以建立一種模式來為我們匹配 url 和取得編號：`^ post/(\d+) / $`。 讓我們將這式子拆開看看我們在這裡做了什麼：

*   **^post/** 是告訴 Django 接受任何以 `post/` 開頭的 url 的內容（^右邊之後） `^`)
*   **(\d+)** 表示這是一個數字（個位數或多數位），且我們要提取這個數字。
*   **/** 告訴 django 另一個 `/` 字元緊跟在後。
*   **$** 表示 URL 的末端，意味只有以 `/` 結束的字串將匹配這個模式。

## 你的第一個 Django url！

該建立我們的第一個 URL 了！我們想要以 'http://127.0.0.1:8000/' 為我們部落格首頁，並且顯示文章 (post) 的清單。

我們也想要保持 `mysite/urls.py` 檔簡潔，所以我們將從我們的`部落格`應用程式導入 urls 到主要的 `mysite/urls.py` 檔案裡。

開始吧，刪除注釋行 (以 `#` 開頭的行)，並加一新行用來將 `blog.urls` 導入到主 url (`''`).

你的 `mysite/urls.py` 檔現在應該像這樣：

    python
    from django.conf.urls import include, url
    from django.contrib import admin 
    
    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'', include('blog.urls')),
    ]
    

Django 現在將所有要瀏覽 'http://127.0.0.1:8000/' 請求，引導到 `blog.urls`，並注意看看有沒有進一步的指示。

在 Python 中編寫正規表示法時，記得要加一個 `r` 於字串前面。 對 Python 而言，這是一個有用的提示，它告訴 Python 這字串可能包含特殊字元，這些特殊字元不是給 Python 而是給正規表示法用的。

## blog.urls

建立一個新的 `blog/urls.py` 空白檔，太棒了！加入下面兩行：

    python
    from django.conf.urls import url
    from . import views
    

在這裡我們僅僅導入 Django 的方法 (method)，並從 `blog` 應用程式 導入我們所有的 `views` （我們沒有建立任何 view，但我們待會兒會做！）

然後，我們可以新增我們第一個 URL 模式：

    python
    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
    ]
    

正如你所看到的，我們現在分配一個稱為 `post_list` 的 `view` 給 `^$` URL。 這個正規表示法將給 `^`（表示開頭）緊接著 `$`（表示結尾）一個匹配 -- 因此，只有一個空的字串將匹配。 這是正確的，因為在 Django URL 解碼器 (resolvers) 中，'http://127.0.0.1:8000/' 不是 URL 的一部分。 這種模式將會告訴 Django，如果有人要以 'http://127.0.0.1:8000/' 網址進入你的網站，那麼 `views.post_list` 是這個請求應該去的地方。

最後一部分 `name='post_list'` 是將用來識別 view 的 URL 名稱。 這可以和 view 的名稱相同，但它也可以是完全不同的名稱。 稍後在這專案，我們將使用被命名的 URL， 因此在應用程式中命名每一個 URL 是很重要的，我們也應該試著保持 URL 名稱不重複和易於記住。

一切都還好嗎？在你的瀏覽器打開 http://127.0.0.1:8000/，查看結果。

![錯誤 (Error)][2]

 [2]: images/error1.png

是沒有出現 "It works" 了，是吧？別擔心，它只是一個錯誤頁面，沒有什麼好害怕的！它們其實是非常有用：

你可以看到 **no attribute 'post_list'**。 *post_list* 提醒你什麼了？ 這是我們所說的 view！ 這意味著一切都到位了，但我們只是還沒有建立我們的*view*。 不用擔心，我們將到達那裡。

> 如果你想要知道更多有關於 Django URLconfs，可查看 Django 官方文件：https://docs.djangoproject.com/en/1.8/topics/http/urls/