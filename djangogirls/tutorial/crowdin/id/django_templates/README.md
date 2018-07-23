# Django templates

Saatnya menampilkan data! Django menyediakan fitur bawaan berupa **template tags** untuk keperluan tersebut.

## Apa itu template tags?

Seperti yang kita tau, kita tidak bisa menyertakan kode Python ke dalam HTML, karena tidak dapat dimengerti oleh browser. Dikarenakan HTML itu bersifat statis, sedangkan kode Python bersifat dinamis.

**Django template tags** memungkinkan kita menyertakan kode seperti Python ke dalam HTML, sehingga kita dapat membangun website yang dinamis dengan lebih cepat dan mudah. Yeay!

## Menampilkan template post list

Di pembahasan sebelumnya kita menyediakan post list ke dalam variabel `posts`.

Untuk mencetak variabel ke dalam Django templates, kita menggunakan dua buah karakter kurung kurawal denga nama variable di dalamnya, seperti ini:

    html
    {{ posts }}
    

Terapkan ke template `blog/templates/blog/post_list.html`. Ubah semua dari `<div>` kedua sampai dengan `</div>` ketiga ganti dengan `{{ posts }}`. Simpan file, dan refresh halaman untuk melihat hasil perubahan:

![Figure 13.1][1]

 [1]: images/step1.png

Seperti yang bisa kita lihat, tercetak seperti berikut:

    [<Post: My second post>, <Post: My first post>]
    

Yang berarti Django dapat mengenalinya sebagai list objek. Ingat pembahasan dari **Introduction to Python** bagaimana kita menampilkan list? Ya, dengan loop! Di Django template, kita menerapkannya seperti ini:

    html
    {% for post in posts %}
        {{ post }}
    {% endfor %}
    

Cobalah terapkan di template.

![Figure 13.2][2]

 [2]: images/step2.png

It works! But we want them to be displayed like the static posts we created earlier in the **Introduction to HTML** chapter. You can mix HTML and template tags. Our `body` will look like this:

    html
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
    

{% raw %}Everything you put between `{% for %}` and `{% endfor %}` will be repeated for each object in the list. Refresh your page:{% endraw %}

![Figure 13.3][3]

 [3]: images/step3.png

Have you noticed that we used a slightly different notation this time `{{ post.title }}` or `{{ post.text }}`? We are accessing data in each of the fields defined in our `Post` model. Also the `|linebreaks` is piping the posts' text through a filter to convert line-breaks into paragraphs.

## One more thing

It'd be good to see if your website will still be working on the public Internet, right? Let's try deploying to PythonAnywhere again. Here's a recap of the steps...

*   First, push your code to Github

    $ git status
    [...]
    $ git add -A .
    $ git status
    [...]
    $ git commit -m "Modified templates to display posts from database."
    [...]
    $ git push
    

*   Then, log back in to [PythonAnywhere][4] and go to your **Bash console** (or start a new one), and run:

 [4]: https://www.pythonanywhere.com/consoles/

    $ cd my-first-blog
    $ git pull
    [...]
    

*   Finally, hop on over to the [Web tab][5] and hit **Reload** on your web app. Your update should be live!

 [5]: https://www.pythonanywhere.com/web_app_setup/

Congrats! Now go ahead and try adding a new post in your Django admin (remember to add published_date!), then refresh your page to see if the post appears there.

Works like a charm? We're proud! Step away from your computer for a bit, you have earned a break. :)

![Figure 13.4][6]

 [6]: images/donut.png