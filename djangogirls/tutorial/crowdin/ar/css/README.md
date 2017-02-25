# إجعلة جميلا بإستخدام CSS!

مدونتنا لا تزال تبدو قبيحة جداً، أليس كذلك؟ حان الوقت لجعلها جميلة! سوف نستخدم CSS لذلك.

## ما هي CSS؟

CSS هي لغة تجميل المواقع,تخيل HTML هي هيكل المنزل يعني الحائط و السارية و السقف و CSS هي الصباغة و الصقل والديكور... و ما إلى ذلك ,مكياج يعني.

ولكن لا نريد أن نبدأ من الصفر مرة أخرى، أليس كذلك؟ سوف، نستخدم مرة أخرى، ماصنعه المبرمجين من قبل ونشر على شبكة الإنترنت مجاناً. كما تعلمون، إعادة اختراع العجلة ليس ممتعا.

## لنستخدم Bootstrap!

Bootstrap اطار عمل الأكثر شعبية لـ HTML و CSS لتطوير مواقع جميلة: http://getbootstrap.com/

كتب بواسطة المبرمجين الذين عملوا على تويتر والآن يتم تطويره من قبل المتطوعين من جميع أنحاء العالم.

## تثبيت Bootstrap

لتثبيت Bootstrap، تحتاج إلى إضافة هذه إلى `< الرأس >` في ملف `.html` (`blog/templates/blog/post_list.html`):

    html <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"> <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    

هذا لا يضيف أي ملفات إلى المشروع الخاص بك. بل يشير فقط إلى الملفات الموجودة على شبكة الإنترنت. افتح موقع الويب الخاص بك وقم بتحديث الصفحة. لاحظت الفرق!

![Figure 14.1][1]

 [1]: images/bootstrap1.png

يبدو اجمل الان!

## الملفات الثابتة في Django

اخيراً سوف نمعن بالنظر على ما اسميناه **بالملفات الثابتة**. الملفات الثابتة هي كل ملف غير ديناميكي كملفات الصور وCSS. فمحتواها لا يتغير باختلاف المستخدمين او طلباتهم المرسلة, ستعرض كما هي لجميع المستخدمين.

### اين توضع الملفات الثابتة لمشروع Django

كما رأيتم عندما قمنا بتشغيل `collectstatic` في الخاودم, جانغو عرف مسبقا أين يجد الملفات الثابتة للتطبيق المضمن المدير. الأن لايلزمنا سوى اضافة بعض الملفات الثابتة للتطبيق الخاص بنا,`blog`.

نقوم بذلك بانشاء مجلد نسميه `static` داخل تطبيق المدونة:

    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    └── mysite
    

جانغو سيجد تلقائيا أي مجلد باسم "static" داخل اي مجلد يحتويه تطبيقك. وسيستطيع استعمال محتوياته كملفات ثابتة.

## الأن مع ملفات CSS

لنقم بانشاء ملف نمطي CSS. لتظيف تعديلاتك الخاصة لموقعك. قم بانشاء مجلد باسم `css` داخل مجلد `static`. قم بانشاء ملف باسم `blog.css` داخل المجلد `css`. Ready?

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css
    

حان الوقت للقيام بكتابة بعض CSS,قم بفتح الملف `blog/static/css/blog.css` داخل المحرر.

لن نتعمق في التعديل و تعلم CSS, لانها سهلة ويمكنك تعلمها بنفسك بعد الانتهاء من هنا. نزكي لك هذا الموقع لتتعلم كل ما تريد معرفته عن HTML و CSS الرابط https://www.codecademy.com/learn/web

لكن لنقم بالقليل على الاقل. ربما نريد تغيير لون الترويسة؟ لفهم الالوان, الحاسوب يستعمل شيفرات خاصة. الشيفرات تبتدأ ب `#` و تليها 6 حروف (A-F) و أرقام (0-9). يمكنك العثور على هذه الشيفرات في هذا الموقع على سبيل المثال: http://www.colorpicker.com/ يمكنك استعمال الالوان المحددة مسبقا ك `red` و `green`.

داخل الملف `blog/static/css/blog.css` يجب عليك اضافة التعليمات البرمجية التالية:

    css
    h1 a {
        color: #FCA205;
    }
    

`h1 a` هو محدد CSS. ذلك يعني أننا نطبق التغييرات لكل عنصر `a` داخل عنصر `h1`, على سبيل المثال `<h1><a href="">link</a></h1>` في هذه الحالة نأمرها بتغيير الون الى `#FCA205`,وهو اللون البرتقالي. بالطبع تستطيع وضع أي لون تريد!

داخل ملف CSS نحدد أنماط العناصر التي توجد داخل ملف HTML. يتم تحديد العناصر باسم العنصر (أي `a`، `h1`، `body`) أو سمة `class` أو سمة `id`. Class و id هي الأسماء التي يمكنك إعطائها للعنصر بنفسك. تحدد class مجموعات من العناصر، و id تشير إلى عناصر محددة. على سبيل المثال، يمكن تحديد العلامة التالية باستخدام سمة `a`, المصنف `external_link` (class), أو المعرف `link_to_wiki_page` (id):

    html
    <a href="http://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page">
    

اقرأ عن [محددات CSS في w3schools][2].

 [2]: http://www.w3schools.com/cssref/css_selectors.asp

وبعد ذلك، نحن بحاجة إلى أن نقول أيضا لقالب HTML أننا أضفنا بعض ال CSS. افتح الملف `blog/templates/blog/post_list.html` وأضف هذا السطر في البداية:

    html
    {% load staticfiles %}
    

نحمل الملفات الثابتة هنا :). Then, between the `<head>` and `</head>`, after the links to the Bootstrap CSS files (the browser reads the files in the order they're given, so code in our file may override code in Bootstrap files), add this line:

    html
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    

We just told our template where our CSS file is located.

Your file should now look like this:

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
    

OK, save the file and refresh the site!

![Figure 14.2][3]

 [3]: images/color2.png

Nice work! Maybe we would also like to give our website a little air and increase the margin on the left side? Let's try this!

    css
    body {
        padding-left: 15px;
    }
    

Add this to your CSS, save the file and see how it works!

![Figure 14.3][4]

 [4]: images/margin2.png

Maybe we can customize the font in our header? Paste this into your `<head>` in `blog/templates/blog/post_list.html` file:

    html
    <link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
    

This line will import a font called *Lobster* from Google Fonts (https://www.google.com/fonts).

Now add the line `font-family: 'Lobster';` in the CSS file `blog/static/css/blog.css` inside the `h1 a` declaration block (the code between the braces `{` and `}`) and refresh the page:

    css
    h1 a {
        color: #FCA205;
        font-family: 'Lobster';
    }
    

![Figure 14.3][5]

 [5]: images/font.png

Great!

As mentioned above, CSS has a concept of classes, which basically allows you to name a part of the HTML code and apply styles only to this part, not affecting others. It's super helpful if you have two divs, but they're doing something very different (like your header and your post), so you don't want them to look the same.

Go ahead and name some parts of the HTML code. Add a class called `page-header` to your `div` that contains your header, like this:

    html
    <div class="page-header">
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>
    

And now add a class `post` to your `div` containing a blog post.

    html
    <div class="post">
        <p>published: {{ post.published_date }}</p>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
    

We will now add declaration blocks to different selectors. Selectors starting with `.` relate to classes. There are many great tutorials and explanations about CSS on the Web to help you understand the following code. For now, just copy and paste it into your `blog/static/css/blog.css` file:

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
    

Then surround the HTML code which displays the posts with declarations of classes. Replace this:

    html
    {% for post in posts %}
        <div class="post">
            <p>published: {{ post.published_date }}</p>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
    

in the `blog/templates/blog/post_list.html` with this:

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
    

Save those files and refresh your website.

![Figure 14.4][6]

 [6]: images/final.png

Woohoo! Looks awesome, right? The code we just pasted is not really so hard to understand and you should be able to understand most of it just by reading it.

Don't be afraid to tinker with this CSS a little bit and try to change some things. If you break something, don't worry, you can always undo it!

Anyway, we really recommend taking this free online [Codeacademy HTML & CSS course][7] as some post-workshop homework to learn everything you need to know about making your websites prettier with CSS.

 [7]: http://www.codecademy.com/tracks/web

Ready for the next chapter?! :)