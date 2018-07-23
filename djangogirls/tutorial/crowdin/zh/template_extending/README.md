# 範本擴展 (Template extending)

Django 提供給你的另一件不錯的事是 **範本擴展 (template extending)**。這是什麼意思？這意味著你可以將相同部分的 html 程式碼用在你網站的不同網頁上。

由這種方式，當您想要使用相同的資訊／格式時，你不必在每個檔中重複相同程式碼。如果你想要改變的某些東西，你不必在每個範本中執行這個動作，你僅僅只要改變一個檔案！

## 建立基礎範本 (base template)

基礎範本是最基本的範本，你擴展它到你網站的每一個網頁上。

讓我們在 `blog/templates/blog/` 建立一個 `base.html `檔:

    blog
    └───templates
        └───blog
                base.html
                post_list.html
    

然後打開它，複製所有 `post_list.html` 的內容到`base.html` 檔案中，像這樣︰

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
                <h1><a href="/">Django Girls Blog</a></h1>
            </div>
    
            <div class="content container">
                <div class="row">
                    <div class="col-md-8">
                    {% for post in posts %}
                        <div class="post">
                            <div class="date">
                                {{ post.published_date }}
                            </div>
                            <h1><a href="">{{ post.title }}</a></h1>
                            <p>{{ post.text|linebreaks }}</p>
                        </div>
                    {% endfor %}
                    </div>
                </div>
            </div>
        </body>
    </html>
    

然後在 `base.html`，把你整個 `<body>` 內容（任何在 `<body>` 和 `</body>` 之間的東西） 替換成這些︰

    html
    <body>
        <div class="page-header">
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
    

我們基本上取代 `{% for post in posts %}{% endfor %}` 之間的所有內容︰

    html
    {% block content %}
    {% endblock %}
    

它是什麼意思？ 您剛剛建立一個`區段(block)`，它是一個範本標籤，這個標籤允許你插入擴展到 `base.html`的範本的 HTML 到這區段中。 我們將立刻告訴你如何使用它。

現在存檔，並再次打開你的 `blog/templates/blog/post_list.html`。 刪除一切在 body 以外的內容，然後也刪除 `<div class="page-header"></div>`，所以這個檔案看起來像這樣︰

    html
    {% for post in posts %}
        <div class="post">
            <div class="date">
                {{ post.published_date }}
            </div>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
    

現在加這行到檔案的開頭︰

    {% extends 'blog/base.html' %}
    

{% raw %}它表示我們現在在 `post_list.html`檔中，擴展 `base.html` 範本。 還有一件事︰把一切（除了我們剛剛加入的行）放到 `{% block content %}` 和 `{% endblock content %}` 之間。 像這樣︰{% endraw %}

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
    

就是這些！確認你的網站是否仍正常運作 :)

> 假如有錯誤訊息 `TemplateDoesNotExists`，它告訴你沒有 `blog/base.html` 檔案存在，且你已經在主控台啟動 `runserver`，試著中斷它（按 Ctrl + C -- 同時按 Control 和 C 按鍵），再執行 `python manage.py runserver` 命令重新啟動伺服器。