# Django ORM และ QuerySets

ในบทนี้ คุณจะได้เรียนรู้การเชื่อต่อ Django กับ ฐานข้อมูล และเก็บข้อมูลลงในนั้น เริ่มกันเลย!

## QuerySet คืออะไร?

QuerySet โดยพื้นฐาน ข้อรายการของวัตถุภายในโมเดล QuerySet ช่วยให้คุณอ่านข้อมูล คัดกรอง และ จัดเรียง จากฐานข้อมูล

ใช้ตัวอย่างจะเห็นภาพกว่า มาลองดูกันเลยไหม?

## Django shell

เปิดคอนโซลบนเครื่องคุณ (ไม่ใช่บน PythonAnywhere) และใช้คำสั่งนี้:

    (myvenv) ~/djangogirls$ python manage.py shell
    

ผลลัพธ์ควรเป็นดังนี้:

    (InteractiveConsole)
    >>>
    

ตอนนี้คุณอยู่ในคอนโซลของ Django มันเหมือนกับคอนโซลของ Python แต่มีเวทมนต์ของ Django เพิ่มเข้ามา :) แน่นอนว่า คุณสามารถใช้ทุกคำสั่งของ Python ในนี้เช่นกัน

### วัตถุทั้งหมด

ลองแสดงผลของทุกโพสต์กัน คุณสามารถทำได้โดยใช้คำสั่งต่อไปนี้:

    >>> Post.objects.all()
    Traceback (most recent call last):
          File "<console>", line 1, in <module>
    NameError: name 'Post' is not defined
    

โอ๊ะโอ! เกิดข้อผิดพลาด มันบอกเราว่า ไม่มี Post ซึ่งถูกแล้ว - เราลืม import เข้ามาก่อน!

    >>> from blog.models import Post
    

ในตัวอย่างนี้: เรา import โมเดล `Post` จาก `blog.models` ลองแสดงโพสต์ทั้งหมดอีกที:

    >>> Post.objects.all()
    [<Post: my post title>, <Post: another post title>]
    

มันคือรายการของโพสต์ที่เราได้สร้างไว้ก่อนหน้านี้! เราสร้างโพสต์เหล่านี้จากหน้า Django admin ตอนนี้ เราต้องการสร้างโพสต์ใหม่โดยใช้ Python แล้วเราจะทำได้อย่างไร?

### สร้างวัตถุ

นี่คือวิธีการสร้างวัตถุโพสต์ใหม่ในฐานข้อมูล:

    >>> Post.objects.create(author=me, title='Sample title', text='Test')
    

แต่เราขาดส่วนผสมไปอย่างนึง: `ตัวเรา` เราต้องการส่งวัตถุในโมเดล `User` เป็นผู้เขียน วิธีทำล่ะ?

นำเข้าโมเดล User ก่อน:

    >>> from django.contrib.auth.models import User
    

เรามีผู้ใช้อยู่ในฐานข้อมูลไหมนะ? ลองนี่:

    >>> User.objects.all()
    [<User: ola>]
    

มี superuser ที่เราได้สร้างไว้ก่อนหน้านี้! เราจะเอามาใช้ทำนู่นนี่ยังไงนะ:

    me = User.objects.get(username='ola')
    

อย่างที่คุณเห็นมันคือการ `get` `User` โดยใช้ `username` ที่ชื่อ 'ola'. สวยงาม! แน่นอนว่าคุณสามารถเปลี่ยนเป็นชื่อคุณได้

ตอนนี้ เราก็สามารถสร้างโพสต์ของเราได้แล้ว:

    >>> Post.objects.create(author=me, title='Sample title', text='Test')
    

ฮูเร้! มาดูกัน ว่ามีอะไรเพิ่มมาบ้าง?

    >>> Post.objects.all()
    [<Post: my post title>, <Post: another post title>, <Post: Sample title>]
    

มีโพสต์มากกว่าหนึ่งอันแล้ว!

### เพิ่มโพสต์

ตอนนี้ คุณสามารถเล่นสนุกได้อีกเล็กน้อย และเพิ่มโพสต์เพิ่มเติมเพื่อศึกษาการทำงานของมัน ลองเพิ่มสัก 2-3 โพสต์ และไปยังส่วนถัดไปได้เลย

### ตัวกรองวัตถุ

ส่วนสำคัญของ QuerySet คือ ความสามารถในการกรองข้อมูล เช่น เราต้องการหาทุกโพสต์ที่ผู้เขียนคือผู้ใช้ชื่อ ola เราจะใช้ `filter` แทน `all` ใน `Post.objects.all()` ในวงเล็บ เราจะระบุเงื่อนไขที่เราต้องการใน queryset ของเรา สำหรับของเรา `author` นั้นคือ `me` วิธีการเขียนใน Django คือ: `author=me` ตอนนี้ ผลลัพธ์จากการกรองจะเป็นดังนี้:

    >>> Post.objects.filter(author=me)
    [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]
    

หรือบางที เราอยากจะได้โพสต์ที่มีคำว่า 'title' อยู่ข้างใน `title`;

    >>> Post.objects.filter(title__contains='title')
    [<Post: Sample title>, <Post: 4th title of post>]
    

> **หมายเหตุ** มีขีดล่างสองอัน (`_`) ระหว่าง `title` และ `contains` Django ORM นั้นใช้รูปแบบนี้ในการ แยกชื่อฟิลด์ ("title") และตัวดำเนินการหรือตัวกรอง ("contains") ถ้าคุณมีขีดล่างแค่อันเดียว คุณจะพบกับข้อผิดพลาด "FieldError: Cannot resolve keyword title_contains"

คุณสามารถดึงโพสต์ที่เผยแพร่ไปแล้ว เราใช้การกรองทุกโพสต์ซึ่งมีค่าของ `published_date` อยู่ข้างใน

> > > from django.utils import timezone Post.objects.filter(published_date__lte=timezone.now()) []

ตอนนี้ โพสต์ของเราจากในคอนโซล Python ยังไม่ได้เผยแพร่ เราสามารถแก้ไขได้! ก่อนอื่น เลือกโพสต์ที่เราต้องการเผยแพร่

    >>> post = Post.objects.get(title="Sample title")
    

จากนั้น เผยแพร่โพสต์โดยใช้ method `publish` ของเรา!

    >>> post.publish()
    

ตอนนี้ลองเรียกดูโพสต์ที่ถูกเผยแพร่แล้วอีกครั้ง (กดลูกศรขึ้น 3 ครั้ง แล้วกด `enter`):

    >>> Post.objects.filter(published_date__lte=timezone.now())
    [<Post: Sample title>]
    

### จัดเรียงวัตถุ

QuerySet ให้คุณสามารถจัดเรียงรายการของวัตถุได้ มาลองเรียงลำดับตาม `created_date` กัน:

    >>> Post.objects.order_by('created_date')
    [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]
    

เรายังสามารถกลับผลการจัดเรียงได้โดยเพิ่ม `-` ไว้ที่ด้านหน้า:

    >>> Post.objects.order_by('-created_date')
    [<Post: 4th title of post>,  <Post: My 3rd post!>, <Post: Post number 2>, <Post: Sample title>]
    

### Chaining QuerySets

นอกจากนี้คุณยังสามารถรวม QuerySet โดยการ **chaining** เข้าไว้ด้วยกัน:

    >>> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    

ตรงนี้มีประโยชน์มากๆ และช่วยให้คุณสร้าง query ที่ซับซ้อนได้

แจ๋ว! คุณพร้อมสำหรับบทถัดไปแล้ว! ปิดคอนโซลโดย:

    >>> exit()
    $