# Django Form

สิ่งสุดท้ายที่เราต้องการทำในเว็บไซต์ของเราคือการสร้างส่วนที่เอาไว้แก้ไขบล็อกโพสต์ของเรา หน้า Django `admin` นั้น ก็เจ๋งดีอยู่หรอกนะ แต่ก็ปรับแต่งได้ค่อนข้างยากอยู่เหมือนกัน ด้วย `form` เราจะมีอำนาจทุกอย่าง - เราสามารถทำได้ทุกอย่างตามจินตนาการที่เรามี!

สิ่งที่ดีอย่างหนึ่งของ Django form คือ เราสามารถเริ่มสร้างจากศูนย์เลย หรือสร้าง `ModelForm` ซึ่งจะบันทึกผลลัพธ์จากฟอร์มไปยังโมเดลของเราทันที

นี่คือสิ่งที่เราต้องการจะทำ: เราจะสร้างฟอร์มจากโมเดล `Post` ของเรา

เช่นเดียวกับทุกส่วนของ Django ฟอร์ม ก็มีไฟล์เป็นของตัวเอง คือ: `forms.py`.

เราต้องสร้างไฟล์นี้ภายในไดเรกทอรี `blog`

    blog
       └── forms.py
    

เอาล่ะ เปิดไฟล์และเพิ่มโค้ดเหล่านี้ลงไป:

    python
    from django import forms
    
    from .models import Post
    
    class PostForm(forms.ModelForm):
    
        class Meta:
            model = Post
            fields = ('title', 'text',)
    

ก่อนอื่น เราต้องนำเข้า Django form เสียก่อน(`from django import forms`) และแน่นอน โมเดล `Post` ของเรา (`form .models import Post`).

`PostForm` ใช่อย่างที่คุณสงสัยนั่นแหละ, ชื่อฟอร์มของเรานั่นเอง เราต้องบอก Django ว่า ฟอร์มของเราคือ `ModelForm` (Django จะร่ายมนต์บางอย่างให้เรา) - `forms.ModelForm` นั้นจะรับผิดชอบให้

ถัดมา เรามี `class Meta` ที่ซึ่งเราจะบอก Django ว่าฟอร์มนี้ จะใช้โมเดลอะไร (`model = Post`).

สุดท้าย เราสามารถบอกได้ว่า เราจะใช้ฟิลด์ไหนบ้างในฟอร์มของเรา ในที่นี้ เราจะใช้แค่ `title` และ `text` เท่านั้น - `author` ควรจะเป็นคนที่ตอนนี้ login อยู่ (คุณนั่นแหละ!) และ `created_date` ควรจะถูกกำหนดโดยอัตโนมัติเมื่อเราสร้างโพสต์ (ตัวอย่าง ในโค้ด) ถูกไหม?

และนั่นแหละ! ที่เราต้องทำตอนนี้คือใช้ฟอร์มข้างใน *view* และแสดงมันออกมาใน template

และอีกครั้งที่เราจะสร้าง: ลิงค์ไปยังหน้าเพจ, URL, view และ template

## ลิงค์ไปยังหน้าเว็บด้วยฟอร์ม

ได้เวลาเปิดไฟล์ `blog/templates/blog/base.html` เราจะเพิ่มลิงค์ใน `div` ชื่อ `page-header`:

    html
    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    

หมายเหตุ เราต้องเรียกใช้ view ใหม่ของเราคือ `post_new`.

หลังจากเพิ่มบรรทัดนี้ ไฟล์ html ของคุณจะมีหน้าตาแบบนี้:

    html
    {% load staticfiles %}
    <html>
        <head>
            <title>Django Girls blog</title>
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
            <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
            <link rel="stylesheet" href="{% static 'css/blog.css' %}">
        </head>
        <body>
            <div class="page-header">
                <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
                <h1><a href="/">Django Girls Blog</a></h1>
            </div>
            <div class="content container">
                <div class="row">
                    <div class="col-md-8">
                        {% block content %}
                        {% endblock %}
                    </div>
                </div>
            </div>
        </body>
    </html>
    

หลังจากบันทึกไฟล์ และโหลดหน้าเว็บ http://127.0.0.1:8000 อีกครั้ง คุณจะเจอกับข้อผิดพลาด `NoReverseMatch`, คุ้นๆ ไหม?

## URL

เปิดไฟล์ `blog/urls.py` และเพิ่มบรรทัดนี้:

    python
        url(r'^post/new/$', views.post_new, name='post_new'),
    

โค้ดสุดท้ายจะมีหน้าตาแบบนี้:

    python
    from django.conf.urls import include, url
    from . import views
    
    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
        url(r'^post/new/$', views.post_new, name='post_new'),
    ]
    

หลังจากโหลดหน้าเว็บ เราจะเห็น `AttributeError`, เพราะเรายังไม่มี view `post_new` นั่นเอง มาสร้างกันเลยตอนนี้

## post_new view

ได้เวลาเปิดไฟล์ `blog/views.py` และเพิ่มบรรทัดเหล่านี้ลงไปพร้อมกับ `form`:

    python
    from .forms import PostForm
    

และ *view* ของเรา:

    python
    def post_new(request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    

การสร้างฟอร์ม `Post` ใหม่, เราต้องเรียกใช้ `PostForm()` และส่งไปให้ template เราจะกลับไปที่ *view* เร็วๆ นี้ แต่ตอนนี้ เราจะสร้าง template สำหรับฟอร์มของเรา

## Template

เราต้องสร้างไฟล์ `post_edit.html` ในไดเรกทอรี `blog/templates/blog`, ในการสร้างฟอร์มนั้น เราต้องการสองสามอย่าง:

*   เราจะแสดงฟอร์มของเรา สามารถทำได้โดยใช้ตัวอย่างนี้ `{% raw %}{{ form.as_p }}{% endraw %}`.
*   บรรทัดด้านบนต้องอยู่ภายใต้ tag form: `<form method="POST">...</form>`
*   เราจำเป็นต้องมีปุ่ม `Save` เราสามารถทำได้โดยใช้ HTML button: `<button type="submit">Save</button>`
*   และสุดท้าย หลังจากเปิด tag `<form ...>` เราต้องเพิ่ม `{% raw %}{% csrf_token %}{% endraw %}`. ซึ่งส่วนี้สำคัญมาก เพราะมันทำให้ฟอร์มของคุณปลอดภัยขึ้น! Django จะด่าคุณ ถ้าคุณลืมส่วนนี้ และพยายามบันทึกฟอร์ม:

![หน้า CSFR Forbidden][1]

 [1]: images/csrf2.png

เอาล่ะ มาดูกันว่า HTML ใน `post_edit.html` จะมีหน้าตายังไง:

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        <h1>New post</h1>
        <form method="POST" class="post-form">{% csrf_token %}
            {{ form.as_p }}
            <button type="submit" class="save btn btn-default">Save</button>
        </form>
    {% endblock %}
    

ได้เวลาโหลดหน้าใหม่อีกครั้ง! เย้! ฟอร์มของคุณปรากฎขึ้นมาแล้ว!

![ฟอร์มใหม่][2]

 [2]: images/new_form2.png

แต่ รอประเดี๋ยว! เมื่อคุณพิมพ์บางอย่างในช่อง `title` และ `text` และพยายามบันทึกมัน - จะเกิดอะไรขึ้น?

ไม่มีอะไรเลย! เราได้หน้าเดิมอีกครั้งและข้อความของเราหายไป... และ ไม่มีโพสต์ใหม่เพิ่มมา ถ้างั้น มีอะไรผิดไปล่ะ?

คำตอบคือ: ไม่มีอะไรผิดหรอก เราต้องทำเพิ่มเติมเล็กน้อยใน *view*.

## บันทึกฟอร์ม

เปิดไฟล์ `blog/views.py` ขึ้นมาอีกครั้ง ในตอนนี้เรามี view `post_new` เท่านี้:

    python
    def post_new(request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    

เมื่อเราบันทึกฟอร์ม เราถูกพาไปยัง view เดียวกัน แต่ครั้งนี้เรามีข้อมูลมาด้วยใน `request` หรือให้เจาะจงคือใน `request.POST` (ชื่อนี้ไม่เกี่ยวอะไรกับที่เรากำลังทำบล็อก "post" มันคือการบอกว่าเรากำลัง "posting" ข้อมูล) จำได้ไหมว่า ในไฟล์ HTML `<form>` มีตัวแปร `method="POST"`? ข้อมูลทั้งหมดจากฟอร์มตอนนี้คือใน `request.POST` เราไม่ควรเปลี่ยนชื่อ `POST` ไปเป็นอย่างอื่น (มีอีกหนึ่งค่าที่ใช้ได้สำหรับ `method` คือ `GET`, แต่เราไม่มีเวลาพอที่จะอธิบายความแตกต่างในตอนนี้)

ดังนั้นใน *view* ของเรา มีสองสิ่งที่เราต้องจัดการ อย่างแรก: เมื่อคุณเปิดหน้าฟอร์มครั้งแรกและเราต้องการฟอร์มเปล่า อย่างที่สอง: เมื่อเรากลับมาที่ *view* ด้วยข้อมูลที่เราได้ป้อนไป ดังนั้น เราต้องเพิ่มเงื่อนไขเหล่านี้ (เราจะใช้ `if` ในการจัดการ)

    python
    if request.method == "POST":
        [...]
    else:
        form = PostForm()
    

ได้เวลาที่เราจะเติมโค้ดของเราใน `[...]` ถ้า `method` คือ `POST` แล้ว เราต้องสร้าง `PostForm` ด้วยข้อมูลจากฟอร์ม ถูกไหม? เราจะทำแบบนั้นโดยใช้:

    python
    form = PostForm(request.POST)
    

ง่ายใช่ไหม! ถัดมา คือการตรวจสอบว่าถ้าข้อมูลที่ป้อนไปยังฟอร์มนั้นถูกต้อง (ทุกข้อมูลที่จำเป็นและค่าที่ไม่ถูกต้องไม่ถูกบันทึก) เราทำแบบนั้นโดยใช้ `form.is_valid()`.

เราตรวจสอบฟอร์ม ถ้าฟอร์มถูกต้อง เราก็สามารถบันทึกได้!

    python
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
    

โดยทั่วไป เรามีสองสิ่งตรงนี้: เราบันทึกฟอร์มด้วย `form.save` และเราเพิ่มผู้เขียน (ซึ่งเราไม่มี `author` ในฟอร์ม `PostForm` และข้อมูลส่วนนี้นั้นจำเป็นต้องมี!) `commit=False` หมายถึง เรายังไม่บันทึกโมเดล `Post` เลยในตอนนี้ - เราต้องเพิ่มผู้เขียนเสียก่อน ส่วนใหญ่เราจะใช้ `form.save()`, โดยไม่มี `commit=False` แต่นี้กรณีนี้เราต้องใช้ `post.save()` จะเก็บการเปลี่ยนแปลง (เพิ่มผู้เขียน) และโพสต์ใหม่ก็ถูกสร้าง!

สุดท้าย มันคงจะเจ๋งถ้าเราไปยังหน้า `post_detail` สำหรับโพสต์ใหม่ที่เราสร้างขึ้น ถูกไหม? เราทำแบบนั้นได้โดยใช้:

    python
    from django.shortcuts import redirect
    

เพิ่มบรรทัดนี้ที่ต้นบรรทัดของไฟล์ และตอนนี้ที่เราจะทำคือ: ไปที่หน้า `post_detail` สำหรับโพสต์ใหม่ที่สร้างขึ้น

    python
    return redirect('blog.views.post_detail', pk=post.pk)
    

`blog.views.post_detail` คือชื่อของ view ที่เราต้องการจะไป ยังจำได้ไหมที่ *view* นั้นต้องการตัวแปร `pk` ? การส่งค่านี้ไปที่ view เราจะใช้ `pk=post.pk`, โดยที่ `post` คือโพสต์ที่เราสร้างขึ้นใหม่

เอาล่ะ พูดมาเยอะแล้ว เราอยากเห็นโค้ดล่าสุดของ *view* แล้วใช่ไหม?

    python
    def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    

มาดูกันว่าทำงานถูกต้องไหม ไปยังหน้า http://127.0.0.1:8000/post/new/ เพิ่ม `title` และ `text`, และบันทึก และ voilà! โพสต์ใหม่ถูกเพิ่มเข้าไป และเราจะถูกพาไปยังหน้า `post_detail` !

คุณอาจจะสังเกตว่า เรามีการกำหนดวันที่เผยแพร่ก่อนที่จะบันทึกโพสต์ แต่หลังจากนี้เราจะทำปุ่ม *publish* ในบท **Django Girls Tutorial: Extensions**.

เจ๋งไปเลย!

## Form validation

ตอนนี้ เราจะแสดงให้คุณได้เห็นถึงความเจ๋งของฟอร์ม Django บล็อกโพสต์ของเราต้องการข้อมูล `title` และ `text` ในโมเดล `Post` ของเรานั้น ไม่ได้บอกว่าข้อมูลเหล่านี้ (ตรงข้ามกับ `published_date`) นั้นจำเป็นต้องใส่ให้ครบ ดังนั้น Django ต้องมีการกำหนดค่าให้

ลองบันทึกฟอร์มโดยที่ไม่ใส่ข้อมูล `title` และ `text` คิดว่าจะเกิดไรขึ้น!

![Form validation][3]

 [3]: images/form_validation2.png

Django จะจัดการเรื่องฟอร์มให้กับเรา ว่าข้อมูลที่ป้อนเข้ามานั้นถูกต้อง มันเจ๋งเลยใช่ไหม?

> อย่างที่เราได้เคยใช้หน้า Django admin ตอนนี้ระบบคิดว่าเราล็อกอินอยู่ มีบางสถานการณ์ที่อาจทำให้เรานั้นออกจากระบบ (ปิดเบราว์เซอร์ ปิดเปิดระบบฐานข้อมูลใหม่ เป็นต้น) ถ้าคุณพบข้อผิดพลาดหลังจากสร้างโพสต์ใหม่เพราะคุณยังไม่ได้เข้าสู่ระบบ ให้ไปยังหน้า admin http://127.0.0.1:8000/admin เพื่อเข้าสู่ระบบอีกครั้ง ตรงนี้จะแก้ไขปัญหาได้ชั่วคราว ซึ่งการแก้ปัญหานี้แบบถาวร รอคุณอยู่ในบท **การบ้าน: เพิ่มความปลอดภัยให้เว็บคุณ!** หลังจากจบบทเรียนหลักนี้แล้ว

![เข้าระบบผิดพลาด][4]

 [4]: images/post_create_error.png

## การแก้ไขฟอร์ม

ตอนนี้คุณทราบวิธีเพิ่มฟอร์มใหม่แล้ว แต่ถ้าเกิดคุณยังแก้ไขของเดิมที่มีอยู่แล้วล่ะ? ซึ่งก็จะคล้ายกับที่เราเคยทำมา มาสร้างสิ่งสำคัญบางอย่างกัน (ถ้าคุณไม่เข้าใจสิ่งใด สามารถถามโค้ชคุณหรือเปิดบทที่แล้วดู ซึ่งเราได้อธิบายไปแล้ว)

เปิดไฟล์ `blog/templates/blog/post_detail.html` และเพิ่มบรรทัดนี้ลงไป:

    python
    <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
    

ดังนั้น template จะมีหน้าตาแบบนี้

    html
    {% extends 'blog/base.html' %}
    
    {% block content %}
        <div class="post">
            {% if post.published_date %}
                <div class="date">
                    {{ post.published_date }}
                </div>
            {% endif %}
            <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
            <h1>{{ post.title }}</h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endblock %}
    

เปิดไฟล์ `blog/urls.py` และเพิ่มบรรทัดนี้:

    python
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    

เราจะนำ template `blog/templates/blog/post_edit.html` มาใช้อีกครั้ง ดังนั้นสิ่งที่ขาดไปสิ่งสุดท้ายคือ *view*.

เปิดไฟล์ `blog/views.py` และเพิ่มบรรทัดเหล่านี้ลงไปท้ายไฟล์:

    python
    def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    

หน้าตาเกือบจะเหมือนกับ view `post_new` ของเราเลยว่าไหม? แต่ไม่ใช่ทั้งหมด สิ่งแรก: เราส่งค่า `pk` เพิ่มเติมจาก urls ถัดมา: เราเลือกโมเดล `Post` ซึ่งเราต้องการแก้ไข ด้วยฟังก์ชัน `get_object_or_404(Post, pk=pk)` และเมื่อเราสร้างฟอร์ม เราส่งค่าโพสต์นี้ โดยส่ง `instance` ไป เมื่อเราบันทึกฟอร์ม:

    python
    form = PostForm(request.POST, instance=post)
    

และเมื่อเราเปิดฟอร์มขึ้นมาพร้อมกับโพสต์ที่ต้องการแก้ไข:

    python
    form = PostForm(instance=post)
    

เอาล่ะ มาดูกันว่าเวิร์คไหม! ไปยังหน้า `post_detail` ซึ่งควรมีปุ่มแก้ไขที่ตำแหน่งมุมบน-ขวา:

![ปุ่มแก้ไข][5]

 [5]: images/edit_button2.png

เมื่อคุณคลิกมัน คุณจะเห็นฟอร์มพร้อมข้อมูลของโพสต์เรา:

![การแก้ไขฟอร์ม][6]

 [6]: images/edit_form2.png

ลองแก้ไข title หรือ text ได้ตามสะดวก และบันทึกมัน!

ยินดีด้วย! แอพของคุณใกล้จะเสร็จเข้าไปทุกทีแล้ว!

หากคุณต้องการข้อมูลเพิ่มเติมเกี่ยวกับ Django form คุณสามารถดูได้ที่หน้าเอกสารของโครงการ Django: https://docs.djangoproject.com/en/1.8/topics/forms/

## ความปลอดภัย

การสร้างโพสต์ใหม่โดยแค่คลิกที่ลิงค์นั้น มันสุดยอดมาก! แต่ตอนนี้ ทุกคนที่เข้ามายังหน้าเว็บคุณจะสามารถเพิ่มโพสต์ใหม่ได้และนั่นไม่ใช่สิ่งที่คุณต้องการ มาทำให้ปุ่มแสดงเฉพาะเราเท่านั้น

ในไฟล์ `blog/templates/blog/base.html` ตรงส่วน `page-header` `div` ควรมีหน้าตาแบบนี้:

    html
    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    

เราจะทำการเพิ่ม `{% if %}` อีกอัน เพื่อแสดงผลลัพธ์เฉพาะผู้ใช้ที่เข้าระบบแล้วเรียบร้อยที่หน้า admin ซึ่งตอนนี้ ก็คือคุณไง! เปลี่ยน tag `<a>` ให้มีหน้าตาแบบนี้:

    html
    {% if user.is_authenticated %}
        <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
    {% endif %}
    

`{% if %}` จะทำให้ลิงค์นั้นแสดงบนบราวเซอร์ก็ต่อเมื่อ ผู้ใช้เข้าสู่ระบบแล้วเท่านั้น นี่เป็นขั้นแรกในการป้องกันการสร้างโพสต์ใหม่เท่านั้น ยังมีส่วนอื่นที่เราต้องทำเพิ่มเติม เราจะอธิบายเรื่องความปลอดภัยในบทเสริมถัดไป

เมื่อเรานั้นเข้าสู่ระบบไว้แล้ว ถ้าคุณโหลดหน้าเว็บอีกครั้ง คุณจะไม่เห็นความแตกต่าง ลองโหลดหน้าเว็บบนเบราว์เซอร์ใหม่ และคุณจะไม่เห็นอะไรแสดงขึ้นมา!

## มีอีกอย่างนึง: ได้เวลาเอาขึ้นเซิร์ฟเวอร์!

มาดูกันว่า มันจะทำงานได้บน PythonAnywhere ไหม ได้เวลาเอาขึ้นแล้ว!

*   อย่างแรก บันทึกโค้ดใหม่ของคุณ และส่งไปเก็บไว้ที่ Github

    $ git status
    $ git add -A .
    $ git status
    $ git commit -m "Added views to create/edit blog post inside the site."
    $ git push
    

*   ต่อมา ในคอนโซล [PythonAnywhere Bash][7]:

 [7]: https://www.pythonanywhere.com/consoles/

    $ cd my-first-blog
    $ source myvenv/bin/activate
    (myvenv)$ git pull
    [...]
    (myvenv)$ python manage.py collectstatic
    [...]
    

*   สุดท้าย เปิด [Web tab][8] และกด **Reload**.

 [8]: https://www.pythonanywhere.com/web_app_setup/

และนั่นควรเสร็จแล้ว! ยินดีด้วย :)