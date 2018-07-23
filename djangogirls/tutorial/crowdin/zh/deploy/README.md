# 部署！ (Deploy!)

> **注意** 這一章節內容有時候比較不容易完成。 堅持下去並完成它；佈署是網站開發過程中的重要部份。 這一章節是放在這份教材的中間部份，所以你的教練可以幫助你將你的網站上線。 這意味著假如你無法跟上課堂進度，你仍然可以自己獨立完成這份教材。

直到目前你的網站只在你的電腦上，現在我們將學習如何將它部署至網際網路上。 部署是發佈你的應用程式 (application) 到網際網路的過程，所以大家終於可以看到你的應用程式 (application )。

就如你所學的，網站必須位於伺服器上。 網際網路上有許多伺服器提供者。 我們將使用一個相對較簡單的部署程序：[PythonAnywhere][1]。 PythonAnywhere 是免費提供給小型應用程式，對沒有很多使用者的小型應用程式，它是足夠使用的，

 [1]: http://pythonanywhere.com/

其他外部服務我們將使用 [GitHub][2]，它是一個程式碼托管服務 (code hosting service)。 還有其他這項服務提供者，但當今幾乎所有程式設計師都有一個 GitHub 帳戶，現在你將有一個。

 [2]: http://www.github.com

我們將使用 GitHub 作為我們和 PythonAnywhere 之間傳輸程式碼的踏腳石。

# Git

Git 是一個被很多程式設計師使用的 ”版本控制系統"(version control system)。 這個軟體可以追蹤檔案在過去時間的變化，所以以後你可召回特定的版本。 有點像 Microsoft Word 中 ”追蹤改變” 的特性，但功能更強大。

## 安裝 Git

> **注意**假如你已經完成安裝步驟，你不需要再做這個動作了，你可以直接進入下一章節，開始建立你的 Git 倉庫 (repository)。

{% include "deploy/install_git.md" %}

## 啟動我們的 Git 倉庫 (repository)

Git 追蹤任何修改到一個放在程式碼倉庫 (code repository 或簡稱 "repo") 的特定檔案集合。 讓我們開始我們的專案。 打開你的主控台，並在 `djangogirls` 目錄下執行這些命令：

> **注意**初始化倉庫 (repository) 之前，先用 `pwd` (OSX/Linux) 或 `cd` (Windows) 命令來確認你目前的工作目錄。 你應該在 `djangogirls` 目錄下。

    $ git init
    Initialized empty Git repository in ~/djangogirls/.git/
    $ git config --global user.name "Your Name"
    $ git config --global user.email you@example.com
    

我們只需要對每個專案做一次初始化倉庫，(你將不需要再輸入使用者名字和電子郵件地址了)。

Git 將會追蹤這個目錄下所有檔案和資料夾的變更，但我們想要它忽略一些檔案。 為此，我們在這專案根目錄下新增一名為 `.gitignore` 的檔案。 打開你的編輯器，新增一個包含下列內容的檔案。

    *.pyc
    __pycache__
    myvenv
    db.sqlite3
    .DS_Store
    

並把它以 `.gitignore` 的名稱儲存在 "djangogirls" 的目錄中。

> **注意**檔名開頭的小圓點 "." 是很重要的。 假如你在建立這個檔案時遇到困難（例如：Macs不喜歡你經由 Finder 來建以小圓點 "." 開頭的檔案），那麼在你的編輯器上使用 "另存新檔 Save As"，這樣就沒問題了。　　

在執行 `git add` 之前，或當你發現你自己不確定那些文件已經被修改，先使用 `git status` 命令確認是一個好主意。 這樣將會防止各種意外發生，像加入或提交錯誤的檔案。 `git status` 命令會傳回任何未被追蹤的／已修改的／暫存的檔案、分部狀態等等。 輸出會像這樣：

    $ git status
    On branch master
    
    Initial commit
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
    
            .gitignore
            blog/
            manage.py
            mysite/
    
    nothing added to commit but untracked files present (use "git add" to track)
    

最後儲存我們的修改；到你的主控台，並執行這些命令：

    $ git add -A .
    $ git commit -m "My Django Girls app, first commit"
     [...]
     13 files changed, 200 insertions(+)
     create mode 100644 .gitignore
     [...]
     create mode 100644 mysite/wsgi.py
    

## 推送我們的程式碼到 GitHub (Pushing our code to GitHub)

到 [GitHub.com][2] 註冊一個新的免費使用者帳戶。（如果你在研討會預習時已經完成，那就太好了）

然後，新增一個名稱為 ”my-first-blog" 的倉庫 (repository)。 保持 "initialise with a README" 選框未勾選，保持 gitignore 選項空白（我們已經手動建立了），並保留 License 選項為無 (None)。

![][3]

 [3]: images/new_github_repo.png

> **注意** `my-first-blog` 這個名字很重要 -- 你可以把它改成其它名字，但在下面的說明中會常提到它，你必須每次都更換成你取的名字。 保持 `my-first-blog` 這個名字學習起來可能較輕鬆。.

在下面的畫面，你將看到你倉庫的複製網址 (repo's clone URL)；選擇"HTTPS"版本，複製網址 (URL)，稍後我們將會把它貼到我們的鐘端機上。

![][4]

 [4]: images/github_get_repo_url_screenshot.png

現在我們需要把你電腦上的 Git 倉庫 (Git repository) 和 GitHub 的連接。

鍵入下面命令到你的主控台（把 `<your-github-username>` 改為你建立你的 GitHub 帳戶時輸入的使用者名稱，但不要輸入尖括號）：

    $ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
    $ git push -u origin master
    

輸入你的 GitHub 使用者名稱和密碼，你應該會看到類似這樣的畫面：

    Username for 'https://github.com': hjwp
    Password for 'https://hjwp@github.com':
    Counting objects: 6, done.
    Writing objects: 100% (6/6), 200 bytes | 0 bytes/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/hjwp/my-first-blog.git
     * [new branch] master -> master
    Branch master set up to track remote branch master from origin.
    

<!--TODO: maybe do ssh keys installs in install party, and point ppl who dont have it to an extention -->

現在你的程式碼已經在 GitHub 上了。 去確認一下吧！ 你將在一群好夥伴 -- [Django][5]、[Django Girls Tutorial][6] 中發現它，許多其他傑出的開放程式碼軟體也把它們的程式碼放在 GitHub :) 上。

 [5]: https://github.com/django/django
 [6]: https://github.com/DjangoGirls/tutorial

# 在 PythonAnywhere 設置我們的部落格 (Setting up our blog on PythonAnywhere)

> **注意**你可能已經在稍早的安裝步驟中建立你的 PythonAnywhere 帳戶，如果是的話，你不須要再做這個動作了。

{% include "deploy/signup_pythonanywhere.md" %}

## 拉取我們的程式碼到 PythonAnywhere 上 (Pulling our code down on PythonAnywhere)

當你登入 PythonAnywhere 後，你將進到你的儀板表 (dashboard) 或主控台 (Consoles) 頁面。 選擇啟動 "Bash" 主控台這一選項，這是 PythonAnywhere 版的主控台，它就像你電腦上的一樣。

> **注意** PythonAnywhere 是建立在 Linux 上，所以如果你是使用Windows，它的主控台會和你電腦上的有一點不同。

讓我們以建立一個我們的倉庫 (repo) 的副本 (clone)，將我們的程式碼從 GitHub 拉到PythonAnywhere上。 鍵入下面命令到 PythonAnywhere 的主控台（不要忘記在 `<your-github-username>` 的地方，使用你的 GitHub 的使用者名稱）：

    $ git clone https://github.com/<your-github-username>/my-first-blog.git
    

這將拉取你的程式副本到 PythonAnywhere，你可以鍵入`tree my-first-blog`確認：

    $ tree my-first-blog
    my-first-blog/
    ├── blog
    │ ├── __init__.py
    │ ├── admin.py
    │ ├── migrations
    │ │ ├── 0001_initial.py
    │ │ └── __init__.py
    │ ├── models.py
    │ ├── tests.py
    │ └── views.py
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
    

### 在 PythonAnywhere 建立虛擬環境 (Creating a virtualenv on PythonAnywhere)

就像在你自己的電腦上一樣，你可以在 PythonAnywhere 上建立虛擬環境 (virtualenv)；在 Bash 主控台，鍵入：

    $ cd my-first-blog
    
    $ virtualenv --python=python3.4 myvenv
    Running virtualenv with interpreter /usr/bin/python3.4
    [...]
    Installing setuptools, pip...done.
    
    $ source myvenv/bin/activate
    
    (mvenv) $ pip install django whitenoise
    Collecting django
    [...]
    Successfully installed django-1.8.2 whitenoise-2.0
    

> **注意**你可能會花幾分鐘在 `pip install` 步驟上，耐心等待！但如果超過五分鐘，可能就有問題；請詢問你的教練。

<!--TODO: think about using requirements.txt instead of pip install.-->

### 收集靜態檔 (Collecting static files)

你疑惑什麼是 "whitenoise" 嗎？ 它是為了服務所謂的 ”靜態檔” ("static files") 的工具。 靜態檔是不會經常更改或不執行程式碼的檔案，例如 HTML 或 CSS 檔。 和在我們自己的電腦相比，在伺服器server它們以不同的方式運轉，我們需要一個 "whitenoise" 的工具來服務它。

在後面的編輯網站 CSS 檔教材中，我們將學習到更多關於靜態檔的內容。

現在，在伺服器我們只需要執行一個額外的命令 `collectstatic`。 它告訴 Django 去收集伺服器上所有它需要的靜態檔。 就目前而言，主要是讓網站管理界面 (admin site) 看起來較美觀的檔案。

    (mvenv) $ python manage.py collectstatic
    
    You have requested to collect static files at the destination
    location as specified in your settings:
    
        /home/edith/my-first-blog/static
    
    This will overwrite existing files!
    Are you sure you want to do this?
    
    Type 'yes' to continue, or 'no' to cancel: yes
    

鍵入 "yes"，然後它會自行運轉！你喜歡讓電腦的印表機列印出一頁又一頁讓人費解的文章嗎？我總是會弄點小噪音幫它伴奏。Brp, brp brp...

    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/actions.min.js'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/inlines.min.js'
    [...]
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/changelists.css'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/base.css'
    62 static files copied to '/home/edith/my-first-blog/static'.
    

### 在 PythonAnywhere 上建立資料庫

你的電腦和伺服器之間還有另一個不同點：它使用一個不同的資料庫；所以您的電腦上的使用者帳戶和文章可能不同於伺服器上。

我們可以使用 `migrate` 和 `createsuperuser` 初始化伺服器的資料庫就像在我們自己的電腦上一樣：　

    (mvenv) $ python manage.py migrate
    Operations to perform:
    [...]
      Applying sessions.0001_initial... OK
    
    
    (mvenv) $ python manage.py createsuperuser
    

## 公佈我們的部落格為網路應用程式 (web app)

現在我們的程式碼在 PythonAnywhere 上，我們的虛擬環境準備好了，靜態檔已收集了，並初始化資料庫；我們準備將公佈它為一個網路應用程式 (web app)。

按 PythonAnywhere 標誌 (logo) 回到 PythonAnywhere 儀表板，然後按 **Web** 選項；最後，按**Add a new web app**。.

確認你的網址後 (domain name)，在對話方塊中，選擇 **manual configuration** （注意 *不是* "Django" 選項）。 接下來選擇 **Python 3.4**，然後按 Next 就完成工作了。

> **注意**請確認你選擇 "Manual configuration" 選項， 不是 "Django" 那個。太好了我們完成 PythonAnywhere Django 預設建置了。;-)

### 設置虛擬環境 (virtualenv)

你將會被帶到 PythonAnywhere 上你的網站應用程式的配置螢幕，這裡是每當你想要更改伺服器上的應用程式時，你需要去的地方。

![][7]

 [7]: images/pythonanywhere_web_tab_virtualenv.png

在 "Virtualenv" 部分，點選紅色文字 "Enter the path to a virtualenv"，再鍵入：`/home/<your-username>/my-first-blog/myvenv/`。 進到下一步之前，請點擊有打勾記號的藍框來保存路徑。

> **注意**用你自己的使用者名稱代替；如果你犯錯，PythonAnywhere 將顯示一個小警告。

### 設定 WSGI 檔 (Configuring the WSGI file)

Django 使用 "WSGI 協定"，這是 PythonAnywhere 支援，為服務使用 Python 的網站的一個標準。 透過編輯 WSGI 設定檔 (WSGI configuration file)，我們設定 PythonAnywhere 去辨識我們的 Django 部落格。

按一下 "WSGI configuration file" 連結 （在 "Code" 部分靠近頁面頂端 -- 它會被命名如 `/var/www/<your-username>_pythonanywhere_com_wsgi.py`），然後你將進入一個編輯器。

刪除所有的內容，並用下面內容代替：

    python
    import os
    import sys
    
    path = '/home/<your-username>/my-first-blog' # use your own username here
    if path not in sys.path:
        sys.path.append(path)
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    
    from django.core.wsgi import get_wsgi_application
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(get_wsgi_application())
    

> **注意**別忘了用你自己的使用者名稱取代 `<your-username>`。 　

這個檔案的工作是告訴 PythonAnywhere，我們的網站應用程式 (web app) 位在什麼地方和 Django 設定檔的名稱，它也設定了 "whitenoise" 靜態檔工具。

點選 **Save**，然後返回到 **Web** 選項。

我們完成了！點選綠色 **Reload** 大按鈕，你將可以看到你的應用程式了，你將發現在頁面頂端有一個它的連結。

## 除錯提示 (Debugging tips)

當你嘗試瀏覽你的網站時，如果你遇到錯誤，首先是去你的 **錯誤日誌 (error log)** 中尋找除錯資訊 你將會在 PythonAnywhere 的 [Web 選項][8] 發現這個連結。 看看這裡是否有任何錯誤資訊；最新的是在底部。 常見的問題包括：

 [8]: https://www.pythonanywhere.com/web_app_setup/

*   忘記執行主控台中的步驟之一：建立虛擬環境、啟動虛擬環境、安裝 Django、執行部署靜態檔、轉移資料庫。

*   在 Web 選項上，虛擬環境路徑設定錯誤，假如有問題，這裡通常將會有一個紅色錯誤訊息。

*   WSGI 設定檔錯誤 -- 你設定到 my-first-blog folder 路徑正確嗎？

*   像對你的網站應用程式 (web app) 一樣，你有選擇相同版本的 Python 給你的虛擬環境嗎？兩者都應該是 3.5。

*   有一些[一般常見的除錯提示在 PythonAnywhere wiki 上][9]。.

 [9]: https://www.pythonanywhere.com/wiki/DebuggingImportError

記住，你的教練會在這裡幫助你！

# 你上線了！

你網站的預設頁面應該出現 "Welcome to Django"，就像在你自己的電腦上一樣。 試著在網址後面加 `/admin/`，你將會進入網站管理畫面。 登入使用者名和密碼，你就會看到你可以在伺服器上新曾文章。

給自己一個 *大大的* 鼓勵！ 伺服器部署是網站開發中最棘手的部分之一，人們通常花費好幾天才能讓它們正常運作。 但是你讓你的網站上線了，在真正的網際網路上，就像其他網站一樣！