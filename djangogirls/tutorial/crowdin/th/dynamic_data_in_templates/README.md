# ข้อมูลแบบ dynamic ใน template

ตอนนี้ เรามีชิ้นส่วนต่างๆ คือ: โมเดล `Post` ที่กำหนดไว้ในไฟล์ `models.py` มี `post_list` ใน `views.py` และ template แต่เราจะทำยังไงให้โพสต์ของเราปรากฎใน HTML template ของเรา? เพราะนั้นคือสิ่งที่เราต้องการ: ใช้เนื้อหาบางอัน (โมเดลที่อยู่ในฐานข้อมูล) และ แสดงผลสวยๆ ใน template ของเรา ใช่ไหม?

และนี่คือสิ่งที่ *view* จะจัดการ: เชื่อมโมเดลและ template เข้าด้วยกัน *view* ที่อยู่ใน `post_list` เราต้องเอาข้อมูลที่อยู่ในโมเดลที่เราต้องการจะแสดงผลออกมา และส่งไปให้ template โดยปกติ ใน *view* เราเป็นคนเลือกเองว่าอะไร (โมเดล) ที่เราต้องการจะให้ template แสดงผลออกมา

โอเค แล้วเราจะทำอย่างไร?

ตอนนี้เราจะเปิดไฟล์ `blog/views.py` ตอนนี้ *view* `post_list` จะมีหน้าตาแบบนี้:

    python
    from django.shortcuts import render
    
    def post_list(request):
        return render(request, 'blog/post_list.html', {})
    

ยังจำตอนที่เราคุยกันเกี่ยวกับการนำเข้าโค้ดที่เขียนอยู่ในไฟล์อื่นได้ไหม? อารมณ์ก็คล้ายกัน ตอนนี้คือการนำเข้าโมเดลที่เราได้เขียนไว้ในไฟล์ `models.py` เราจะเพิ่มบรรทัดนี้เข้าไป `from .models import Post` ซึ่งผลจะมีหน้าตาคล้ายนี้:

    python
    from django.shortcuts import render
    from .models import Post
    

เครื่องหมายจุด ที่ต่อท้าย `from` หมายถึง *ไดเรกทอรีปัจจุบัน* หรือ *application ปัจจุบัน* เนื่องจากไฟล์ `views.py` และ `models.py` อยู่ในไดเรกทอรีปัจจุบัน เราสามารถใช้ `.` และชื่อไฟล์เหล่านี้ได้เลย (โดยไม่มีนามสกุล `.py`) จากนั้นเราก็นำเข้าชื่อของโมเดล (`Post`).

แล้วอย่างไรต่อ? การเอาข้อมูลบล็อกจากโมเดล `Post` เราต้องใช้สิ่งที่เรียกว่า `QuerySet`.

## QuerySet

คุณอาจจะคุ้นเคยกับการทำงานของ QuerySet มาบ้างแล้ว ซึ่งเราได้รู้จักไปในบท [Django ORM (QuerySets)][1].

 [1]: ../django_orm/README.md

ตอนนี้เรามุ่งความสนใจไปยังรายการของบล็อกโพสต์ที่ได้ถูกเผยแพร่ โดยจัดเรียงตาม `published_date` ถูกไหม? เราได้ทำไปในบทที่แล้วยังไงล่ะ!

    Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    

ตอนนี้เรามีโค้ดอยู่ในไฟล์ `blog/views.py` โดยได้เพิ่มฟังก์ชัน `def post_list(request)` เข้าไป

    python
    from django.shortcuts import render
    from django.utils import timezone
    from .models import Post
    
    def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {})
    

จำไว้ว่าตอนนี้เราได้สร้าง *ตัวแปร* สำหรับ QuerySet ของเรา: นั่นคือ `posts` คิดซะว่าเป็นชื่อ QuerySet ของเรา และเราจะใช้ชื่อนี้ในการอ้างถึงในครั้งหน้า

และโค้ดใช้ฟังก์ชัน `timezone.now()` ดังนั้นเราจึงต้องนำเข้า `timezone` มาด้วย.

ส่วนสุดท้ายที่ขาดไปคือการส่งค่าของ `posts` QuerySet ไปยัง template (เราจะแสดงวิธีการนั้น ในบทถัดไป)

ในฟังก์ชัน `render` เรามีพารามิเตอร์ `request` แล้ว (ทุกสิ่งที่ได้รับมาจากผู้ใช้ทางอินเทอร์เน็ต) และไฟล์ template `'blog/post_list.html'` พารามิเตอร์สุดท้าย ซึ่งมีหน้าตาเหมือนกับ: `{}` คือส่วนที่เราจะเพิ่มบางสิ่งลงไปสำหรับให้ template นำไปใช้ เราต้องตั้งชื่อให้กับค่าเหล่านั้น (เราจะใช้ชื่อ `'posts'` ในตอนนี้ :)) ผลลัพธ์ควรมีหน้าตาแบบนี้: `{'posts': posts}` โปรดสังเกตว่าในส่วนก่อนเครื่องหมาย `:` นั้นเป็น string; คุณควรครอบส่วนนั้นด้วยเครื่องหมายคำพูด `''`.

สุดท้าย ไฟล์ `blog/views.py` ของเราจะมีหน้าตาแบบนี้:

    python
    from django.shortcuts import render
    from django.utils import timezone
    from .models import Post
    
    def post_list(request):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})
    

เรียบร้อย! ถึงเวลาที่จะกลับไปยัง template ของเรา และแสดงผล QuerySet!

ข้อมูลเพิ่มเติมเกี่ยวกับ QuerySet ของ Django สามารถดูได้ที่หน้าเอกสารของโครงการ Django: https://docs.djangoproject.com/en/1.8/ref/models/querysets/