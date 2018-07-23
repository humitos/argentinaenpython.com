# CSS - จับแต่งหน้าให้สวยปิ๊ง!

อุต๊ะ บล๊อคของเราทำไมดูน่าเกลียดอย่างนี้ ได้เวลาที่จะทำให้มันดีขึ้น เราจะใช้ CSS สำหรับการปรับแต่ง

## อะไรคือ CSS?

Cascading Style Sheets (CSS) เป็นภาษาที่ใช้สำหรับอธิบายลักษณะ และรูปแบบของเว็บไซต์ที่ถูกเขียนในรูปภาษามาร์กอับ (เช่น HTML) อาจจะเรียกมันว่า เป็น make-up สำหรับเว็บไซต์ก็ได้นะ :)

แต่เราจะไม่เริ่มจากศูนย์อีกครั้ง บางอย่างเราจะใช้สิ่งที่โปรแกรมเมอร์คนอื่นทำมาแล้วแจกให้เราโหลดในเนตฟรี และคุณรู้ดีว่าการต้องทำใหม่อีกครั้งไม่เห็นสนุกเลย

## Bootstrap คือคำตอบ!

Bootstrap เป็นหนึ่งใน frameworks ภาษา HTML และ CSS ที่ได้รับความนิยมอย่างสูงสำหรับการพัฒนาเว็บไซด์ให้สวยงาม ลองเข้าไปที่ http://getbootstrap.com/

มันถูกเขียนโดยเหล่าโปรแกรมเมอร์ที่เคยทำงานให้กับ Twitter และตอนนี้ได้ถูกพัฒนาต่อโดยอาสาสมัครจะทั่วทุกมุมโลก

## ติดตั้ง Bootstrap

การติดตั้ง Bootstrap คุณจำเป็นต้องเพิ่มโค๊ดข้างล่างนี้ที่ `<head>` ของคุณ ในไฟล์.html (`blog/templates/blog/post_list.html`):

    html <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"> <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    

มันจะไม่เพิ่ม files ใดๆที่โปรเจคของคุณ มันแค่ทำหน้าที่ชี้ไปยัง files ที่มีอยู่แล้วบนอินเตอร์เน็ด ก็ดำเนินการต่อไป เปิดเว็บไซด์ของคุณและรีเฟรช หน้าตาจะเป็นอย่างนี้ แท้เด้มมมม

![รูปที่ 14.1][1]

 [1]: images/bootstrap1.png

ดูดีขึ้นแล้ว!

## Static files ใน Django

ในที่สุดเราก็จะได้ดูสิ่งที่เราเรียกกันว่า **static file** static file คือทุกไฟล์ CSS และ รูปภาพ ของคุณ -- ไฟล์ที่ไม่มีการเปลี่ยนแปลง ซึ่งข้อมูลนั้นจะไม่เปลี่ยนตามคำร้องขอ และจะเป็นข้อมูลเดิมเสมอสำหรับผู้ใช้ทุกคน

### แล้วจะเราเก็บไฟล์ static ไว้ที่ไหนสำหรับ Django

อย่างที่คุณเห็นเมื่อคุณใช้คำสั่ง `collectstatic` บนเซิร์ฟเวอร์ Django รู้ว่าจะหาไฟล์ static สำหรับ "admin" ได้ที่ไหน ตอนนี้เราต้องการเพิ่มไฟล์ static สำหรับแอป `blog` ของเรา.

เราสามารถทำแบบนั้นได้โดยสร้างโฟลเดอร์ชื่อ `static` ข้างในแอป blog:

    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    └── mysite
    

Django จะค้นหาโฟลเดอร์ชื่อ "static" ข้างโฟลเดอร์ของทุกแอป โดยอัตโนมัติ และเราจะสามารถใช้ไฟล์เหล่านั้นเป็นไฟล์ static ได้

## ไฟล์ CSS แรกของคุณ!

มาสร้างไฟล์ CSS สำหรับตกแต่งหน้าเว็บตามสไตล์ของคุณกัน สร้างไดเรกทอรีชื่อ `css` ข้างในไดเรกทอรี `static` ของคุณ จากนั้นสร้างไฟล์ใหม่ชื่อ `blog.css` ข้างในไดเรกทอรี `css` เมื่อสักครู่ พร้อมหรือยัง?

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css
    

ได้เวลาเขียน CSS กันแล้ว! เปิดไฟล์ `blog/static/css/blog.css` ด้วยตัวแก้ไขโค้ดของคุณ

เราจะไม่ลงลึกเกี่ยวกับ CSS ในที่นี้ เพราะเราจะตกแต่งแบบง่ายๆ และคุณสามารถไปเรียนรู้เพิ่มเติมด้วยตัวคุณเองได้ในภายหลัง เราแนะนำบทเรียนออนไลน์ที่ [Codeacademy HTML & CSS][2] เพื่อเรียนรู้ทุกสิ่งที่คุณต้องการใช้สำหรับทำเว็บไซต์ให้สวยงามด้วย CSS

 [2]: http://www.codecademy.com/tracks/web

แต่ตอนนี้เราจะลองตกแต่งสักเล็กน้อย บางทีเราอาจจะลองเปลี่ยนสีข้อความส่วนหัวของเรา? การจะเข้าใจสีนั้น คอมพิวเตอร์จะใช้รหัสพิเศษ รหัสนี้จะเริ่มด้วยเครื่องหมาย `#` และตามด้วยตัวอักษร 6 ตัว (A-F) และตัวเลข (0-9) คุณสามารถหารหัสสีตัวอย่างได้ที่: http://www.colorpicker.com/ คุณอาจใช้ [สีที่กำหนดไว้แล้ว][3] เช่น `red` และ `green`.

 [3]: http://www.w3schools.com/cssref/css_colornames.asp

ในไฟล์ `blog/static/css/blog.css` ของคุณ ควรเพิ่มโค้ดต่อไปนี้ลงไป:

    css
    h1 a {
        color: #FCA205;
    }
    

`h1 a` คือการเลือกโดย CSS ส่วนนี้หมายความว่า เราจะใช้รูปแบบสไตล์นี้ กับทุกๆ ส่วนที่อยู่ใน tag `a` ที่อยู่ด้านใน tag `h1` (เช่น เมื่อเรามีโค้ดแบบนี้: `<h1><a href="">link</a></h1>`) ในกรณีนี้ คือการบอกว่า เราต้องการให้เปลี่ยนสีให้เป็นรหัส `#FCA205` ซึ่งคือสีส้มนั่นเอง แน่นอนว่าคุณสามารถเปลี่ยนเป็นสีที่คุณต้องการได้นะ!

ในไฟล์ CSS เราจะกำหนดลักษณะรูปแบบต่างๆ ให้กับองค์ประกอบที่อยู่ในไฟล์ HTML องค์ประกอบต่างๆ ถูกระบุโดยชื่อ (เช่น `a`, `h1`, `body`), ชื่อ `class` หรือ ชื่อ `id` class และ id คือชื่อที่คุณตั้งให้กับองค์ประกอบในหน้าเว็บเอง class กำหนดกลุ่มขององค์ประกอบ และ id ระบุไปยังองค์ประกอบที่จำเพาะเจาะจง ตัวอย่างเช่น tag ต่อไปนี้อาจะถูกระบุโดย CSS โดยใช้ ชื่อ tag `a`, class `external_link`, หรือ id `link_to_wiki_page`:

    html
    <a href="http://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page">
    

อ่านเกี่ยวกับ [CSS selector ใน w3schools][4].

 [4]: http://www.w3schools.com/cssref/css_selectors.asp

จากนั้น เราต้องบอก template HTML ของเราให้เพิ่ม CSS เข้าไป โดย เปิดไฟล์ `blog/templates/blog/blog_list.html` และเพิ่มบรรทัดนี้ที่ต้นไฟล์:

    html
    {% load staticfiles %}
    

เราโหลดไฟล์ static ของเราตรงนี้นี่เอง :) จากนั้น ระหว่าง `<head>` และ `</head>`,หลังจากลิงค์ไฟล์ CSS ของ Bootstrap (เบราว์เซอร์อ่านไฟล์เป็นลำดับ ดังนั้นโค้ดในไฟล์ของเรานั้นอาจจะแทนที่บางโค้ดของไฟล์ใน Bootstrap), และเพิ่มบรรทัดนี้:

    html
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    

ตรงนี้เราบอก tempate ไปว่าจะหาไฟล์ CSS ของเราได้จากที่ไหน

ตอนนี้ ไฟล์ของคุณควรมีหน้าตาแบบนี้:

    html
    {% load staticfiles %}
    <html>
        <head>
            <title>Django Girls blog</title>
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
            <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
            <link rel="stylesheet" href="{% static 'css/blog.css' %}">
        </head>
        <body>
            <div>
                <h1><a href="/">Django Girls Blog</a></h1>
            </div>
    
            {% for post in posts %}
                <div>
                    <p>published: {{ post.published_date }}</p>
                    <h1><a href="">{{ post.title }}</a></h1>
                    <p>{{ post.text|linebreaks }}</p>
                </div>
            {% endfor %}
        </body>
    </html>
    

โอเค บันทึกไฟล์และโหลดหน้าเว็บอีกครั้ง!

![รูปที่ 14.2][5]

 [5]: images/color2.png

คุณเก่งมาก! บางทีเราอาจต้องการให้เว็บของเรามีพื้นที่ส่วนขอบด้านซ้ายสักเล็กน้อยไหม? ลองนี่!

    css
    body {
        padding-left: 15px;
    }
    

เพิ่มโค้ดเหล่านี้ลงไฟล์ CSS ของคุณ บันทึกและดูผลลัพธ์สิ!

![รูปที่ 14.3][6]

 [6]: images/margin2.png

บางที เราอยากจะปรับแต่งแบบอักษรในส่วนหัวของเรา? ลองเพิ่มบรรทัดนี้ใน `<head>` ในไฟล์ `blog/templates/blog/post_list.html`:

    html
    <link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
    

บรรทัดนี้เรานำเข้าแบบอักษร *Lobster* จาก Google Fonts (https://www.google.com/fonts)

ตอนนี้ เพิ่มบรรทัด `font-family: 'Lobster';` ลงในไฟล์ CSS `blog/static/css/blog.css` ในส่วน `h1 a` (ระหว่างวงเล็บ `{` และ `}`) และโหลดหน้าเว็บอีกครั้ง:

    css
    h1 a {
        color: #FCA205;
        font-family: 'Lobster';
    }
    

![รูปที่ 14.3][7]

 [7]: images/font.png

ดีงาม!

อย่างที่เคยบอกไปก่อนหน้านี้ CSS นั้นมีแนวคิดของ class ซึ่งสามารถทำให้คุณกำหนดชื่อให้กับบางส่วนในโค้ด HTML และเปลี่ยนลักษณะหรือรูปแบบเฉพาะส่วนที่ต้องการนั้น โดยไม่มีผลกับส่วนอื่น มันจะดีมาก ถ้าหากคุณมี div สองอัน และแต่ละอันนั้นมีลักษณะที่แตกต่างกัน (เหมือนกับส่วนหัวของโพสต์คุณ) ดังนั้น คุณไม่ต้องการให้มันมีหน้าตาเหมือนกันนั่นเอง

มาตั้งชื่อให้กับบางส่วนในโค้ด HTML กัน เพิ่ม class ชื่อ `page-header` ให้กับ `div` ซึ่งมีส่วนหัวของโพสต์คุณ เช่น:

    html
    <div class="page-header">
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>
    

และตอนนี้ เพิ่ม class `post` ให้กับ `div` ที่มีบล็อกโพสต์

    html
    <div class="post">
        <p>published: {{ post.published_date }}</p>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
    

เราจะเพิ่มส่วนประกาศ ที่จะใช้เลือกในแต่ละบล็อคที่เราได้กำหนด ตัวเลือกที่เริ่มต้นด้วยเครื่องหมายจุด `.` จะใช้กับการเลือก class มีเว็บที่สอนและอธิบายเกี่ยวกับ CSS อยู่มากมาย ที่ช่วยคุณเข้าใจโค้ดด้านล่างนี้ สำหรับตอนนี้ คัดลอกและวางลงในไฟล์ `blog/static/css/blog.css` ของคุณ:

    css
    .page-header {
        background-color: #ff9400;
        margin-top: 0;
        padding: 20px 20px 20px 40px;
    }
    
    .page-header h1, .page-header h1 a, .page-header h1 a:visited, .page-header h1 a:active {
        color: #ffffff;
        font-size: 36pt;
        text-decoration: none;
    }
    
    .content {
        margin-left: 40px;
    }
    
    h1, h2, h3, h4 {
        font-family: 'Lobster', cursive;
    }
    
    .date {
        float: right;
        color: #828282;
    }
    
    .save {
        float: right;
    }
    
    .post-form textarea, .post-form input {
        width: 100%;
    }
    
    .top-menu, .top-menu:hover, .top-menu:visited {
        color: #ffffff;
        float: right;
        font-size: 26pt;
        margin-right: 20px;
    }
    
    .post {
        margin-bottom: 70px;
    }
    
    .post h1 a, .post h1 a:visited {
        color: #000000;
    }
    

จากนั้นแทนที่โค้ด HTML ที่แสดงโพสต์ของเราด้วยโค้ดที่เราได้ทำกับปรับแต่งหน้าตา:

    html
    {% for post in posts %}
        <div class="post">
            <p>published: {{ post.published_date }}</p>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
    

ในไฟล์ `blog/templates/blog/post_list.html` ด้วยโค้ดนี้:

    html
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
    

บันทึกไฟล์และโหลดหน้าเว็บอีกครั้ง

![รูปที่ 14.4][8]

 [8]: images/final.png

วู้ฮู้ว! ดูดีขึ้นเยอะ ใช่ไหม? โค้ดที่เราเพิ่มไปนั้น ไม่ยากที่จะทำความเข้าใจ และคุณควรเข้าใจโค้ดเหล่านั้นเกือบทั้งหมดเพียงแค่อ่านเท่านั้น

อย่ากลัวที่จะลองแก้ไข CSS เล่นดู ถ้าคุณทำแล้วมันพัง ไม่ต้องกลัวนะ คุณสามารถย้อนกลับโค้ดได้ตลอดเวลา

เราแนะนำให้ลองไปเรียนที่ [Codeacademy HTML & CSS][2] เป็นการบ้านหลังจากตรงนี้ เพื่อเรียนรู้ทุกสิ่งที่คุณต้องการใช้ในการทำเว็บให้สวยขึ้นด้วย CSS

พร้อมสำหรับบทต่อไปหรือยัง?! :)