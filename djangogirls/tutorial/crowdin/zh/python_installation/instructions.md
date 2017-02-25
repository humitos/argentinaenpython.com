> 本次節是源於怪咖女孩 Carrots (http://django.carrots.pl/)

Django 是用 Python 寫成的。 我們需要使用 Python 在 Django 中做任何事。 讓我們開始安裝吧！ 我們希望你安裝 Python 3.4，所以如果你的電腦裡有其他更早期的版本，你將需要升級它。

### Windows

你可以從這個網站 https://www.python.org/downloads/release/python-343/ 下載給 Windows 使用的 Python。 在下載了一個 ***.msi** 檔案之後，你就直接運行它 (雙擊左鍵)，然後跟著提示的步驟做。 還有一件很重要的事情，一定要記住你安裝 Python 的路徑 (資料夾)。 我們稍後會需要這個路徑！

還有一件事要注意：第二個螢幕上的安裝精靈中，標記為「自訂」，請確保您向下滾動並選擇「將 python.exe 添加到路徑」選項，如下所示：

![別忘了將 Python 添加到路徑](../python_installation/images/add_python_to_windows_path.png)

### Linux

通常你已經內建 Python 了。檢查看看你是不是已安裝（以及它的版本），打開終端機然後輸入下面這個指令：

    $ python3 --version
    Python 3.4.3
    

如果你沒有已安裝的 Python 或是你的版本不一樣，你可以如下步驟來安裝：

#### Debian 或 Ubuntu

在你的終端機輸入以下指令：

    $ sudo apt-get install python3.4
    

#### Fedora (up to 21)

在你的終端機輸入以下指令：

    $ sudo yum install python3.4
    

#### Fedora (22+)

在你的終端機輸入以下指令：

    $ sudo dnf install python3.4
    

### OS X

你需要到這個網站 https://www.python.org/downloads/release/python-343/ 下載 Python 安裝檔:

  * 下載這個 *Mac OS X 64-bit/32-bit installer* DMG 檔案，
  * 雙擊點開 *python-3.4.3-macosx10.6.pkg*

打開你的 *終端機(terminal)* 驗證安裝過程是否有成功，像這樣子運行 `python3` 指令：

    $ python3 --version
    Python 3.4.3
    

* * *

如果你有什麼問題或是有什麼奇怪的錯誤讓你不知道該如何繼續下去 -- 就問你的教練吧！ 請教一個經驗豐富的人有時可以讓事情更順利更完美！