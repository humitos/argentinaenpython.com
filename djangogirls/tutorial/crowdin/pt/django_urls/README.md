# Urls

Estamos prestes a construir nossa primeira página Web: uma página inicial para o seu blog! Mas primeiro, vamos aprender um pouco mais sobre Django URLs.

## O que é uma URL?

Uma URL é simplesmente um endereço da web. Você pode ver uma URL toda vez que você visita um website - é visível na barra de endereços do seu browser (sim! `127.0.0.1:8000` é uma URL! E `https://djangogirls.com` também é uma URL):

![URL][1]

 [1]: images/url.png

Cada página na Internet precisa de sua própria URL. Desta forma seu aplicativo sabe o que deve mostrar a um usuário que abre uma URL. Em Django, usamos algo chamado `URLconf` (configuração de URL). URLconf é um conjunto de padrões que o Django vai tentar coincidir com a URL recebida para encontrar a visão correta.

## Como funcionam as URLs em Django?

Vamos abrir o arquivo `mysite/urls.py` no seu editor de código preferido e ver o que aparece:

    python
    from django.conf.urls import include, url
    from django.contrib import admin
    
    urlpatterns = [
        # Exemplos:
        # url(r'^$', 'mysite.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),
    
        url(r'^admin/', include(admin.site.urls)),
    ]
    

Como você pode ver, o Django já colocou alguma coisa lá pra nós.

As linhas que começam com `#` são comentários - isso significa que essas linhas não serão executadas pelo Python. Muito útil, não?

A URL do admin, que você visitou no capítulo anterior já está aqui:

    python
        url(r'^admin/', include(admin.site.urls)),
    

Isso significa que para cada URL que começa com `admin /` o Django irá encontrar um correspondente *modo de exibição*. Neste caso nós estamos incluindo um monte de admin URLs para que isso não fique tudo embalado neste pequeno arquivo..--é mais legível e mais limpo.

## Regex

Você quer saber como o Django coincide com URLs para views? Bem, esta parte é complicada. O Django usa `regex`, contração de "regular expressions", que significa "expressões regulares", do Inglês. Regex tem muito (muito!) de normas que formam um padrão de pesquisa. Como expressões regulares são um tópico mais avançado, não veremos em detalhes como elas funcionam.

Se você ainda quiser entender como criamos os padrões, aqui está um exemplo do processo - só precisamos um subconjunto limitado de regras para expressar o padrão que procuramos, ou seja:

    ^ para o início do texto
    $ para o final do texto 
    \d para um dígito 
    + para indicar que o item anterior deve ser repetido pelo menos uma vez 
    () para capturar parte do padrão
    

Qualquer outra coisa na definição de uma URL será levada literalmente.

Agora imagine que você tem um site com o endereço assim: `http://www.mysite.com/post/12345/`, onde `12345` é o número do seu post.

Escrever views separadas para todos os números de post seria muito chato. Com expressões regulares podemos criar um padrão que irá coincidir com a url e extrair o número para nós: `^ post/(\d+) / $`. Vamos aos poucos ver o que estamos fazendo aqui:

*   **^ post /** está dizendo ao Django para pegar tudo que tenha `post /` no início da url (logo após o `^`)
*   **(\d+)** significa que haverá um número (um ou mais dígitos) e que queremos o número capturado e extraído
*   **/** diz para o Django que deve seguir outro `/`
*   **$** indica o final da URL significando que apenas sequências terminando com o `/` irão corresponder a esse padrão

## Sua primeira url Django!

É hora de criar nossa primeira URL! Queremos http://127.0.0.1:8000 / para ser uma página inicial do nosso blog e exibir uma lista de posts.

Também queremos manter o arquivo de `mysite/urls.py` limpo, aí nós importaremosurls da nossa aplicação `blog` para o arquivo principal `mysite/urls.py`.

Vá em frente, apague as linhas comentadas (as linhas que começam com `#`) e adicione uma linha que vai importar `blog.urls` para a url principal (`''`).

O seu arquivo `mysite/urls.py` deve agora se parecer com isto:

    python
    from django.conf.urls import include, url
    from django.contrib import admin
    
    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'', include('blog.urls')),
    ]
    

O Django agora irá redirecionar tudo o que entra em 'http://127.0.0.1:8000 /'para `blog.urls` e procurar por novas instruções lá.

Sempre escrevemos expressões regulares em Python com um `r` na frente da string. Essa é uma dica para o Python que a string pode conter caracteres especiais que não possuem significado para o interpretador Python, mas sim para a expressão regular.

## blog.urls

Crie um novo arquivo vazio `blog/urls.py`. Tudo bem! Adicione estas duas primeiras linhas:

    python
    from django.conf.urls import url
    from . import views
    

Aqui nós estamos apenas importando métodos do Django e todos os nossos `views` do aplicativo `blog` (ainda não temos nenhuma, mas teremos em um minuto!)

Depois disso nós podemos adicionar nosso primeira URL padrão:

    python
    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
    ]
    

Como você pode ver, estamos agora atribuindo uma `view` chamada `post_list` para a URL `^ $`. Essa expressão regular corresponderá a `^` (um começo) seguido por `$` (fim) - então somente uma seqüência vazia irá corresponder. Está correto, porque no Django 'http://127.0.0.1:8000/' não faz parte da URL. Essa expressão diz algo Django que `views.post_list` é o que deve ser chamado quando alguém acessar seu website pelo endereço 'http://127.0.0.1:8000/'.

A última parte, `name='post_list'`, é o nome da URL que será usado para identificar a view. Este nome pode ser o mesmo nome da view, mas também pode ser algo completamente diferente. Nós vamos usar URLs nomeadas mais à frente, então é importante nomearmos agora todas as URLs de nossa aplicação. Também devemos fazer com que os nomes das URLs sejam únicos e fáceis de lembrar.

Tudo certo? Abra http://127.0.0.1:8000/ no seu navegador pra ver o resultado.

![Erro][2]

 [2]: images/error1.png

Não existe um "It Works!' mais, ein? Não se preocupe, é só uma página de erro, nada a temer! Elas são na verdade muito úteis:

Você pode ler que existe um **no attribute 'post_list'**. O *post_list* te lembra alguma coisa? Esse é o nome que demos à view! Isso significa que tudo está correto porém nós ainda não criamos nossa *view*. Não se preocupe, nós chegaremos lá.

> Se você quer saber mais sobre a configuração de URLs no Django, veja a documentação oficial: https://docs.djangoproject.com/en/1.8/topics/http/urls/