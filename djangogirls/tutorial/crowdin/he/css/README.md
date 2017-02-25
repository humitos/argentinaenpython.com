# CSS - בואי נעשה את זה יפה!

הבלוג שלנו עדיין נראה די מכוער, לא? הגיע הזמן לגרום לו להראות טוב! בשביל זה, נשתמש ב-CSS.

## מה זה CSS?

CSS (Cascading Style Sheets, או בעברית - גליונות סגנון מדורגים) היא שפה המשמשת לתאר את המראה והעיצוב של אתר הכתוב בשפת markup (כמו HTML). תחשבי על זה כמו על איפור לדף אינטרנט שלנו :)

אבל אנחנו לא רוצים להתחיל מהתחלה שוב, נכון? גם הפעם נשתמש במשהו שכבר נכתב על ידי מתכנתים אחרים והועלה לאינטרנט בחינם. את יודעת, להמציא את הגלגל מחדש זה לא כיף.

## בואי נשתמש ב-Bootstrap!

Bootstrap היא אחת מחבילות ה-HTML ו-CSS הפופולריות ביותר ליצירה של אתרים יפים: http://getbootstrap.com/

היא נכתבה על ידי מתכנתים שעבדו בטוויטר, ועכשיו היא מפותחת ומתוחזקת על ידי מתנדבים מכל העולם.

## התקנת Bootstrap

כדי להתקין Bootstrap, תצטרכי להוסיף בקובץ ה-`.html` שלך, תחת `<head>`, את השורות הבאות (`blog/templates/blog/post_list.html`):

    html
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    

זה לא מוסיף קבצים לפרויקט שלך; זה פשוט מצביע לקבצים קיימים באינטרנט. אז פשוט לכי על זה, תפתחי את הדפדפן שלך, תרענני את העמוד, והנה!

![תמונה 14.1][1]

 [1]: images/bootstrap1.png

זה כבר נראה טוב יותר!

## קבצים סטטיים ב Django

סוף-סוף אנחנו יכולים להתעמק במה שנקרא **קבצים סטטיים** (או בעברית, קבועים). קבצים סטטיים הם כל קבצי ה-CSS וכל התמונות שלך - כלומר, קבצים שאינם דינאמיים (או בעברית, משתנים), כיוון שהתוכן שלהם אינו תלוי בהקשר, אלא נשאר קבוע לכל משתמש.

### איפה לשים קבצים סטטיים בג'נגו

כמו שראית כשהרצנו את `collectstatic` בשרת, ג'נגו כבר יודע מאיפה להביא את הקבצים הסטטיים עבור אפליקציית ה-admin המובנית. כל מה שנשאר לעשות זה להוסיף קבצים סטטיים גם לאפליקציה שלנו, ה-`blog`.

נעשה זאת על ידי יצירה של קובץ בשם `static` בתיקייה של האפליקציה שלנו:

    djangogirls
    ├── blog
    │   ├── migrations
    │   └── static
    └── mysite
    

ג'נגו ימצא אוטומטית את כל תתי-התיקיות שנקראות static בכל התיקיות של האפליקציות שלנו, ויאפשר להשתמש בתוכן שלהן כמו שהוא, כקבצים סטטיים.

## קובץ ה-CSS הראשון שלך!

בואי נכתוב קובץ CSS, ונוסיף סגנון לעמוד שלך. תייצרי תיקייה חדשה בשם `css` בתוך תיקייה ה-`static` שלך. עכשיו, תייצרי קובץ חדש בשם `blog.css` בתוך תיקיית ה-`css`. Ready?

    djangogirls
    └─── blog
         └─── static
              └─── css
                   └─── blog.css
    

הגיע הזמן לכתוב קצת CSS! תפתחי את הקובץ `blog/static/css/blog.css` בעורך הקוד שלך.

אנחנו לא הולכים להכנס עמוק מדי לתוך כל הפרטים והדקויות של CSS, כיוון שזה די פשוט ותוכלי להשלים את זה בעצמך אחרי הסדנה. אנחנו ממליצות לעשות את הקורס [CodeAcademy HTML & CSS][2] כדי ללמוד את כל מה שיש לדעת על איך לכתוב אתרים יפים עם CSS.

 [2]: http://www.codecademy.com/tracks/web

אבל בואי נלמד לפחות קצת. אולי נשנה את צבע הכותרות? כדי להבין צבעים, מחשבים משתמשים בקידודים מיוחדים. הם מתחילים ב-`#` (סולמית) וממשיכים ב-6 תוים, שיכולים להיות האותיות A-F או הספרות 0-9. את יכולה למצוא קידודי צבע לדוגמה כאן: http://www.colorpicker.com/. את גם יכולה להשתמש ב[צבעים מוגדרים מראש][3] עם שמות ידועים, כמו `red` ו-`green`.

 [3]: http://www.w3schools.com/cssref/css_colornames.asp

בקובץ `blog/static/css/blog.css` שלך, הוסיפי את השורות הבאות:

    css
    h1 a {
        color: #FCA205;
    }
    

`h1` הוא מה שנקרא CSS Selector (או בעברית, בורר CSS). זה אומר שאנחנו מחילים את העיצוב שלנו על כל תגית `a` שנמצאת בתוך תגית `h1` (למשל, אם יש לנו בקוד משהו כמו `<h1><a href="">link</a></h1>`). במקרה כזה, אנחנו קובעים שצבע הטקסט יהיה `#FCA205`, שזה כתום. כמובן שאת יכולה לבחור כאן איזה צבע שמוצא-חן בעיניך!

בקובץ ה-CSS אנחנו בוחרים עיצוב לתגיות המופיעות בקובץ ה-HTML. אנו יכולים לברור תגיות לפי שמן (למשל, `a`, `h1`, או `body`), או לפי המאפיין `class` והמאפיין `id`. המאפיינים class ו-id מוסיפים לתגיות שלך שמות שאת בוחרת בעצמך. מאפייני class מגדירים קבוצות (מחלקות) של תגיות, ומאפייני id מייחדים תגיות מסוימות. לדוגמה, התגית הבאה יכולה להיברר ב-CSS על ישי שם התגית `a`, על ידי מאפיין ה-class `external_link`, או על ידי מאפיין ה-id `link_to_wiki_page`:

    html
    <a href="http://en.wikipedia.org/wiki/Django" class="external_link" id="link_to_wiki_page">
    

קראי עוד על CSS ב- [CSS Selectors in w3schools][4].

 [4]: http://www.w3schools.com/cssref/css_selectors.asp

עכשיו, נשאר רק להגיד לתבנית ה-HTML שלנו להוסיף קצת CSS. תפתחי את הקובץ `blog/templates/blog/post_list.html` ותוסיפי את השורה הבאה ממש בהתחלה שלו:

    html
    {% load staticfiles %}
    

אנחנו רק מוסיפות קבצים סטטיים פה :). עכשיו, בין ה-`<head>` וה-`</head>`, אחרי התגיות המוסיפות את קבצי ה-CSS של Bootstrap (הדפדפן טוען את הגדרות העיצוב מהקבצים בסדר בו הם מופיעים, אז ההגדרות בקובץ שלך יכולות לדרוס את ההגדרות בקבצים של Bootstrap), תוסיפי את השורה הבאה:

    html
    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    

הרגע גילינו לתבנית שלנו איפה נמצא קובץ ה-CSS שלנו.

בשלב הזה, הקובץ שלך צריך להיראות בערך כך:

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
    

אחלה, תשמרי את הקובץ ותרענני את העמוד!

![תמונה 14.2][5]

 [5]: images/color2.png

עבודה טובה! אולי עכשיו נוסיף לאתר שלנו קצת אוויר, ונגדיל את הרווח מצד שמאל? בואי ננסה!

    css
    body {
        padding-left: 15px;
    }
    

תוסיפי את זה ל-CSS שלך, תשמרי את הקובץ ובואי נבדוק איך זה נראה!

![תמונה 14.3][6]

 [6]: images/margin2.png

אולי אנחנו יכולים לשנות קצת את הגופן בכותרות שלנו? תעתיקי לתוך ה-`<head>` של קובץ ה-0>blog/templates/blog/post_list.html</code> שלך את השורות הבאות:

    html
    <link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
    

השורה הזאת תייבא קובץ שנקרא *Lobster* מ-Google Fonts (https://www.google.com/fonts).

עכשיו תוסיפי את השורה `font-family: 'Lobster';` בקובץ ה-CSS שלך ב-`blog/static/css/blog.css`, בתוך ההגדרות של ה`h1 a` (הקוד בין הסוגריים המסולסלים `{` ו-`}`), ותרענני את העמוד:

    css
    h1 a {
        color: #FCA205;
        font-family: 'Lobster';
    }
    

![תמונה 14.3][7]

 [7]: images/font.png

מגניב!

כמו שהזכרנו למעלה, ב-CSS יש את הרעיון הזה של מחלקות, שבגדול מאפשר לך לתת שם לחתיכת קוד HTML ולהחיל עליה עיצוב מסוים מבלי להשפיע על חלקים אחרים. זה ממש שימושי אם יש לך, למשל, שני divים, אבל הם משמשים למשהו שונה בתכלית (למשל, אחד לכותרת ואחד לגוף ההודעה), אז את לא רוצה שהם יראו אותו דבר.

יאללה, נסי לתת שמות לחתיכות קוד HTML. הוסיפי מאפיין class עם הערך `page-header` ל-`div` שמכיל את הכותרת שלך, ככה:

    html
    <div class="page-header">
        <h1><a href="/">Django Girls Blog</a></h1>
    </div>
    

ועכשיו תוסיפי מאפיין class בשם `post` ל-`div` שלך שמכיל את גוף ההודעה.

    html
    <div class="post">
        <p>published: {{ post.published_date }}</p>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
    

עכשיו נוסיף עיצוב למחלקות השונות שהגדרנו. סלקטורים המתחילים ב-`.` (נקודה) מתאימים למאפייני class. יש מלא הסברים מעולים על CSS באינטרנט כדי לעזור לך להבין את הקוד בהמשך. בינתיים, פשוט תעתיקי ותדביקי אותו בקובץ ה-`blog/static/css/blog.css` שלך:

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
    

ואז תוסיפי את מאפייני ה-class לקוד ה-HTML שלך, שמציג את הפוסטים בבלוג. תחליפי את זה:

    html
    {% for post in posts %}
        <div class="post">
            <p>published: {{ post.published_date }}</p>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
    

בקובץ ה-`blog/templates/blog/post_list.html` שלך בזה:

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
    

תשמרי את הקבצים ותרענני את העמוד.

![תמונה 14.4][8]

 [8]: images/final.png

יש! נראה טוב, לא? הקוד שהעתקנו לפני רגע לא כזה מסובך, ואת אמורה להבין את רובו רק מלקרוא אותו.

אל תחששי לשחק קצת עם ה-CSS ולנסות לשנות כל מני דברים. אם תשברי משהו, אל תדאגי, אפשר פשוט להחזיר אותו למה שהיה!

בכל מקרה, אנחנו ממש ממליצות על הקורס החינמי [Codeacademy HTML & CSS course][2] בתור מעין שיעורי-בית לאחרי הסדנה, כדי ללמוד כל מה שיש על איך להפוך את האתרים שלך ליפים יותר עם CSS.

מוכנה לפרק הבא?! :)