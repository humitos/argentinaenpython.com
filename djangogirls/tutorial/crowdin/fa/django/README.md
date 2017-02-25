# جنگو چیست؟

جنگو (جَنگو) یک فریم ورک تحت وب رایگان و متن باز است که با زبان پایتون نوشته شده است. یک وب فریم ورک مجموعه ای از اجزا است که به شما کمک می کنند تا یک وب سایت را سریع تر و راحت تر توسعه دهید.

وقتی شما در حال ساخت یک وب سایت هستید،شما همیشه نیاز دارید به مجموعه ای از اجزای مشابه:یک روش برای کنترل کردن احراز هویت کاربر (ثبت نام ، ورود به حساب کاربری ، خروج از حساب کاربری) ، یک پنل مدیریت برای وب سایت خود ، فرم ها ، روشی برای آپلود فایل ها و غیره.

خوشبختانه خیلی وقت پیش ، افرادی متوجه این موضوع شدند که یک توسعه دهنده وب با مشکلات مشابهی روبرو می شود هنگام ساختن یک سایت جدید ، بنابر این آن ها تیم شدند و فریم ورک ها را ساختند(جنگو یکی از آن هاست) که به شما اجزای آماده به کار می دهد که می توانید استفاده کنید.

Frameworks exist to save you from having to reinvent the wheel and help alleviate some of the overhead when you’re building a new site.

## چرا شما به یک فریم ورک نیاز دارید؟

To understand what Django actually is for, we need to take a closer look at the servers. The first thing is that the server needs to know that you want it to serve you a webpage.

Imagine a mailbox (port) which is monitored for incoming letters (requests). This is done by a web server. The web server reads the letter, and sends a response with a webpage. But when you want to send something, you need to have some content. And Django is something that helps you create the content.

## وقتی کسی یک وب سایت را از سرور شما درخواست می کند ، چه اتفاقی می افتد؟

When a request comes to a web server it's passed to Django which tries to figure out what actually is requested. It takes a webpage address first and tries to figure out what to do. This part is done by Django's **urlresolver** (note that a website address is called a URL - Uniform Resource Locator - so the name *urlresolver* makes sense). It is not very smart - it takes a list of patterns and tries to match the URL. Django checks patterns from top to the bottom and if something is matched then Django passes the request to the associated function (which is called *view*).

Imagine a mail carrier with a letter. She is walking down the street and checks each house number against the one on the letter. If it matches, she puts the letter there. This is how the urlresolver works!

In the *view* function all the interesting things are done: we can look at a database to look for some information. Maybe the user asked to change something in the data? Like a letter saying "Please change the description of my job." The *view* can check if you are allowed to do that, then update the job description for you and send back a message: "Done!". Then the *view* generates a response and Django can send it to the user's web browser.

Of course, the description above is a little bit simplified, but you don't need to know all the technical things yet. Having a general idea is enough.

So instead of diving too much into details, we will simply start creating something with Django and we will learn all the important parts along the way!