# 命令行介面簡介

嗯，實在是好興奮啊，對嗎？待會兒你就要寫第一行程式碼了 :)

**容我們為你介紹你的第一個新朋友：命令行！**

接下來的步驟將會為你示範如何使用這個駭客們都一定要使用的黑畫面。這或許第一次看起來有點可怕，但其實不過就是一個閃爍的小游標在等著你下命令給它啦。

> **溫馨小提示** 請記住本書中我們使用的術語「目錄」和「資料夾」可以互換，他們其實是同一個東西。

## 什麼是命令行？

這個視窗，就是通常被稱為 **命令行** 或 **命令行介面** 的東西，這是一個以文字為主的應用程式，可以查看、處理並且控制你電腦裡的檔案們。 更像是 Windows 系統中的檔案總管或是 Mac 裡的 Finder，但是少了圖形化界面 還有其他稱呼像是 *cmd*, *CLT*, *prompt*, *console* 或是 *terminal*.

## 打開命令行介面

開始試驗看看吧，首先我們需要打開命令行介面。

### Windows

按下開始 → 所有程式 → 附屬應用程式 → 命令提示字元。

### Mac OS X

應用程式 → 工具程式 → 終端機。

### Linux

他有可能在 應用程式 → 附屬應用程式 → 終端機 這個路徑下，但主要視你的版本而定。如果不是這裡所提到的開啟方式，就麻煩 Google 它一下 :)

## 命令提示字元

你應該看到一個白的（或黑的）視窗正在等候你的命令。

如果你是用 Mac 或 Linux, 你大概看到一個 `$` 符號，像這樣：

    $
    

在 Windows 下，它是 `>`，像這樣：

    >
    

每個命令都將會以這個提示字元與一個空白字元來準備運行，但是你不需要鍵入這兩個字元，你的電腦會很貼心的幫你打好 :)

> 小提示：在你的情況下可能會像是 `C:\Users\ola>` 或 `Olas-MacBook-Air:~ ola$`在你的命令提示字元之前，那也是 100% 正確的。 在這本教程我們會僅可能讓事情敘述的單純點。

## 你的第一個命令 (耶!)

我們來點簡單的開頭的，輸入以下指令：

    $ whoami
    

或

    > whoami
    

然後按下 `enter`。這是我們的結果：

    $ whoami
    olasitarska
    

如同你所看到的，電腦就會秀出你的使用者名稱，很簡潔對吧？:)

> 試著鍵入每一個指令，不要複製貼上。用這個方法你可以記住更多！

## 基礎

每一個作業系統的命令行都有可觀的不同的指令，所以確定遵循你的自有設備，現在就容我們來試試看吧？

### 目前路徑

知道我們現在身在路徑的哪裡是很棒的事情，讓我們試試看，鍵入以下指令並按下 `enter`：

    $ pwd
    /Users/olasitarska
    

如果你使用 Windows 作業系統：

    > cd
    C:\Users\olasitarska
    

你將可能在你的電腦上看到這些相似的結果。通常你打開命令行，都會以你的使用者根目錄為起點。

> 溫馨小提示：'pwd' 代表「印出目前路徑」。

* * *

### 列出所有檔案和路徑

有哪些東西在這個資料夾下呢？試著找找吧，讓我們看看：

    $ ls
    Applications
    Desktop
    Downloads
    Music
    ...
    

Windows：

    > dir
     Directory of C:\Users\olasitarska
    05/08/2014 07:28 PM <DIR>      Applications
    05/08/2014 07:28 PM <DIR>      Desktop
    05/08/2014 07:28 PM <DIR>      Downloads
    05/08/2014 07:28 PM <DIR>      Music
    ...
    

* * *

### 改變現在的路徑

或許我們現在可以到「桌面」這個路徑去看看？

    $ cd Desktop
    

Windows：

    > cd Desktop
    

檢查看看是不是路徑已經變更了：

    $ pwd
    /Users/olasitarska/Desktop
    

Windows：

    > cd
    C:\Users\olasitarska\Desktop
    

就是這麼簡單！

> 進階技巧：如果你輸入 `cd D` 然後按一下鍵盤上的 `tab` 鍵，這個命令就會自動完成剩下未打完的部分，你可以輸入的更快速。 如果有超過一個開頭是 "D" 的資料夾，那就重複按 `tab` 鍵來選擇你真的要進入的目錄。

* * *

### 創建路徑

新建一個 practice 的資料夾在你的桌面上怎麼樣？你可以這麼做：

    $ mkdir practice
    

Windows：

    > mkdir practice
    

這些小指令可以建立一個叫做 `practice` 的資料夾在你的桌面。 你可以用 `ls` 或 `dir` 指令檢查看看是不是真的有在你的桌面上！ 試試看吧 :)

> 進階技巧：如果你不想重複的輸入一樣的指令，試著使用 `上方向鍵` 和 `下方向鍵` 來選擇你使用過的指令。

* * *

### 實戰！

給你的一個小挑戰： 在你新創建的 `practice` 資料夾下創造一個叫做 `test` 的資料夾，使用 `cd` 及 `mkdir` 指令。

#### 解答：

    $ cd practice
    $ mkdir test
    $ ls
    test
    

Windows：

    > cd practice
    > mkdir test
    > dir
    05/08/2014 07:28 PM <DIR>      test
    

恭喜完成! :)

* * *

### 清除

我們不想弄得一團亂，所以來移除上一個練習我們所創建的全部東西。

首先，我們需要回到桌面：

    $ cd ..
    

Windows：

    > cd ..
    

回到上層目錄使用 `..` 與 `cd` 將會改變你目前的資料夾令你回到父目錄 (就是個包含你現在目錄的目錄)

檢查一下現在你在哪了：

    $ pwd
    /Users/olasitarska/Desktop
    

Windows：

    > cd
    C:\Users\olasitarska\Desktop
    

是時候刪除 `practice` 資料夾了:

> **注意了**：用 `del`， `rmdir` 或 `rm` 來刪除檔案以後就無法挽回了，這表示 *已經刪除的檔案就會一去不復返了*！ 所以呢，必須要非常小心地使用這些指令。

    $ rm -r practice
    

Windows：

    > rmdir /S practice
    practice, Are you sure <Y/N>? Y
    

完成！確保這個資料夾真的被刪除了，我們可以輸入：

    $ ls
    

Windows：

    > dir
    

### 離開

是時候了！你現在可以安全地關閉命令行。我們用更 hacker 的方法來做這件事，試試看吧？:)

    $ exit
    

Windows：

    > exit
    

酷吧？:)

## 彙總

總結

| 指令 (Windows) | 指令 (Mac OS / Linux) | 描述        | 例子                                                |
| ------------ | ------------------- | --------- | ------------------------------------------------- |
| exit         | exit                | 關閉視窗      | **exit**                                          |
| cd           | cd                  | 改變目錄      | **cd test**                                       |
| dir          | ls                  | 列出目錄/檔案   | **dir**                                           |
| copy         | cp                  | 複製檔案      | **copy c:\test\test.txt c:\windows\test.txt** |
| move         | mv                  | 移動檔案      | **move c:\test\test.txt c:\windows\test.txt** |
| mkdir        | mkdir               | 創建新目錄     | **mkdir testdirectory**                           |
| del          | rm                  | 刪除一個目錄/檔案 | **del c:\test\test.txt**                        |

這裡只是一些最基礎的命令行，你可以跑跑看。但是今天我們不打算更深入下去了。

如果你還好奇，[ss64.com][1] 包含了非常完整所有作業系統的的指令。

 [1]: http://ss64.com

## 準備好了嗎？

讓我們迎接 Python 吧！