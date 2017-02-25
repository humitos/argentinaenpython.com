> Essa seção é baseada em um tutorial escrito por Geek Girls Carrots (http://django.carrots.pl/)

Django é escrito em Python. Nós precisamos do Python para fazer qualquer coisa em Django. Vamos começar com sua instalação! Nós queremos que você instale o Python 3.4, então se você tem qualquer versão anterior, você vai precisar atualizá-la.

### Windows

Você pode baixar o Python para Windows no website https://www.python.org/downloads/release/python-343/. Depois de fazer o download do arquivo ***.msi**, você precisa executá-lo (dando um duplo-clique nele) e seguir as instruções. É importante lembrar o caminho (a pasta) onde você instalou o Python. Isto será útil depois!

Atenção: na segunda janela da instalação marque "Customize" (personalizar) e marque a opção "Add python.exe to the Path", como mostrado a seguir:

![Não se esqueça de adicionar o Python no Path](../python_installation/images/add_python_to_windows_path.png)

### Linux

É muito provável que você já tenha o Python instalado e configurado. Para ter certeza se ele está instalado (e qual a sua versão), abra um terminal e digite o seguinte comando:

    $ python3 --version
    Python 3.4.3
    

Se você não tiver o Python instalado, ou se você quiser uma versão diferente, você pode fazer da seguinte maneira:

#### Debian ou Ubuntu

Digite o seguinte comando no terminal:

    $ sudo apt-get install python3.4
    

#### Fedora (até a versão 21)

Use o seguinte comando no terminal:

    $ sudo yum install python3.4
    

#### Fedora (versão 22 em diante)

Use o seguinte comando no terminal:

    $ sudo dnf install python3.4
    

### OS X

Você precisa ir até o site https://www.python.org/downloads/release/python-343/ e fazer o download do instalador do Python:

  * Faça o download do arquivo *Mac OS X 64-bit/32-bit installer*,
  * Dê um duplo clique no arquivo *python-3.4.3-macosx10.6.pkg* para executar o instalador.

Verifique se a instalação foi bem sucedida abrindo o *Terminal* e digitando o comando `python3`:

    $ python3 --version
    Python 3.4.3
    

* * *

Se você está com alguma dúvida ou se alguma coisa deu errado e você não faz a menor ideia do que fazer por favor pergunte ao seu instrutor! Nem sempre tudo sai como o esperado e é melhor pedir ajuda a alguém mais experimente.