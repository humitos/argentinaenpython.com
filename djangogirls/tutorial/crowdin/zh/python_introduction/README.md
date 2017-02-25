# Python 簡介

> 本章節的部份內容是源自怪咖女孩卡蘿 (Geek Girls Carrots) 的教材(http://django.carrots.pl/)。

讓我們寫一點程式碼吧！

## Python 提示字元

要開始玩 Python，我們需要打開您的電腦上的 *命令行*。 你應該已經知道如何做了 — — 你在 [命令列簡介][1] 那章學過。

 [1]: ../intro_to_command_line/README.md

一旦你準備好了，就跟著下面的說明操作吧。

我們想要開啟 Python 主控台，所以在 Windows 上輸入 `python` 或在 Mac OS/Linux 上輸入 `python3` 並按下 `enter`.

    $ python3
    Python 3.4.3 (...)
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    

## 你第一個的 Python 命令！

運行 Python 命令後，命令提示字元改為 `>>>`。 對我們來說這意味著現在我們只可以使用 Python 語言中的命令們。 你不需要再鍵入 `>>>` - Python 會為你輸入的。

如果你想要在任何時間退出 Python 主控台，只要鍵入 `exit()` ，或在 Windows 下使用快速鍵 `Ctrl + Z` ，或者在 Mac/Linux 環境下使用 `Ctrl + Z` 都可以退出主控台。 然後你就不會再看到 `>>>` 了。

現在，我們不想要退出 Python 主控台。 我們想要瞭解更多它的事情。 讓我們從最簡單的東西開始。 例如，試著輸入一些數學運算，如 `2 + 3` 然後按下 `enter`.

    >>> 2 + 3 
    5
    

太好了！看到答案出來了嗎？Python 了解數學！你可以試其他命令： -`4 * 5` -`5-1` -`40 / 2`

好了，你可以試著自己玩會兒 :)。

正如你所看到的 Python 是一個偉大的計算機。如果你還想知道你能做什麼...

## 字串

那輸入你的名字呢？你可以像下面這樣試試看：

    >>> "Ola"
    'Ola'
    

你現在已經創造了你的第一個字串！ 這是一個可以被電腦運用的字元集合。 字串通常會以一個同樣的字元來起頭和結束。 或許是一個單引號 (`'`) 或者雙引號 (`"`) (這兩者沒有差別！)，這會讓 Python 知道引號中的東西是一個字串。

字串們也可以被串在一起，試試看這招：

    >>> "Hi there " + "Ola"
    'Hi there Ola'
    

你也可以用一個數字來把字串乘起來：

    >>> "Ola" * 3
    'OlaOlaOla'
    

還有，如果你想要放一個單引號在你的字串裡面，你有兩種方式可以達成這個目標。

使用雙引號來宣告字串：

    >>> "Runnin' down the hill"
    "Runnin' down the hill"
    

或者，在想要加入的單引號前面給他一個反斜線 (``):

    >>> 'Runnin\' down the hill'
    "Runnin' down the hill"
    

不賴吧？去看看如何把你的名字全部換成大寫，簡單的輸入這個：

    >>> "Ola".upper()
    'OLA'
    

你只需要用 `upper` 這個 **函數 (function)** 在你的字串後面就可以了！ 一個函數（像是 `upper()`）就是一個指令集，讓 Python 可以在這個物件 (`"Ola"`) 中展現你呼叫這個函數的效果。

如果你想要知道你的名字總共有幾個字元，也有相對應的函數可以叫用！

    >>> len("Ola")
    3
    

你應該很好奇，為什麼有時候你會在字串結尾用 `.` 來叫用一個函數（例如 `"Ola".upper()`），但有時你會先呼叫函數，然後把字串放在括號中？ 嗯，在某些狀況下，函數屬於某個物件，像是 `upper()` ，這個函數就只能表現在字串上。 在這個狀況下，我們可以稱呼這類型函數為 **方法(method)**。 其他時候，函數不屬於任何特定的類型或物件，可為各種不同類型或物件所用，像是 `len()`。 這是為什麼我們可以在 `len()` 這個函數中放入一個 `"Ola"` 字串作為參數。

### 彙總

好了，說夠了字串。目前為止你學到了：

*   **命令提示字元** - 在 Python 的命令提示字元下輸入指令（程式碼）來得到結果
*   **數字與字串** - 在 Python 中數字可計算，而字串表示一個文字物件
*   **運算子** - 像是 + 與 *, 可結合兩個數值進行運算產生一個新的值
*   **函數** - 像是 upper() 與 len(), 讓物件展現出某種行為。

你剛剛學到的是所有程式語言的基礎。準備好接受更多挑戰了嗎？來吧！

## 錯誤訊息

我們來試試新的東西。看看我們能不能使用找到我們名字長度的那個函數，來得到某個數字的長度呢？輸入 `len(304023)` 按下 `enter`:

    >>> len(304023)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: object of type 'int' has no len()
    

恭喜！我們得到了我們的第一個錯誤訊息！它抱怨說這個物件的類型是 "int" (integer, 整數) 所以根本沒有長度這件事。所以我們現在應該怎麼辦呢？或許我們可以把我們這個數字寫成一個字串看看如何？字串就有長度啦，對吧？

    >>> len(str(304023))
    6
    

看起來成功了！我們 `len` 函數中使用了 `str` 函數。`str()` 可以任何物件轉成字串。

*   `str` 函數可將物件轉為 **字串**
*   `int` 函數可將物件轉為 **整數**

> 重要：我們可以轉數字為字串，但我們不必然能把文字轉為數字 - 想想看要是 `int('hello')` 會有怎樣的結果？

## 變數

程式設計中有一個重要的觀念稱為變數 (variables)。 一個變數其實沒什麼，就是一個你稍後可以叫用的一個名字。 程序員使用這些變數去儲存資料，讓他們的程式碼有更高的可讀性，這樣他們就不必一直記得那些資料是什麼。

假設現在我們做了一個新的變數叫做 `name`:

    >>> name = "Ola"
    

你看吧？就這麼簡單！其實只代表一件事情：這個叫做 name 的變數等於 "Ola" 這個字串。

如同你所注意到的，你的程式沒有回傳任何你宣告的東西。所以我們如何得知我們所宣告的變數確實存在呢？簡單的輸入 `name` 然後按下 `enter`:

    >>> name
    'Ola'
    

呀比！你的第一個變數啊啊啊 :)！你可以隨時改變它的值像這樣：

    >>> name = "Sonja"
    >>> name
    'Sonja'
    

你也可以在函數中使用它：

    >>> len(name)
    5
    

太完美了，對吧？當然，變數可以是任何東西，數字亦然！試試看這個：

    >>> a = 4
    >>> b = 6
    >>> a * b
    24
    

但是萬一我們叫錯變數了呢？你可以猜到會發生什麼事情嗎？讓我們試試看吧！

    >>> city = "Tokyo"
    >>> ctiy
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'ctiy' is not defined
    

又是一個錯誤訊息！ 如同你所見，Python 有各式各樣的錯誤訊息，這個就叫做一個 **NameError**。 Python 會在你試圖使用一個從未宣告的變數時給你這個錯誤訊息。 如果你得到像這樣的錯誤，就回頭看看你的程式碼裡面是不是有什麼變數的名字是打錯的。

玩一會兒吧，看看你還能做什麼！

## Print 函數

試試這招：

    >>> name = 'Maria'
    >>> name
    'Maria'
    >>> print(name)
    Maria
    

當你只是輸入 `name`，Python 直譯器會馬上 *回應* 你變數「name」所代表的字串，就是個用單引號包起來的 M-a-r-i-a 字母們。 當你說 `print(name)` ，Python 就會在螢幕上「印出」這個變數的乾淨內容，沒有引號。

就像是我們稍後會看到的， 當我們想要印出某些東西時，或是想要印出一個有很多行的東西時，`print()` 就是個超有用的函數。

## 清單

除了字串和整數，Python 還有一堆不同形態的物件。 現在我們要介紹的稱為 **清單 (list)**。 清單就是你想的那樣：它是一個列出一堆物件的物件 :)

開始建立一個 List 吧：

    >>> []
    []
    

對沒錯，這就是一個空的 List。看起來沒什麼用啊... 我們來建立一組包含樂透彩數字的 List 吧。我們不想每次都重覆輸入這個長的 List，所以我們就把它存進一個變數裡吧：

    >>> lottery = [3, 42, 12, 19, 30, 59]
    

好了，我們有一個 List 了！我們可以拿它來幹嘛？來看看這個 List 的長度吧。你想到可以用什麼函數了嗎？沒錯就是它！

    >>> len(lottery)
    6
    

賓果！ `len()` 可以告訴你這個 List 有多長。真是太神奇了傑克！或許我們還可以幫這個 List 排序：

    >>> lottery.sort()
    

這不會回傳任何值，只是默默的的改變了 List 中數字們的順序。我們把它印出來看看發生了什麼事吧：

    >>> print(lottery)
    [3, 12, 19, 30, 42, 59]
    

如你所見，這串 List 數字已經從小到大排序了。恭喜囉！

那如果我們想要反排序呢？試試看吧！

    >>> lottery.reverse()
    >>> print(lottery)
    [59, 42, 30, 19, 12, 3]
    

很簡單對吧？如果你還想替 List 新加一點東西，可以輸入這個指令：

    >>> lottery.append(199)
    >>> print(lottery)
    [59, 42, 30, 19, 12, 3, 199]
    

如果你只想要秀某一個數字，你可以使用 **索引 (index)** 來指定。 索引就是一個指出 List 某個物件位置的數字。 電腦宅們喜歡讓索引從 0 開始，所以你的 List 中的第一個物件的索引就是 0，下一個物件則是 1，以此類推。 試試這招：

    >>> print(lottery[0])
    59
    >>> print(lottery[1])
    42
    

如你所見，你可以呼叫 List 變數的名字並指定索引值，並將索引值放在中括號中，來取得 List 裡不同的物件。

想要從你的 List 刪掉一些東西的話，你將需要使用我們剛剛學到的 **index** 和 **del** 語法 (del 是 delete 的縮寫)。 讓我們試個例子來加深學習印象；我們將刪除我們的 List 中的第一個數字。

    >>> print(lottery)
    [59, 42, 30, 19, 12, 3, 199]
    >>> print(lottery[0])
    59
    >>> del lottery[0]
    >>> print(lottery)
    [42, 30, 19, 12, 3, 199]
    

帥吧！

更多好玩的是，請嘗試些其他的 index: 6，7，1000，-1，-6 或 -1000。看看是否你能嘗試在執行命令前預測結果。這些結果合理嗎？

你可以在這個 Python 文件章節中，找到所有支援 List 物件的方法：https://docs.python.org/3/tutorial/datastructures.html

## 字典

字典 (Dictionary) 和清單 (List) 有點像，差別在於，你可以用鍵值 (key) 而非索引值 (index) 來取得在 Dictionary 中的值 (value)。一個 key 可以是字串或數字。你可以使用兩個大括號來宣告一個 dictionary：

    >>> {}
    {}
    

這樣就創建了一個空字典，喲齁！

現在，試著輸入下面指令（你也可以試著輸入你自己的資訊）：

    >>> participant = {'name': 'Ola', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
    

使用這個指令，你就等於是宣告了一個叫做 `participant` 的三個 key-value 結對變數：

*   Name 這個 `key` 對應到 `'Ola'` 這個 value (一個 `字串` 物件),
*   `country` 對應到 `'Poland'` (另一個 `字串`),
*   還有 `favorite_numbers` 對應到 `[7, 42, 92]` (一個包含了三個數字在內的 `清單`)。

你可以指定獨特的 key 來檢查內容，語法如下：

    >>> print(participant['name'])
    Ola
    

你看，和 List 有點像。不過你就不需要再記住 index 了 - 變成一個好記的名稱。

如果你向 Python 要一個不存在的 key 所對應的 value 的話會發生什麼事呢？我們試試看吧！

    >>> participant['age']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'age'
    

看到了吧，又是一個錯誤訊息，這次是 **KeyError** 。Python 會讓你知道這個 `'age'` key 事實上是不存在目前的 dictionary 中的。

什麼時候要用 List，什麼時候又要用 Dictionary 呢？嗯，這個問題值得深思。再看看下面內容前先把這個問題放在心裡吧。

*   你是不是只是需要一個有序的序列呢？就使用 List 吧。
*   你需要有 key 值的 value，好讓你可以更有效率地 (使用 key) 找到特定值嗎？那就使用 Dictionary 吧。

Dictionary 也像 List 一樣，可以 *默默地* 把它裡面的東西做點改變，你可以加入一對新的 key/value 值像這樣：

    >>> participant['favorite_language'] = 'Python'
    

如同 List，Dictionary 也可以使用 `len()`，回傳 Dictionary 總共有幾對 key-value 值吧，輸入下面指令：

    >>> len(participant)
    4
    

我希望目前為止對你來說都還可以了解。 :) 準備好玩玩更多有趣的 Dictionary 了嗎？跳到下一行看看一些很酷的事情吧。

你可以使用 `del` 指令來刪除 Dictionary 中的項目。 如果你說，想要刪掉一個叫做 `'favorite_numbers'` 的 key，就輸入下面指令：

    >>> del participant['favorite_numbers']
    >>> participant
    {'country': 'Poland', 'favorite_language': 'Python', 'name': 'Ola'}
    

輸出結果如你所見，符合 'favorite_numbers' 的 key-value 數對已經被刪除了。

除此之外，你也可以改變已經建立的 Dictionary 中的特定值，輸入：

    >>> participant['country'] = 'Germany'
    >>> participant
    {'country': 'Germany', 'favorite_language': 'Python', 'name': 'Ola'}
    

一樣如同你所看見的，一個 key 值為 `'country'` 的值從 `'Poland'` 變成了 `'Germany'`。 :) 興奮嗎？喲齁！你剛剛學到更多超棒的知識了！

### 彙總

太完美了！你現在了解更多程式設計的知識了。在上面你學到了：

*   **錯誤訊息** - 當 Python 看不懂你給的指令時，你現在知道怎麼去閱讀並且了解錯誤訊息的意思了
*   **變數** - 這是物件的名字，讓你可以更輕鬆的寫程式，也讓你的程式更具可讀性
*   **清單** - 可以用特定順序來儲存多個物件的清單
*   **字典**- 可以儲存 key/value 結對物件

人生要進階了，興奮嗎？ :)

## 比較事物

對比事物是程式設計中很大的一部分。最容易比較的是什麼? 那當然就是比較數目了。讓我們看看這是如何運作:

    >>> 5 > 2
    True
    >>> 3 < 1
    False
    >>> 5 > 2 * 2
    True
    >>> 1 == 1
    True
    >>> 5 != 2
    True
    

我們給了 Python 一些數目字來比較。正如你所看到的 Python 可以作比較的不只是數目字，它也可以比較算術的結果。不錯，是吧?

當我們想確認兩個數字是否同等時，為什麼我們把兩個等號 = `=` 放在一起嗎? 我們使用單個 `=` 用於將值分配給變數。 如果你想要檢查兩個事物是否彼此相等，你永遠，**永遠** 需要放兩個 `==`。 我們也可以說兩個事物東西彼此不相等。 為此，我們使用符號 `!=`，如上例所示。

給 Python 多兩個任務︰

    >>> 6 >= 12 / 2
    True
    >>> 3 <= 2
    False
    

`>` 和 `<` 很簡易，但 `>=` 和 `<=`是什麼意思？像這樣讀他們︰

*   x `>` y 表示：x 大於 y
*   x `<` y 表示：x 小於 y
*   x `<=` y 表示：x 小於或等於 y
*   x `>=` y 表示：x 大於或等於 y

真棒！想要做一次嗎？試試這個︰

    >>> 6 > 2 and 2 < 3
    True
    >>> 3 > 2 and 2 < 1
    False
    >>> 3 > 2 or 2 < 1
    True
    

你可以給 Python 任何數量你想要它比較的數字，它會給你答案！很聰明，對吧？

*   **and** -- 如果你使用 `and` 運算子，兩個比較值必須為真 (True)，才能讓整個命令為真 (True)
*   **or** -- 如果您使用 `or` 運算子，只要其中一個比較值為真 (True)，就能讓整個命令為真 (True)

你聽過 ”比較蘋果和橘子” 說法嗎？讓我們試著 Python 等同詞︰

    >>> 1 > 'django'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unorderable types: int() > str()
    

在這裡就像你在運算式中看到，Python 是不能比較一個數字 (`int`) 和一個字串 (`str`)。 相反地，它顯示 **TypeError**，並告訴我們不能這兩種類型不能相互比較。

## 布林值 (Boolean)

順便一提，你剛剛學習了一種新型的 Python 物件。它叫做 **Boolean** 而且可能是最簡單的類型。

布林值只有兩個布林物件：

為了讓 Python 理解這一點，你永遠需要把它寫成 'True'（第一個字母大寫，其餘字母小寫）。 **true、TRUE、 tRUE 不會正常運作 -- 只有 True 是正確的。**（當然，這個同樣適用於 False。）

布林值也可以是變數！看看這裡︰

    >>> a = True
    >>> a
    True
    

你也可以這樣做︰

    >>> a = 2 > 5
    >>> a
    False
    

練習並由試著執行以下命令體會布林值的樂趣︰

*   `True and True`
*   `False and True`
*   `True or 1 == 1`
*   `1 != 2`

恭喜！在程式設計中，布林值是最酷的功能之一，而且你剛剛學會了如何使用它們！

# 儲存它！(Save it!)

到目前為止，我們已經在解譯器上寫了我們所有的 python 程式碼，解譯器限制了我們一次只能輸入一行程式碼。 正常程式是儲存在檔中，並由我們的程式語言的**解譯器 (interpreter)** 或 **編譯器 (compiler)** 執行。 到目前為止，我們已經在 Python **解譯器**上一次執行一行我們的程式。 我們接下來的幾個任務將需要不止一行的程式碼，所以我們很快將需要︰

*   離開 Python 解譯器
*   打開我們選擇的程式碼編輯器
*   儲存一些程式碼到一個新的 python 檔
*   執行它！

要退出我們一直在使用 Python 解譯器，只需鍵入 ~~~ exit()~~~ 功能函數 (function)︰

    >>> exit()
    $
    

這將讓你返回到命令列提示字元。

早些時候，我們在[程式碼編輯器][2] 章節中選擇了一個程式碼編輯器。現在我們將需要打開程式碼編輯器和寫一些程式碼到一個新的檔案︰

 [2]: ../code_editor/README.md

    python
    print('Hello, Django girls!')
    

> **注意** 你應該注意到程式碼編輯器最酷的地方之一︰ 顏色！ 在 Python 主控台中，所有東西都是相同的顏色，現在你應該看到 `print` 函數的顏色是不同於字串顏色。 這就所謂的 ”語法強調”，在編寫程式碼時是非常有用的功能。 顏色將會給你提示，如未閉合的字串或關鍵字名稱錯誤（如在 `def` 函數中，我們會在下面看到） 。 這是我們使用程式碼編輯器中的的原因之一 :)

明顯地，你現在是一個經驗相當豐富的 Python 開發人員，所以便意編寫一些你今天已經學到了的程式碼。

現在，我們需要儲存這個檔案並給它一個描述性的名字。 讓我們稱這個檔案為 **python_intro.py** 並將它儲存到你的桌面。 我們可以給檔案取任何我們想要的名字，但重要的部分是要確保檔名以 **.py** 結尾。 **.py** 副檔名告訴我們的作業系統，這是一個 **python 可執行檔**，Python 可以執行它。

存檔後，現在可以執行它！用你已經在命令列章節學到的技能，使用終端機 **更改目錄** 到桌面。

在 Mac 上，命令列將看起來像這樣︰

    $ cd /Users/<your_name>/Desktop
    

在 Linux 上，它將會像這樣（這個詞 ”桌面” 可能會被翻譯成你的語言）︰

    $ cd /home/<your_name>/Desktop
    

在 windows 上，它將會像這樣︰

    > cd C:\Users\<your_name>\Desktop
    

如果你遇到困難，就尋求幫助。

現在使用 Python 執行檔案中的程式碼，像這樣︰

    $ python3 python_intro.py
    Hello, Django girls!
    

好！你剛好執行你的第一個被儲存到檔案的 Python 程式 。很棒的感覺吧？

你現在可以繼續程式設計的基本工具︰

## If...elif...else

很多程式碼應該當某些滿足條件時才能執行，這就是為什麼 Python 有一種叫做 **if 語法 (statements)**。.

將你 **python_intro.py** 檔中的程式碼替換成這︰

    python
    if 3 > 2:
    

如果我們存檔和執行它，我們會看到這樣的錯誤︰

    $ python3 python_intro.py
    File "python_intro.py", line 2
             ^
    SyntaxError: unexpected EOF while parsing
    

Python 期望我們能夠給進一步指示，假如條件 `3 > 2` 為真（或 `True` 就此而言）該執行什麼。 我們試著讓 Python 列印 ”成功了！”。 把你 **python_intro.py** 的程式碼改為這樣︰

    python
    if 3 > 2:
        print('It works!')
    

注意為什麼我們在下一行程式碼內縮４個空白？ 我們需要這樣做，所以 Python 知道假如結果為真 (true) 該執行什麼程式碼。 你可以內縮１個空白，但幾乎所有的 Python 程式設計師都內縮４個空白，使程式碼看起來很整潔。 一個 `tab` 等同４個空白。

存檔並給再執行它︰

    $ python3 python_intro.py
    It works!
    

### 什麼情況下一個條件式不是真的？

在前面的例子，程式碼只有當條件是真時才執行。但 Python 也有 `elif` 和 `else` 語法︰

    python
    if 5 > 2:
        print('5 is indeed greater than 2')
    else:
        print('5 is not greater than 2')
    

當你執行它將顯示出︰

    $ python3 python_intro.py
    5 is indeed greater than 2
    

如果２是比５大的數字，則會執行第二個命令。很簡單，對吧？讓我們看看 `elif` 如何運作︰

    python
    name = 'Sonja'
    if name == 'Ola':
        print('Hey Ola!')
    elif name == 'Sonja':
        print('Hey Sonja!')
    else:
        print('Hey anonymous!')
    

並執行：

    $ python3 python_intro.py
    Hey Sonja!
    

看看那裡發生了什麼？ 假如前面的條件式失敗的話，`elif` 讓你增加額外可執行的條件式。

在你的 `if` 後面，你可以增加任何你想要的 `elif` 語句。例如︰

    python
    volume = 57
    if volume < 20:
        print("It's kinda quiet.")
    elif 20 <= volume < 40:
        print("It's nice for background music")
    elif 40 <= volume < 60:
        print("Perfect, I can hear all the details")
    elif 60 <= volume < 80:
        print("Nice for parties")
    elif 80 <= volume < 100:
        print("A bit loud!")
    else:
        print("My ears are hurting! :(")
    

Python 依序執行每個測試，並顯示︰

    $ python3 python_intro.py
    Perfect, I can hear all the details
    

### 彙總

在最後三個練習中你學到了︰

*   **比較事物** -- 在 Python 中你可以使用 `>`、`>=`、`==`、`<=`、`<` 和 `and`、`or` 運算子來比較事物。
*   **布林值** -- 一種只能有兩個值之一的物件︰`True` 或 `False`。
*   **存檔** -- 儲存程式碼在檔案中，所以你可以執行較大的程式。
*   **if...elif...else** -- 允許只在滿足特定條件時才執行程式碼的語法。

現在是這一章的最後一部分了！

## 你自己的函數！(Your own functions!)

還記得可以在 Python 中執行函數像 `len()`？很好，好消息 -- 現在你將學習如何編寫你自己的函數！

函數是 Python 應該執行的一序列的指令。 在 Python 中每個函數都以關鍵字 `def` 開頭、給定一個名稱、並且可以有一些參數。 讓我們從一個簡單的開始。 將 **python_intro.py** 中的程式碼替換為以下內容︰

    python
    def hi():
        print('Hi there!')
        print('How are you?')
    
    hi()
    

Okay，我們的第一個函數準備好了！

你可能想知道為什麼我們把函數的名稱寫在檔案的底部。 這是因為 Python 從頂部到底部讀取檔案並執行它。 所以為了使用我們的函數，我們必須重新把它寫在底部。

現在讓我們執行這個，看看會發生什麼︰

    $ python3 python_intro.py
    Hi there!
    How are you?
    

這很簡單！我們要建立我們的第一個有參數的函數。我們將使用前面的例子 -- 一個對執行它的人說 ’hi’ 功能 -- 並加上名字稱呼︰

    python
    def hi(name):
    

正如你所看到的，我們現在給我們的函數一個我們叫它 `name` 的參數︰

    python
    def hi(name):
        if name == 'Ola':
            print('Hi Ola!')
        elif name == 'Sonja':
            print('Hi Sonja!')
        else:
            print('Hi anonymous!')
    
    hi()
    

記住︰在 `if` 語句內的 `print` 向內的縮進四個空白。這是因為當滿足條件時函數才執行。現在讓我們看看它是如何運作：

    $ python3 python_intro.py
    Traceback (most recent call last):
    File "python_intro.py", line 10, in <module>
      hi()
    TypeError: hi() missing 1 required positional argument: 'name'
    

哎呀，一個錯誤。 幸運地，Python 給我們一個非常有用的錯誤訊息。 它告訴我們，函數 `hi()`（我們定義的那一個）必需有一個參數（名為 `name`），而且我們忘了把它傳遞函數當我們呼叫它時。 讓我們在檔的底部修復它︰

    python
    hi("Ola")
    

並再次執行它︰

    $ python3 python_intro.py
    Hi Ola!
    

而如果我們更改名字？

    python
    hi("Sonja")
    

然後執行它︰

    $ python3 python_intro.py
    Hi Sonja!
    

現在，你認為會發生什麼事假如你填另一個名字在那裡？（不是 Ola 或 Sonja）試一試，看看你是否正確。它應該顯示這︰

    Hi anonymous!
    

這太棒了，對吧？ 以這種方式，當你想要改變函數要問候的人名時，你自己不需要每次重複所有動作。 而這正是為什麼我們需要函數 -- 你永遠不會想要重複你的代碼！

讓我們做些更聰明的事 -- 有比兩個更多的名字，而為每個人名寫一個狀況將會很難，對吧？

    python
    def hi(name):
        print('Hi ' + name + '!')
    
    hi("Rachel")
    

現在讓我們呼叫程式碼︰

    $ python3 python_intro.py
    Hi Rachel!
    

恭喜你！你剛剛學會了如何編寫函數！:)

## 迴圈 (Loops)

這已經是最後一部分，很快速，對吧？:)

程式設計師不喜歡重複。程式設計核心是自動化，所以我們不想人工地呼叫每個我們想問候的人，對吧？這是迴圈派上用場的地方。

還記得列表 (lists) 嗎？讓我們做一個 girls 列表︰

    python
    girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
    

我們想要用他們的名字問候它們每一個人，我們有 `hi` 函數來完成這個，所以讓我們在一個迴圈中使用它︰

    python
    for name in girls:
    

~~~ for~~~ 語法類似 ~~~ if~~~ 語法；它們下面的程式碼都需要向內縮４個空白。

這是將會在檔中的完整程式碼︰

    python
    def hi(name):
        print('Hi ' + name + '!')
    
    girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
    for name in girls:
        hi(name)
        print('Next girl')
    

然後當我們執行它︰

    $ python3 python_intro.py
    Hi Rachel!
    Next girl
    Hi Monica!
    Next girl
    Hi Phoebe!
    Next girl
    Hi Ola!
    Next girl
    Hi You!
    Next girl
    

正如你所看到的，所有你內縮放進 `for` 語句的程式碼都會對 `girls` 列表的每一個元素執行一次。.

你也可以在 `for` 使用以`range` 函數計數的數字。

    for i in range(1, 6):
        print(i)
    

這將顯示︰

    1
    2
    3
    4
    5
    

`range` 是一個函數，它建立一系列數字，一個接一個（你提供這些數字作為參數）。

請注意這兩個數字的第二並未包括在 Python 輸出清單中（這表示 `range(1, 6)` 是從１數到５，但不包括數字６）。 這是因為 ”range” 是半開，意思是它包含第一個值，但不包括最後一個。

## 彙總

就是這些。**你太棒了！**這是一個棘手的章節，所以你應該為自己感到驕傲。我們當然為你的進展感到驕傲！

你可能想要短暫地做一些別的事 -- 伸伸懶腰，走動一會兒，讓你的眼睛休息 -- 再往下一章節前。:)

![杯子蛋糕][3]

 [3]: images/cupcake.png