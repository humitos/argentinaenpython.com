# Introdução à linha de comando

É emocionante, não?! Você vai escrever sua primeira linha de código em poucos minutos :)

**Deixe-nos apresentá-lo ao seu primeiro novo amigo: a linha de comando!**

As etapas a seguir mostraram a você como usar a janela preta que todos os hackers usam. Pode parecer um pouco assustador no começo, mas realmente é apenas um prompt esperando por comandos de você.

> **Nota** Note que ao longo deste livro intercalamos o uso dos termos 'diretório' e 'pasta', mas eles são a mesma coisa.

## Qual é a linha de comando?

A janela, que geralmente é chamada de **linha de comando** ou **interface de linha de comando**, é uma aplicação de texto para ver e manipular arquivos de seu computador. Como se fosse o Windows Explorer (no Windows) ou o Finder (no Mac), porém sem a interface gráfica. Outros nomes para a linha de comando são: *cmd*, *CLI*, *prompt*, *console* ou *terminal*.

## Abra a interface de linha de comando

Para começar alguns experimentos, precisamos abrir a nossa interface de linha de comando primeiro.

### Windows

Vá em Iniciar → Todos os Programas → Acessórios → Prompt de comando.

### Mac OS X

Applications → Utilities → Terminal.

### Linux

Provavelmente você vai achar em Applications → Accessories → Terminal, mas isso depende do seu sistema operacional. Qualquer coisa é só procurar no Google :)

## Prompt

Agora você deve ver uma janela branca ou preta que está à espera de seus comandos.

Se você estiver em Mac ou num Linux, você provavelmente verá um `` $, como este:

    $
    

No Windows, é um sinal de `>`, como este:

    >
    

Cada comando será antecedido por este sinal e um espaço, mas você não precisa digitá-lo. Seu computador fará isso por você :)

> Uma pequena nota: no nosso caso existe algo como `C:\Users\ola>` ou `Olas-MacBook-Air:~ ola$` antes do cursor e isso está correto. Neste tutorial nós apenas simplificaremos essa parte para o mínimo.

## Seu primeiro comando (YAY!)

Vamos começar com algo simples. Digite o seguinte comando:

    $ whoami
    

ou

    > whoami
    

E em então aperte `enter`. Este é o nosso resultado:

    $ whoami
    olasitarska
    

Como você pode ver o computador acabou de mostrar seu nome de usuário na tela. Legal, né? :)

> Tente escrever cada comando, não copie e cole. Você vai se lembrar mais fácil os comandos desse jeito!

## O Básico

Cada sistema operacional tem o seu próprio conjunto de instruções para a linha de comando, então se certifique que você está seguindo as instruções do seu sistema operacional. Vamos tentar, certo?

### Pasta atual

Seria legal se soubéssemos em que diretório estamos, certo? Para isso, digite o seguinte comando e aperte `enter`:

    $ pwd
    /Users/olasitarska
    

Se você estiver no Windows:

    > cd
    C:\Users\olasitarska
    

Você vai ver algo parecido em seu computador. Quando você abre a linha de comando ele em geral fica em seu diretório de usuário, também chamado de diretório "home", em Inglês.

> Nota: 'pwd' significa 'print working directory' (imprima/mostre o diretório de trabalho).

* * *

### Listando arquivos e pastas

Então o que tem nele? Seria legal descobrir. Vamos ver:

    $ ls
    Applications
    Desktop
    Downloads
    Music
    ...
    

Windows:

    > dir
     Directory of C:\Users\olasitarska
    05/08/2014 07:28 PM <DIR>      Applications
    05/08/2014 07:28 PM <DIR>      Desktop
    05/08/2014 07:28 PM <DIR>      Downloads
    05/08/2014 07:28 PM <DIR>      Music
    ...
    

* * *

### Entrar em outra pasta

Agora, vamos para a pasta Desktop:

    $ cd Desktop
    

Windows:

    > cd Desktop
    

Veja se realmente entramos na pasta:

    $ pwd
    /Users/olasitarska/Desktop
    

Windows:

    > cd
    C:\Users\olasitarska\Desktop
    

Aqui está!

> Dica de profissional: se você digitar `cd D` e apertar a tecla `tab` no seu teclado, a linha de comando irá preencher automaticamente o resto do nome para que você possa navegar rapidamente. Se houver mais de uma pasta que comece com "D", aperte a tecla `tab` duas vezes para obter uma lista de opções.

* * *

### Criando uma pasta

Que tal criar um diretório em sua área de trabalho para praticarmos? Você pode fazer isso com o seguinte comando:

    $ mkdir practice
    

Windows:

    > mkdir practice
    

Esse pequeno comando criará um diretório chamado `practice` em sua área de trabalho. Você pode verificar se o diretório realmente está lá olhando sua área de trabalho ou executando o comando `ls` ou `dir`! Experimente :)

> Dica de profissional: Se você não quiser digitar o mesmo comando várias vezes, tente pressionar `seta para cima` e `seta para baixo` no teclado para percorrer comandos usados recentemente.

* * *

### Exercite-se!

Um pequeno desafio para você: crie um diretório dentro do diretório `practice` chamando `test`. Use os comandos `cd` e `mkdir`.

#### Solução:

    $ cd practice
    $ mkdir test
    $ ls
    test
    

Windows:

    > cd practice
    > mkdir test
    > dir
    05/08/2014 07:28 PM <DIR>      test
    

Parabéns! :)

* * *

### Limpando

Não queremos deixar uma bagunça, então vamos remover tudo o que fizemos até agora.

Primeiro, precisamos voltar para a pasta Desktop:

    $ cd ..
    

Windows:

    > cd ..
    

Utilizar o `..` com o comando `cd` vai mudar seu diretório atual para o diretório pai (o diretório que contém o seu diretório).

Veja onde você está:

    $ pwd
    /Users/olasitarska/Desktop
    

Windows:

    > cd
    C:\Users\olasitarska\Desktop
    

Agora é hora de deletar o diretório `pratice`:

> **Atenção**: A exclusão de arquivos usando `del`, `rmdir` ou `rm` é irrecuperável, significando que os *Arquivos excluídos vão embora para sempre*! Então, tenha cuidado com este comando.

    $ rm -r practice
    

Windows:

    > rmdir /S practice
    practice, Are you sure <Y/N>? Y
    

Pronto! Para ter certeza que a pasta foi excluída, vamos checar:

    $ ls
    

Windows:

    > dir
    

### Saindo

Isso é tudo, por enquanto! Agora você pode fechar a janela do terminal, mas vamos fazer isso de um jeito hacker, certo? :)

    $ exit
    

Windows:

    > exit
    

Legal, né?:)

## Sumário

Aqui vai uma lista de alguns comandos úteis:

| Comando (Windows) | Comando (Mac OS / Linux) | Descrição                     | Exemplo                                           |
| ----------------- | ------------------------ | ----------------------------- | ------------------------------------------------- |
| exit              | exit                     | Fecha a janela                | **exit**                                          |
| cd                | cd                       | Muda a pasta                  | **cd test**                                       |
| dir               | ls                       | Lista as pastas e/ou arquivos | **dir**                                           |
| copy              | cp                       | Copia um arquivo              | **copy c:\test\test.txt c:\windows\test.txt** |
| move              | mv                       | Move um arquivo               | **move c:\test\test.txt c:\windows\test.txt** |
| mkdir             | mkdir                    | Cria uma pasta                | **mkdir testdirectory**                           |
| del               | rm                       | Deleta uma pasta e/ou arquivo | **del c:\test\test.txt**                        |

Esses são apenas alguns dos comandos que você pode rodar na sua linha de comando, porém não vamos usar mais do que isso hoje.

Se você estiver curioso, [ss64.com][1] contém uma referência completa de comandos para todos os sistemas operacionais.

 [1]: http://ss64.com

## Pronto?

Vamos mergulhar no Python!