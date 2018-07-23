# Django ORM 和查詢集 (QuerySets)

在這一章中，您將學習 Django 如何連接到資料庫，並將資料存儲在裡面。一起去探究吧！

## 查詢集 (QuerySet) 是什麼？

從本質上說，查詢集 (QuerySet) 是一特定模型的物件列表。查詢集 (QuerySet) 允許你讀取、篩選和排序資料庫中的資料。

從例子中學習是最容易的。讓我們試試，好嗎？

## Django shell

打開你的主控台（不是在 PythonAnywhere上），鍵入以下命令︰

    (myvenv) ~/djangogirls$ python manage.py shell
    

結果應該像這樣︰

    (InteractiveConsole)
    >>>
    

你現在在 Django 的互動式主控台中，它就像 Python 提示字元，但有一些附加的 Django 魔法 :)，當然，在這裡你可以使用 Python 所有命令。

### 所有物件 (All objects)

首先，讓我們試著顯示所有我們的文章。你可以用下面的命令︰

    >>> Post.objects.all()
    Traceback (most recent call last):
          File "<console>", line 1, in <module>
    NameError: name 'Post' is not defined
    

哎呀！出現了一個錯誤，它告訴我們沒有文章，它是正確的 -- 我們忘了先導入它！

    >>> from blog.models import Post
    

這很簡單︰我們從 `blog.models` 導入模型 `Post`。讓我們再試著顯示所有文章︰

    >>> Post.objects.all()
    [<Post: my post title>, <Post: another post title>]
    

它是我們先前建立的文章清單！我們使用 Django 管理介面建立這些文章。然而，現在我們想要使用 Python建立新的文章，所以我們該如何做？

### 建立物件 (Create object)

這是你如何在資料庫中建立一個新的文章物件︰

    >>> Post.objects.create(author=me, title='Sample title', text='Test')
    

但這裡遺漏一個要素︰`me`。我們需要傳遞一個模型 `User` 的實例作為一名作者 (author)。如何做到這一點？

讓我們首先導入 User 模型︰

    >>> from django.contrib.auth.models import User
    

在我們的資料庫中我們有哪些使用者？試試這個︰

    >>> User.objects.all()
    [<User: ola>]
    

它是我們先前建立的超級使用者 (superuser)！讓我們現在取得一個使用的者實例︰

    me = User.objects.get(username='ola')
    

正如你所看到的，我們現在以 `username` `取得(get)` 一個等於 'ola' 的 `User` ，簡潔吧！當然，你必須調整你的 username。

現在我們終於可以建立我們的文章︰

    >>> Post.objects.create(author=me, title='Sample title', text='Test')
    

萬歲！想要確認它是否成功？

    >>> Post.objects.all()
    [<Post: my post title>, <Post: another post title>, <Post: Sample title>]
    

在這裡，又多一個文章在清單中！

### 新增更多文章 (Add more posts)

現在，你可以有點樂趣和新增更多的文章，看它是如何運作。新增2至3個並進到下一部分。

### 篩選物件 (Filter objects)

QuerySets 的一個重要部分是能夠進行過濾。 比如說，我們想要找到所有的由使用者 (User) ola編寫的文章。 我們將使用 `filter` 而不是在 `Post.objects.all()` 中的 `all`。 在括弧中我們將說明最後在我們的查詢集 (queryset) 中的文章要滿足什麼條件。 在我們的情況下，它是 `author` 等於 `me`。 在 Django 的寫法是︰`author=me`。 現在我們的程式碼部份看起來像這樣︰

    >>> Post.objects.filter(author=me)
    [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]
    

或者，也許我們想要看到所有 `title` 欄位含有 'title' 的文章？

    >>> Post.objects.filter(title__contains='title')
    [<Post: Sample title>, <Post: 4th title of post>]
    

> **注意**有兩個底線字元（`_`）在 `title` 和 `contains` 之間。 Django 的 ORM 使用這個語法來區分欄位名稱 ("title") 和運算元 (operations) 或 filters ("contains")。 如果您只使用一個底線，你將收到錯誤訊息像 "FieldError: Cannot resolve keyword title_contains"。

你也可以取得所有已發佈的文章清單。我們篩選有 `published_date` 設定在過去時間所有文章來完成這工作︰

> > > from django.utils import timezone Post.objects.filter(published_date__lte=timezone.now()) []

不幸的，我們從 Python 主控台新增的文章是尚未發佈的。我們可以改變它！首先取得一個我們想要發佈文章實例︰

    >>> post = Post.objects.get(title="Sample title")
    

然後用我們的 `publish` 方法 (method) 將它發佈！

    >>> post.publish()
    

現在試著再取得已發佈文章清單（按向上箭號按鈕３次，在按`enter`）︰

    >>> Post.objects.filter(published_date__lte=timezone.now())
    [<Post: Sample title>]
    

### 排序物件 (Ordering objects)

QuerySets 還允許你排序清單的物件。讓我們試著按 `created_date` 欄位來排序︰

    >>> Post.objects.order_by('created_date')
    [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]
    

我們也可以在欄位開頭添加 `-`，做反向排序：

    >>> Post.objects.order_by('-created_date')
    [<Post: 4th title of post>, <Post: My 3rd post!>, <Post: Post number 2>, <Post: Sample title>]
    

### 連結查詢集 (QuerySets)

你還可以使用**連結**將查詢集 (QuerySets) 合併在一起︰

    >>> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    

這真是強而有力，並可讓你寫相當複雜的查詢 (queries)。

酷！你現在已經可以到下一部分！若要關閉 shell，請鍵入這︰

    >>> exit()
    $