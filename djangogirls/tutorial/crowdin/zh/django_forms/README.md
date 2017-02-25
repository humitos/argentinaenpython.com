# Django 表單 (Forms)

我們想要在我們網站做最後一件事是建立一種友善的方式來新增和編輯部落格文章。 Django 的 `管理介面 (admin)` 是很酷，但它是很難自訂格式和美化。 有了 `表格`，我們將對我們的介面有絕對的權力 -- 我們幾乎可以做任何我們可以想像事情！

Django 表單的好處是，我們可以從零開始定義一個或者建立一個 `ModelForm`，它將會儲存表單的結果到模型。

這正是我們想要做的︰我們將為我們的 `Post` 模型建立表單。

像所有 Django 的重要部份，表單有他們自己的檔案︰`forms.py`.

我們需要在 `blog` 目錄中建立這個檔案。

    blog
       └── forms.py
    

Ok，讓我們打開，然後鍵入以下的程式碼︰

    python
    from django import forms
    
    from .models import Post
    
    class PostForm(forms.ModelForm):
    
        class Meta:
            model = Post
            fields = ('title', 'text',)
    

我們需要先導入 Django forms（`from django import forms`），然後，很明顯地，我們的 `Post` 模型（`from .models import Post`).

`PostForm`，正如你可能猜想的，是我們表單的名稱。 我們需要告訴 Django，這個表單是 `ModelForm`（所以 Django 會為我們施展一些魔術）-- `forms.ModelForm` 負起這個責任。

接下來，我們有 `class Meta`，在這裡我們告訴 Django 應該用什麼模型來建立這個表單（`model = Post`).

最後，我們可以說哪些欄位應該在我們的表單上。 在這裡，我們只想要顯示`title` 和 `text` -- `author` 應該是當前登錄的（你！）的人，而 `created_date` 應該在我們建立一篇文章時自動設定（例如在程式碼上設定），對吧？

就是這些！現在所有我們需要做的是在 *view* 中使用這表單，並將它顯示在範本中。

所以再一次，我們將建立︰一個連結到網頁、一個 URL、一個 view 和一個範本。

## 連結表單到網頁 (Link to a page with the form)

現在，打開 `blog/templates/blog/base.html`，我們將增加一個連結到名稱為 `page-header` 的 `div` 裡面︰

    html
    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    

注意，我們想要稱呼我們的新 view 為 `post_new`。.

增加這行之後，您的 html 檔案現在應該像這樣︰

    html
    {% load staticfiles %}
    <html>
        <head>
            <title>Django Girls blog</title>
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
            <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
            <link rel="stylesheet" href="{% static 'css/blog.css' %}">
        </head>
        <body>
            <div class="page-header">
                <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
                <h1><a href="/">Django Girls Blog</a></h1>
            </div>
            <div class="content container">
                <div class="row">
                    <div class="col-md-8">
                        {% block content %}
                        {% endblock %}
                    </div>
                </div>
            </div>
        </body>
    </html>
    

存檔並更新網頁 http://127.0.0.1:8000 後，你會明顯看到一個熟悉的錯誤 `NoReverseMatch`，對吧？

## URL

我們打開 `blog/urls.py`，並增加一行︰

    python
        url(r'^post/new/$', views.post_new, name='post_new'),
    

最後程式碼將會像這樣︰

    python
    from django.conf.urls import include, url
    from . import views
    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
        url(r'^post/new/$', views.post_new, name='post_new'),
    ]
    

在更新網站之後，我們看到 `AttributeError`，因為我們還沒完成 `post_new` view。現在，讓我們新增它吧。

## post_new view

現在打開 `blog/views.py` 檔，並增加以下行到 `from` 下︰

    python
    from .forms import PostForm
    

和我們的 *view*︰

    python
    def post_new(request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    

若要建立新的 `Post` 表單，我們需要呼叫 `PostForm()`，並將它傳遞給範本。 我們將會再回到這 *view*，但現在，讓我們快速為表單建立一個範本。

## 範本 (Template)

我們需要在 `blog/templates/blog` 目錄中建立 `post_edit.html`。為使表單能運作，我們需要幾件東西︰

*   我們需要顯示表單，我們可以用簡單的`{% raw %}{{ form.as_p }}{% endraw %}`做到這一點。.
*   上面那一行需要包括在 HTML 表單標籤裡面︰`<form method="POST">...</form>`
*   我們需要一個 `儲存` 按鈕，我們可以使用 HTML 按鈕來完成︰`<button type="submit">儲存</button>`
*   以及最後，就在 `<form ...>` 標籤後，我們需要加入 `{% raw %}{% csrf_token %}{% endraw %}`。 這是非常重要的，因為它讓你的表單較安全！ Django 將會提醒你，如果你試著要儲存表單但忘記這一點︰

![CSFR Forbidden page][1]

 [1]: images/csrf2.png

Ok，讓我們看看 HTML 在 `post_edit.html` 裡應該看起來怎麼樣︰

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        <h1>New post</h1>
        <form method="POST" class="post-form">{% csrf_token %}
            {{ form.as_p }}
            <button type="submit" class="save btn btn-default">Save</button>
        </form>
    {% endblock %}
    

現在更新網頁！耶！表單顯示出來了！

![西][2]

 [2]: images/new_form2.png

但是，等一下！當你在 `title` 和 `text` 欄位中鍵入東西並試著存檔時 -- 會發生什麼事？

什麼都沒有！我們又在同一網頁上，且我們的文字內容已經不見了，而且沒有增加新的文章。所以錯在哪裡？

答案是︰沒有錯誤。我們需要對我們的 *view* 做多一點的工作。.

## 儲存表單 (Saving the form)

再打開 `blog/views.py`。目前，在 `post_new` view 中，我們的內容是︰

    python
    def post_new(request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    

當我們提交表單，我們又回到相同的 view，但是這次我們有更多的資料在 `request`，更具體地說在 `request.POST` 裡面（這個名字和部落格的 "post" 無關，它是關於我們"上傳 (posting)" 資料的狀況）。 記得在 HTML 檔案，我們的 `<form>` 定義裡有變數 `method="POST"`？ 所有表單的欄位內容現在都在 `request.POST` 中。 你不應該重新命名 `POST` 為其他東西（其他唯一有效的 `method` 值是 `GET`，但我們沒有時間解釋它們的差異）。

所以在我們的 *view* 中，我們有兩種不同情況要處理。 第一︰當我們第一次存取網頁時，以及我們想要一個空白表單。 第二︰當我們回到 *view*，我們要有剛剛鍵入的所有表單資料。 所以我們需要增加一個條件（為此，我們將使用 `if`）。

    python
    if request.method == "POST":
        [...]
    else:
        form = PostForm()
    

現在來填寫 `[...]`，如果 `method` 是 `POST`，然後我們想用來自表單的資料建造 `PostForm` 對吧？我們將會這樣做︰

    python
    form = PostForm(request.POST)
    

簡單！下一件事是檢查表單是否正確（所有必填的欄位都被設定，且沒有不正確的數值將被儲存）。我們使用 `form.is_valid()`.

我們檢查表單是否有效，如果是的話，我們可以儲存它！

    python
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
    

基本上，在這裡我們有兩件事︰我們用 `form.save` 將表單儲存，且我們增加 author（因為在 `PostForm` 裡沒有 `author` 欄位，但這欄位是必填的！）。 `commit=False` 表示我們還不想儲存 `Post` 模型 -- 我們想要先新增 author。 大多數情況下，你使用 `form.save()` 時，不會用到 `commit=False`，但在這裡，我們需要這樣做。 `post.save()` 將保留變動（增加 author），建立新的部落格文章！

最後，假如我們可以馬上去 `post_detail` 網頁建立新的部落格文章，那會很酷，對吧？要做到這些，我們需要多一個導入︰

    python
    from django.shortcuts import redirect
    

將它加到你的檔開頭。現在我們可以說︰去 `post_detail` 網頁建立新的文章。

    python
    return redirect('blog.views.post_detail', pk=post.pk)
    

`blog.views.post_detail` 是我們想要去 view 的名稱。 還記得這個 *view* 須要一個 `pk` 變數嗎？ 要將它傳遞給 views，我們使用 `pk=post.pk`，其中 `post` 是新建立的部落格文章！

Ok，我們談了很多，但我們可能想要看看整個 *view* 現在看起來像什麼，對吧？

    python
    def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    

讓我們看看它是否能運作。 到 http://127.0.0.1:8000/post/new/ 網頁，新增 `title` 和 `text`，儲存它... 然後，瞧！ 新的文章已經加進來了，我們被到重新導向到 `post_detail` 網頁！

你可能已經注意到在儲存文章之前我們先設定發佈日期；稍後，在 **Django Girls 教材: 續集**中，我們將引進一個 *發佈按鈕*。.

這真棒！

## 表單驗證 (Form validation)

現在，我們將向你展示 Django 表單有多酷。 一篇部落格文章需要有 `title` 和 `text` 欄位。 在我們的 `Post` 模型中，我們並沒有說（相對於 `published_date`) 這些欄位不是必填的，所以 Django，在預設情況下，預期它們將被設定。

試著儲存沒有`title` 和 `text` 內容的表單，猜猜看，會發生什麼事！

![表單驗證 (Form validation)][3]

 [3]: images/form_validation2.png

Django 負責驗證我們表單中的所有欄位都是正確的，是不是很棒？

> 因為我們最近使用 Django 管理介面，系統目前認為我們已登錄了。 有幾種情況可能導致我們被登出（關閉瀏覽器、重新啟動資料庫等等）。 如果你發現，當建立一篇文章時，你得到缺少一個登錄使用者的錯誤訊息，到 admin 網頁 http://127.0.0.1:8000/admin 並再次登錄。 這將暫時解決這個問題。 還有一個一勞永逸的方法在等你，在這主教材之後的 **Homework: add security to your website!** 章節。

![Logged in error][4]

 [4]: images/post_create_error.png

## 編輯表單 (Edit form)

現在我們知道如何增加一個新的表單。 但如果我們想要編輯一個現存的？ 它是非常類似我們剛剛做的。 讓我們快速地建立一些重要的事情（如果你不懂的某些東西，你應該問你的教練或看看前面的章節，因為我們已經涵蓋了所有這些步驟）。

打開 `blog/templates/blog/post_detail.html`，並加入這行︰

    python
    <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    

所以範本將看起來像這樣︰

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        <div class="post">
            {% if post.published_date %}
                <div class="date">
                    {{ post.published_date }}
                </div>
            {% endif %}
            <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk%}"><span class="glyphicon glyphicon-pencil"></span></a>
            <h1>{{ post.title }}</h1>
            <p>{{ post.text|linebreaks }}</p>
        </div> 
    {% endblock %}
    

在 `blog/urls.py` 中我們加入這行︰

    python
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    

我們將再使用範本 `blog/templates/blog/post_edit.html`，因此最後欠缺的是一個 *view*。.

讓我們打開 `blog/views.py`並在檔案的末尾加入︰

    python
    def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    

這看起來幾乎和我們的 `post_new` view 完全相同，對吧？ 但不是全部。 第一件事︰我們從 urls 傳遞一個額外的 `pk` 參數。 其次︰我們以 `get_object_or_404(Post, pk=pk)` 取得我們想要編輯的 `Post` 模型，然後，當我們建立表單時，我們以`instance`傳遞這篇文章，當我們儲存表單︰

    python
    form = PostForm(request.POST, instance=post)
    

以及當我們只是打開文章表單編輯時︰

    python
    form = PostForm(instance=post)
    

Ok，讓我們來測試它是否能運作！讓我們到 `post_detail` 網頁。在右上角應該有一個編輯按鈕︰

![Edit button][5]

 [5]: images/edit_button2.png

當你點選它時，你將看到我們部落格文章的表單︰

![編輯表單 (Edit form)][6]

 [6]: images/edit_form2.png

隨意更改 title 或 text 並保存更改！

祝賀你！你的應用程式變得越來越完整！

如果你需要更多關於 Django 表單的資訊，你應該閱讀文件︰https://docs.djangoproject.com/en/1.8/topics/forms/

## 安全性 (Security)

只透過點選一個連結就能夠建立新的文章，是很棒的！ 但是，現在，任何人訪問你的網站將能夠發佈新的部落格文章，這可能不是你想要的東西。 讓我們讓按鈕只顯示給你，但不是顯示給其他人。

在 `blog/templates/blog/base.html`，找我們的 `page-header` `div` 和你稍早放在那裡的錨點 (anchor) 疵標籤。它看起來應該像這樣︰

    html
    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    

我們要將增加另一個 `{% if %}` 標籤到這裡，這樣將使這連結僅顯示給登錄到管理員介面 (admin) 的使用者，現在，那就是你！ 更改 `<a>` 標籤，讓它看起來像這樣︰

    html
    {% if user.is_authenticated %}
        <a href="{% url 'post_new' %}" class="top-menu"><span
    class="glyphicon glyphicon-plus"></span></a>
    {% endif %}
    

這 `{% if %}` 將使連結只發送到那些已登錄使用者的瀏覽器。 這並不會完全地防止新文章的建立，但它是很好的起步。 在延伸課程中，我們將含概更多的安全性。

因為你可能已經登錄了，如果你更新網頁，你將不會看到有什麼不同。不過，在新的瀏覽器或匿名視窗中載入這個網頁，你將會看到連結不會出現！

## 還有一件事：部署時間！ (One more thing: deploy time!)

讓我們看看這一切能否在 PythonAnywhere 上運作。另一次的部署時間！

*   首先，提交你的新程式碼，並把它推送 GitHub。

    $ git status
    $ git add -A .
    $ git status
    $ git commit -m "Added views to create/edit blog post inside the site."
    $ git push
    

*   然後，在 [PythonAnywhere Bash 主控台][7]︰

 [7]: https://www.pythonanywhere.com/consoles/

    $ cd my-first-blog
    $ source myvenv/bin/activate
    (myvenv)$ git pull
    [...]
    (myvenv)$ python manage.py collectstatic
    [...]
    

*   最後，跳到 [Web 選項][8] 並點選 **Reload**。.

 [8]: https://www.pythonanywhere.com/web_app_setup/

那應該是它！恭喜 :)