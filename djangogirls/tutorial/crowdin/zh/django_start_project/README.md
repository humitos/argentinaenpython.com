# 你的第一個 Django 專案 ！

> 本章節的部份內容是源自怪咖女孩卡蘿 (Geek Girls Carrots) 的教材(http://django.carrots.pl/)。
> 
> 本章節的部份內容是源自 Creative Commons Attribution-ShareAlike 4.0 International License 授權的 [django-marcador 教材][1]。 Markus Zapke-Gründemann 等人擁有 django-marcador 教材的版權

 [1]: http://django-marcador.keimlink.de/

我們將要建立一個簡單的部落格！

第一個步驟是開始一個新的 Django 專案。 基本上，這意味著我們將執行一些 Django 提供的 scripts ，它將為我們建立一個 Django 專案的骨架。 這只是一些目錄和檔案，之後我們將用到。

某些檔案和目錄的名稱對 Django 是非常重要的， 你不應該重新命名我們將要建立的檔案， 將它們移動到不同的地方也不是一個好主意， Django 需要維持一定的結構，以便能夠找到重要的事項。

> 記得在虛擬環境 (virtualenv) 上執行每一個指令。 如果你沒看到字首是`(myvenv)`的提示字元在你的主控台上，你必需要啟動你虛擬環境 (virtualenv) 。 怎麼做，我們在 **Django 安裝 **章節中的**使用虛擬環境 (virtualenv) ** 部份說明過了。 在 Windows 上鍵入 `myvenv\Scripts\activate`，或者在 Mac OS / Linux 鍵入 `source myvenv/bin/activate`，來完成這項工作。

在 Mac 或 Linux 主控台上，您應該執行下面的命令；**別忘了最後的句點（`.`） **：

    (myvenv) ~/djangogirls$ django-admin startproject mysite .
    

在 Windows上；**別忘了最後的句點（`.`） **：

    (myvenv) C:\Users\Name\djangogirls> django-admin startproject mysite .
    

> 句點（`.`）是很重要的，因為它告訴 script 安裝 Django 在你目前的目錄（這個句點 （`.`）是速記參考記號）。
> 
> **注意**當鍵入上述命令時，記住你只鍵入由 `django admin` 或 `django-admin.py` 開始的部分。 在這裡 `(myvenv) ~/djangogirls$` 和 `(myvenv) C:\Users\Name\djangogirls>` 只是一個提示字元的範例，你將可以在這裡輸入命令。　

`django-admin.py` 是一個將為你建立目錄和檔案的 script，現在你應該有一個看起來像這樣的目錄架構。

    djangogirls
    ├───manage.py
    └───mysite
            settings.py
            urls.py
            wsgi.py
            __init__.py
    

`manage.py` 是一個幫助網站管理的 script，有了它我們不需要安裝其他任何東西就能在我們電腦上啟動一個網路伺服器 (web server)。

`settings.py` 檔案包含了你網站的配置數據。

還記得當我們談過郵遞員確認應該把信送到那裡嗎？`urls.py` 檔包含了`urlresolver`使用的形態列表。.

現在讓我們暫且忽略其他檔案，因為我們將不會改變他們。要記住的唯一一點是不要不小心刪除了他們！

## 更改設定 (Changing settings)

讓我們對 `mysite/settings.py` 做一些改變，用你之前安裝的程式編輯器打開這個檔案。

有正確的時間在我們的網站上是很不錯的。 到 [維基百科時區清單 (wikipedia timezones list) ][2] 並複製您相關的時區 (TZ)。 （例如： `Europe/Berlin`）

 [2]: http://en.wikipedia.org/wiki/List_of_tz_database_time_zones

在 settings.py，找到包含 `TIME_ZONE` 的那一行，並修改成你選擇的時區：

    python
    TIME_ZONE = 'Europe/Berlin'
    

適當的改成"Europe/Berlin"。（台灣屬於 "Asia/Taipei" 時區）

我們還需要為我們的靜態檔 (static files) 增加一個路徑（在稍後教材中，我們將找出所有的靜態檔和 CSS 檔）。 到檔案的*最底部*，就在 `STATIC_URL` 這行下面，加上一新內容 `STATIC_ROOT`：

    python
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    

## 安裝資料庫 (Setup a database)

有很多的不同的資料庫軟體，可以存儲你網站的資料。我們將使用預設的 `sqlite3`。.

這已經在 `mysite/settings.py` 檔中設定了：

    python
    DATABASES = {
       'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    

為了建立我們部落格的資料庫，讓我們在主控台上執行下列命令：`python manage.py migrate`（我們需要在包含 `manage.py` 檔的 `djangogirls` 目錄中）。 如果一切進行順利，您應該看到這樣的東西：

    (myvenv) ~/djangogirls$ python manage.py migrate
    Operations to perform:
      Synchronize unmigrated apps: messages, staticfiles
      Apply all migrations: contenttypes, sessions, admin, auth
    Synchronizing apps without migrations:
       Creating tables...
          Running deferred SQL...
       Installing custom SQL...
    Running migrations: DONE
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying sessions.0001_initial... OK
    

完成工作了，啟動網站伺服器 (web server) 看看我們的網站是否正常運作！

你需要在包含 `manage.py` 檔的目錄中（`djangogirls` 目錄）。 在主控台上，我們可以執行 `python manage.py runserver` 啟動網站伺服器 (web server) ：

    (myvenv) ~/djangogirls$ python manage.py runserver
    

如果你在 Windows 上，不能成功執行這命令，使用這個命令 `UnicodeDecodeError` 代替：

    (myvenv) ~/djangogirls$ python manage.py runserver 0:8000
    

現在你需要做的一切是檢查你的網站是否正常運作。打開您的瀏覽器（Firefox、 Chrome、 Safari、 Internet Explorer 或任何你使用的瀏覽器），並輸入這個網址：

    http://127.0.0.1:8000/
    

網站伺務器 (web server) 將取代你的命令提示，直到你停止它。 當網站伺服器在執行時，你想要鍵入更多命令，開啟一個新的視窗台並啟動你的虛擬環境 (virtualenv) 。 若要停止網站伺服器，切換回原執行這個命令的視窗並按 CTRL + C - 同時按 Control 和 C 按鈕（在 Windows 上，你可能需要按 Ctrl + Break）。

恭喜你！你剛剛建立了你的第一個網站並使用網站伺服器 (web server) 執行它！是不是很棒？

![It worked!][3]

 [3]: images/it_worked2.png

準備好下一步了嗎？是時間建立一些內容了！