# การ extend template

อีกความเก่งข้อหนึ่งของ Django คือ **ความสามารถในการ extend template** หมายความว่าไง? มันหมายถึงว่า คุณสามารถใช้ชิ้นส่วน HTML เดียว ได้กับหลายๆ หน้าของเว็บคุณ

วิธีนี้ทำให้คุณไม่จำเป็นต้องมีเนื้อหาเดิมซ้ำๆ ในทุกๆ ไฟล์ เมื่อคุณต้องการใช้ข้อมูล/เค้าโครงเดิม และคุณต้องการเปลี่ยนคือบางสิ่งบางอย่าง คุณไม่จำเป็นต้องทำกับทุก template ใช้แค่อันเดียวเท่านั้น!

## สร้าง template หลัง

template หลัก คือ template ที่เป็นพื้นฐานที่สุด ที่คุณสามารถนำไปสร้างเป็นหน้าอื่นในเว็บของคุณได้

สร้างไฟล์ `base.html` ใน `blog/templates/blog/`:

    blog
    └───templates
        └───blog
                base.html
                post_list.html
    

จากนั้นเปิดไฟล์และคัดลองทุกบรรทัดจาก `post_list.html` ไปยังไฟล์ `base.html` แบบนี้:

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
                <h1><a href="/">Django Girls Blog</a></h1>
            </div>
    
            <div class="content container">
                <div class="row">
                    <div class="col-md-8">
                    {% for post in posts %}
                        <div class="post">
                            <div class="date">
                                {{ post.published_date }}
                            </div>
                            <h1><a href="">{{ post.title }}</a></h1>
                            <p>{{ post.text|linebreaks }}</p>
                        </div>
                    {% endfor %}
                    </div>
                </div>
            </div>
        </body>
    </html>
    

จากนั้น ในไฟล์ `base.html` แทนที่ทุกสิ่งใน `<body>` (ทุกสิ่งระหว่าง `<body>` และ `</body>`) ด้วย:

    html
    <body>
        <div class="page-header">
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
    

จริงๆ แล้วเราแทนที่ทุกสิ่งระหว่าง `{% for post in posts %}{% endfor %}` ด้วย:

    html
    {% block content %}
    {% endblock %}
    

ที่ทำมาหมายความว่าอย่างไร? คุณเพิ่งสร้าง `block` ซึ่งคือ tag ของ template ที่ช่วยให้คุณใส่โค้ด HTML ลงไปใน template อื่นที่ extend มาจาก `base.html` เราจะแสดงวิธีให้คุณดูเร็วๆ นี้ล่ะ

ตอนนี้ บันทึกไฟล์ และเปิดไฟล์ `blog/templates/blog/post_list.html` ขึ้นมาอีกครั้ง ลบทุกสิ่งที่ไม่อยู่ใน body และรวมถึง `<div class="page-header"></div>` ดังนั้น ไฟล์จะมีหน้าตาแบบนี้:

    html
    {% for post in posts %}
        <div class="post">
            <div class="date">
                {{ post.published_date }}
            </div>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
    

และเพิ่มบรรทัดนี้ที่ต้นไฟล์:

    {% extends 'blog/base.html' %}
    

{% raw %}หมายความว่า เรา extend template `base.html` ใน `post_list.html` เหลืออีกสิ่งหนึ่ง: เพิ่มทุกอย่างลงไป (ยกเว้นบรรทัดที่เราเพิ่งเพิ่มเข้าไป) ระหว่าง `{% block content %}` และ `{% endblock content %}` แบบนี้:{% endraw %}

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
    

เสร็จแล้ว! ลองดูว่าเว็บเรายังทำงานอยู่ไหม :)

> ถ้าคุณเจอกับข้อผิดพลาด `TemplateDoesNotExists` นั่นแสดงว่าคุณยังไม่มีไฟล์ `blog/base.html` และคุณยังใช้คสั่ง `runserver` ไว้อยู่ในคอนโซล ลองปิดมัน (โดยกดปุ่ม Ctrl+C - Control และ C พร้อมกัน) และ เปิดขึ้นใหม่ โดยใช้คำสั่ง `python manage.py runserver`