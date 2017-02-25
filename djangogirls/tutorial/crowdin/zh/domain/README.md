# 網域名稱 (Domain)

Heroku 給了你一個網域名稱，但是它很長、很難記、又醜。有一個簡短和容易記住的網域名稱將會很酷，對吧？

在這一章我們將教你如何購買網域名稱和將它連結到 Heroku！

## 到哪裡註冊一個網域名稱？

一個典型網域名稱成本約１５美元一年。 取決於網域提供者，有更便宜和更昂貴的選擇。 你可以從很多公司買到域網域名稱︰一個簡單[谷歌搜尋][1] 會給數以百計的選擇。

 [1]: https://www.google.com/search?q=register%20domain

我們最喜歡的一個是 [I want my name][2]。他們的廣告是 "無痛網域管理 (painless domain management)"，而且它真的是無痛的。

 [2]: https://iwantmyname.com/

## 如何在 IWantMyName 註冊網域名稱？

到 [iwantmyname][3] 並在搜尋格 (search box) 鍵入您想要網域名稱。

 [3]: http://iwantmyname.com

![][4]

 [4]: images/1.png

你現在應該看到和你搜尋詞相關且可用的網域名稱清單。 正如你所看到的，一張笑臉表示這個網域名稱是你可購買的，而悲傷的臉表它已經被使用了。

![][5]

 [5]: images/2.png

我們已經決定購買 `djangogirls.in`：

![][6]

 [6]: images/3.png

去結帳，如果你還沒有 iwantmyname 帳戶，你現在應該註冊一個；然後，提供您的信用卡資訊和購買網域名稱！

在那之後，點選功能表中的 `Domains` 和選擇你新買的網域。找到之後點選 `manage DNS records` 連結︰

![][7]

 [7]: images/4.png

現在你需要找到這張表單︰

![][8]

 [8]: images/5.png

並填寫以下內容： - Hostname: www - Type: CNAME - Value: your domain from Heroku (for example djangogirls.herokuapp.com) - TTL: 3600

![][9]

 [9]: images/6.png

在底部點選 Add 按鈕並除存這些更改。

它可能花費長達數小時才能讓你的網域開始運作，所以請耐心等待！

## 在 Heroku 上設定網域 (Configure domain in Heroku)

你也需要告訴 Heroku 你想要使用你自訂的網域名稱。

到 [Heroku 儀表板 (Dashboard)][10]，登錄你的 Heroku 帳戶並選擇的應用程式。然後進入應用程式設定且在 `Domains` 部份加入你的網域名稱，以及儲存你的更改。

 [10]: https://dashboard.heroku.com/apps

就這樣！