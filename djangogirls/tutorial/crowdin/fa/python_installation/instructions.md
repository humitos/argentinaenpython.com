> این قسمت بر اساس خودآموز Geek Girls Carrots نوشته شده است.(http://django.carrots.pl/)

جنگو با پایتون نوشته شده است. برای نجام هر کاری در جنگو، به زبان پایتون احتیاج داریم. پس بهتره اول پایتونو نصب کنیم! ما ازتون می خوایم پایتون 3.4 رو نصب کنید، پس اگه یک نسخه قدیمی تر رو دارید لازمه ارتقاء ش بدید.

### Windows

میشه پایتون رو برای ویندوز از آدرس https://www.python.org/downloads/release/python-343/ دانلود کرد. بعد از دانلود فایل با پسوند ***.msi**، اجراش کنید و مراحل نصب رو انجام بدید. It is important to remember the path (the directory) where you installed Python. It will be needed later!

One thing to watch out for: on the second screen of the installation wizard, marked "Customize", make sure you scroll down and choose the "Add python.exe to the Path" option, as shown here:

![Don't forget to add Python to the Path](../python_installation/images/add_python_to_windows_path.png)

### Linux

It is very likely that you already have Python installed out of the box. To check if you have it installed (and which version it is), open a console and type the following command:

    $ python3 --version
    Python 3.4.3
    

If you don't have Python installed, or if you want a different version, you can install it as follows:

#### Debian or Ubuntu

Type this command into your console:

    $ sudo apt-get install python3.4
    

#### Fedora (up to 21)

Use this command in your console:

    $ sudo yum install python3.4
    

#### Fedora (22+)

Use this command in your console:

    $ sudo dnf install python3.4
    

### OS X

You need to go to the website https://www.python.org/downloads/release/python-343/ and download the Python installer:

  * Download the *Mac OS X 64-bit/32-bit installer* file,
  * Double click *python-3.4.3-macosx10.6.pkg* to run the installer.

Verify the installation was successful by opening the *Terminal* application and running the `python3` command:

    $ python3 --version
    Python 3.4.3
    

* * *

If you have any doubts, or if something went wrong and you have no idea what to do next - please ask your coach! Sometimes things don't go smoothly and it's better to ask for help from someone with more experience.