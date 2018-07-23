# CSS - 讓它變漂亮！

我們的部落格看起來仍然很醜，對吧？時間使讓它變好啊！為此，我們將使用 CSS。

## CSS 是什麼？

串接樣式表 (Cascading Style Sheets, CSS) 是一種語言，它用於描述以標記語言（像 HTML）編寫的網站的外觀和格式，你可以把它當作我們網頁的化妝品 :)。

但我們不想要再從頭開始，對吧？ 我們將再一次使用已經由程式師完成並發怖在網際網路上的免費軟體。 你知道，重複發明一點都不好玩。

## 讓我們使用 Bootstrap！

Bootstrap 是最受歡迎的 HTML 和 CSS 架構之一，它可以用來開發漂亮的網站︰http://getbootstrap.com/

它是由 Twitter 程式設計師編寫，現在由來自世界各地的志願者開發編寫。

## 安裝 Bootstrap

若要安裝 Bootstrap，你需要加這個到你的 `.html` 檔的 `<head>` 部份 (`blog/templates/blog/post_list.html`)：

    html
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    

這並不會加任何檔案到你的專案，它只是指向存在網際網路上的檔案；繼續往下，打開你的網站並更新頁面。它在這兒！

![圖 14.1][1]

 [1]: images/bootstrap1.png

它看起來更漂亮！

## Django 中的靜態檔案 (Static files in Django)

最後，我們將仔細看看這些我們稱為**靜態檔 (static files)** 的東西。 靜態檔是所有的 CSS 和圖像 -- 這些檔案不是動態的，所以他們的內容不依賴請求上下文並且顯示相同的內容給每個使用者。

### Django的靜態檔放那裡

正如你看到的，當我們在伺服器上執行 `collectstatic`，Django 已經知道在哪裡可以為內建的管理應用程式 ("admin" app) 找到靜態檔。現在我們只需要為我們自己的應用程式， `blog` 加一些靜態檔。.

我們在部落格應用程式 (blog app) 裡建立一個名為 `static` 資料夾︰

    djangogirls
    ├── blog
    │ ├── migrations
    │ └── static
    └── mysite
    

Django 將會自動地在你的任何應用程式的資料夾內尋找任何名稱為 "static" 的資料夾，並且它將能使用它們的內容作為靜態檔。

## 你的第一個 CSS 檔！

現在，讓我們建立一個 CSS 檔，加入你自己的風格到你的網頁。 在你的 `static` 目錄內，建立一個新的目錄，名稱為 `css` 。 然後，在這個 `css` 目錄裡，建立一個新的檔，稱為 `blog.css`。 準備好了嗎？

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css
    

是時候寫一些 CSS！在你的程式碼編輯器，打開你的 `blog/static/css/blog.css`檔案。

在這裡，我們不會太深入到自訂格式和學習 CSS，因為它很容易，且在這研討會後你可以自學。 我們很建議你到 [Codeacademy HTML & CSS course][2] 學習你需要知道有關使用 css 讓你網站更漂亮的所有事物。

 [2]: http://www.codecademy.com/tracks/web

但讓我們至少做一些事吧。 也許我們可以改變我們標題的顏色？ 為瞭解顏色，電腦使用特殊的代碼。 它們以 `#` 開始，後面跟著６個字母 (A-F) 或數字 (0-9)， 在這裡你可以找到顏色代碼︰http://www.colorpicker.com/， 您也可以使用 [預定義的顏色 (predefined colors)][3]，如 `red` 和 `green`。.

 [3]: http://www.w3schools.com/cssref/css_colornames.asp

在你的 `blog/static/css/blog.css` 檔中，你應該加入以下程式碼︰

    css
    h1 a {
        color: #FCA205;
    }
    

`h1 a` 是一個 CSS 選取項 (Selector)。 這表示我們要使用我們的格式 (styles) 到在 `h1` 元素 (element) 內的任何 `a` 元素（例如：當我們的有像這樣的程式碼：`<h1><a href="">link</a></h1>`）。 在這種情況下，我們會告訴它要把顏色改為 `#FCA205`，它是橘色。 當然，你可以放你自己的顏色在這裡！

在 CSS 檔中，我們決定的 HTML 檔案中元素的樣式 (styles)。 我們用元素名稱（如：`a`，`h1`，`body`）、`class` 屬性 或 `id` 屬性來辨識元素。 Class 和 id 是你自己給元素的名稱。 Classes 定義一群組的元素，而 ids 指向特定的元素。 例如，CSS 可能以標籤名稱 `a`、class 屬性 `external_link` 或 id 屬性 `link_to_wiki_page` 來辨識下列標籤︰

    html
    <a href="http://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page">
    

瞭解更多 [CSS 選取器 (Selectors) 在 w3schools][4].

 [4]: http://www.w3schools.com/cssref/css_selectors.asp

然後，我們還需要告訴我們的 HTML 範本 (template)，我們增加了一些 CSS。打開 `blog/templates/blog/post_list.html` 檔，並最前面加入這一行︰

    html
    {% load staticfiles %}
    

我們只是在這裡載入靜態檔 :)。 然後，在 `<head>` 和 `</head>` 之間的連結到 Bootstrap CSS 檔案的程式碼後面（瀏覽器按照檔案給予的順序讀取檔案，所以我們檔案中的程式碼可能會覆蓋 Bootstrap 檔案的程式碼），加入這一行：

    html
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    

我們只是告訴我們的範本我們 CSS 檔位於何處。

現在，你的檔案應該像這樣︰

    html
    {% load staticfiles %}
    <html>
        <head>
            <title>Django Girls blog</title>
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
            <link rel="stylesheet" href="{% static 'css/blog.css' %}">
        </head>
        <body>
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
        </body>
    </html>
    

OK，存檔並更新網頁！

![圖 14.2][5]

 [5]: images/color2.png

非常好！也許我們要給我們的網站一點空間，並增加左側邊距？讓我們試試這個！

    css
    body {
        padding-left: 15px;
    }
    

將這個加到你的 CSS，存檔並查看它如何運作！

![圖 14.3][6]

 [6]: images/margin2.png

也許我們可以自訂我們的 header 中的字體？把這個貼到你 `blog/templates/blog/post_list.html` 檔案的 `<head>` 中︰

    html
    <link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
    

這行將從谷歌字體 (https://www.google.com/fonts) 導入稱為*Lobster*的字體。

現在，在 CSS 檔 `blog/static/css/blog.css` 中的 `h1 a` 宣告區段（在大括號 `{` and `}` 之間），加入這行 `font-family: 'Lobster';`，並更新頁面︰

    css
    h1 a {
        color: #FCA205;
        font-family: 'Lobster';
    }
    

![圖 14.3][7]

 [7]: images/font.png

太好了！

如上所述，CSS 有一個 classes 的概念，它基本上允許你對一部分的 HTML 程式碼進行命名，且只使用樣式在這部分，不影響其他程式碼。 它是非常有用的，如果你有兩個 div，但他們做不同事情（如你的 header 和你的 post），所以你不想他們看起來相同。

繼續為部分的 HTML 程式碼命名。加入一個名稱為 `page-header` 的 class 到包含你的標題的 `div`，像這樣︰

    html
    <div class="page-header">
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>
    

現在，加一個名稱為 `post` 的 class 到包含部落格文章的 `div`。

    html
    <div class="post">
        <p>published: {{ post.published_date }}</p>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
    

我們現在將增加宣告區域到不同選項器。 以 `.` 開始的選項器是關於 classes 的。 在網際網路上，有很多很棒的 CSS 教材和解說，幫助你理解下面的程式碼。 現在，只要複製並貼到你的 `blog/static/css/blog.css` 檔︰

    css
    .page-header {
        background-color: #ff9400;
        margin-top: 0;
        padding: 20px 20px 20px 40px;
    }
    
    .page-header h1, .page-header h1 a, .page-header h1 a:visited, .page-header h1 a:active {
        color: #ffffff;
        font-size: 36pt;
        text-decoration: none;
    }
    
    .content {
        margin-left: 40px;
    }
    
    h1, h2, h3, h4 {
        font-family: 'Lobster', cursive;
    }
    
    .date {
        float: right;
        color: #828282;
    }
    
    .save {
        float: right;
    }
    
    .post-form textarea, .post-form input {
        width: 100%;
    }
    
    .top-menu, .top-menu:hover, .top-menu:visited {
        color: #ffffff;
        float: right;
        font-size: 26pt;
        margin-right: 20px;
    }
    
    .post {
        margin-bottom: 70px;
    }
    
    .post h1 a, .post h1 a:visited {
        color: #000000;
    }
    

然後將顯示文章的 HTML 程式碼用 classes宣告包圍起來。將以下內容︰

    html
    {% for post in posts %}
        <div class="post">
            <p>published: {{ post.published_date }}</p>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
    

`blog/templates/blog/post_list.html`，更換為：

    html
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
    

存檔並更新你的網頁。

![圖 14.4][8]

 [8]: images/final.png

喔耶~~~！看起來不錯，對吧？我們剛剛貼上去的程式碼並不真的那麼難理解，且只透過閱讀它你應該能夠理解大部分。

不要害怕稍微修改這個 CSS，且試著去改變一些內容。如果你弄砸某些內容，不必擔心，你總是可以把它恢復原狀！

還有，我們很建議你把免費線上 [Codeacademy HTML & CSS 課程][2] 當成研討會後功課，去學習你需要知道有關使用 css 讓你網站更漂亮的所有事物。

準備好進到下一章了嗎？！:)