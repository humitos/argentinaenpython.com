> このセクションの部分は、Geek Girls Carrots (http://django.carrots.pl/) でチュートリアルに基づいています。
> 
> このチャプターの一部はCreative Commons Attribution-ShareAlike 4.0 International License のライセンスによるdjango-marcador tutorialに基づいています。このdjango-marcador tutorialはMarkus Zapke-Gründemann et al.が著作権を保有しています。 このdjango-marcador tutorialはMarkus Zapke-Gründemann らが著作権を保有しています。 

## 仮想環境

Django をインストールする前に、あなたのコーディング環境を、きれいにしておく便利な道具をインストールしてもらいます。 このステップをとばすこともできますが、しかし、このステップをとばすことは全くお勧めしまません。 可能な限りベストなセットアップで始めることは将来のたくさんのトラブルからあなたを救うはずですから！

さあ、**仮想環境（virtual environment )**(*virtualenv*とも呼ばれています）を作成してみましょう。 仮想環境（virtual environment）ではプロジェクト単位であなたのPython/Djangoのセットアップを他から隔離します。 これは、あなたがひとつのウェブサイトにおこなったどんな変更も、あなたが開発している他のサイトに影響を及ぼさないということです。 わかりましたか？

あなたがしなければならないのは、あなたが`仮想環境（virtual environment）`を作成したいディレクトリを見つけることです（たとえばホームディレクトリなどです）。 Windows のホームディレクトリは `C:\Users\Name` (`名前` はあなたのログインの名前です) のようになります。

このチュートリアルのために、ホームディレクトリに新しいディレクトリ`djangogirls`を作成します。

    mkdir djangogirls
    cd djangogirls
    

`myvenv`という仮想環境（virtual environment）を作成します。一般的なコマンドは以下のようになります：

    python3 -m venv myvenv
    

### Windows

新しい0<>仮想環境(virtualenvironment)</code>を作成するために、コンソールを開き（コンソールについては何章か前にお話ししましたね。覚えてますか？）、`C:\Python34\python -m venv myvenv`を実行して下さい。例えばこのように入力してください こんな感じですね。

    C:\Users\Name\djangogirls > C:\Python34\python -m venv myvenv
    

`C:\Python34\python`はあなたが Python をインストールしたディレクトリ、 `myvenv` は、あなたの `仮想環境(virtualenvironment)` の名前です。 どんな名前でも使うことができますが、必ず小文字で表記し、スペース・アクセント記号・特殊文字は入れないでください。 短い名前にしておくのもいいアイデアですーあなたはこの名前を何度も参照しますから！

### Linux と OS X

LnuxやOX Xで'仮想環境(virtualenvironment)'を作るときは、`Python3 -m venv myvenv` を実行するだけです。例えばこんな感じです：

    ~/djangogirls$ python3 -m venv myvenv
    

`myvenv` は、あなたの `仮想環境(virtualenvironment)` の名前です。 どんな名前でも使うことができますが、必ず小文字で表記し、スペースは入れないでください。 短い名前にしておくのもいいアイデアですーあなたはこの名前を何度も参照しますから！

> **備考:**この方法によるUbuntu 14.04でのvirtual environmentの初期化は次のエラーが出ます：
> 
>     Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1
>     
>     
> 
> このエラーを回避するために、代わりに`仮想環境(virtualenvironment)`コマンドを使います。
> 
>     ~/djangogirls$ sudo apt-get install python-virtualenv
>     ~/djangogirls$ virtualenv --python=python3.4 myvenv
>     

## 仮想環境の操作

上に示したコマンドは仮想環境（基本的には一連のディレクトリとファイル）を含む`myvenv` という名前（あるいはあなたが選んだ名前）のディレクトリを生成します。次に我々がしたいのは、これを実行し、開始することです。

#### Windows

実行して、仮想環境を起動します。

    C:\Users\Name\djangogirls > myvenv\Scripts\activate
    

#### Linux と OS X

実行して、仮想環境を起動します。

    ~/djangogirls$ source myvenv/bin/activate
    

`myvenv`のところをあながた選んだ`仮想環境(virtualenvironment)`名に置き換えることを忘れないで下さいね！

> **備考:** `source` ではできない場合もあります。その場合は、代わりに以下のように入力してみてください：
> 
>     ~/djangogirls$ source myvenv/bin/activate
>     

あなたのコンソールが以下のように見える事により、`仮想環境(virtualenvironment)`が起動した事を知る事ができるでしょう。

    (myvenv) C:\Users\Name\djangogirls>
    

または

    (myvenv) ~/djangogirls$
    

行頭に `(myvenv)` が表示されます！

virtual environment(仮想環境)の中で作業しているとき、`python`は自動的に正しいバージョンの`Python`を参照しますので、`python3`の代わりに<0>python</0>を使うことができます。.

OK,これでDjangoのインストール前に入れておきたい依存関係の準備がすべて整いました。いよいよDjangoのインストールです！

## Djangoのインストール

今あなたは、あなたの仮想環境(virtualenvironment)をスタートしています。あなたは`pip`を使ってDjangoをインストールする事ができます。コンソールで `pip install django==1.8`(ここではダブルイコールサイン == を使います)と入力し実行してください。 `==`).

    (myvenv) ~$ pip install django==1.8
    Downloading/unpacking django==1.8
    Installing collected packages: django
    Successfully installed django
    Cleaning up...
    

Windowsの場合

> Windowsでpipを呼んだときにエラーが起きた場合は、あなたのプロジェクトのパス名がスペース・アクセント・特殊文字を含んでいないか確認してみて下さい(例：. `C:\Users\User Name\djangogirls`)) もし、含まれている場合は、そのディレクトリをスペース・アクセント・特殊文字を含まない場所（例：`C:\djangogirls`)】に移動する事を検討してください。 移動させた後にもう一度上記のコマンドを実行してみてください。

Linuxの場合

> Ubuntu 12.04でpipを呼んだときにエラーが起きた場合は、仮想環境(virtualenvironment)内でpipインストールをフィックスするために`python -m pip install -U --force-reinstall pip` を実行して下さい。

以上です！あなたは（ついに）Djangoアプリケーションを作成する準備が整いました！