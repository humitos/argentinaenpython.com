# 在範本中的動態資料 (Dynamic data in templates)

我們把不同的東西安排妥當了︰`Post` 模型定義在 `models.py`，我們定義 `post_list` 在 `views.py`，且新增範本 (template) 了。 但我們究竟將如何使我們的文章出現在我們的 HTML 範本 (template) 上？ 因為那正是我們想要的︰取得一些內容（保存在資料庫中的模型）並將它顯示在我們的範本上，正確吧？

這就是 *views* 應該做的：連接模型 (models) 和範本 (templates)。 在我們的 `post_list` *view* 中，我們將需要取得我們想要顯示的模型，並將它們傳遞到範本。 所以基本上在 *view* 中，我們決定什麼（模型）將顯示在範本中。

OK，那麼，我們將如何實現它？

我們需要打開我們的 `blog/views.py`，到目前為止 `post_list` *view* 看起來像這樣︰

    python
    from django.shortcuts import render
    
    def post_list(request):
        return render(request, 'blog/post_list.html', {})
    

還記得當我們談到導入 (including) 程式碼編寫在不同檔案中嗎？ 現在是我們必須導入 (include) 我們已經寫在 `models.py` 中的模型的時候。 我們將增加這一行 `from .models import Post` 像這樣︰

    python
    from django.shortcuts import render
    from .models import Post
    

`from` 後面的小圓點表示 *目前目錄* 或 *目前應用程式 (application)*。 因為 `views.py` 和 `models.py` 是在相同的目錄中，我們可以簡單地使用 `.` 和檔名（沒有 `.py`）。 然後，我們將導入 (import) 模型的名稱 (`Post`).

但接下來做什麼？從 `Post` 模型取得實際的部落格文章，我們需要某個東西叫做 `QuerySet`。.

## 查詢集 (QuerySet)

您應該已經熟悉 QuerySets 是如何運作的，我們在 [Django ORM (QuerySets) 章節][1] 中談到它。.

 [1]: ../django_orm/README.md

所以現在我們感興趣的是以 `published_date`排序的已發佈的部落格文章清單，正確吧？我們已經在 Queryset 章節中做過了！

    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    

現在我們把這段程式碼放到 `blog/views.py` 檔中的 `def post_list(request)` 的函數內：

    python
    from django.shortcuts import render
    from django.utils import timezone
    from .models import Post
    
    def post_list(request):
        posts =
    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {})
    

請注意，我們為我們的 QuerySet 建立了一個*變數 (variable)*︰`posts`，並將它視為我們的 QuerySet 的名稱，從現在開始我們可以透過這個名字引用它。

此外，程式碼使用到 `timezone.now()` 函數，所以我們需要為 `timezone` 新增一個導入 (import) 。.

最後缺少部分是傳遞 `posts` QuerySet 到範本 (template) （我們將在下一章介紹如何顯示它）。

在 `render` 函數我們已經有 `request` 參數（所以，所有我們經由網際網路收到來自使用者的訊息）和範本檔 `'blog/post_list.html'`。 最後一個參數，看起來像這樣：`{}`，它是我們可以新增一些東西給範本使用的地方。 我們需要給它們名字（現在我們將沿用 `'posts'` :) ）。 它應該看起來像這樣︰`{'posts': posts}`。 請注意，`:` 之前的部分是字串；你需要用引號將它括起來。 `''`.

所以，最後我們的 `blog/views.py` 檔應像這樣︰

    python
    from django.shortcuts import render
    from django.utils import timezone
    from .models import Post
    
    def post_list(request):
        posts =
    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})
    

就這些！現在回到我們的範本並顯示這個 QuerySet！

如果你想要瞭解更多關於 Django 的 QuerySets，你應該查看這裡︰https://docs.djangoproject.com/en/1.8/ref/models/querysets/