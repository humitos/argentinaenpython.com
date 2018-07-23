# Django 管理員 (Django admin)

要新增、 編輯和刪除我們剛剛模型化的文章，我們將使用 Django 管理員。

讓我們打開 `blog/admin.py` 檔，並將其內容替換這些︰

    python
    from django.contrib import admin
    from .models import Post
    
    
    admin.site.register(Post)
    

如你所看到的，我們導入 （包括） 在前一章節€中定義的 Post 模型。 要使我們的模型在管理頁面上可以看見，我們需要以 `admin.site.register(Post)` 註冊模型。.

OK，現在來看看我們的 Post 模型。 記得在主控台上執行 `python manage.py runserver` 啟動網站伺服器。 打開瀏覽器，鍵入網址 http://127.0.0.1:8000/admin/，你將看到像這樣的登錄頁面：

![登入頁面][1]

 [1]: images/login_page2.png

要登錄，您需要建立一個 *超級使用者(superuser)* - 這是一個能掌控網站上一切事物的使用者。 回到命令列 (command-line)，鍵入 `python manage.py createsuperuser` 並按 enter。 當提示字元出現時，鍵入您的使用者姓名（小寫、不能有空白）、電子郵件地址和密碼。 不用擔心你不能看見你在輸入的密碼，它就是設定這樣。 你就輸入你的密碼，並按 `enter` 繼續就好了。 輸出畫面應該看起來像這樣（其中使用者名字和密碼應該是你自己的）。

    (myvenv) ~/djangogirls$ python manage.py createsuperuser
    Username: admin
    Email address: admin@admin.com
    Password:
    Password (again):
    Superuser created successfully.
    

回到您的瀏覽器，用你選擇超級使用者資料登入後，你應該看到 Django 的管理儀表板

![Django 管理員 (Django admin)][2]

 [2]: images/django_admin3.png

到 Posts 試用一下，增加五或六篇文章，不要擔心內容 -- 為了節省時間，你可以簡單地複製-貼上這教材上的一些文字 :)。

請確定至少有兩或三篇文章（但不是全部）已設定發佈日期，這對我們以後會很有幫助。

![Django 管理員 (Django admin)][3]

 [3]: images/edit_post3.png

如果你想要知道更多有關於 Django 管理員，您應該查看 Django 文件：https://docs.djangoproject.com/en/1.8/ref/contrib/admin/

現在可能是來一杯咖啡（或茶）或吃一些東西來重振自己的時刻。你建立了你的第一個 Django 模型 -- 你應該暫停一下！