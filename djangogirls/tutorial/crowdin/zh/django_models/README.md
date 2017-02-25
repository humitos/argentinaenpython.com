# Django 模型 (Django models)

我們現在想要做的是將來能存儲我們部落格中的所有文章的東西。但為了能夠做我們需要，我們必須談一下`物件`這東西。.

## 物件 (Objects)

在程式設計中有是一個概念，稱為 `物件導向的程式設計`。 這觀念是，與其為每一事物寫一連串煩人的程式指令，我們可以把事物模組化並定義它們彼此的互動關係。

那麼什麼是物件？它是一個屬性 (properties) 和動作 (actions) 的集合。聽起來很奇怪吧，但是我們將會給你一個例子。

假如我們想要塑造一隻貓的模型，我們將建立一個物件 `Cat` 它具有一些屬性如︰`color`, `age`, `mood` （例如：good, bad, sleepy ;)），和`owner` （這是一個 `Person` 物件，或許它的屬性是空的如果它是一隻流浪的貓）。

接著，`Cat` 有一些行為 (actions) ： `purr（嗚嗚叫）`, `scratch（用爪子抓）`或 `feed（餵食）` (我們會給貓 `CatFood（貓食）`，這可能是一個有屬性如：`taste` 的個別物件).

    Cat
    --------
    color
    age
    mood
    owner
    purr()
    scratch()
    feed(cat_food)
    
    
    CatFood
    --------
    taste
    

所以基本上，這概念是用包含屬性（稱為`object properties`）和方法（稱為`methods`）的程式碼來描寫真實的事物。).

那麼我們將如何建立我們的部落格文章 (blog posts) 的模型？我們想要建立一個部落格，對吧？

我們需要回答這個問題：什麼是部落格文章 (blog post) ？它應該有什麼屬性？

嗯，確定的是我們的博客文章 (blog post) 需要一些文字內容和標題，對嗎？ 知道是誰寫的也不錯 ── 所以我們需要作者。 最後，我們想要知道文章是什麼時候建立和公佈。

    Post
    --------
    title
    text
    author
    created_date
    published_date
    

那些工作和部落格文章有關？有一些公佈文章的`方法 (method) `是不錯的，對吧

所以我們將需要一個`公佈(publish)` 的方法。

既然我們已經知道我們想要完成什麼，讓我們開始在 Django 上建立模型吧。

## Django 模型 (Django model)

知道什麼是物件 (object) 之後，我們可以為我們的部落格文章 (blog post) 建立一個 Django 模型。

在 Django 上，模型是一種特殊的物件 ── 它儲存在`資料庫(database)` 中。 資料庫是資料的集合。 這是你將存儲有關使用者 (users) 和你的部落格文章 (blog posts) 等資訊的地方。 我們將使用一個 SQLite 資料庫來存儲我們的資料。 這是 Django 預設的資料庫裝置 ── 對我們現在而言，它是足夠的。

你可以把資料庫中的模型看作是有列（欄位）和行（資料）的試算表。

### 建立應用程式 (Creating an application)

為了讓一切保持整潔，我們將在我們的專案內建立一個別的應用程式。 一開始就讓一切井然有序是很好的。 我們需要在主控台上（從 `djangogirls` 檔所在目錄 `manage.py` ）執行以下命令來建立一個應用程式：

    (myvenv) ~/djangogirls$ python manage.py startapp blog
    

你會看到一個新的 `blog` 目錄被建立了，這個目錄現在包含一些檔案；在我們的專案裡，我們的目錄和檔案應該看起來像這樣：

    djangogirls
    ├── mysite
    | __init__.py
    | settings.py
    | urls.py
    | wsgi.py
    ├── manage.py
    └── blog
        ├── migrations
        | __init__.py
        ├── __init__.py
        ├── admin.py
        ├── models.py
        ├── tests.py
        └── views.py
    

建立應用程式後，我們還需要告訴 Django 應該去使用它。 我們在 `mysite/settings.py` 檔中做這個告知動作。 我們需要找到 `INSTALLED_APPS`，並在 `)` 之上增加一行 `'blog',`。 所以最終的節結果應如下所示：

    python
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',
    )
    

### 建立一個部落格文章張貼模型 (Creating a blog post model)

在 `blog/models.py` 檔中，我們定義所有名稱為 `Models` 的物件 ── 這是我們將定義我們部落格文章 (blog post) 的地方。

讓我們打開 `blog/models.py`，刪除裡面的內容並編寫這樣的程式碼：

    python
    from django.db import models
    from django.utils import timezone
    
    
    
    class Post(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True) 
    
        def publish(self):
            self.published_date = timezone.now()
            self.save()
    
        def __str__(self):
            return self.title
    

> 再確認你在 `str` 的兩邊是使用兩個底線字元 (`undescore character, _`)。 這個規矩在 Python 中頻繁地使用，有時候我們也稱它為 "dunder" （是 "double-underscore" 的縮寫）。　

它看起來可怕，是吧？但不用擔心，我們將會解釋這幾行的意思！

所有以 `from` 或 `import` 開始的程式行都從其他檔案添加一些內容。 所以與其複製和張貼相同的東西到每一個檔案　我們可以用 `from ... import ...` 導入這些東西。.

`class Post(models.Model):` -- 這一行定義了我們的模型（它是一個 `object`）。).

*   `class` 是一個特殊的關鍵字，表示我們在定義一個物件 (object) 。
*   `Post` 是我們模型的名字，我們可以給它不同的名字（但我們要避免用特殊字元和空白），永遠要用大寫做為名稱開頭。
*   `models.Model` 意味 Post 是一個 Django 模型，所以 Django 知道這模型應該被儲存在資料庫。

現在我們要定義之前談論到的屬性 (properties) ：`title`, `text`, `created_date`, `published_date` 和 `author`。 完成這件工作我們需要定義每一個欄位 (field) 的型態 (type) （它是文字？ 數字？ 日期？ 和令一個物件的關係，例如：a User？）

*   `models.CharField` -- 這是你如何以有限的字元定義文本 (text) 。
*   `models.TextField` -- 這是沒有長度限制的長文本 (text)，對部落格文章內容而言，聽起來很不錯，對吧？
*   `models.DateTimeField` -- 這是時間和日期。
*   `models.ForeignKey` -- 這是連結到另一個模組。

我們不會在這裡解說每一個程式碼，因為這會花費太多時間。 你應該看一看 Django 的文件，如果你想要知道更多有關模型欄位和如何定義上面未提及的東西 (https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types)。

什麼是 `def publish(self):`？ 它就是我們之前談到的 `publish` 方法 (method)。 `def` 意味著這是一個函數／方法 (function/method)，而 `publish` 是這個方法 (method) 的名字。 如果需要，你可以更改方法的名字。 命名規則是我們使用小寫字母，且用底線代替空白。 例如：一個計算平均價格的方法可以叫做 `calculate_average_price`。.

方法 (methods) 通常會`傳回(return)` 一些東西。 在 `__str__` 方法中有一個例子。 在這種情況下，當我們呼叫 `__str__()` 我們將得到一個有 Post 標題 (title) 的文本 (text)（**字串(string) **）。

假如對於模型尚有不清楚的地方，請隨時問你的教練！ 我們知道它很複雜，尤其是當你在同一時間學習物件 (objects) 和函數 (functions)。 但希望現在對你而言它看起來沒有那麼神奇。

### 為你資料庫中的模組建立表格 (Create tables for models in your database)

在這裡的最後一個步驟是把我們新的模型加到我們的資料庫。 首先我們必須讓 Django 知道我們已經修改過我們的模型（我們剛剛建立的那一個）。 鍵入 `python manage.py makemigrations blog`。 它將看起來像這樣：

    (myvenv) ~/djangogirls$ python manage.py makemigrations blog
    Migrations for 'blog':
      0001_initial.py:
     - Create model Post
    

Django 為我們準備了一個我們現在必須使用的轉移檔 (migration file) 到我們的資料庫。鍵入 `python manage.py migrate blog`，它輸出應該是這樣：

    (myvenv) ~/djangogirls$ python manage.py migrate blog
    Operations to perform:
      Apply all migrations: blog
    Running migrations:
      Rendering model states... DONE
      Applying blog.0001_initial... OK
    

萬歲！我們的 Post 模型現在在我們的資料庫了！看一下它是不錯的主意，對吧？進到下一章，看看你的 Post 的樣子！