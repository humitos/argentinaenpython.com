# Seu primeiro projeto Django!

> Parte deste capítulo é baseado nos tutoriais do Geek Girls Carrots (http://django.carrots.pl/).
> 
> Parte deste capítulo é baseado no [django-marcador tutorial][1] licenciado sobre Creative Commons Attribution-ShareAlike 4.0 International License. O tutorial do django-marcador é protegido por direitos autorais por Markus Zapke-Gründemann et al.

 [1]: http://django-marcador.keimlink.de/

Nós vamos criar um blog simples!

O primeiro passo é iniciar um novo projeto Django. Basicamente, isso significa que devemos rodar alguns scripts providos pelo Django que irão criar um esqueleto de projeto Django para nós. Isso é apenas um conjunto de diretórios e arquivos que nós iremos utilizar mais tarde.

Os nomes de alguns arquivos e diretórios são muito importantes para o Django. Não renomeie os arquivos que estamos prestes a criar. Mover para um lugar diferente também não é uma boa idéia. O Django precisa manter uma certa estrutura para conseguir encontrar algumas coisas importantes.

> Lembre-se de rodar tudo no virtualenv. Se você não vê um prefixo `(myvenv)` em seu console, você precisa ativar o virtualenv. Nós explicamos como fazer isso no capítulo **Instalação do Django** na parte **Ambiente Virtual**. Digitar `myvenv\Scripts\activate` no Windows ou `source myvenv/bin/activate` no Mac OS / Linux irá fazer isso para você.

No MacOS ou no console do Linux você pode rodar o seguinte comando; **não esqueça de adicionar o ponto `.` no final**:

    (myvenv) ~/djangogirls$ django-admin startproject mysite .
    

No Windows; **não esqueça de adicionar o ponto `.` no final**:

    (myvenv) C:\Users\Name\djangogirls> django-admin startproject mysite .
    

> O ponto `.` é crucial por que ele diz para o script instalar o Django no diretório atual (o ponto `.` é uma referência para isso)
> 
> **Nota** Quando digitar o comando acima, lembre-se de digitar apenas a parte que inicia em `django-admin` ou `django-admin.py`. As partes `(myvenv) ~/djangogirls$` e `(myvenv) C:\Users\Name\djangogirls>` apresentadas aqui são apenas exemplos do terminal onde você irá digitar seus comandos.

`Django-admin` é um script que irá criar os diretórios e arquivos para você. Agora, você deve ter um diretório estrutura que se parece com isso:

    djangogirls
    ├───manage.py
    └───mysite
            settings.py
            urls.py
            wsgi.py
            __init__.py
    

`manage.py` é um script que ajuda com a gestão do site. Com isso seremos capazes de iniciar um servidor de web no nosso computador sem instalar nada, entre outras coisas.

O arquivo `settings.py` contém a configuração do seu site.

Lembra quando falamos sobre um carteiro verificando onde entregar uma carta? arquivo `urls.py` contém uma lista dos padrões usados por `urlresolver`.

Vamos ignorar os outros arquivos por enquanto pois não vamos modificá-los. A única coisa a ser lembrada é para não excluí-los por acidente!

## Configurando

Vamos fazer algumas alterações no `mysite/settings.py`. Abra o arquivo usando o editor de código que você instalou anteriormente.

Seria bom ter a hora correta no nosso site. Vá para a <[wikipedia timezones list][2] e copie seu fuso horário. (por exemplo. `Europa/Berlim`)

 [2]: http://en.wikipedia.org/wiki/List_of_tz_database_time_zones

Em settings.py, localize a linha que contém `TIME_ZONE` e modifique para escolher seu próprio fuso horário:

    python
    TIME_ZONE = 'Europe/Berlin'
    

Modifique "Europa/Berlim", conforme o caso

Nós também precisaramos adicionar um caminho para arquivos estáticos (nós vamos descobrir tudo sobre arquivos estáticos e CSS mais tarde no tutorial). Desça até o *final* do arquivo e logo abaixo da entrada `STATIC_URL`, adicione um novo um chamado `STATIC_ROOT`:

    python
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    

## Instalação de um banco de dados

Há um monte de software de banco de dados diferente que pode armazenar dados para o seu site. Nós vamos usar o padrão, `sqlite3`.

Isto já está configurado nesta parte do seu arquivo `mysite/settings.py`:

    python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    

Para criar um banco de dados para o nosso blog, vamos fazer o seguinte no console. Digite: `python manage.py migrate` (precisamos estar no diretório que contém o arquivo `manage.py` `djangogirls`). Se isso der certo, você deve ver algo como isto:

    (myvenv) ~/djangogirls$ python manage.py migrate
    Operations to perform:
      Synchronize unmigrated apps: messages, staticfiles
      Apply all migrations: contenttypes, sessions, admin, auth
    Synchronizing apps without migrations:
       Creating tables...
          Running deferred SQL...
       Installing custom SQL...
    Running migrations:
      Rendering model states... DONE
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying sessions.0001_initial... OK
    

E está pronto! Hora de iniciar o servidor web e ver se nosso site está funcionando!

Você precisa estar no diretório que contém o arquivo `manage.py` (o diretório `djangogirls`). No console, nós podemos iniciar o servidor web executando o `python manage.py runserver`:

    (myvenv) ~/djangogirls$ python manage.py runserver
    

Se você estiver no Windows e o comando falhar com `UnicodeDecodeError`, use o este comando:

    (myvenv) ~/djangogirls$ python manage.py runserver 0:8000
    

Agora nós precisamos verificar que o nosso site está rodando. Abra seu browser (Firefox, Chrome, Safari, Internet Explorer ou qualquer outro que você utilizar) e digite o endereço:

    http://127.0.0.1:8000/
    

O servidor irá assumir o seu terminal até que você o interrompa. Para rodar mais comandos enquanto o servidor está rodando, abra uma nova janela do terminal e ative o seu virtualenv. Para interromper o seu servidor, volte para a janela onde ele está rodando e pressione CTRL+C - botões Control e C juntos (no Windows, você pode precisar pressionar Ctrl+Break).

Parabéns! Você criou seu primeiro site e o executou usando um servidor de web! Não é impressionante?

![Funcionou!][3]

 [3]: images/it_worked2.png

Pronto para o próximo passo? Está na hora de criar algum conteúdo!