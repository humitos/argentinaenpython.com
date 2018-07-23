> บางส่วนของบทนี้ อิงมาจากบทเรียนโดย Geek Girls Carrots (http://django.carrots.pl/)
> 
> บางส่วนในบทนี้ อิงมาจาก [django-marcador tutorial](http://django-marcador.keimlink.de/) ภายใต้สัญญาอนุญาต Creative Commons Attributions-ShareAlike 4.0 International License บทเรียน django-marcador เป็นลิขสิทธิ์ของ Markus Zapke-Gründemann

## สภาพแวดล้อมเสมือน

ก่อนที่เราจะติดตั้ง Django เราจะให้คุณติดตั้งเครื่องมีที่มีประโยชน์สุดๆ ตัวนึงก่อน ซึ่งช่วยให้คุณมีสภาพแวดล้อมในการทำงานที่ไม่รบกวนระบบหลักของคุณ คุณจะข้ามขั้นตอนนี้ไปก็ได้นะ แต่เราขอแนะนำอย่างแรง การทำสิ่งนี้จะช่วยให้คุณเจอปัญหาน้อยที่สุดภายในอนาคตอันใกล้นี้!

เอาล่ะ มาสร้าง **สภาพแวดล้อมเสมือน** กัน (เรียกว่า *virtualenv*). Virtualenv จะช่วยแยกสภาพแวดล้อมของ Python/Django ออกจากระบบหลัก ซึ่งหมายความว่า ขณะที่คุณกำลังสร้างเว็บไซต์ จะไม่มีผลกระทบกับระบบอื่นๆ ที่กำลังพัฒนาอยู่ เจ๋งใช่ไหมล่ะ?

ทั้งหมดที่คุณต้องการคือ หาไดเรกทอรีที่คุณต้องการจะสร้าง `virtualenv`; เช่น ไดเรกทอรี home เป็นต้น บน Windows จะมีหน้าตาประมาณ `C:\Users\Name` (ซึ่ง `Name` คือชื่อ login ของคุณ).

สำหรับบทเรียนนี้ เราจะใช้ไดเรกทอรีใหม่ ชื่อ `djangogirls` ภายในไดเรกทอรี home ของคุณ

    mkdir djangogirls
    cd djangogirls
    

เราจะสร้าง virtualenv เรียกว่า `myvenv` คำสั่งทั่วไปจะอยู่ในรูปแบบ:

    python3 -m venv myvenv
    

### วินโดวส์

การสร้าง `virtualenv` ใหม่ คุณต้องเปิดคอนโซล (เราเคยบอกคุณเกี่ยวกับเรื่องนี้แล้วนะ จำได้ไหมเอ่ย?) จากนั้นรันคำสั่ง `C:\Python34\python -m venv myvenv` ผลลัพธ์จะคล้ายนี้:

    C:\Users\Name\djangogirls> C:\Python34\python -m venv myvenv
    

ซึ่ง `C:\Python34\python` คือไดเรกทอรี่ที่คุณได้ติดตั้ง Python และ `myvenv` คือชื่อ `virtualenv` ของคุณ คุณใช้ชื่ออื่นได้นะ แต่ขอแค่ให้ใช้ตัวพิมพ์เล็กไม่มีช่องว่าง, หรืออักขระพิเศษเป็นพอ เป็นไอเดียที่ดีที่จะใช้ชื่อสั้นๆ เพราะคุณต้องอ้างถึงมันบ่อยมาก!

### Linux และ OS X

สร้าง `virtualenv` ทั้งใน Linux และ OS X นั้นง่ายมาก แค่รันคำสั่ง `python3 -m venv myvenv` จะมีหน้าตาประมาณนี้:

    ~/djangogirls$ python3 -m venv myvenv
    

`myvenv` คือชื่อ `virtualenv` ของคุณ คุณใช้ชื่ออื่นได้นะ แต่ขอให้ใช้ตัวพิมพ์เล็กไม่มีช่องว่างหรืออักขระพิเศษเป็นพอ เป็นไอเดียที่ดีที่จะใช้ชื่อสั้นๆ เพราะคุณต้องอ้างถึงมันบ่อยมาก!

> **หมายเหตุ:** การสร้างสภาพแวดล้อมเสมือน บน Ubuntu 14.04 เช่นด้านล่างนี้ จะเกิด error:
> 
>     Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1
>     
> 
> การแก้ปัญหา, ให้ใช้คำสั่ง `virtualenv` แทน
> 
>     ~/djangogirls$ sudo apt-get install python-virtualenv
>     ~/djangogirls$ virtualenv --python=python3.4 myvenv
>     

## การทำงานกับ virtualenv

คำสั่งข้างต้น จะสร้างไดเรกทอรีชื่อ `myvenv` (หรือชื่อที่คุณเลือก) ข้างในจะมีสภาพแวดล้อม (โดยทั่วไป จะมีทั้งไดเรกทอรีและไฟล์จำนวนนึง)

#### วินโดวส์

เริ่มใช้สภาพแวดล้อมเสมือน โดยใช้คำสั่ง:

    C:\Users\Name\djangogirls> myvenv\Scripts\activate
    

#### Linux และ OS X

เริ่มใช้สภาพแวดล้อมเสมือน โดยใช้คำสั่ง:

    ~/djangogirls$ source myvenv/bin/activate
    

อย่าลืมแทนที่ `myvenv` ด้วยชื่อ `virtualenv` ที่คุณได้สร้างไว้!

> **หมายเหตุ:** บางครั้งคำสั่ง `source` จะไม่มีให้ใช้ ในกรณีนี้ให้ทำคำสั่งนี้แทน:
> 
>     ~/djangogirls$ . myvenv/bin/activate
>     

คุณจะรู้ได้ว่า `virtualenv` ถูกเริ่มใช้แล้ว โดยดูที่ prompt บน console จะมีหน้าตาแบบนี้:

    (myvenv) C:\Users\Name\djangogirls>
    

หรือ:

    (myvenv) ~/djangogirls$
    

สังเกตตรงที่จะมี `(myvenv)` นำหน้า!

เมื่อทำงานกับสภาพแวดล้อมเสมือน `python` จะอ้างถึงเวอร์ชันที่ถูกต้องให้ ซึ่งจะทำให้คุณใช้คำสั่ง `python` แทนคำสั่ง `python3` ได้เลย.

โอววเคย์ ในที่สุดตอนนี้เราพร้อมที่ติดตั้ง Django กันแล้ว!

## การติดตั้ง Django

ตอนนี้ `virtualenv` ของคุณได้ทำงานแล้ว คุณสามารถติดตั้ง Django โดยใช้คำสั่ง `pip` โดยใน console ใช้คำสั่ง `pip install django==1.8` (เราใช้เครื่องหมายเท่ากับสองอันนะ: `==`).

    (myvenv) ~$ pip install django==1.8
    Downloading/unpacking django==1.8
    Installing collected packages: django
    Successfully installed django
    Cleaning up...
    

บน Windows

> หากคุณใช้ pip บน Windows แล้วเกิด error ให้ลองเช็ค project pathname ว่ามี ช่องว่าง หรืออักขระพิเศษหรือไม่ (เช่น `C:\Users\User Name\djangogirls`) หากใช่เราแนะนำให้ย้ายไปยังที่อื่น (แนะนำที่: `C:\djangogirls`) หลังจากย้ายแล้ว ลองคำสั่งด้านบนอีกครั้ง

บน Linux

> ถ้าเกิด error ตอนรันคำสั่ง pip บน Ubuntu 12.04 ให้ลองใช้คำสั่ง `python -m pip install -U --force-reinstall pip` เพื่อแก้ไข

นั่นล่ะ! ตอนนี้คุณก็พร้อม(สักที)ที่จะสร้าง Django application แล้ว!