# Modelos do Django

Agora o que queremos criar é algo que armazene todos os posts em nosso blog. Mas para podermos fazer isto temos que falar um pouco sobre coisas chamadas `objects`.

## Objetos

Existe um conceito na programação chamado `Programação Orientada à Objetos (POO)`. A ideia é que ao invés de escrever tudo como uma chata sequência de instruções de programação podemos modelar as coisas e definir como elas interagem umas com as outras.

Então o que é um objeto? É uma coleção de propriedades e ações. Isto pode parecer estranho, mas vamos lhe dar um exemplo.

Se queremos modelar um gato, vamos criar um objeto `Gato` que tem algumas propriedades, tais como: `cor`, `idade`, `humor` (ou seja, bom, mau, dorminhoco ;)), e o `proprietário` (que é um objeto `Pessoa` ou talvez, em caso de um gato de rua, esta propriedade é vazia).

E então o `Gato` tem algumas ações: `ronronar`, `arranhar` ou `alimentar` (no qual vamos dar ao gato alguma `ComidaDeGato `, que poderia ser um objeto separado com propriedades, como `sabor`).

    Gato
    --------
    cor
    idade
    humor
    dono
    ronronar()
    arranhar()
    alimentar(comida_de_gato)
    
    
    ComidaDeGato
    --------
    sabor
    

Então, basicamente, a ideia é descrever coisas reais no código com propriedades(chamadas de `propriedades do objeto`) e ações (chamadas de `métodos`).

Como nós iremos modelar as postagens do blog então? Queremos construir um blog, certo?

Nós precisamos responder as questões: O que é um post de blog? Que propriedades ele deve ter?

Bem, com certeza nosso blog precisa de alguma postagem com o seu conteúdo e um título, certo? Também seria bom saber quem a escreveu - então precisamos de um autor. Finalmente, queremos saber quando a postagem foi criada e publicada.

    Post
    --------
    title
    text
    author
    created_date
    published_date
    

Que tipo de coisa pode ser feita com uma postagem? Seria legal ter algum `método` que publique a postagem, não é mesmo?

Então, nós precisaremos de um método `publicar (publish)`.

Como nós já sabemos o que queremos alcançar, vamos começar a modelá-lo no Django!

## Modelo do Django

Sabendo o que um objeto é, nós criaremos um modelo no Django para a postagem do blog.

Um modelo no Django é um tipo especial de objeto - ele é salvo em um `banco de dados`. Um banco de dados é uma coleção de dados. O banco de dados é um local em que você vai salvar dados sobre usuários, suas postagens, etc. Usaremos um banco de dados chamado SQLite para armazenar as nossas informações. Este é o adaptador de banco de dados padrão Django -- ele vai ser o suficiente para nós neste momento.

Você pode pensar em um modelo de banco de dados como uma planilha com colunas (campos) e linhas (dados).

### Criando uma aplicação

Para manter tudo arrumado vamos criar um aplicativo separado dentro do nosso projeto. É muito bom ter tudo organizado desde o início. Para criar um aplicativo precisamos executar o seguinte comando no console (a partir do diretório `djangogirls` onde está o arquivo `manage.py`):

    (myvenv) ~/djangogirls$ python manage.py startapp blog
    

Você vai notar que um novo diretório `blog` é criado e que ele agora contém um número de arquivos. Nossos diretórios e arquivos no nosso projeto devem se parecer com este:

    djangogirls
    ├── mysite
    |       __init__.py
    |       settings.py
    |       urls.py
    |       wsgi.py
    ├── manage.py
    └── blog
        ├── migrations
        |       __init__.py
        ├── __init__.py
        ├── admin.py
        ├── models.py
        ├── tests.py
        └── views.py
    

Depois de criar um aplicativo também precisamos dizer ao Django que deve usá-lo. Fazemos isso no arquivo `mysite/settings.py`. Precisamos encontrar o `INSTALLED_APPS` e adicionar uma linha com `'blog',` logo acima do `)`. É assim que o produto final deve ficar assim:

    python
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog',
    )
    

### Criando o modelo Post do nosso blog

No arquivo `blog/models.py` definimos todos os objetos chamados `Modelos` - este é um lugar em que vamos definir nossa postagem do blog.

Vamos abrir `blog/models.py`, remova tudo dele e escreva o código como este:

    python
    from django.db import models
    from django.utils import timezone
    
    
    class Post(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)
    
        def publish(self):
            self.published_date = timezone.now()
            self.save()
    
        def __str__(self):
            return self.title
    

> Verifique que você usou dois caracteres de sublinhado (`_`) em cada lado de `str`. Esta convenção é utilizada frequentemente em Python e, muitas vezes, chamamos de "dunder" (redução de "double-underscore").

Parece assustador, certo? Mas não se preocupe, iremos explicar o que essas linhas significam!

Todas as linhas começando com `from` ou `import` são linhas que adicionam alguns pedaços de outros arquivos. Então ao invés de copiar e colar as mesmas coisas em cada arquivo, podemos incluir algumas partes com `from... import ...`.

`class Post(models.Model):` - esta linha define o nosso modelo (é um `objeto`).

*   `class` é uma palavra-chave especial que indica que estamos definindo um objeto.
*   `Post` é o nome do nosso modelo. Nós podemos dar um nome diferente (mas precisamos evitar caracteres especiais e espaços em branco). Sempre inicie o nome de uma classe com uma letra em maiúsculo.
*   `models.Model` significa que o Post é um modelo de Django, então o Django sabe ele que deve ser salvo no banco de dados.

Agora definimos as propriedades que comentamos: `title`, `text`, `created_date`, `published_date` e `author`. Para fazermos isso, nós precisamos definir um tipo para cada campo (É um texto? É um número? Uma data? Uma relação com outro objeto, por exemplo, um usuário?).

*   `models.CharField` - assim é como você define um texto com um número limitado de caracteres.
*   `models.TextField` - este é para textos sem um limite. Parece ideal para o conteúdo de um blog, certo?
*   `models.DateTimeField` - este é uma data e hora.
*   `models.ForeignKey` - este é um link para outro modelo.

Nós não explicaremos cada pedaço de código aqui pois isso levaria muito tempo. Você deve dar uma olhada na documentação do Django se você quiser saber mais sobre campos de modelos e como definir outras coisas além das descritas acima (https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types).

Que tal `def publish(self):`? É exatamente o método `publish` que falamos anteriormente. `def` significa que é uma função/método e `publish` é seu nome. Você pode mudar o nome do método, se quiser. A regra para nomeação é que usamos letras minúsculas e sublinhados ao invés de espaços em branco. Por exemplo, um método que calcula o preço médio poderia se chamar `calculate_average_price` (do inglês, calcula_preco_medio).

Métodos muitas vezes retornam (`return`) algo. Há um exemplo de que, no método `__str__`. Nesse cenário, quando chamamos `__str__()` teremos um texto (**string**), com um título do Post.

Se algo ainda não está claro sobre modelos, sinta-se livre para pedir o seu treinador! Nós sabemos que é complicado, especialmente quando se aprende o que objetos e funções são ao mesmo tempo. Mas espero que isto se pareça um pouco menos mágica para você agora!

### Criando tabelas para nossos modelos no banco de dados

O último passo é adicionar nosso novo modelo para nosso banco de dados. Primeiro, precisamos fazer que o Django entenda que fizemos algumas alterações no nosso modelo (nós recém criamos ele!). Digite `python manage.py makemigrations blog`. Será algo parecido com isto:

    (myvenv) ~/djangogirls$ python manage.py makemigrations blog
    Migrations for 'blog':
      0001_initial.py:
      - Create model Post
    

O Django preparou para nós um arquivo de migração que nós precisamos aplicar no nosso banco de dados. Digite `python manage.py migrate blog` e a saída deverá ser:

    (myvenv) ~/djangogirls$ python manage.py migrate blog
    Operations to perform:
      Apply all migrations: blog
    Running migrations:
      Rendering model states... DONE
      Applying blog.0001_initial... OK
    

Uhul! Nosso modelo Post está agora no nosso banco de dados! Seria legal vê-lo, né? Vá para o próximo capítulo para ver como nosso Post se parece!