# Django view - ได้เวลาสร้างแล้ว!

ได้เวลาแก้บั๊กในบทก่อนหน้านี้แล้ว :)

*view* คือส่วนที่เราใส่ "logic" ของโปรแกรมของเรา โดยจะขอข้อมูลจาก `model` ที่คุณสร้างก่อนหน้านี้และส่งไปยัง `template` เราจะสร้าง template ในบทถัดไป view นั้นเป็นเพียง Python method ซึ่งมีความซับซ้อนกว่าที่เราเคยสร้างในบท **Introduction to Python** นิดหน่อย

view จะอยู่ในไฟล์ `views.py` เราจะเพิ่ม *view* ของเราลงในไฟล์ `blog/views.py`

## blog/views.py

โอเค เปิดไฟล์นี้ขึ้นมาดูว่ามีอะไรข้างใน:

    python
    from django.shortcuts import render
    
    # Create your views here.
    

ยังไม่มีอะไรมากข้างใน *view* ที่พื้นฐานที่สุด จะมีลักษณะแบบนี้

    python
    def post_list(request):
        return render(request, 'blog/post_list.html', {})
    

อย่างที่คุณเห็น เราได้สร้าง method (`def`) ชื่อว่า `post_list` โดยรับ `request` และ `return` method `render` ซึ่งจะแสดงผล (ซึ่งรวมเข้ากับ) template ของเราคือไฟล์ `blog/post_list.html`.

บักทึกไฟล์ และเปิดไปที่ http://127.0.0.1:8000/ และดูว่าเกิดไรขึ้น

เกิดข้อผิดพลาดอีกแล้ว! ลองอ่านดูว่าเกิดไรขึ้นตอนนี้:

![ข้อผิดพลาด][1]

 [1]: images/error.png

อันนี้ไม่ยาก: *TemplateDoesNotExist* มาแก้บั๊กนี้กันโดยการสร้าง template ในบทถัดไป!

> ข้อมูลเพิ่มเติมเกี่ยวกับ Django view สามารถดูได้ที่หน้าเอกสารของโครงการ Django: https://docs.djangoproject.com/en/1.8/topics/http/views/