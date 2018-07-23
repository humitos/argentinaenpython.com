# 建立 Django views

是時候來排除我們在上一章節中造成的錯誤 (bug) 了。

*view* 是我們放應用程式的 "邏輯" 的地方。 它將要求你之前建立的 `模型(model)` 提供資訊，並將它傳遞給 `範本(template)`。 在下一章，我們將建立一個範本。 Views 正是 Python 的方法 (methods)，它比我們在 **Python 簡介**一章中提到的較複雜一點點。

Views 都放在 `views.py` 檔中，我們將會新增我們 *views* 到 `blog/views.py` 檔。

## blog/views.py

OK，讓我們打開這個檔，看看裡面有什麼？

    python
    from django.shortcuts import render
    
    # Create your views here.
    

還沒有太多的東西在這裡，最簡單的 *view* 可能像這個樣子。

    python
    def post_list(request):
        return render(request, 'blog/post_list.html', {})
    

正如你所看到的，我們建立一個名為 `post_list` 的方法 (method (`def`))，它接受 `request` 這參數，並`傳回`一個方法 (method) `render`，這方法將呈現（整理出）我們的範本 (template) `blog/post_list.html`。　.

存檔，到 http://127.0.0.1:8000/ 看看我們有什麼。

另一個錯誤！讀看看現在發生什麼：

![錯誤 (Error)][1]

 [1]: images/error.png

這個很簡單：*TemplateDoesNotExist*，讓我們修復這個錯誤，並在下一章中建立一個範本！

> 想了解更多有關於 Django views，可查看官方文件：https://docs.djangoproject.com/en/1.8/topics/http/views/