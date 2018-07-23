# Views - hora de criar!

É hora de resolver o bug que criamos no capítulo anterior :)

Uma *view* é colocada onde nós colocamos a "lógica" da nossa aplicação. Ela vai extrair informações do `model` que você criou e entregá-las a um `template`. Nós vamos criar um template no próximo capítulo. Views são somente funções Python que são um pouco mais complicadas do que aquelas que criamos no capítulo **Introdução ao Python**.

As views são postas no arquivo `views.py`. Nós vamos adicionar nossas *views* no arquivo `blog/views.py`.

## blog/views.py

OK, vamos abrir o arquivo e ver o que tem nele:

    python
    from django.shortcuts import render
    
    # Create your views here.
    

Não tem muita coisa. A *view* mais básica se parece com isto.

    python
    def post_list(request):
        return render(request, 'blog/post_list.html', {})
    

Como você pode ver, nós criamos um método (`def`) chamado `post_list` que aceita o `pedido` e `retornar` um método `render` será processado (para montar) nosso modelo `blog/post_list.html`.

Agora salve o arquivo, abra a página http://127.0.0.1:8000/ e veja o que temos.

Outro erro! Leia o que está acontecendo agora:

![Erro][1]

 [1]: images/error.png

Esta é fácil: *TemplateDoesNotExist*. Vamos corrigir este bug e criar um modelo no próximo capítulo!

> Aprenda mais sobre as views do Django lendo a documentação oficial: https://docs.djangoproject.com/en/1.6/topics/http/views/