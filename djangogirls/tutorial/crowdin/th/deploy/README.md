# Deploy!

> **หมายเหตุ** บทนี้อาจจะไม่ง่ายนักที่จะผ่านไปได้ ขอให้อดทนและทำให้เสร็จ; deployment เป็นส่วนสำคัญในกระบวนการพัฒนาเว็บไซต์ บทนี้อยู่ในครึ่งทางของบทเรียนทั้งหมด ดังนั้นผู้ช่วยของคุณจะพาคุณนำเว็บไซต์ออนไลน์โดยจะมีขั้นตอนยุ่งยากเล็กน้อย ซึ่งหมายความว่า ถึงคุณมีเวลาไม่พอ ก็จะยังสามารถจบบทนี้ได้แน่นอน

จนถึงตอนนี้ เว็บไซต์ของคุณสามารถใช้ได้เฉพาะบนเครื่องของคุณเท่านั้น ตอนนี้เราจะเรียนรู้ที่จะนำมันขึ้นออนไลน์! Deploying คือกระบวนการเผยแพร่โปรแกรมของคุณขึ้นสู่อินเทอร์เน็ต สุดท้ายแล้ว ทุกคนก็จะสามารถเห็นเว็บของคุณได้ :)

อย่างที่คุณได้ทราบ เว็บไซต์นั้นอาศัยอยู่ในเครื่องเซิร์ฟเวอร์ มีผู้ให้บริการด้านเซิร์ฟเวอร์จำนวนมากบนอินเทอร์เน็ต เราจะใช้หนึ่งในผู้ให้บริการด้านนี้ ที่กระบวนการใช้งานนั้นง่าย: [PythonAnywhere][1] PythonAnywhere เป็นบริการฟรีสำหรับโปรแกรมขนาดเล็ก ที่มีผู้เข้าชมมีจำนวนไม่มาก ดังนั้นมันจึงพอดีสำหรับคุณในตอนนี้

 [1]: http://pythonanywhere.com/

มีบริการภายอื่นที่เราจะใช้เช่นกัน คือ [GitHub][2] ซึ่งเป็นบริการที่เก็บโค้ดของเรา จริงๆ ก็มีบริการจากที่อื่นเช่นกัน แต่โปรแกรมเมอร์เกือบทุกคนในตอนนี้มีบัญชี GitHub และคุณก็กำลังจะมีด้วยเช่นกัน!

 [2]: http://www.github.com

เราจะใช้ GitHub เป็นสะพานในการส่งโค้ดของทั้งจากของเรา และจาก PythonAnywhere

# Git

Git คือ "version control system" ถูกใช้โดยโปรแกรมเมอร์จำนวนมาก ซอฟต์แวร์นี้สามารถติดตามการเปลี่ยนแปลงของไฟล์ในทุกช่วงเวลาเพื่อให้คุณสามารถย้อนกลับไปยังเวอร์ชันเก่าๆ ได้ในภายหลัง คล้ายกับฟีเจอร์ "track changes" ใน Microsoft Word แต่มีประสิทธิภาพมากกว่า

## ติดตั้ง Git

> **หมายเหตุ** ถ้าคุณผ่านขั้นตอนในหัวข้อติดตั้งมาแล้ว คุณไม่จำเป็นต้องทำอีกครั้ง - คุณสามารถข้ามไปยังส่วนถัดไป และเริ่มสร้าง Git repository ได้เลย

{% include "deploy/install_git.md" %}

## เริ่มต้นจาก Git repository

Git ติดตามการเปลี่ยนแปลงของไฟล์เป็นชุด โดยเรียกชุดไฟล์เหล่านี้ว่า โค้ด repository (หรือสั้นๆ ว่า "repo") เริ่มจากโครงการของเรา เปิดคอนโซลของคุณ และรันคำสั่งต่อไปนี้ในไดเรกทอรี `djangogirls`:

> **หมายเหตุ** ตรวจสอบไดเรกทอรีปัจจุบันโดยใช้คำสั่ง `pwd` (OSX/Linux) หรือ `cd` (วินโดวส์) ก่อนจะเริ่มสร้าง repository คุณควรอยู่ในโฟลเดอร์ `djangogirls`

    $ git init
    Initialized empty Git repository in ~/djangogirls/.git/
    $ git config --global user.name "Your Name"
    $ git config --global user.email you@example.com
    

การเริ่มต้น git repository เป็นสิ่งที่เราทำเพียงครั้งเดียวในแต่ละโครงการ (และคุณไม่จำเป็นต้องป้อน username และ email อีกเลยหลังจากนี้)

Git จะติดตามการเปลี่ยนแปลงในทุกไฟล์และโฟลเดอร์ที่อยู่ภายในไดเรกทอรีนี้ แต่ก็จะมีบางไฟล์ที่เราไม่ต้องการให้ติดตาม สามารถทำได้โดยสร้างไฟล์ชื่อ `.gitignore` ในไดเรกทอรีบนสุด เปิดตัวแก้ไขไฟล์ และสร้างไฟล์ที่มีเนื้อหาดังนี้:

    *.pyc
    __pycache__
    myvenv
    db.sqlite3
    .DS_Store
    

จากนั้นบันทึกเป็นไฟล์ชื่อ `.gitignore` อยู่ภายในโฟลเดอร์ "djangogirls"

> **หมายเหตุ** เครื่องหมายจุดนำหน้าชื่อไฟล์นั้นสำคัญมาก! ถ้าคุณมีปัญหาในการสร้างไฟล์นี้ (เช่น Mac ไม่ชอบให้คุณสร้างไฟล์ที่เริ่มต้นด้วยเครื่องหมายจุดใน Finder) ดังนั้น คุณควรใช้ "Save As" จากตัวแก้ไขไฟล์แทน

ควรใช้คำสั่ง `git status` ก่อนที่จะใช้คำสั่ง `git add` หรือเมื่อใดก็ตามที่คุณไม่แน่ใจว่า มีการเปลี่ยนแปลงอะไรไปบ้าง วิธีนี้จะช่วยให้คุณไม่เจอเหตุการณ์แปลกๆ ขึ้น เช่น คุณเพิ่มไฟล์เข้าไปและยืนยันการบันทึกไปผิดไฟล์ คำสั่ง `git status` จะบอกข้อมูลเกี่ยวกับสถานะของไฟล์ที่ ไม่ได้ติดตาม/มีการแก้ไข/พร้อมบันทึกการแก้ไข และสถานะอื่นๆ ผลลัพธ์ที่ได้จะมีลักษณะดังนี้:

    $ git status
    On branch master
    
    Initial commit
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
    
            .gitignore
            blog/
            manage.py
            mysite/
    
    nothing added to commit but untracked files present (use "git add" to track)
    

และสุดท้าย เราบันทึกการเปลี่ยนแปลง เปิดคอนโซลของคุณและใช้คำสั่ง:

    $ git add -A .
    $ git commit -m "My Django Girls app, first commit"
     [...]
     13 files changed, 200 insertions(+)
     create mode 100644 .gitignore
     [...]
     create mode 100644 mysite/wsgi.py
    

## ส่งโค้ดของเราไปยัง GitHub

ไปที่ [GitHub.com][2] และลงทะเบียนบัญชีผู้ใช้ใหม่ (ถ้าคุณทำแล้วเรียบร้อย ก็แจ๋วไปเลย!)

จากนั้น สร้าง repository ใหม่ ตั้งชื่อว่า "my-first-blog" ยังไม่ต้องติ๊กที่ "initialise with a README" และไม่ต้องทำอะไรกับตัวเลือก .gitignore (เราทำไปแล้ว) และไม่ต้องแก้ไข License

![][3]

 [3]: images/new_github_repo.png

> **หมายเหตุ** ชื่อ `my-first-blog` นั้นสำคัญ -- คุณสามารถใช้ชื่ออื่นได้ แต่ชื่อนี้จะปรากฎตลอดทั้งหน้านี้ และคุณจำเป็นต้องเปลี่ยนชื่อตามในทุกครั้ง จะเป็นการง่ายกว่าถ้าเราใช้ชื่อ `my-first-blog`.

หน้าจอถัดไป คุณจะเห็น URL สำหรับโคลน repo ของคุณ ให้เลือก "HTTPS" คัดลอกลิงค์และวางไปยังเทอร์มินัล:

![][4]

 [4]: images/github_get_repo_url_screenshot.png

ตอนนี้เราจะทำการชี้ Git repository บนเครื่องของเราไปยังบน GitHub

ใช้คำสั่งต่อไปบนคอนโซลของคุณ (แทนที่ `<your-github-username>` ด้วยชื่อ username ที่คุณสมัคร Github ไว้ แต่ไม่ต้องมีเครื่องหมายวงเล็บมุม):

    $ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
    $ git push -u origin master
    

ป้อนชื่อ username และ password ที่คุณใช้สมัคร GitHub และคุณควรจะเห็นผลลัพธ์คล้ายๆ แบบนี้:

    Username for 'https://github.com': hjwp
    Password for 'https://hjwp@github.com':
    Counting objects: 6, done.
    Writing objects: 100% (6/6), 200 bytes | 0 bytes/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/hjwp/my-first-blog.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.
    

<!--TODO: maybe do ssh keys installs in install party, and point ppl who dont have it to an extention -->

ตอนนี้โค้ดของคุณได้อยู่บน GitHub แล้ว ลองไปดูกันว่าจริงไหม! คุณจะเห็นว่า บริษัทเจ๋งๆ อย่าง - [Django][5], [Django Girls Tutorial][6] และโครงการซอฟต์แวร์เสรีมากมาย ก็เก็บโค้ดไว้ที่ GitHub :)

 [5]: https://github.com/django/django
 [6]: https://github.com/DjangoGirls/tutorial

# ติดตั้งบล็อกของเราที่ PythonAnywhere

> **หมายเหตุ** คุณอาจจะสร้างบัญชีของ PythonAnywhere มาแล้ว - คุณก็ไม่จำเป็นต้องสร้างอีก

{% include "deploy/signup_pythonanywhere.md" %}

## ดึงโค้ดของเราลงมาที่ PythonAnywhere

เมื่อคุณลงทะเบียนเข้า PythonAnywhere คุณจะถูกพาไปยังหน้า "Consoles" หลัก เลือกไปยังตัวเลือกเพื่อเริ่ม "Bash" คอนโซล -- ซึ่งเป็นเวอร์ชันหนึ่งที่ PythonAnywhere ใช้ เช่นเดียวกับที่คุณใช้บนเครื่องของคุณ

> **หมายเหตุ** PythonAnywhere นั้นใช้ลินุกซ์เป็นฐาน หากคุณใช้วินโดวส์ คอนโซลที่คุณเห็นจะหน้าตาต่างไปจากเดิมที่เคยใช้

เรามาเริ่มดึงโค้ดของเราจาก GitHub มายัง PythonAnywhere โดยการสร้าง "clone" ของ repo ของเรา พิมพ์คำสั่งต่อไปลงในคอนโซลบน PythonAnywhere (อย่าลืมใช้บัญชี GitHub ของคุณ แทนที่ `<your-github-username>`):

    $ git clone https://github.com/<your-github-username>/my-first-blog.git
    

คำสั่งนี้จะทำการสำเนาข้อมูลโค้ดของคุณลงบน PythonAnywhere ตรวจสอบโดยการใช้คำสั่ง `tree my-first-blog`:

    $ tree my-first-blog
    my-first-blog/
    ├── blog
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
    

### สร้าง virtualenv บน PythonAnywhere

เช่นเดียวกับที่คุณสร้างในเครื่องของคุณ คุณสามารถสร้างบน PythonAnywhere ได้เช่นกัน ใน Bash คอนโซล พิมพ์คำสั่ง:

    $ cd my-first-blog
    
    $ virtualenv --python=python3.4 myvenv
    Running virtualenv with interpreter /usr/bin/python3.4
    [...]
    Installing setuptools, pip...done.
    
    $ source myvenv/bin/activate
    
    (mvenv) $  pip install django whitenoise
    Collecting django
    [...]
    Successfully installed django-1.8.2 whitenoise-2.0
    

> **หมายเหตุ** ขั้นตอน `pip install` อาจใช้เวลาสองสามนาที รอหน่อยนะ! แต่ถ้าเกิดใช้เวลาเกิน 5 นาที บางอย่างอาจจะผิดพลาด โปรดถามโค้ดของคุณเพื่อแก้ปัญหา

<!--TODO: think about using requirements.txt instead of pip install.-->

### รวบรวมไฟล์ static

คุณคงสัยสัย "whitenoise" นี่คืออะไร? มันคือเครื่องมือสำหรับให้บริการ และจัดการสิ่งที่เรียกว่า "static files" ไฟล์ static คือ ไฟล์ที่ไม่ค่อยมีการเปลี่ยนแปลงหรือเรียกใช้โค้ดใดๆ ตัวอย่างเช่นไฟล์ HTML หรือ CSS ไฟล์เหล่านี้ เมื่ออยู่บนเครื่องเซิร์ฟเวอร์ จะทำงานแตกต่างกันกับไฟล์ที่อยู่บนเครื่องของเรา จึงต้องมีเครื่องมือเช่น "whitenoise" สำหรับให้บริการ

เราจะมาคุยกันต่อเกี่ยวกับไฟล์ static เร็วๆ นี้ เมื่อเราจะแก้ไข CSS สำหรับเว็บไซต์ของเรา

สำหรับตอนนี้ เราต้องเรียกคำสั่งพิเศษคือ `collectstatic` บนเซิร์ฟเวอร์ เป็นการบอกให้ Django รวบรวมไฟล์ static ทั้งหมดที่จำเป็นต้องใช้บนเครื่องเซิร์ฟเวอร์ ในตอนนี้ ไฟล์เหล่านี้ทำให้หน้า admin นั้นดูสวยงาม

    (mvenv) $ python manage.py collectstatic
    
    You have requested to collect static files at the destination
    location as specified in your settings:
    
        /home/edith/my-first-blog/static
    
    This will overwrite existing files!
    Are you sure you want to do this?
    
    Type 'yes' to continue, or 'no' to cancel: yes
    

พิมพ์ "yes" และมันจะเริ่มทำงาน! คุณชอบไหมเวลาที่คอมพิวเตอร์พิมพ์ข้อความออกมาเหมือนกำลังยุ่งๆ อยุ่? ฉันจะทำเสียงแบบนี้ตามมันไปด้วย Brp brp brp...

    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/actions.min.js'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/inlines.min.js'
    [...]
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/changelists.css'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/base.css'
    62 static files copied to '/home/edith/my-first-blog/static'.
    

### สร้างฐานข้อมูลบน PythonAnywhere

นี่เป็นอีกสิ่งที่แตกต่างระหว่างเครื่องของคุณเองและเซิร์ฟเวอร์: คือใช้ฐานข้อมูลคนละอันกัน ดังนั้ง ข้อมูลต่างๆ จึงแตกต่างกันระหว่างสองเครื่องนี้

เราสามารถสร้างฐานข้อมูลบนเซิร์ฟเวอร์เหมือนกันที่เราเคยทำบนเครื่องของเรา โดยใช้ `migrate` และ `createsuperuser`:

    (mvenv) $ python manage.py migrate
    Operations to perform:
    [...]
      Applying sessions.0001_initial... OK
    
    
    (mvenv) $ python manage.py createsuperuser
    

## เผยแพร่บล็อกของเราให้เป็นหน้าเว็บ

ตอนนี้โค้ดของเราอยู่ที่ PythonAnywhere แล้ว virtualenv ก็พร้อมแล้ว ไฟล์ static ก็ถูกรวบรวมแล้ว ฐานข้อมูลก็สร้างแล้ว เราพร้อมที่จะเปิดเว็บของเราแล้ว!

กลับไปยังหน้าหลักของ PythonAnywhere โดยคลิกที่โลโก้ จากนั้นคลิกที่แท็บ **Web** สุดท้ายคลิกที่ **Add a new web app**.

หลังจากยืนยันชื่อโดเมนแล้ว เลือกที่ **manual configuration** (หมายเหตุ *ไม่ใช่* ตัวเลือก "Django") ในกล่องโต้ตอบ ถัดมา เลือก **Python 3.4** และคลิกที่ Next เพื่อเสร็จสิ้น

> **หมายเหตุ** ตรวจสอบให้แน่ใจว่าคุณได้เลือก "Manual configuration" และไม่ใช่ "Django" พวกเราเจ๋งพอที่จะไม่ใช่ตัวเลือก Django ของ PythonAnywhere ;-)

### ตั้งค่า virtualenv

คุณจะถูกพามายังหน้าตั้งค่า PythonAnywhere ซึ่งหน้านี้เป็นหน้าที่คุณต้องเข้ามา หากต้องการแก้ไขค่าต่างๆ ของเว็บเรา

![][7]

 [7]: images/pythonanywhere_web_tab_virtualenv.png

ในส่วนของ "Virtualenv" คลิกที่ข้อความสีแดง "Enter the path to a virtualenv" และป้อน: `/home/<your-username>/my-first-blog/myvenv/` คลิกที่กล่องสีน้ำเงินเพื่อเลือกที่จะบันทึก ก่อนที่จะไปยังขั้นถัดไป

> **หมายเหตุ** เปลี่ยน username ให้สอดคล้องกันของคุณ ถ้ามีอะไรผิดพลาด PythonAnywhere จะแสดงคำเตือนบอกคุณ

### ตั้งค่าไฟล์ WSGI

Django ทำงานโดยใช้ "WSGI protocol" เป็นมาตรฐานการให้บริการเว็บไซต์ที่ใช้ Python ซึ่ง PythonAnywhere รองรับการทำงานเช่นกัน วิธีที่เรากำหนดค่าให้ PythonAnywhere ทำงานกับบล็อก Django ของเราคือตั้งค่าไฟล์ WSGI

คลิกที่ลิงค์ "WSGI configuration file" (ภายในส่วน "Code" ใกล้กับส่วนบนสุดของหน้า -- มันจะมีชื่อคล้ายกับ `/var/www/<your-username>_pythonanywhere_com_wsgi.py`) และคุณจะถูกพาไปยังหน้าแก้ไข

ลบเนื้อหาทั้งหมดออก และแทนที่ด้วยค่าเหล่านี้:

    python
    import os
    import sys
    
    path = '/home/<your-username>/my-first-blog'  # use your own username here
    if path not in sys.path:
        sys.path.append(path)
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    
    from django.core.wsgi import get_wsgi_application
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(get_wsgi_application())
    

> **หมายเหตุ** อย่าลืมแทนที่ username ของคุณใน `<your-username>`

หน้าที่ของไฟล์นี้คือ บอก PythonAnywhere ว่าเว็บของเราอยู่ตรงไหนและไฟล์ตั้งค่า Django ชื่ออะไร และจะตั้งค่า "whitenoise" ด้วยเช่นกัน

กดปุ่ม **Save** และกลับไปยังแท็บ **Web**

เรียบร้อยแล้ว! คลิกที่ปุ่มเขียวๆ ใหญ่ๆ **Reload** และคุณจะสามารถดูเว็บของคุณได้ คุณจะเห็นลิงค์ปรากฎอยู่บนสุดของหน้า

## เคล็ดลับการ Debugging

ถ้าคุณเห็นข้อผิดพลาดเกิดขึ้นเมื่อคุณเข้าดูหน้าเว็บ ที่แรกที่คุณควรตรวจสอบคือใน **error log** คุณจะเห็นลิงค์นี้บน แท็บ [Web tab][8] ใน PythonAnywhere หากมีข้อผิดพลาด ก็จะปรากฎที่นี่ โดยข้อผิดพลาดล่าสุดจะปรากฎอยู่ด้านล่าง ปัญหาที่พบบ่อยได้แก่:

 [8]: https://www.pythonanywhere.com/web_app_setup/

*   ลืมทำบางขั้นตอนในคอนโซล: สร้าง virtualenv, เรียกใช้มัน, ติดตั้ง Django ข้างใน, เรียกใช้ collectstatic, migrate ฐานข้อมูล

*   ป้อนที่อยู่ของ virtualenv ในแท็บ Web ไม่ถูกต้อง -- ถ้ามีข้อผิดพลา จะปรากฎข้อความสีแดงบอก

*   แก้ไขไฟล์ตั้งค่า WSGI ผิด -- คุณตั้งค่าตำแหน่งโฟลเดอร์ my-first-blog ถูกต้องหรือไม่?

*   คุณใช้ Python เวอร์ชันเดียวกันกับทั้ง virtualenv และเว็บของคุณหรือไม่? ทั้งคู่ควรจะใช้ 3.4 เหมือนกัน

*   และมี [การแกไขปัญหาเบื้องต้นใน PythonAnywhere wiki][9].

 [9]: https://www.pythonanywhere.com/wiki/DebuggingImportError

และอย่าลืม โค้ชของคุณช่วยคุณได้!

# คุณกำลังออนไลน์!

หน้าเริ่มต้นสำหรับเว็บไซต์ของคุณควรจะเป็น "Welcome to Django" เช่นเดียวกับที่อยู่บนเครื่องของคุณ ลองเพิ่ม `/admin/` ต่อท้าย URL และคุณจะได้หน้า admin เข้าระบบด้วย username และ password และคุณจะสามารถเพิ่มโพสต์ใหม่ได้ บนเซิร์ฟเวอร์

ให้รางวัล *ใหญ่* กับตัวคุณเองหน่อย! การนำเว็บขึ้นบนเซิร์ฟเวอร์เป็นขั้นตอนที่ยุ่งยากในการพัฒนาเว็บไซต์ และ บางคนมักใช้เวลาสองสามวันกว่าจะเอาขึ้นได้ แต่คุณมีเว็บไซต์ที่พร้อมใช้ บนอินเตอร์เน็ตจริงๆ แล้วตอนนี้!