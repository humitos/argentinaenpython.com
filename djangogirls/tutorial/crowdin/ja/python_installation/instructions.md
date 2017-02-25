> このセクションはGeek Girls Carrots(http://django.carrots.pl)をベースで作成しました。

DjangoはPythonで書かれています。 Djangoで何かをするためにはPythonが必要です。 まず、設置しましょう！ 私たちはPython3.4を使う予定です。3.4より低いバージョンを使っていたら、アップデートして下さい。

### Windows

Windows用のPythonは https://www.python.org/downloads/release/python-343/　からダウンロードができます。 サイトから ***.msi** ファイルをダウンロードして、起動(ダブルクリックで)、順番に実行してください。 Pythonを設置したPath(Directory) をちゃんと覚えて下さい。 それは後、必要です。

One thing to watch out for: on the second screen of the installation wizard, marked "Customize", make sure you scroll down and choose the "Add python.exe to the Path" option, as shown here:

![Don't forget to add Python to the Path](../python_installation/images/add_python_to_windows_path.png)

### Linux

It is very likely that you already have Python installed out of the box. To check if you have it installed (and which version it is), open a console and type the following command:

    $ python3 --version
    Python 3.4.3
    

If you don't have Python installed, or if you want a different version, you can install it as follows:

#### Debian 及び Ubuntu

Type this command into your console:

    $ sudo apt-get install python3.4
    

#### フェドーラ (21 まで)

Use this command in your console:

    $ sudo yum install python3.4
    

#### Fedora (22+)

Use this command in your console:

    $ sudo dnf install python3.4
    

### OS X

You need to go to the website https://www.python.org/downloads/release/python-343/ and download the Python installer:

  * *Mac OS X 64-bit/32-bit installer* ファイルをダウンロードしてください。
  * *python-3.4.3-macosx10.6.pkg*をダブルクリックして設置プログラムを起動してください。

Verify the installation was successful by opening the *Terminal* application and running the `python3` command:

    $ python3 --version
    Python 3.4.3
    

* * *

If you have any doubts, or if something went wrong and you have no idea what to do next - please ask your coach! Sometimes things don't go smoothly and it's better to ask for help from someone with more experience.