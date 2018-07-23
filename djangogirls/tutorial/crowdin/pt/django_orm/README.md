# QuerySets e ORM do Django

Neste capítulo você vai aprender como Django se conecta ao banco de dados e como ele armazena dados. Vamos nessa!

## O que é um QuerySet?

Um QuerySet (conjunto de pesquisa), no fundo, é uma lista de objetos de um dado modelo. Um QuerySet permite que você leia os dados do banco, filtre e ordene o mesmo.

É mais fácil aprender por exemplos. Vamos tentar?

## O Shell do Django

Abre o seu terminal (não no PythonAnywhere) e digite o seguinte comando:

    (myvenv) ~/djangogirls$ python manage.py shell
    

O resultado deve ser:

    (InteractiveConsole)
    >>>
    

Agora você está no console interativo do Django. Ele é como o prompt do Python só que com umas mágicas a mais :). Você pode usar todos os comandos do Python aqui também, é claro.

### Todos os objetos

Antes, vamos tentar mostrar todas as nossas postagens. Podemos fazer isso com o seguinte comando:

    >>> Post.objects.all()
    Traceback (most recent call last):
          File "<console>", line 1, in <module>
    NameError: name 'Post' is not defined
    

Oops! Um erro apareceu. Ele nos diz que não existe algo chamado Post. É verdade -- nós esquecemos de importá-lo primeiro!

    >>> from blog.models import Post
    

Isso é simples: importamos o modelo `Post` de dentro do `blog.models`. Vamos tentar mostrar todas as postagens novamente:

    >>> Post.objects.all()
    [<Post: my post title>, <Post: another post title>]
    

É uma lista dos posts que criamos mais cedo! Nós criamos estes posts utilizando a interface do Django admin. Porém, agora nós queremos criar novos posts utilizando Python, então como nós fazemos isso?

### Criando um objeto

É assim que você cria um objeto Post no banco de dados:

    >>> Post.objects.create(author=me, title='Sample title', text='Test')
    

Mas aqui temos um ingrediente que faltava: `me`. Precisamos passar uma instância de `User` modelo como autor. Como fazer isso?

Primeiro vamos importar o modelo User:

    >>> from django.contrib.auth.models import User
    

Quais usuários temos no nosso banco de dados? Experimente isso:

    >>> User.objects.all()
    [<User: ola>]
    

É o superusuário que criamos anteriormente! Vamos obter uma instância de usuário agora:

    me = User.objects.get(username='ola')
    

Como você pode ver, nós agora usamos um `get` a `User` with a `username` igual a 'ola'. Claro, você tem que adaptar a seu nome de usuário.

Agora nós finalmente podemos criar nosso post:

    >>> Post.objects.create(author=me, title='Sample title', text='Test')
    

Viva! Quer ver se funcionou?

    >>> Post.objects.all()
    [<Post: my post title>, <Post: another post title>, <Post: Sample title>]
    

É isso aí, mais um post na lista!

### Adicione mais postagens

Agora você pode se divertir um pouco e adicionar mais postagens para ver como funciona. Adicione mais uns 2 ou 3 posts e siga para a próxima parte.

### Filtrar objetos

Um ponto importante sobre QuerySets é a possibilidade de filtrá-los. Digamos que queremos encontrar todas as postagens escritas pelo usuário ola. Nós usaremos `filter` em vez de `all` em `Post.objects.all()`. Entre parênteses indicamos quais as condições precisam ser atendidas por um post para acabar dentro da nossa queryset. Em nosso caso é `author` que é igual a `me`. A maneira de escrever isso no Django é: `author=me`. Agora o nosso trecho de código parece com este:

    >>> Post.objects.filter(author=me)
    [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]
    

Ou talvez nós queremos ver todos os posts que contenham a palavra 'title' no campo `title`?

    >>> Post.objects.filter(title__contains='title')
    [<Post: Sample title>, <Post: 4th title of post>]
    

> **Nota** Existem dois caracteres de sublinhado (`_`) entre `title` e `contains`. O ORM do Django usa esta sintaxe para separar nomes de campo ("title") e operações ou filtros ("contains"). Se você usar apenas um sublinhado, você obterá um erro como "FieldError: Cannot resolve keyword title_contains".

Você também pode obter uma lista de todos os posts publicados. Fazemos isso filtrando todos os posts com `published_date` definido no passado:

> > > from django.utils import timezone Post.objects.filter(published_date__lte=timezone.now()) []

Infelizmente, o post que nós criamos pelo console do Python não está publicado ainda. Nós podemos mudar isso! Primeiro, busque uma instância do post que queremos publicar:

    >>> post = Post.objects.get(title="Sample title")
    

E então publicá-lo com o nosso método de `publish`!

    >>> post.publish()
    

Agora, busque a lista de posts publicados novamente (aperte a seta para cima 3 vezes e pressione `enter`):

    >>> Post.objects.filter(published_date__lte=timezone.now())
    [<Post: Sample title>]
    

### Ordenando objetos

Um QuerySet também nos permite ordenar a lista de objetos. Vamos tentar ordenar as postagens pelo campo `created_date`:

    >>> Post.objects.order_by('created_date')
    [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]
    

Você também pode inverter a ordem adicionando `-` no início:

    >>> Post.objects.order_by('-created_date')
    [<Post: 4th title of post>,  <Post: My 3rd post!>, <Post: Post number 2>, <Post: Sample title>]
    

### Encadeando QuerySets

Você também pode combinar QuerySets **encadeando** elas:

    >>> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    

Isso é muito poderoso e permite que você crie consultas bastante complexas.

Legal! Você já está pronto para a próxima parte! Para fechar o terminal digite:

    >>> exit()
    $