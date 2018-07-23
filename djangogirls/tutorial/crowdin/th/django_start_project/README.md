# Django project แรก ของคุณ!

> บางส่วนของบทนี้ อิงมาจากบทเรียนโดย Geek Girls Carrots (http://django.carrots.pl/)
> 
> บางส่วนในบทนี้ อิงมาจาก [django-marcador tutorial][1] ภายใต้สัญญาอนุญาต Creative Commons Attributions-ShareAlike 4.0 International License บทเรียน django-marcador เป็นลิขสิทธิ์ของ Markus Zapke-Gründemann

 [1]: http://django-marcador.keimlink.de/

เราจะมาสร้างบล็อกแบบง่ายๆ กัน!

ขั้นตอนแรกคือการสร้าง Django project ใหม่ โดยทั่วไปแล้ว เราจะทำการเรียกใช้สคริปต์บางอย่างที่มาพร้อมกับ Django ซึ่งจะทำการสร้างโครงของ project Django ให้กับเรา ซึ่งประกอบไปด้วย ไฟล์และไดเรกทอรีจำนวนหนึ่งที่เราจะใช้ต่อไป

บางชื่อในบางไฟล์และไดเรกทอรีนั้นสำคัญมากๆ สำหรับ Django และคุณไม่ควรเปลี่ยนชื่อไฟล์เหล่านั้น และการย้ายไฟล์เหล่านั้นไปยังที่อื่น ก็ไม่ใช่ความคิดที่ดีแน่ๆ Django นั้นต้องการโครงสร้างที่แน่นอน เพื่อที่จะสามารถหาสิ่งที่จำเป็นที่จะต้องใช้ได้

> อย่าลืมที่จะรันทุกสิ่งอย่างภายใต้ virtualenv ถ้าคุณไม่เห็น `(myvenv)` นำหน้าในคอนโซลของคุณ คุณต้องเปิดใช้ virtualenv เสียก่อน เราอธิบายวิธีทำไว้แล้วในบท **การติดตั้ง Django** อยู่ในส่วนของ **การทำงานกับ virtualenv** โดยพิมพ์ `myvenv\Scripts\activate` บนวินโดวส์ หรือ `source myvenv/bin/activate` บน Mac OS / ลินุกซ์

ในคอนโซลบน MacOS หรือ ลินุกซ์ของคุณ ใช้คำสั่งต่อไปนี้ **และอย่าลืมใส่เครื่องหมายมหัพภาพ (หรือ จุด) `.` ด้านท้าย**:

    (myvenv) ~/djangogirls$ django-admin startproject mysite .
    

บน Windows; **อย่าลืมเครื่องหมายมหัพภาค (หรือ จุด) `.` ต่อท้าย**:

    (myvenv) C:\Users\Name\djangogirls> django-admin startproject mysite .
    

> เครื่องหมายจุด `.` นี้ สำคัญ เพราะเป็นตัวบอกว่าให้ติดตั้ง Django ลงในไดเรกทอรีปัจจุบัน (ใช้เครื่องหมาย `.` เป็นการอ้างอิงถึงไดเรกทอรีปัจจุบันแบบลัด)
> 
> **หมายเหตุ** เมื่อเราพิมพ์คำสั่งข้างต้น เราใช้เพียงแค่คำสั่ง `django-admin` หรือ `django-admin.py` ได้เลย `(myvenv) ~/djangogirls$` และ `(myvenv) C:\Users\Name\djangogirls>` แสดงถึงตัวอย่างว่า พร้อมรับคำสั่งจากเราผ่านบรรทัดคำสั่ง

`django-admin.py` เป็นสคริปต์สำหรับสร้างไฟล์และไดเรกทอรีให้กับคุณ และตอนนี้คุณควรจะมีโครงสร้างไฟล์และไดเรกทอรีตามนี้:

    djangogirls
    ├───manage.py
    └───mysite
            settings.py
            urls.py
            wsgi.py
            __init__.py
    

`manage.py` เป็นสคริปต์ที่ช่วยจัดการของไซต์ของคุณ ด้วยสคริปต์นี้เราจะสามารถเริ่มต้นเว็บเซิร์ฟเวอร์บนคอมพิวเตอร์ของเราโดยไม่ต้องติดตั้งอะไรเพิ่มเติมอีก

ไฟล์ `settings.py` ประกอบไปด้วยไฟล์ที่กำหนดค่าต่างๆ ในเว็บไซต์ของคุณ

จำเกี่ยวกับคนส่งจดหมายได้ไหม? `urls.py` คือไฟล์ที่มีรายการรูปแบบที่ถูกนำไปใช้ใน `urlresolver`.

ไฟล์อื่นๆ เราไว้ว่ากันทีหลัง สิ่งสำคัญตอนนี้คือ อย่าเผลอไปลบไฟล์พวกนี้เล่นล่ะ!

## เปลี่ยนการตั้งค่า

เรามาแก้ไขไฟล์ `mysite/settings.py` กัน เปิดไฟล์นี้ด้วยโปรแกรมแก้ไขโค้ดที่คุณติดตั้งไว้แล้ว

คงจะดีไม่น้อยถ้าเว็บของเรามีการตั้งค่าเวลาที่ถูกต้อง เปิดหน้า [รายการเขตเวลา ในวิกิพีเดีย][2] และคัดลอกเขตเวลา (TZ) ที่ตรงกับของคุณ (เช่น `Europe/Berlin` )

 [2]: http://en.wikipedia.org/wiki/List_of_tz_database_time_zones

ในไฟล์ settings.py มองหาบรรทัด `TIME_ZONE` และเปลี่ยนให้ตรงกับเขตเวลาที่คุณเลือก:

    python
    TIME_ZONE = 'Europe/Berlin'
    

เปลี่ยน "Europe/Berlin" ให้ตรงตามเหมาะสม

เราต้องการเพิ่มพาธสำหรับไฟล์ static เช่นกัน (เราจะอธิบายเกี่ยวกับไฟล์ static และ CSS ในภายหลัง) เลื่อนลงไปยัง *บรรทัดสุดท้าย* ของไฟล์ ใต้บรรทัด `STATIC_URL` และเพิ่มบรรทัด `STATIC_ROOT`:

    python
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    

## ตั้งค่าฐานข้อมูล

มีซอฟต์แวร์ฐานข้อมูลจำนวนมากที่สามารถเก็บข้อมูลของเว็บคุณได้ เราจะใช้ฐานข้อมูลเริ่มต้น คือ `sqlite3`.

ซึ่งได้ถูกตั้งค่าไว้เรียบร้อยแล้วในไฟล์ `mysite/settings.py` ของคุณ:

    python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    

การสร้งฐานข้อมูลสำหรับบล็อกของเรา เริ่มต้นด้วยการใช้คำสั่งต่อไปนี้ในคอนโซล: `python manage.py migrate` (เราจำเป็นต้องอยู่ไดเรกทอรี `djangogirls` ซึ่งมีไฟล์ `manage.py` อยู่ด้านใน) ถ้าทุกอย่างเป็นไปด้วยดี คุณจะเห็นผลคล้ายๆ แบบนี้:

    (myvenv) ~/djangogirls$ python manage.py migrate
    Operations to perform:
      Synchronize unmigrated apps: messages, staticfiles
      Apply all migrations: contenttypes, sessions, admin, auth
    Synchronizing apps without migrations:
       Creating tables...
          Running deferred SQL...
       Installing custom SQL...
    Running migrations:
      Rendering model states... DONE
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying sessions.0001_initial... OK
    

เป็นอันเสร็จสิ้น! ได้เวลาเปิดเว็บเซิร์ฟเวอร์และดูว่าเว็บเราทำงานไหม!

คุณต้องอยู่ในไดเรกทอรีที่มีไฟล์ `manage.py` (ไดเรกทอรี `djangogirls` นั่นเอง) ในคอนโซล เราสามารถเริ่มต้นเว็บเซิร์ฟเวอร์โดยรันคำสั่ง `python manage.py runserver`:

    (myvenv) ~/djangogirls$ python manage.py runserver
    

ถ้าคุณอยู่บนวินโดวส์ และเกิดข้อผิดพลาด `UnicodeDecodeError` ให้ใช้คำสั่งนี้แทน:

    (myvenv) ~/djangogirls$ python manage.py runserver 0:8000
    

ตอนนี้ คุณสามารถเช็คได้ว่าเว็บเรารันแล้วหรือยัง โดย เปิดเว็บเบราว์เซอร์ของคุณ (Firefox, Chrome, Safari, Internet Explorer หรือ อะไรก็ตามที่คุณใช้) และป้อนที่อยู่:

    http://127.0.0.1:8000/
    

เว็บเซิร์ฟเวอร์รันบน prompt คำสั่งของคุณจนกว่าคุณหยุดการทำงานของมัน การใช้คำสั่งอื่นๆ ในขณะที่รันอยู่ ให้เปิดหน้าต่างเทอร์มินัลใหม่และเปิดใช้งาน virtualenv การหยุดเว็บเซิร์ฟเวอร์ สลับกลับไปที่หน้าต่างที่รันอยู่ แล้วกดปุ่ม CTRL+C - ปุ่ม Control และปุ่ม C พร้อมกัน (บนวินโดวส์ คุณอาจต้องใช้ Ctrl+Break)

ขอแสดงความยินดี! คุณเพิ่งสร้างเว็บแรกของคุณและรันมันบนเว็บเซิร์ฟเวอร์! เจ๋งไปเลยว่าไหม?

![It worked!][3]

 [3]: images/it_worked2.png

พร้อมสำหรับขั้นถัดไปแล้ว? ถึงเวลาสร้างเนื้อในเว็บกันแล้ว!