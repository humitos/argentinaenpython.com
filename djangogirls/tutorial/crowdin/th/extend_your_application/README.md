# เพิ่มความสามารถให้เว็บคุณ

เราได้เรียนรู้ขั้นตอนทั้งหมดในการสร้างเว็บไซต์แล้ว: เรารู้วิธีสร้าง โมเดล, url, view และ template รวมถึงการทำให้เว็บเราสวยงามขึ้น

ได้เวลาฝึกแล้ว!

สิ่งแรกที่เราต้องการสำหรับบล็อกของเราคือ หน้าเว็บที่จะแสดงโพสต์หนึ่งโพสต์ของเรา ถูกไหม?

ซึ่งเรามีโมเดล `Post` แล้ว ดังนั้น เราไม่จำเป็นต้องเพิ่มอะไรลงไปใน `models.py`.

## สร้าง template ที่แสดงหน้ารายละเอียดของโพสต์

เราเริ่มด้วยการเพิ่มลิงค์ข้างในไฟล์ `blog/templates/blog/post_list.html` ดังนั้น ควรมีหน้าตาแบบนี้:

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        {% for post in posts %}
            <div class="post">
                <div class="date">
                    {{ post.published_date }}
                </div>
                <h1><a href="">{{ post.title }}</a></h1>
                <p>{{ post.text|linebreaks }}</p>
            </div>
        {% endfor %}
    {% endblock content %}
    
    

{% raw %}เราต้องการที่จะมีลิงค์ที่ชื่อของโพสต์ในหน้ารายการโพสต์ เพื่อไปยังหน้ารายละเอียดของโพสต์ เปลี่ยนบรรทัด `<h1><a href="">{{ post.title }}</a></h1>` ให้เป็นแบบนี้:{% endraw %}

    html
    <h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
    

{% raw %}ได้เวลาอธิบายบรรทัดเหล่านี้แล้ว `{% url 'post_detail' pk=post.pk %}` คุณอาจสงสัยสัญลักษณ์ `{% %}` นี้ ซึ่งก็คือ เรากำลังใช้ template tag ของ Django ตอนนี้เราจะใช้เพื่อสร้าง URL ให้กับเรา!{% endraw %}

`blog.views.post_detail` คือเส้นทางไปที่ `post_detail` *view* ที่เราต้องสร้าง หมายเหตุ: `blog` คือชื่อของแอปพลิเคชันของเรา (หรือก็คือไดเรกทอรี `blog`), `views` คือชื่อของไฟล์ `views.py` และส่วนสุดท้าย - `post_detail` - คือชื่อของ *view*.

ตอนนี้ เปิดหน้า: http://127.0.0.1:8000/ เราจะเจอข้อผิดพลาด (ตามที่คาดเอาไว้, เนื่องจากเรายังไม่มี URL หรือ *view* สำหรับ `post_detail`) โดยมีหน้าตาแบบนี้:

![NoReverseMatch error][1]

 [1]: images/no_reverse_match2.png

## สร้าง URL สำหรับ รายละเอียดโพสต์

สร้าง URL ไฟล์ `urls.py` สำหรับ `post_detail` *view* ของเรา!

เราต้องการให้รายละเอียดของโพสต์แรกของเรา แสดงโดยการเข้าถึง **URL**: http://127.0.0.1:8000/post/1/

เรามาสร้าง URL ในไฟล์ `blog/urls.py` ให้ชี้ Django ไปยัง *view* ชื่อ `post_detail`, ซึ่งจะแสดงหน้าโพสต์ และเพิ่มบรรทัด `url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),` ที่ไฟล์ `blog/urls.py` ตอนนี้ ไฟล์ของคุณควรมีหน้าตาแบบนี้:

    python
    from django.conf.urls import include, url
    from . import views
    
    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    ]
    

ในส่วน `^post/(?P<pk>[0-9]+)/$` จะดูน่ากลัวสักหน่อย, แต่ไม่ต้องห่วง - เราจะอธิบายให้คุณเข้าใจแน่นอน: - เริ่มจาก `^` อีกครั้ง -- "จุดเริ่มต้น" - `post/` หมายถึง หลังจากจุดเริ่มต้น, URL ควรจะมีคำว่า **post** และ **/** ไปได้สวยทีเดียว - `(?P<pk>[0-9]+)` - ส่วนนี้ซับซ้อนนิดหน่อย มันหมายถึง Django จะรับข้อมูลเข้ามา และส่งต่อไปยัง view โดยผ่านตัวแปรชื่อ `pk` `[0-9]` ยังบอกเราว่า สามารถเป็นได้เฉพาะตัวเลขเท่านั้น, ใช้ตัวอักษรอื่นไม่ได้ (ดังนั้นก็คือ ตัวเลขตั้งแต่ 0 ถึง 9) `+` หมายถึง ต้องมีตัวเลขอย่างน้อยหนึ่งหลัก ดังนั้น ตัวอย่างเช่น `http://127.0.0.1:8000/post//` นั้นไม่ถูกต้อง, แต่ `http://127.0.0.1:8000/post/1234567890/` ใช้ได้! - `/` - เราต้องการ **/** อีกครั้ง - `$` - "จุดสิ้นสุด"!

นั่นคือ ถ้าคุณป้อน `http://127.0.0.1:8000/post/5/` มายังเบราว์เซอร์ของคุณ Django จะเข้าใจว่าคุณกำลังมองหา *view* ชื่อ `post_detail` และส่งข้อมูลคือ `pk` ซึ่งมีค่าเท่ากับ `5` ไปยัง *view* นั้น.

`pk` นั้นย่อมาจาก `primary key` ชื่อนี้มักถูกใช้ใน Django บ่อยๆ แต่คุณก็สามารถตั้งชื่อตัวแปรที่ต้องการได้ (อย่าลืม: ใช้ตัวพิมพ์เล็ก และ `_` แทนที่ whitespaces!) ตัวอย่างเช่น แทนที่จะใช้ `(?P<pk>[0-9]+)` เราควรมีตัวแปร `post_id`, ดังนั้นในส่วนนี้จะมีหน้าตาแบบนี้แทน: `(?P<post_id>[0-9]+)`.

เอาล่ะ เราต้องการเพิ่มรูปแบบ URL ใหม่ ใน `blog/urls.py`! ลองโหลดหน้า: http://127.0.0.1:8000/ ตู๊ม! เจอข้อผิดพลาดอีกอัน! ตามคาด!

![AttributeError][2]

 [2]: images/attribute_error2.png

คุณยังจำขั้นตอนถัดไปได้ไหม? แน่นอน: เพิ่ม view ใหม่!

## เพิ่ม view รายละเอียดของโพสต์

ตอนนี้ *view* ของเราจะได้พารามิเตอร์เพิ่มเข้ามาคือ `pk` *view* ของเราต้องจับมันไว้ ใช่ไหม? ดังนั้นเราจะสร้างฟังก์ชันใหม่ โดยใช้ `def post_detail(request, pk):` สังเกตว่าเราต้องใช้ชื่อเดียวกันกับชื่อที่เรากำหนดไว้ใน url (`pk`) การละเว้นตัวแปรนี้ จะทำให้เกิดขึ้นผิดพลาด!

ตอนนี้ เราต้องการโพสต์เดียวเท่านั้น เราสามารถทำได้ โดยใช้ queryset แบบนี้:

    Post.objects.get(pk=pk)
    

แต่โค้ดนี้มีปัญหา ถ้าเกิดว่ามันไม่มี `Post` ตามค่า `primary key` (`pk`) ที่ส่งมา เราจะได้ข้อผิดพลาดหน้าตาน่าเกลียดสุดๆ!

![DoesNotExist error][3]

 [3]: images/does_not_exist2.png

เราไม่ต้องการแบบนี้! แต่ แน่ล่ะ Django มาพร้อมกับสิ่งที่สามารถจัดการปัญหานี้ได้: `get_object_or_404` ในกรณีที่ไม่มี `Post` จากค่า `pk` ที่ส่งไป มันจะแสดงหน้าเว็บที่ดูดีกว่าให้เรา (เรียกว่าหน้า `Page Not Found 404`)

![Page not found][4]

 [4]: images/404_2.png

ข่าวดีคือ คุณสามารถสร้างหน้า `Page not found` เป็นของคุณเองได้ และทำให้สวยแค่ไหนก็ได้ตามแต่คุณต้องการ แต่ตอนนี้ยังไม่จำเป็นเท่าไหร่นัก เราจะขอข้ามไปก่อน

เอาล่ะ ได้เวลาเพิ่ม *view* ไปยังไฟล์ `views.py` ของเราแล้ว!

เราจะเปิดไฟล์ `blog/views.py` ขึ้นมา และเพิ่มโค้ดเหล่านี้ลงไป:

    from django.shortcuts import render, get_object_or_404
    

ใกล้ๆ บรรทัด `from` และท้ายบรรทัดของไฟล์ เราจะเพิ่ม *view* ของเรา:

    def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})
    

ได้เวลาโหลดหน้าเว็บนี้ใหม่: http://127.0.0.1:8000/

![Post list view][5]

 [5]: images/post_list2.png

ใช้ได้แล้ว! แต่ เกิดอะไรขึ้นเมื่อคุณคลิกที่ลิงค์บนชื่อโพสต์?

![TemplateDoesNotExist error][6]

 [6]: images/template_does_not_exist2.png

โอ้ ไม่นะ! ข้อผิดพลาดอีกแล้ว! แต่เรารู้วิธีรับมือปัญหานี้แล้ว ถูกไหม? เราต้องเพิ่ม template ไงล่ะ!

## สร้าง template สำหรับหน้ารายละเอียดโพสต์

เราจะสร้างไฟล์ใน `blog/templates/blog` ชื่อ `post_detail.html`.

ผลลัพธ์จะคล้ายนี้:

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        <div class="post">
            {% if post.published_date %}
                <div class="date">
                    {{ post.published_date }}
                </div>
            {% endif %}
            <h1>{{ post.title }}</h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endblock %}
    

เป็นอีกครั้งที่เรา extend ไฟล์ `base.html` ใน block `content` เราต้องการแสดง published_date ของโพสต์ (ถ้ามี), ชื่อโพสต์ และ เนื้อหา แต่เราควรจะมาคุยกันถึงเรื่องสำคัญอีกอย่างก่อน ดีไหม?

{% raw %}`{% if ... %} ... {% endif %}` คือ template tag ที่เราสามารถใช้ เมื่อเราต้องการตรวจสอบบางอย่าง (ยังจำ `if ... else ..` จากบท **แนะนำให้รู้จัก Python** ได้ไหม?) ในกรณีนี้ เราต้องการตรวจสอบดูว่า `published_date` ของโพสต์นั้นมีอยู่หรือไม่{% endraw %}

เอาล่ะ เรามาลองโหลดหน้าเว็บของเราอีกครั้ง ตอนนี้หน้า `Page not found` ควรจะหายไปแล้ว

![Post detail page][7]

 [7]: images/post_detail2.png

เย้! ใช้ได้แล้ว!

## มีอีกอย่างนึง: ได้เวลาเอาขึ้นเซิร์ฟเวอร์!

มันคงจะดี ถ้าเราจะดูหน้าเว็บของเราทำงานอยู่บน PythonAnywhere อีกครั้ง ใช่ไหม? มา deploy กันอีกครั้ง

    $ git status
    $ git add -A .
    $ git status
    $ git commit -m "Added view and template for detailed blog post as well as CSS for the site."
    $ git push
    

*   ต่อมา ในคอนโซล [PythonAnywhere Bash][8]:

 [8]: https://www.pythonanywhere.com/consoles/

    $ cd my-first-blog
    $ source myvenv/bin/activate
    (myvenv)$ git pull
    [...]
    (myvenv)$ python manage.py collectstatic
    [...]
    

*   สุดท้าย เปิด [Web tab][9] และกด **Reload**.

 [9]: https://www.pythonanywhere.com/web_app_setup/

และนั่นควรเสร็จแล้ว! ยินดีด้วย :)