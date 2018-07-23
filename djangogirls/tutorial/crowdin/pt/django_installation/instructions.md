> Parte deste capítulo é baseado nos Tutoriais da Geek Girls Carrots (http://django.carrots.pl/).
> 
> Parte deste capítulo é baseado em [django-marcador tutorial](http://django-marcador.keimlink.de/) licenciado sob Creative Commons Attribution-ShareAlike 4.0 International License. O tutorial do django-marcador é protegido por direitos autorais por Markus Zapke-Gründemann et al.

## Ambiente virtual

Antes de instalarmos o Django, vamos instalar uma ferramenta muito útil para ajudar a manter nosso ambiente de trabalho organizado no nosso computador. Você pode pular esse passo, mas ele é altamente recomendado. Iniciar com a melhor instalação possível salvará você de muito trabalho no futuro!

Então, vamos criar um **ambiente virtual**(também chamado um *virtualenv*). O virtualenv irá isolar seu código Python/Django em um ambiente "por projeto". Isso significa que qualquer alteração que você fizer em um website não afetará os outros que você também estiver desenvolvendo. Legal, certo?

Tudo o que você precisa fazer é encontrar um diretório no qual você deseja criar o `virtualenv`; seu diretório Home, por exemplo. No Windows pode parecer como `C:\Usuário\Nome` (onde `Nome` é o nome do seu login).

Para este tutorial usaremos um novo diretório`djangogirls` do seu diretório home:

    mkdir djangogirls
    cd djangogirls
    

Nós vamos fazer um virtualenv chamado `meuenv`. O formato geral desse comando é:

    python3 -m venv myvenv
    

### Windows

Para criar um novo `virtualenv`, você precisa abrir o console (nós falamos sobre isso há alguns capítulos atrás, lembra?) e executar `C:\Python34\python -m venv myvenv`. Vai ficar desse jeito:

    C:\Usuário\Nome\djangogirls> C:\Python34\python -m venv myvenv
    

onde `C:\Python34\python` é o diretório em que você previamente instalou Python e `myvenv` é o nome da sua `virtualenv`. Você pode usar qualquer outro nome, mas sempre use minúsculas e sem espaços, acentos ou caracteres especiais. Também é uma boa ideia manter o nome curto - você irá referenciá-lo muitas vezes!

### Linux e OS X

Criar um `virtualenv` tanto no Linux como OS X é simples como executar `python3 -m venv myvenv`. Será algo parecido com isto:

    ~/djangogirls$ python3 -m venv myvenv
    

`myvenv` é o nome do seu `virtualenv`. Você pode usar qualquer outro nome, mas permaneça em caixa baixa(minúsculas) e não use espaços entre os nomes. Também é uma boa idéia manter o nome curto pois você vai referenciá-lo muitas vezes!

> **NOTA:**Iniciar o ambiente virtual no Ubuntu 14.04 assim retornará o seguinte erro:
> 
>     Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1
>     
> 
> Para contornar esse problema, use o comando `virtualenv`.
> 
>     ~/djangogirls$ sudo apt-get install python-virtualenv
>     ~/djangogirls$ virtualenv --python=python3.4 myvenv
>     

## Trabalhando com o virtualenv

O comando acima criará um diretório chamado `myvenv` (ou qualquer que seja o nome que você escolheu) que contém o nosso ambiente virtual (basicamente um conjunto de diretórios e arquivos).

#### Windows

Inicie o seu ambiente virtual executando:

    C:\Usuário\Nome\djangogirls> myvenv\Scripts\activate
    

#### Linux e OS X

Inicie o seu ambiente virtual executando:

    ~/djangogirls$ source myvenv/bin/activate
    

Lembre-se de substituir `myvenv` com seu nome escolhido do `virtualenv`!

> **NOTE:** às vezes `source` pode não estar disponível. Nesses casos, tente fazer isso em vez disso:
> 
>     ~/djangogirls$ . myvenv/bin/activate
>     

Você vai saber que tem um `virtualenv` funcionando quando ver o prompt no seu console se parecer com:

    (myvenv) C:\Usuário\Nome\djangogirls>
    

ou:

    (myvenv) ~/djangogirls$
    

Perceba que o prefixo `(myvenv)` aparece!

Ao trabalhar dentro de um ambiente virtual, `python` irá automaticamente se referir a versão correta para que possa utilizar `python` em vez de `python3`.

Ok, nós temos todas as dependências importantes no lugar. Finalmente podemos instalar o Django!

## Instalando o Django

Agora que você tem a sua `virtualenv` iniciada, você pode instalar Django usando `pip`. No console, execute `pip install django==1.8` (perceba que usamos um duplo sinal de igual: `==`).

    (myvenv) ~$ pip install django==1.8
    Downloading/unpacking django==1.8
    Installing collected packages: django
    Successfully installed django
    Cleaning up...
    

no Windows

> Se você receber um erro ao chamar o pip na plataforma Windows por favor, verifique se o caminho do projeto contém espaços, acentos ou caracteres especiais (exemplo, `C:\Users\User Name\djangogirls`). Se sim, por favor considere movê-lo para outro lugar sem espaços, acentos ou caracteres especiais (a sugestão é: `C:\djangogirls`). Após a mudança, por favor tente novamente o comando acima.

no Linux

> Se você receber um erro ao chamar pip no Ubuntu 12.04 por favor execute `python -m pip install -U --force-reinstall pip` para corrigir a instalação do pip no virtualenv.

É isso! Agora você está (finalmente) pronta para criar uma aplicação Django!