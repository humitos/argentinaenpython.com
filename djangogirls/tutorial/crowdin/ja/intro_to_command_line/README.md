# Introduction to the command-line interface

さぁ、これから最初のコードを書いていきますよ。楽しんでいきましょう！

**最初にお友達になるのはコレです。: コマンドライン!**

プログラマーが黒い画面に向かっている光景を見たことがありますか？ここからは、その黒い画面を触ってみます。最初はちょっとコワイと思うかもしれませんが、そんなことはありません。プロンプトと呼ばれるものがあなたの命令（コマンド）を待っています。

> 使用用語に’ディレクトリ’と’フォルダ’という表現があります。それらは同じ事である事に注意してください。

## What is the command line?

さて、コマンドライン あるいは コマンドライン　インターフェイスと呼ばれるこの画面は、キーボードで入力したテキストで命令を出してコンピューターと直接対話するように、 ファイルを見たり、変更したり (グラフィカル・インターフェースじゃないだけで、WindowsのエクスプローラやMacのファインダーと同じ役割です) するものです。 このコマンドラインは、 cmd, CLI, プロンプト, コンソール or ターミナル と呼ばれることもあります。.

## Open the command-line interface

では、実際にコマンドラインを開いて、触ってみることとしましょう。

### Windows

スタートメニュー → すべてのプログラム → アクセサリ → コマンド プロンプト

### Mac OS X

アプリケーション → ユーティリティ → ターミナル

### Linux

おそらく ［アプリケーション］ー［アクセサリ］ー［ターミナル］と選択し起動できるでしょう。あなたのシステムによってはこの通りではないことがあります。見つからないときは、Google先生にきいてみましょう。 

## Prompt

おそらく今、真っ白または真っ黒な画面が開かれていることでしょう。この画面はあなたの命令を待っています。

If you're on Mac or Linux, you probably see `$`, just like this:

    $
    

Windowsの方は、 > という記号が表示されていることでしょう。

    >
    

各コマンドの先頭には、この記号とスペースがつきます。あなたのコンピューターが表示してくれるので、自分で入力する必要はありません。 

> ちょっと補足です。プロンプト記号の前にC:\Users\ola> or Olas-MacBook-Air:~ ola$ のような表示がありますね。これは間違いではありません。100%正解です。 このチュートリアルでは、シンプルにわかりやすくするために、その部分を省略して記述します。

## Your first command (YAY!)

では最初は簡単なコマンドを実行してみましょう。次のように入力してみてください。

    $ whoami
    

または

    > whoami
    

そして最後にEnterキーを押して下さい。このような結果が返ってきます

    $ whoami
    olasitarska
    

ご覧のとおり、コンピューターがあなたのユーザーネームを表示してくれましたね。面白いでしょ?

> コピー＆ペーストではなく、コマンドを入力して試してみてください。そのうち自然と覚えられるようになりますからね！

## Basics

OSによってコマンドが若干違います。あなたのコンピューターのOSの方法に従って、以下は進めていってくださいね。次にいってみましょう。

### Current directory

今どこのディレクトリにいるか（どのフォルダで作業をしているか）、知りたいですよね？では、このようにキーボードで入力して、Enterキーをおしてください。

    $ pwd
    /Users/olasitarska
    

Windowsの場合：

    > cd
    C:\Users\olasitarska
    

おそらく、似たようなものがあなたの画面に表示されたのではないでしょうか。コマンドラインを起動した最初は、通常ユーザーのホームディレクトリが表示されます。

> 補足: 'pwd' は'print working directory'を意味しており、現在いる作業ディレクトリを取得することです。

* * *

### List files and directories

では、その中には何があるのでしょうか？表示させてみましょう。

    $ ls
    Applications
    Desktop
    Downloads
    Music
    ...
    

Windows:

    > dir
     Directory of C:\Users\olasitarska
    05/08/2014 07:28 PM <DIR>      Applications
    05/08/2014 07:28 PM <DIR>      Desktop
    05/08/2014 07:28 PM <DIR>      Downloads
    05/08/2014 07:28 PM <DIR>      Music
    ...
    

* * *

### Change current directory

次に、デスクトップのディレクトリに移動してみましょう。

    $ cd Desktop
    

Windows:

    > cd Desktop
    

本当に変更されたかどうか確認してみてください：

    $ pwd
    /Users/olasitarska/Desktop
    

Windows:

    > cd
    C:\Users\olasitarska\Desktop
    

できていますね！

> cd Dと入力して、キーボードのtabボタンを押してください。すると、Dに続く残りの部分が自動的に補完されて入力されます。 もし、Dから始まるディレクトリ名が他にもあれば、tabボタンを繰り返し押すと候補が次々と表示されます。入力が楽になりますね

* * *

### Create directory

それでは、Django Girlsのディレクトリをデスクトップに新規作成してみましょう。

    $ mkdir practice
    

Windows:

    > mkdir practice
    

この短いコマンドで、デスクトップにpracticeという名前の新しいフォルダが作成されました。 あなたのデスクトップを見てフォルダが作成されていることを確認してみましょう。あるいは、先ほど学んだコマンド` ls/dir` を使って確認しましょう。 やってみてください。

> 同じコマンドを何度もなんども入力したくない時は、上下矢印キー↑，↓を押せば、先ほどキーボードから入力したものが現れます。内容を修正したい場合には，左右矢印キー←，→を利用して修正したい位置にカーソルを移動させて，修正することができますよ。

* * *

### Exercise!

練習をしてみましょう。先ほど作成したpracticeディレクトリの中に、新たにtestという名前のディレクトリを作成してください。使うコマンドは、 cd と mkdir ですよ。

#### Solution:

    $ cd practice
    $ mkdir test
    $ ls
    test
    

Windows:

    > cd practice
    > mkdir test
    > dir
    05/08/2014 07:28 PM <DIR>      test
    

おめでとうございます！よくできました！

* * *

### Clean up

練習がおわったら、それをそのままに置いておくと邪魔になりますね。削除しておきましょう。

はじめに、作業するディレクトリをデスクトップに戻しましょう。

    $ cd ..
    

Windows:

    > cd ..
    

cdの後にある..で、現在の親ディレクトリに移動します。（今作業しているフォルダのひとつ上のフォルダに移動するということですね。）

現在の作業ディレクトリを確認しておきましょう。

    $ pwd
    /Users/olasitarska/Desktop
    

Windows:

    > cd
    C:\Users\olasitarska\Desktop
    

では、practiceディレクトリを削除しましょう。

> **Attention**:del, rmdir や rm のコマンドを使って削除したファイルは、復活できません。完全に消えてしまいます。 このコマンドを使う時は、よく気をつけてくださいね。

    $ rm -r practice
    

Windows:

    > rmdir /S practice
    practice, Are you sure <Y/N>? Y
    

Done! To be sure it's actually deleted, let's check it:

    $ ls
    

Windows:

    > dir
    

### Exit

ここまでです。それではコマンドラインを終了しましょう。かっこいいやり方で終わりたいですよね？

    $ exit
    

Windows:

    > exit
    

かっこいいですね！

## 概要

ここに学んだコマンドをまとめておきます。

| コマンド (Windows) | コマンド (Mac OS / Linux) | 説明                | 例                                                 |
| -------------- | --------------------- | ----------------- | ------------------------------------------------- |
| exit           | exit                  | ウインドウを閉じる         | **exit**                                          |
| cd             | cd                    | ディレクトリを変更         | **cd test**                                       |
| dir            | ls                    | ディレクトリ/ファイルの一覧を表示 | **dir**                                           |
| copy           | cp                    | ファイルのコピー          | **copy c:\test\test.txt c:\windows\test.txt** |
| move           | mv                    | ファイルを移動           | **move c:\test\test.txt c:\windows\test.txt** |
| mkdir          | mkdir                 | 新しいディレクトリを作成      | **mkdir testdirectory**                           |
| del            | rm                    | ディレクトリ/ファイルを削除    | **del c:\test\test.txt**                        |

ここで勉強したのはコマンドのほんの一部でしたが、このワークショップで使うコマンドはこれだけです。

もっと勉強したい方は、 ss64.com に各OSのコマンド一覧があります。ご参考までに。

## Ready?

よし、次はPythonを勉強していきましょう!