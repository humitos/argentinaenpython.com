> 本章節的部份內容是源自怪咖女孩卡蘿 (Geek Girls Carrots) 的教材(http://django.carrots.pl/)。
> 
> 本章節的一部份內容是源自 Creative Commons Attribution-ShareAlike 4.0 International License 授權的 [django-marcador 教材](http://django-marcador.keimlink.de/)。 Markus Zapke-Gründemann 等人擁有 django-marcador 教材的版權

## 虛擬環境 (Virtual environment)

在安裝 Django 之前，我們將讓你安裝一個非常有用的工具，這個工具可以幫助你保持電腦上編碼環境的整潔。 你可以跳過這個步驟，但我們強烈建議你完成這個部份。 以最佳的設定環境開始，將會在未來為省去很多麻煩。

所以，讓我們來建立一個**虛擬環境** (也稱為*virtualenv*)。 虛擬環境將以專案單位 (per-project) 為基礎將你的 Python/Django 設定隔離開。 這意味你對一個網站做的修改將不會影響到任何你正在開發的網站。 很棒吧！對不對？

你所必需做的是找一個你想建立 `virtualenv` 的目錄 (directory) ，例如：你的主目錄 (home directory) 。 在 Windows 上，它可能看起來向這樣 `C:\Users\Name` （其中 `Name` 是你登入的名字）。

在這份教材中，我們將使用你主目錄 (home directory) 下的新目錄 `djangogirls`：

    mkdir djangogirls
    cd djangogirls
    

我們將稱這個虛擬環境 (virtualenv) 為 `myvenv` ，一般的命令 (command) 格式如下：

    python3 -m venv myvenv
    

### Windows

要建立新的虛擬環境 (`virtualenv`)，你必須打開主控台（我們在幾章前已經告訴過你了，記得嗎？），然後執行 `C:\Python34\python -m venv myvenv`。 它將看起來像這樣：

    C:\Users\Name\djangogirls> C:\Python34\python -m venv myvenv
    

其中 `C:\Python34\python` 是你之前安裝 Python 的目錄，`myvenv` 是你`虛擬環境 (virtualenv) `的名字。 你可以使用任何其他名字，但遵守使用小寫字母，及不使用空白、重音符號和特殊字元。 保持名字簡短也是一個好主意，因為之後你將會常常提到它。

### Linux and OS X

在 Linux 和 OS X 上，建立 `虛擬環境 (virtualenv)` 就和執行 `python3 -m venv myvenv` 一樣簡單。

    ~/djangogirls$ python3 -m venv myvenv
    

`myvenv` 是你`虛擬環境 (virtualenv)` 的名字。 你可以使用任何其他名字，但遵守使用小寫字母，及不使用空白。 保持名字簡短也是一個好主意，因為之後你將會常常提到它。

> **注意：**在 Ubuntu 14.04 啟動虛擬環境會出現如下錯誤：
> 
>     Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1
>     
> 
> 避開這個錯誤，請使用 `virtualenv` 指令 (command) 。
> 
>     ~/djangogirls$ sudo apt-get install python-virtualenv
>     ~/djangogirls$ virtualenv --python=python3.4 myvenv
>     

## 使用虛擬環境 (virtualenv)

上面的指令建立了一個名字為`myvenv`的目錄（或任何你選擇的名字），這目錄裡包含了我們的虛擬環境（基本上是一些目錄和檔案）。　

#### Windows

執行下列命令進入虛擬環境 (virtual environment) ：

    C:\Users\Name\djangogirls> myvenv\Scripts\activate
    

#### Linux and OS X

執行下列命令進入虛擬環境 (virtual environment) ：

    ~/djangogirls$ source myvenv/bin/activate
    

記得把 `myvenv` 更換成你選擇的`虛擬環境 virtualenv` 的名字。

> **注意：**有時候可能無法使用 `source` ，在這種情況下試試下面指令：
> 
>     ~/djangogirls$ . myvenv/bin/activate
>     

你將知道你已經啟動 `虛擬環境 virtualenv` ，當你看到主控台的提示字元看起來像這樣：

    (myvenv) C:\Users\Name\djangogirls>
    

或：

    (myvenv) ~/djangogirls$
    

注意字首會出現 `(myvenv)`

使用虛擬環境時，`python` 將會自動引用正確的版本，所以你可以使用 `python` 代替 `python3` 。.

不錯，所有的支援環境設定都到位了，我們終於可以安裝 Django 。

## 安裝 Django

現在啟動 `虛擬環境 (virtualenv)`，你就可以使用 `pip` 安裝 Django ；在主控台 console 執行 `pip install django==1.8` （注意我們使用雙等號： `==`).

    (myvenv) ~$ pip install django==1.8
    Downloading/unpacking django==1.8
    Installing collected packages: django
    Successfully installed django
    Cleaning up...
    

在 Windows 上

> 假如你在 Windows 平台上執行 pip 時得到錯誤訊息，請檢查你的專案路徑名稱 (pathname) 是否包含空白、重音符號或特殊字元（例如：`C:\Users\User Name\djangogirls`）。　 如果是這樣的話，請考慮搬移到沒有空白、重音符號或特殊字元的地方（建議 `C:\djangogirls` ）。 移動之後，請重試上面的命令。

在 Linux 上

> 假如你在 Ubuntu 12.04 上執行 pip 時得到錯誤訊息，請執行 `python -m pip install -U --force-reinstall pip` 修復在虛擬環境 (virtualenv) 下的 pip 安裝。

就這樣！你現在（終於）準備好建立一個 Django 應用程式了！