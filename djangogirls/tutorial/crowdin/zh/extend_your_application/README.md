# 擴展你的應用程式 (Extend your application)

我們已經完成了所有建立我們的網站所需的不同步驟︰我們知道如何編寫模型、url、view和範本，我們也知道如何讓我們的網站變漂亮。

現在來練習！

很明顯，在我們的部落格我們需要的第一件事是一網頁顯示一篇文章，正確吧？

我們已經有 `Post` 模型，所以我們不需要增加任何東西到 `models.py`。.

## 建立一個範本連結到一篇文章內容 (Create a template link to a post's detail)

我們將在 `blog/templates/blog/post_list.html` 檔中增加一個連結，到目前為止它應該看起來像這樣︰

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        {% for post in posts %}
            <div class="post">
                <div class="date">
                    {{ post.published_date }}
                </div>
                <h1><a href="">{{ post.title }}</a></h1>
                <p>{{ post.text|linebreaks }}</p>
            </div>
        {% endfor %}
    {% endblock content %}
    
    

{% raw %}我們想要一個從文章清單的文章標題到文章內容頁的連結。 讓我們修改 `<h1><a href="">{{ post.title }}</a></h1>`，如此它連結到文章的內容頁︰{% endraw %}

    html
    <h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
    

{% raw %}現在解釋這神秘的 `{% url 'post_detail' pk=post.pk %}`。 正如你可能猜想的，`{% %}` 符號表示我們正在使用 Django 範本標籤。 這次我們將使用一個能為我們建立 URL的！{% endraw %}

`blog.views.post_detail` 是一個到我們想建立的 `post_detail` *view* 的路徑。 請注意︰`blog` 是我們應用程式（目錄 `blog`）的名稱，`views`是來自 `views.py` 檔的名稱，最後一點 -- `post_detail` -- 是 *view* 的名稱。.

現在，當我們去︰http://127.0.0.1:8000/，我們會有一個錯誤（如預期的，因為我們沒有給 `post_detail` 的 URL 或 *view*）。它看起來會像這樣︰

![NoReverseMatch error][1]

 [1]: images/no_reverse_match2.png

## 建立一個文章內容頁 URL (Create a URL to a post's detail)

讓我們在 `urls.py` 為我們的 `post_detail` *view* 建立一個 URL。!

我們希望顯示我們第一篇文章的內容在這個 **URL**：http://127.0.0.1:8000/post/1/

讓我們在 `blog/urls.py` 檔中增加一個 URL 來指示 Django 到名稱為 `post_detail` 的 *view* ，它將顯示整篇部落格文章。 增加這行 `url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),` 到 `blog/urls.py` 檔案。 檔案應該像這樣︰

    python
    from django.conf.urls import include, url
    from . import views
    
    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    ]
    

`^post/(?P<pk>[0-9]+)/$` 這部份看起來很嚇人，不用擔心 -- 我們將解釋給你聽： - 它還是以 `^` 開頭 -- "開始" - `post/` 只是表示，緊接著開頭，URL 應該包含文字 **post** 和 **/**. 目前為止，一切順利。 - `(?P<pk>[0-9]+)` - 這部份較棘手。 它表示 Django 會接受放在這裡的東西，並將它以變數 `pk` 傳遞給 view 。 `[0-9]` 也告訴我們，它只能是數字，不是文字（所以範圍是介於０和９之間）。 `+` 表示這裡需要有一個或一個以上的數字。 所以像 `http://127.0.0.1:8000/post//` 是無效的，但 `http://127.0.0.1:8000/post/1234567890/` 是完全沒問題的！ - `/` - 然後我們還需要 **/** - `$` - "結束"！

這表是如果你輸入 `http://127.0.0.1:8000/post/5/` 到你的瀏覽器，Django 將會理解你正在尋找一個叫做 `post_detail` 的 *view*，傳遞 `pk` 等於 `5` 的資訊到那個 *view*。.

`pk` 是 `primary key` 的簡化。 在 Django 專案中，經常使用這個名稱。 但你可以以你喜歡的名字來命名你的變數（記住︰使用小寫和 `_` 而不是空格！）。 例如，不使用 `(?P<pk>[0-9]+)`，我們可以有變數 `post_id`，如此它看起來就像︰`(?P<post_id>[0-9]+)`.

Ok，我們已經增加一個新的 URL 模式到 `blog/urls.py`！讓我們更新網頁︰http://127.0.0.1:8000/ 轟！還有另一個錯誤！果然！

![AttributeError][2]

 [2]: images/attribute_error2.png

你記得下一步是什麼嗎？當然︰增加一個 view！

## 增加一個文章的內容 view

這次 Django 給我們的 *view* 一個額外的參數 `pk`。 我們的 *view* 需要接住它，對吧？ 所以，我們將定義我們的函數為 `def post_detail(request, pk):`。 注意，我們需要使用我們在urls (`pk`) 中指定的名稱。 忽略這個變數是不正確，而且將會導致錯誤！

現在，我們想要一個且單一一個部落格文章。要做到這一點，我們可以使用像這樣的查詢集 (querysets)︰

    Post.objects.get(pk=pk)
    

但是這段程式碼有一個問題，假如沒有一個含有`primary key` (`pk`) 的 `Post`，我們將有一個超級醜的錯誤！

![DoesNotExist error][3]

 [3]: images/does_not_exist2.png

我們不想要這樣！ 但是，當然，Django 會為我們處理這問題︰`get_object_or_404`。 在這情況下，沒有一個含有 `pk` 的 `Post`， 它將會顯示較友善的網頁（稱為 `Page Not Found 404` 網頁）。

![Page not found][4]

 [4]: images/404_2.png

好消息是你實際上可以建立你自己的 `Page not found` 網頁，並使它如你期望的友善；但現在這不是超級重要的，所以我們將跳過它。

好吧，現在增加一個 *view* 到我們的`views.py`檔！

我們應該打開 `blog/views.py` 並加入以下程式碼︰

    from django.shortcuts import render, get_object_or_404
    

在其他 `from` 行附近；並在檔案末端，我們將加入我們的 *view*︰

    def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})
    

是的。是時間來更新網頁︰http://127.0.0.1:8000/

![Post list view][5]

 [5]: images/post_list2.png

成功了！但當你點選部落格文章標題的連結時，發生了什麼？

![TemplateDoesNotExist error][6]

 [6]: images/template_does_not_exist2.png

哦不！另一個錯誤！但我們已經知道如何處理它，對吧？我們需要增加一個範本 (template)！

## 為文章內容建立範本 (Create a template for post detail)

我們將在 `blog/templates/blog` 中，建立一個檔案名稱為 `post_detail.html`。.

它將看起來像這樣：

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        <div class="post">
            {% if post.published_date %}
                <div class="date">
                    {{ post.published_date }}
                </div>
            {% endif %}
            <h1>{{ post.title }}</h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endblock %}
    

我們再一次擴展 `base.html`。 在 `content` 區段，我們想要顯示一篇文章的發佈日期（假如存在的話）、標題、和內容。 但我們應該討論一些重要的東西，對吧？

{% raw %}`{% if ... %} ... {% endif %}` 是範本標籤 (template tag)，當我們想要檢查某些東西時，我們可以使用它。（記得 ` if ... else ..` 在 **Python簡介**？）。 在這裡，我們想要檢查是否文章的 `published_date` 是不是空的。{% endraw %}

Ok，現在，我們可以更新我們的網頁，看看 `Page not found` 是否消失了。

![Post detail page][7]

 [7]: images/post_detail2.png

耶！成功了！

## 還有一件事：部署時間！ (One more thing: deploy time!)

看到你的網站仍然會繼續在 PythonAnywhere 上運作，是很不錯，對吧？讓我們試著再次部署。

    $ git status
    $ git add -A .
    $ git status
    $ git commit -m "Added view and template for detailed blog post as well as CSS
    for the site."
    $ git push
    

*   然後，在 [PythonAnywhere Bash 主控台][8]︰

 [8]: https://www.pythonanywhere.com/consoles/

    $ cd my-first-blog
    $ source myvenv/bin/activate
    (myvenv)$ git pull
    [...]
    (myvenv)$ python manage.py collectstatic
    [...]
    

*   最後，跳到 [Web 選項][9] 並點選 **Reload**。.

 [9]: https://www.pythonanywhere.com/web_app_setup/

那應該是它！恭喜 :)