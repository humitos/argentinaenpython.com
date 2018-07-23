# Deploy!

> **Nota** O capítulo seguinte pode ser às vezes um pouco difícil de terminar. Persista e termine-o; Deploy é uma parte importante do processo de desenvolvimento de website. Colocar o seu site no ar é um pouco mais complicado, então esse capítulo está no meio do tutorial para que seu treinador possa lhe ajudar nessa tarefa. Isto significa que você ainda pode terminar o tutorial por conta própria se você continuar em outro momento.

Até agora nosso site só estava disponível no seu computador, agora você vai aprender como publicar ele na internet! O deploy é o processo de publicação do seu aplicativo na Internet de tal forma que as pessoas possam, finalmente, ver seu aplicativo :).

Como você aprendeu, um website precisa estar localizado num servidor. Existem muitos provedores deste serviço disponíveis na internet. Nós usaremos um que tem um processo relativamente simples de deploy: o [PythonAnyWhere][1]. O PythonAnyWhere é grátis para pequenas aplicações que não possuem muitos visitantes, então com certeza ele será suficiente pra você por enquanto.

 [1]: http://pythonanywhere.com/

O outro serviço externo que usaremos é [GitHub][2], que é um serviço de hospedagem de código. Existem outros, mas quase todos os programadores possuem uma conta no GitHub atualmente e agora você também!

 [2]: http://www.github.com

Usaremos o GitHub como um trampolim para transportar nosso código para o PythinAnywhere.

# Git

O Git é um "sistema de controle de versão" usado por muitos programadores. Este software pode rastrear mudanças nos arquivos ao longo do tempo para que você possa recuperar versões específicas mais tarde. Um pouco parecido com o recurso "rastrear alterações" do Microsoft Word, mais muito mais poderoso.

## Instalando o Git

> **Nota** Se você já fez os passos de instalação, não precisa fazer isso novamente - você pode pular para a próxima seção e comece a criar seu repositório Git.

{% include "deploy/install_git.md" %}

## Começando nosso repositório no Git

O Git controla as alterações para um determinado conjunto de arquivos no que chamamos de repositório de código (ou "repo"). Vamos começar um para nosso projeto. Abra o console e execute esses comandos, no diretório `djangogirls`:

> **Nota**: Verifique o seu diretório de trabalho atual com um `pwd` (OSX/Linux) ou o comando `cd` (Windows) antes de inicializar o repositório. Você deve estar na pasta `djangogirls`.

    $ git init
    Initialized empty Git repository in ~/djangogirls/.git/
    $ git config --global user.name "Seu Nome"
    $ git config --global user.email voce@exemplo.com
    

Inicializar o repositório git é algo que só precisamos fazer uma vez por projeto (e você não terá que redigitar o nome de usuário e e-mail nunca mais).

Git irá controlar as alterações para todos os arquivos e pastas neste diretório, mas existem alguns arquivos que queremos ignorar. Fazemos isso através da criação de um arquivo chamado `.gitignore` no diretório base. Abra seu editor e crie um novo arquivo com o seguinte conteúdo:

    *.pyc
    __pycache__
    myvenv
    db.sqlite3
    .DS_Store
    

E salve como `.gitignore` na pasta de nível superior "djangogirls".

> **Nota** O ponto no início do nome do arquivo é importante! Se você está tendo alguma dificuldade em criá-lo (Macs não gostam de criar arquivos que começam com um ponto através do Finder, por exemplo), use o recurso "Salvar Como" no seu editor que sempre funciona.

É uma boa idéia usar um comando `git status` antes de `git add` ou sempre que você não tiver certeza do que mudou. Isto vai ajudar a impedir qualquer surpresa, como arquivos errados sendo adicionados ou commitados. O comando `git status` retorna informações sobre todos os arquivos não-rastreados/modificados/indexados, status do branch (ramo) e muito mais. O output deve ser semelhante a:

    $ git status
    On branch master
    
    Initial commit
    
    Untracked files:
      (use "git add <file>..." to include in what will be committed)
    
            .gitignore
            blog/
            manage.py
            mysite/
    
    nothing added to commit but untracked files present (use "git add" to track)
    

E finalmente nós salvamos nossas alterações. Vá para o seu console e execute estes comandos:

    $ git add -A .
    $ git commit -m "Meu Django Girls app, primeiro commit"
     [...]
     13 files changed, 200 insertions(+)
     create mode 100644 .gitignore
     [...]
     create mode 100644 mysite/wsgi.py
    

## Subindo o nosso código para o GitHub

Vá para o [GitHub.com][2] e crie uma nova conta de usuário gratuita. (Se você já fez isto na preparação do workshop, parabéns!)

Em seguida, crie um novo repositório, e dê o nome "my-first-blog". Deixe o "initialise with a README" desmarcado, deixe a opção .gitignore em branco (já fizemos isso manualmente) e a licença como None.

![][3]

 [3]: images/new_github_repo.png

> **Nota** O nome `my-first-blog` é importante --você poderia escolher outro nome, mas vamos usá-lo muitas vezes nas instruções abaixo e você teria que substituí-lo cada vez. É provavelmente mais fácil ficar com o nome `my-first-blog`.

Na tela seguinte, você será mostrada à URL de clone do seu repo. Escolha a versão "HTTPS", copie, e vamos colá-lo no terminal em breve:

![][4]

 [4]: images/github_get_repo_url_screenshot.png

Agora precisamos associar o repositório Git no seu computador com o no GitHub.

Digite o seguinte no seu terminal (Substitua `<your-github-username>` pelo nome de usuário que você escolheu quando criou sua conta no GitHub, mas sem os símbolos de maior e menor):

    $ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
    $ git push -u origin master
    

Entre com o nome de usuário e a senha do GitHub e então você deverá ver algo parecido com isso:

    Username for 'https://github.com': hjwp
    Password for 'https://hjwp@github.com':
    Counting objects: 6, done.
    Writing objects: 100% (6/6), 200 bytes | 0 bytes/s, done.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/hjwp/my-first-blog.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.
    

<!--TODO: maybe do ssh keys installs in install party, and point ppl who dont have it to an extention -->

Seu código agora está no GitHub. Vá e confira! Você saberá que está em boa companhia - [Django][5], o [Django Girls Tutorial][6] e muitos outros grandes projetos de software de código aberto também hospedam seu código no GitHub :)

 [5]: https://github.com/django/django
 [6]: https://github.com/DjangoGirls/tutorial

# Criação de nosso blog no PythonAnywhere

> **Nota** Pode ser que você já tenha criado uma conta no PythonAnyWhere antes - se você já fez, então não precisa fazer de novo.

{% include "deploy/signup_pythonanywhere.md" %}

## Colocando nosso código no PythonAnywhere

Quando você se inscreve para PythonAnywhere, você é levado ao seu painel de controle ou página "Consoles". Escolha a opção para iniciar um terminal Bash -- esta é a versão de um terminal normal no PythonAnywhere, igual ao que existe no seu computador.

> **Nota** O PythonAnywhere é baseado no Linux, então se você estiver no Windows, o terminal vai parecer um pouco diferente daquele no seu computador.

Vamos trazer nosso código do GitHub para o PythonAnywhere criando um "clone" do nosso repositório. Digite o seguinte no seu console no PythonAnywhere (não esqueça de utilizar seu username do GitHub no lugar de `<your-github-username>`):

    $ git clone https://github.com/<your-github-username>/my-first-blog.git
    

Isto irá baixar uma cópia do seu código no PythonAnywhere. Verifique digitando `tree my-first-blog`:

    $ tree my-first-blog
    my-first-blog/
    ├── blog
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
    

### Criando um virtualenv no PythonAnywhere

Assim como fez em seu próprio computador, você pode criar um virtualenv no PythonAnywhere. No console Bash, digite:

    $ cd my-first-blog
    
    $ virtualenv --python=python3.4 myvenv
    Running virtualenv with interpreter /usr/bin/python3.4
    [...]
    Installing setuptools, pip...done.
    
    $ source myvenv/bin/activate
    
    (mvenv) $  pip install django whitenoise
    Collecting django
    [...]
    Successfully installed django-1.8.2 whitenoise-2.0
    

> **Nota** O passo `pip install` pode levar alguns minutos. Paciência, paciência! Mas se demorar mais de 5 minutos, algo está errado. Pergunte ao seu treinador.

<!--TODO: think about using requirements.txt instead of pip install.-->

### Coleta de arquivos estáticos.

Você estava se perguntando o que o "whitenoise" era? É uma ferramenta para servir os arquivos chamados "arquivos estáticos" (do inglês, "static files"). Arquivos estáticos são arquivos que não mudam normalmente ou não rodam códigos, como, por exemplo, HTML ou arquivos CSS. Eles trabalham diferente nos servidores comparados aos nossos computadores, e nós precisamos de ferramentas como o "whitenoise" para servi-los.

Vamos descobrir um pouco mais sobre arquivos estáticos mais tarde no tutorial, quando editarmos o CSS para o nosso site.

Por enquanto nós só precisamos executar um comando extra chamado `collectstatic`, no servidor. Isso diz pro Django reunir todos os arquivos estáticos que ele precisa no servidor. Até o presente momento, eles são basicamente os arquivos que fazem o admin ficar bonito.

    (mvenv) $ python manage.py collectstatic
    
    You have requested to collect static files at the destination
    location as specified in your settings:
    
        /home/edith/my-first-blog/static
    
    This will overwrite existing files!
    Are you sure you want to do this?
    
    Type 'yes' to continue, or 'no' to cancel: yes
    

Digite "yes" e vambora! Você não adora fazer computadores exibirem páginas e páginas de texto? Eu sempre faço pequenos ruídos para acompanhá-lo. Brp, brp brp...

    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/actions.min.js'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/js/inlines.min.js'
    [...]
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/changelists.css'
    Copying '/home/edith/my-first-blog/mvenv/lib/python3.4/site-packages/django/contrib/admin/static/admin/css/base.css'
    62 static files copied to '/home/edith/my-first-blog/static'.
    

### Criando o banco de dados no PythonAnywhere

Este é outro processo que é diferente entre nossos computadores e o servidor: ele usa um banco de dados diferente. Então, as contas de usuário e postagens podem ser diferentes no servidor e no nosso computador.

Nós podemos inicializar o banco de dados no servidor da mesma forma que fizemos no nosso próprio computador, com `migrate` e `createsuperuser`:

    (mvenv) $ python manage.py migrate
    Operations to perform:
    [...]
      Applying sessions.0001_initial... OK
    
    
    (mvenv) $ python manage.py createsuperuser
    

## Publicando nosso blog como uma aplicação web

Agora nosso código está no PythonAnywhere, nosso virtualenv está pronto, os arquivos estáticos estão coletados, e o banco de dados está iniciado. Estamos prontas para publicar o nosso blog como um aplicativo web!

Volte para a dashboard do PythonAnywhere clicando na sua logo, e clique na aba **Web**. Finalmente, clique em **Add a new web app**.

Depois de confirmar seu nome de domínio, escolha **manual configuration** (NB *e não* a opção "Django") na caixa de diálogo. Depois escolha o **Python 3.4**, e clique em Próximo para concluir o assistente.

> **Nota** Se certifique de escolher a opção "Manual configuration", e não "Django". Nós somos boas demais pra usar a configuração padrão do Django que o PythonAnywhere oferece ;-)

### Definindo o virtualenv

Você será levada para a tela de configuração do PythonAnywhere para seu webapp, que é onde você precisará ir quando quiser fazer alterações para o aplicativo no servidor.

![][7]

 [7]: images/pythonanywhere_web_tab_virtualenv.png

Na sessão "Virtualenv", clique no texto em vermelho que diz "Enter the path to a virtualenv", e digite: `/home/<seu-usuário>/my-first-blog/myvenv/`. Clique na caixa azul com a marcação para salvar o caminho antes de seguir em frente.

> **Nota** Substitua seu próprio nome de usuário apropriadamente. Se você errar, o PythonAnywhere vai mostrar um pequeno aviso.

### Configurando o arquivo WSGI

Django funciona usando o protocolo WSGI, um padrão para servir sites usando Python, que oferece suporte a PythonAnywhere. A maneira que configuramos PythonAnywhere para reconhecer nosso blog Django é editando um arquivo de configuração do WSGI.

Clique no link "WSGI configuration file" (na seção "Code" perto do topo da página -- ele vai ser nomeado algo como `/var/www/<your-username>_pythonanywhere_com_wsgi.py`), e você será levada para um editor.

Delete todo o conteúdo e substitua-o por algo mais ou menos assim:

    python
    import os
    import sys
    
    path = '/home/<your-username>/my-first-blog'  # use seu usuário aqui
    if path not in sys.path:
        sys.path.append(path)
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    
    from django.core.wsgi import get_wsgi_application
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(get_wsgi_application())
    

> **Nota** Não esqueça de substituir o seu usuário onde diz `<your-username>`

O que esse arquivo faz é dizer ao PythonAnywhere onde mora a nossa aplicação web e qual o nome do arquivo de configurações Django. Ele também define a ferramenta de arquivos estáticos "whitenoise".

Clique em **Save** e depois volte para a aba **Web**.

Tudo pronto! Clique no grande botão verde **Reload** e você poderá ir visualizar sua aplicação. Você encontrará um link para ela no topo da página.

## Dicas de debugging

Se você encontrar um erro ao tentar acessar seu site, o primeiro lugar para buscar informações sobre para debugar é o seu **error log**. Você encontrará um link para ele na [aba Web][8] do PythonAnywhere. Verifique se existem mensagens de erro aqui; os erros mais recentes estarão no final do arquivo. Problemas comuns incluem:

 [8]: https://www.pythonanywhere.com/web_app_setup/

*   Esquecer algum dos passos que fizemos no terminal: criar o virtualenv, ativá-lo, instalar o Django nele, rodar o collectstatic, migrar o banco de dados.

*   Cometer algum erro no caminho do virtualenv na aba Web -- normalmente existirá uma pequena mensagem em vermelho lá, caso exista algum problema.

*   Cometer algum erro no arquivo de configuração WSGI -- você escreveu o caminho correto para a sua pasta my-first-blog?

*   Você escolheu a mesma versão do Python para o seu virtualenv daquela escolhida para sua aplicação? Ambas devem ser 3.4.

*   Exitem algumas [dicas gerais de debug na wiki do PythonAnywhere][9].

 [9]: https://www.pythonanywhere.com/wiki/DebuggingImportError

E lembre-se, o seu treinador está aqui para ajudar!

# Você está no ar!

A página padrão para o seu site deve dizer "Welcome to Django", assim como ela é em seu computador local. Tente adicionar `/admin/` no final da URL, e você será levado ao site admin. Fazer login com o nome de usuário e senha, e você verá que você pode adicionar novos Posts no servidor.

Dê a você um *Grande* tapinha nas costas! :D Deploy no servidor é uma das partes mais complicadas no desenvolvimento web, e muitas vezes as pessoas levam dias até conseguir deixar tudo funcionando. Mas você já tem seu site publicado, na internet! \o