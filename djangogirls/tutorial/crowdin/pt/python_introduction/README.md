# Introdução ao Python

> Parte deste capítulo é baseado nos Tutoriais de Geek Girls Carrots (http://django.carrots.pl/).

Vamos escrever um pouco de código!

## Interpretador Python

Para começar a brincar com Python nós precisamos abrir uma *linha de comando* no seu computador. Você já sabe dever como fazer isso -- você aprendeu isso no capítulo  [Introdução à Linha de Comando][2].</p> 
Assim que estiver pronto, siga as instruções abaixo.

Queremos abrir um console do Python, então digite`python` no Windows ou `python3`no Mac OS/Linux e pressione`enter`.

    $ python3
    Python 3.4.3 (...)
    Digite "help", "copyright", "credits" or "license" para mais informações.
    >>>
    

## Seu primeiro comando Python!

Depois de executar o comando Python, o prompt mudou para `>>>`. Para nós, isso significa que por enquanto só utilizaremos comandos na linguagem Python. Você não precisa digitar `>>>` - O Python fará isso por você.

Se você deseja sair do console do Python, apenas digite `exit()` ou use o atalho `Ctrl + Z` no Windows e `Ctrl + D` no Mac/Linux. Então você não vai ver mais o `>>>`.

Por enquanto, não queremos sair do console de Python. Queremos saber mais sobre isso. Vamos começar com algo realmente simples. Por exemplo, tente digitar algumas contas, como `2 + 3` e pressione `enter`.

    >>> 2 + 3
    5
    

Incrível! Vê como a resposta simplesmente aparece? O Python conhece matemática! Você pode tentar outros comandos como: - `4 * 5` - `5 - 1` - `40 / 2`

Divirta-se com isso por um tempo e depois volte aqui :).

Como você pode ver, o Python é uma ótima calculadora. Se você está se perguntando o que mais você pode fazer...

## Strings

Que tal o seu nome? Digite seu primeiro nome entre aspas, desse jeito:

    >>> "Ola"
    'Ola'
    

Você acabou de criar sua primeira string! String é um sequência de caracteres que podem ser processada pelo computador. A string sempre precisa iniciar e terminar com o mesmo caractere. Ela pode ser aspa simples (`'`) ou dupla (`"`) (não há nenhuma diferença!) As aspas dizem ao Python que o que está dentro delas é uma string, ou sequência de caracteres.

Strings podem ser juntadas. Tente isto:

    >>> "Oi " + "Ola"
    'Oi Ola'
    

Você também pode multiplicar strings por um número:

    >>> "Ola" * 3
    'OlaOlaOla'
    

Se você precisa colocar uma apóstrofe dentro de sua string, existem duas maneiras de fazer.

Usando aspas duplas:

    >>> "Correndo' ladeira abaixo" 
    "Correndo' ladeira abaixo"
    

ou escapando a aspa simples (fazendo com que o Python entenda que ela não é o final da nossa string) com uma contra-barra (``):

    >>> "Correndo\' ladeira abaixo" 
    "Correndo' ladeira abaixo"
    

Legal, hein? Para ver seu nome em letras maiúsculas, basta digitar:

    >>> "Ola".upper()
    'OLA'
    

Você acabou de usar a **função** `upper` na sua string! Uma função (como `upper()`) é um conjunto de instruções que o Python tem que realizar em um determinado objeto (`"Ola"`), sempre que você chamar por ele.

Se você quer saber o número de letras do seu nome, existe uma função para isso também!

    >>> len("Ola")
    3
    

Se perguntando porque algumas vezes você chama funções com um `.` no fim de uma string (como `"Ola".upper()`) e algumas vezes você primeiro chama a função colocando a string nos parênteses? Bem, em alguns casos, funções pertencem a objetos, como `upper()`, que só pode ser utilizada em strings. Nesse caso, nós chamamos a função de **método**. Outras vezes, funções não pertencem a nada específico e podem ser usadas em diferentes tipos de objetos, assim como `len()`. É por isso que nós estamos fornecendo `"Ola"` como um parâmetro para a função `len`.

### Sumário

OK, chega de strings. Até agora você aprendeu sobre:

*   **o prompt** - digitar comandos (códigos) no interpretador Python resulta em respostas em Python
*   **números e strings** - no Python, números são usados para matemática e strings para objetos de texto
*   **operadores** - como + e *, combinam valores para produzir um novo valor
*   **funções** - como upper() e len(), executam ações nos objetos.

Isso é o básico sobre todas as linguagens de programação que você aprende. Pronto para algo mais difícil? Apostamos que sim!

## Erros

Vamos tentar algo novo. Será que conseguimos ver o tamanho de um número da mesma forma que nós encontramos o tamanho de nosso nome? Digite `len(304023)` e aperte `enter`:

    >>> len(304023)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: object of type 'int' has no len()
    

Temos nosso primeiro erro! Ele diz que objetos do tipo "int" (inteiros, apenas números) não têm nenhum comprimento. Então o que podemos fazer agora? Talvez possamos escrever nosso número como uma string? Strings têm um comprimento, certo?

    >>> len(str(304023))
    6
    

Funcionou! Usamos a função `str` dentro da função `len`. `str ()` converte tudo para strings.

*   A função `str` converte as coisas em **strings**
*   A função `int` converte as coisas em **números inteiros**

> Importante: podemos converter números em texto, mas nós não podemos, necessariamente, converter texto em números - o que `int('hello')` quer dizer?

## Variáveis

Um conceito importante na programação é o conceito de variáveis. Uma variável não é nada mais do que um nome para alguma coisa, de tal forma que você possa usá-la mais tarde. Os programadores usam essas variáveis para guardar dados, para fazer seus códigos mais legíveis e para não ter que se lembrar sempre o que algumas coisas significam.

Digamos que queremos criar uma nova variável chamada `nome`:

    >>> name = "Ola"
    

Vê? É fácil! É só fazer: nome igual a Ola.

Como você deve ter percebido, a última linha não nos retornou algo como nas anteriores. Assim, como vamos saber se a variável realmente existe? Basta digitar `name` e apertar `enter`:

    >>> name
    'Ola'
    

Yippee! Sua primeira variável:)! Você sempre pode mudar o seu valor:

    >>> name = "Sonja"
    >>> name
    'Sonja'
    

Você pode usá-la também em funções:

    >>> len(name)
    5
    

Incrível não? Claro, variáveis podem ser qualquer coisa, então podem ser números também! Tente isso:

    >>> a = 4
    >>> b = 6
    >>> a * b
    24
    

Mas, e se digitarmos o nome errado? Você consegue adivinhar o que aconteceria? Vamos tentar!

    >>> city = "Tokyo"
    >>> ctiy
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'ctiy' is not defined
    

Um erro! Como você pode ver, Python tem diferentes tipos de erros e este é chamado **NameError**. Python dará este erro se você tentar usar uma variável que não foi definida ainda. Se você encontrar esse erro depois, veja se no seu código se você não digitou o nome de uma variável errado.

Brinque com isso por um tempo e veja o que você consegue fazer!

## A função print

Tente isso:

    >>> name = 'Maria'
    >>> name
    'Maria'
    >>> print(name)
    Maria
    

Quando você apenas digita `name`, o interpretador Python responde com a *representação* como string da variável 'name', que são as letras M-a-r-i-a, entre aspas simples. Quando você diz `print(name)`, Python vai "imprimir" o conteúdo da variável na tela, sem as aspas, o que é mais puro.

Como veremos mais tarde, `print()` também é útil quando queremos imprimir algo dentro de funções, ou quando queremos imprimir algo em várias linhas.

## Listas

Além de strings e inteiros, o Python tem todos os tipos diferentes de objetos. Vamos apresentar um chamado **lista**. Listas são exatamente o que você pensa que elas são: objetos que são listas de outros objetos. :)

Vá em frente e crie uma lista:

    >>> []
    []
    

Sim, esta é uma lista vazia. Não é muito, não é? Vamos criar uma lista dos números da loteria. Como não queremos ficar repetindo o código todo o tempo vamos criar uma variável para ela:

    >>> lottery = [3, 42, 12, 19, 30, 59]
    

Tudo certo, nós temos uma lista! O que podemos fazer com isso? Vamos ver quantos números de loteria existem nesta lista. Você tem ideia de qual função deve usar para isso? Você já sabe disso!

    >>> len(lottery)
    6
    

Sim! `len()` pode te dar o número de objetos que fazem parte de uma lista. Uma mão na roda, não? Vamos organizar isso agora:

    >>> lottery.sort()
    

Isso não retorna nada, apenas troca a ordem em que os números aparecem na lista. Vamos imprimir isso outra vez e ver o que acontece:

    >>> print(lottery)
    [3, 12, 19, 30, 42, 59]
    

Como você pode ver, os números na nossa lista estão ordenados do menor para o maior. Parabéns!

Talvez a gente queira inverter essa ordem? Vamos fazer isso!

    >>> lottery.reverse()
    >>> print(lottery)
    [59, 42, 30, 19, 12, 3]
    

Moleza né? Se você quiser adicionar alguma coisa à sua lista, você pode fazer isto digitando o seguinte comando:

    >>> lottery.append(199)
    >>> print(lottery)
    [59, 42, 30, 19, 12, 3, 199]
    

Se você quiser mostrar apenas o primeiro número você pode usar **indices**. Um índice é um número que diz onde um item da lista está. Programadores preferem começar a contar a partir do zero, então o primeiro objeto em sua lista está no índice 0, o segundo no 1 e assim por diante. Tente isso:

    >>> print(lottery[0])
    59
    >>> print(lottery[1])
    42
    

Como você pode ver, você pode acessar diferentes objetos na sua lista usando o nome da lista e o índice do objeto dentro dos colchetes.

Para deletar algum objeto de sua lista você precisa usar os **índices** como aprendemos acima e a declaração **del** (que é uma abreviação para "deletar"). Vamos a um exemplo, aproveitando para reforçar o que aprendemos antes: deletaremos o primeiro número de nossa lista.

    >>> print(lottery)
    [59, 42, 30, 19, 12, 3, 199]
    >>> print(lottery[0])
    59
    >>> del lottery[0]
    >>> print(lottery)
    [42, 30, 19, 12, 3, 199]
    

Funcionou perfeitamente!

Agora tente alguns outros índices, como: 6, 7, 1000, -1, -6 ou -1000. Veja se você consegue prever o resultado antes de executar o comando. Os resultados fazem sentido para você?

Você pode encontrar uma lista de todos os métodos disponíveis neste capítulo na documentação do Python: https://docs.python.org/3/tutorial/datastructures.html

## Dicionários

Um dicionário é semelhante a uma lista, mas você pode acessar valores através de uma chave ao invés de um índice. Uma chave pode ser qualquer string ou número. A sintaxe para definir um dicionário vazio é:

    >>> {}
    {}
    

Isso mostra que você acabou de criar um dicionário vazio. Hurra!

Agora, tente escrever o seguinte comando (tente substituir com as suas próprias informações também):

    >>> participant = {'name': 'Ola', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
    

Com esse comando, você acabou de criar uma variável chamada `participant` com três pares de chave-valor:

*   A chave `nome` aponta para o valor `'Ola'` (um objeto `string`),
*   `pais` aponta para `'Polonia'` (outra `string`),
*   e `numeros_favoritos` apontam para `[7, 42, 92]` (uma `list` com três números nela).

Você pode verificar o conteúdo de chaves individuais com a sintaxe:

    >>> print(participant['name'])
    Ola
    

Veja, é similar a uma lista. Mas você não precisa lembrar o índice - apenas o nome.

O que acontece se pedirmos ao Python o valor de uma chave que não existe? Você consegue adivinhar? Vamos tentar e descobrir!

    >>> participant['age']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'age'
    

Olha, outro erro! Esse é um **KeyError**. Python é bastante prestativo e te diz que a chave `'age'` não existe no nesse dicionário.

Você deve estar se perguntando quando deveria usar um dicionário ou uma lista, certo? Boa pergunta! A resposta rápida é:

*   Você precisa de uma sequência ordenada de itens? Use uma list.
*   Você precisa associar valores com chaves, assim você pode procurá-los eficientemente (pela chave) mais tarde? Use um dictionary.

Dicionários, assim como listas, são *mutáveis*, isso significa que eles podem ser alterados depois de serem criados. Você pode adicionar um novo par chave/valor a um dicionário depois de ele ser criado, por exemplo:

    >>> participant['favorite_language'] = 'Python'
    

Como nas listas, se usarmos a função `len()` em dicionários teremos o número de pares chave-valor no dicionário. Siga em frente e digite na sua linha de comando:

    >>> len(participant)
    4
    

Espero que faça sentido até agora. :) Pronta para mais diversão com dicionários? Pule para a próxima linha para coisas incríveis.

Você pode usar o comando `del` para deletar um item no dicionario. Digamos, se você quer excluir a entrada correspondente a chave `'favorite_numbers'`, basta digitar o seguinte comando:

    >>> del participant['favorite_numbers']
    >>> participant
    {'country': 'Poland', 'favorite_language': 'Python', 'name': 'Ola'}
    

Como você pode ver no retorno, o par chave-valor correspondente à chave 'favorite_numbers' foi excluído.

Além disso você pode mudar o valor associado com uma chave já criada no dicionário. Digite:

    >>> participant['country'] = 'Germany'
    >>> participant
    {'country': 'Germany', 'favorite_language': 'Python', 'name': 'Ola'}
    

Como você pode ver, o valor da chave `'country'` foi alterado de `'Poland'` para `'Germany'`. :) Emocionante? Hurra! Você acabou de aprender outra coisa incrível.

### Sumário

Incrível! Agora você sabe muito sobre programação. Nesta última parte você aprendeu sobre:

*   **erros** - agora você sabe como ler e entender erros que aparecem se o Python não entender um comando que você deu
*   **variáveis** - nomes para objetos que permitem você programar facilmente e deixar seu código mais legível
*   **listas** - listas de objetos armazenados em uma ordem específica
*   **dicionários** - objetos armazenados como pares chave-valor

Empolgado(a) para o próximo passo? :)

## Compare coisas

Grande parte da programação consiste em comparar coisas. O que é mais fácil de comparar? Números, é claro. Vamos ver como isso funciona:

    >>> 5 > 2
    True
    >>> 3 < 1
    False
    >>> 5 > 2 * 2
    True
    >>> 1 == 1
    True
    >>> 5 != 2
    True
    

Demos ao Python alguns números para comparar. Como você pode ver, Python pode comparar não só números mas também resultados de métodos. Legal, hein?

Você está se perguntando por que colocamos dois sinais de igual `==` lado a lado para comparar se os números são iguais? Nós usamos um único `=` para atribuir valores a variáveis. Você sempre, **sempre** precisa colocar dois `==` se quiser verificar se as coisas são iguais. Também é possível afirmar que as coisas são desiguais entre si. Para isso, usamos o símbolo `! =`, conforme mostrado no exemplo acima.

Dê ao Python mais duas tarefas:

    >>> 6 >= 12 / 2
    True
    >>> 3 <= 2
    False
    

`>` e `<` são fáceis, mas o que `>=` e `<=` significam? Leia eles da seguinte forma:

*   x `>` y significa: x é maior que y
*   x `<` y significa: x é menor que y
*   x `< =` y significa: x é menor ou igual a y
*   x `>=` y significa: x é maior ou igual a y

Fantástico! Quer mais? Tente isto:

    >>> 6 > 2 and 2 < 3
    True
    >>> 3 > 2 and 2 < 1
    False
    >>> 3 > 2 or 2 < 1
    True
    

Você pode dar ao Python quantos números para comparar quanto você quiser, e ele vai te dar uma resposta! Espertinho, certo?

*   **and** - se você usar o operador `and`, ambas as comparações terão que ser verdadeiras para que todo o comando seja verdadeiro
*   **or** - se você usar o operador `or`, apenas uma das comparações precisa ser verdadeira para que o comando todo seja verdadeiro

Já ouviu a expressão "comparar maçãs com laranjas"? Vamos tentar o equivalente em Python:

    >>> 1 > 'django'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unorderable types: int() > str()
    

Aqui vemos que assim como na expressão, Python não é capaz de comparar um número (`int`) e uma string (`str`). Em vez disso, ele mostrou um **TypeError** e nos disse que os dois tipos não podem ser comparados juntos.

## Booleano

Acidentalmente, você aprendeu sobre um novo tipo de objeto em Python. É chamado de **booleano** -- e provavelmente o tipo mais fácil que existe.

Existem apenas dois objetos booleanos: - True (verdadeiro) - False (falso)

Mas para que o Python entenda você precisa escrever exatamente 'True' (primeira letra maiúscula e as outras minúsculas -- mas sem as aspas). **true, TRUE ou tRUE não vão funcionar -- só True está correto.** (A mesma coisa vale para 'False', obviamente.)

Booleanos podem ser variáveis também! Veja:

    >>> a = True
    >>> a
    True
    

Você também pode fazer desse jeito:

    >>> a = 2 > 5
    >>> a
    False
    

Pratique e divirta-se com os valores booleanos, tentando executar os seguintes comandos:

*   `True and True`
*   `False and True`
*   `True or 1 == 1`
*   `1 != 2`

Parabéns! Booleanos são um dos recursos mais interessantes na programação, e você acabou de aprender como usá-los!

# Salvá-lo!

Até agora escrevemos todos os códigos no interpretador Python, que nos limita a digitar uma linha por vez. Programas normais são salvos em arquivos e executados pelo nosso **interpretador** de linguagem de programação ou **compilador**. Até agora já corremos nossos programas de uma linha de cada vez no **interpretador** Python. Nós vamos precisar de mais de uma linha de código para as próximas tarefas, então precisaremos rapidamente:

*   Saída do interpretador Python
*   Abra o editor de código de sua escolha
*   Salvar algum código em um novo arquivo de python
*   Executá-lo!

Para sair do interpretador Python que estamos usando, simplesmente digite a função ~~~ exit() ~~~:

    >>> exit()
    $
    

Isso vai colocá-lo de volta no prompt de comando.

Anteriormente, nós escolhemos um editor de código da seção do [editor de código][4]. Nós precisamos abrir o editor agora e escrever algum código em um novo arquivo:</p> 
    python
    print('Hello, Django girls!')
    

> **Nota** Você deve notar uma das coisas mais legais nos editores de código: cores! No interpretador Python tudo é da mesma cor, mas agora você deve ver que a função `print` está em uma cor diferente da string. Isso é chamado de destaque de sintaxe ("syntax highlightning", do Inglês) e é uma funcionalidade muito útil para usar quando estamos escrevendo código. As cores de cada parte nos dão dicas, como strings que esquecemos de fechar, erro de digitação em uma palavra reservada (como `def` na definição de uma função, que veremos adiante). Esta é uma das razões pelas quais que nós usamos um editor de código :)

Agora você é um desenvolvedor Python bastante experiente, então sinta-se livre para escrever códigos com o que você aprendeu hoje.

Agora temos de salvar o arquivo e dar a ele um nome descritivo. Vamos chamar o arquivo **python_intro.py** e salvá-lo na sua área de trabalho. Nós podemos nomear esse arquivo do jeito que quisermos, mas é importante que ele termine com **.py**. A extensão **.py** diz ao sistema operacional que esse é um **arquivo Python executável** e o interpretador Python pode rodá-lo.

Com o arquivo salvo, é hora de executá-lo! Usando as habilidades que você aprendeu na seção de linha de comando, use o terminal para **alterar os diretórios** para o desktop.

Em um Mac, o comando será parecido com isto:

    $ cd /Users/<your_name>/Desktop
    

No Linux, será assim (a palavra "Desktop" pode ser traduzida para seu idioma):

    $ cd /home/<seu_nome>/Desktop
    

E no windows, vai ser assim:

    > cd C:\Users\<your_name>\Desktop
    

Se você não conseguir é só pedir ajuda.

Agora use o interpretador Python para executar o código que está dentro do arquivo, assim:

    $ python3 python_intro.py
    Hello, Django girls!
    

Muito bom! Você acabou de rodar o seu primeiro programa Python que foi salvo a um arquivo. Sente-se incrível?

Você pode agora passar para uma ferramenta essencial na programação:

## if...elif...else

Muitas coisas no código só podem ser executadas se determinadas condições forem atendidas. É por isso que o Python tem alguma coisa chamada **declaração if**.

Troque o código no arquivo **python_intro.py** para isso:

    python
    if 3 > 2:
    

Se salvou este e ele foi executado, nós veríamos um erro como este:

    $ python3 python_intro.py
    File "python_intro.py", line 2
             ^
    SyntaxError: unexpected EOF while parsing
    

O Python espera que lhe demos instruções que devem ser executadas caso a condição `3 > 2` seja verdadeira (ou `True`). Vamos tentar fazer o Python imprimir "It works!". Altere o seu código no seu arquivo **python_intro.py** para isto:

    python
    if 3 > 2:
        print('It works!')
    

Notou que a linha após o "if" começa com 4 espaços? Fizemos isso para que o Python saiba que essa linha só deve ser executada se a expressão do "if" for verdadeira. Você pode quantos espaços quiser, mas por convenção os programadores Python usam 4, para que os códigos fiquem mais uniformes. Um `tab` também conta como 4 espaços.

Salve-o e execute novamente:

    $ python3 python_intro.py
    It works!
    

### E se uma condição não for verdadeira?

Nos exemplos anteriores, o código foi executado somente quando as condições eram verdadeiras, mas o Python também tem as instruções `elif` e `else`:

    python
    if 5 > 2:
        print('5 é de fato maior que 2')
    else:
        print('5 não é maior que 2')
    

Rode o código acima e verá:

    $ python3 python_intro.py
    5 é de fato maior que 2
    

Se 2 for um número maior do que 5, então o segundo comando será executado. Fácil, né? Vamos ver como funciona o `elif`:

    python
    name = 'Sonja'
    if name == 'Ola':
        print('Hey Ola!')
    elif name == 'Sonja':
        print('Hey Sonja!')
    else:
        print('Hey anonymous!')
    

e executando:

    $ python3 python_intro.py
    Hey Sonja!
    

Mas o que aconteceu ali? `elif` te possibilita adicionar uma condição extra que roda caso a primeira condição seja falsa.

Você pode adicionar quantos `elif` quiser depois do `if`. Por exemplo:

    python
    volume = 57
    if volume < 20:
        print("Está bem quieto.")
    elif 20 <= volume < 40:
        print("Está bom para música de fundo")
    elif 40 <= volume < 60:
        print("Perfeito, posso ouvir todos os detalhes")
    elif 60 <= volume < 80:
        print("Bom para festas")
    elif 80 <= volume < 100:
        print("Muito alto!")
    else:
        print("Meus ouvidos estão doendo! :(")
    

Python irá testar cada condição sequencialmente e então irá imprimir:

    $ python3 python_intro.py
    Perfeito, posso ouvir todos os detalhes
    

### Sumário

Nos últimos três exercícios você aprendeu:

*   **comparar as coisas** - em Python, você pode comparar as coisas usando os operadores `>`, `>=`, `==`, `<=`, `<` e o `and`, `or`
*   **Booleano** - um tipo de objeto que só tem um dos dois valores: `True` ou `False`
*   **Salvando arquivos** - armazenamento de código em arquivos assim você pode executar programas maiores.
*   **if... elif... else**-instruções que permitem que você execute o código somente se determinadas condições forem atendidas.

É hora da última parte deste capítulo!

## Suas próprias funções!

Lembra de funções como `len()`? Boas notícias: agora você vai aprender como escrever suas próprias funções!

Uma função é um sequência de instruções que o Python deve executar. Cada função em Python se inicia com a palavra reservada `def`, possui um nome e pode ter parâmetros. Vamos começar com uma função simples. Substitua o código no **python_intro.py** com o seguinte:

    python
    def hi():
        print('Hi there!')
        print('How are you?')
    
    hi()
    

Ok, nossa primeira função está pronta!

Você pode se perguntar por que escrevemos o nome da função na parte inferior do arquivo. Isto é porque Python lê o arquivo e executa-lo de cima para baixo. Então, para usar a nossa função, temos re-escrevê-lo na parte inferior.

Vamos executá-lo agora e ver o que acontece:

    $ python3 python_intro.py
    Hi there!
    How are you?
    

Isso foi fácil! Vamos construir nossa primeira função com parâmetros. Usaremos o exemplo anterior - uma função que diz 'hi' para quem o executa - com um name:

    python
    def hi(name):
    

Como você pode ver, agora demos um parâmetro chamado `name` para nossa função:

    python
    def hi(name):
        if name == 'Ola':
            print('Hi Ola!')
        elif name == 'Sonja':
            print('Hi Sonja!')
        else:
            print('Hi anonymous!')
    
    hi()
    

Lembre-se: a função `print` está endentada de 4 espaços depois do `if`. Isso é necessário porque a função só rodará se a condição for verdadeira. Vamos ver como isso funciona agora:

    $ python3 python_intro.py
    Traceback (most recent call last):
    File "python_intro.py", line 10, in <module>
      hi()
    TypeError: hi() missing 1 required positional argument: 'name'
    

Oops, um erro. Felizmente, Python nos fornece uma mensagem de erro bastante útil. Ela diz que a função `hi()` (aquela que declaramos) tem um argumento obrigatório (chamado `name`) e que nós esquecemos de passá-lo ao chamar a função. Vamos corrigi-lo na parte inferior do arquivo:

    python
    hi("Ola")
    

E rode novamente:

    $ python3 python_intro.py
    Hi Ola!
    

E se mudarmos o nome?

    python
    hi("Sonja")
    

E rode novamente:

    $ python3 python_intro.py
    Hi Sonja!
    

Agora, o que você acha que aconteceria se você escrevesse um outro nome lá (que não seja "Ola" ou "Sonja")? Faça um teste e verifique se você estava certo. Ele deve imprimir o seguinte:

    Hi anonymous!
    

Isto é incrível, não? Dessa maneira você não precisa se repetir (DRY - don't repeat yourself) cada vez que for mudar o nome da pessoa que a função pretende cumprimentar. E é exatamente por isso que precisamos de funções - você nunca quer repetir seu código!

Vamos fazer algo mais inteligente..--existem mais que dois nomes, e escrever uma condição para cada um seria difícil, certo?

    python
    def hi(name):
        print('Hi ' + name + '!')
    
    hi("Rachel")
    

Vamos chamar o código agora:

    $ python3 python_intro.py
    Hi Rachel!
    

Parabéns! Você acabou de aprender como criar funções. :)

## Laços

Essa já é a última parte! Rápido, né? :)

Programadores não gostam de repetirem código. Programar é automatizar coisas, então não queremos cumprimentar a cada pessoa manualmente, certo? É aí que entram os laços (ou "loops", em Inglês).

Ainda se lembra das listas? Vamos fazer uma lista de garotas:

    python
    girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
    

Queremos cumprimentar todas elas pelos seus nomes. Temos a função `hi` para fazer isso, então vamos usá-la em um laço:

    python
    for name in girls:
    

A instrução ~~~ for~~~ funciona parecida com o ~~~ if~~~ : o código em seguida deve ser endentado com 4 espaços.

Aqui está o código completo que será salvo no arquivo:

    python
    def hi(name):
        print('Hi ' + name + '!')
    
    girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
    for name in girls:
        hi(name)
        print('Next girl')
    

E quando rodamos:

    $ python3 python_intro.py
    Hi Rachel!
    Next girl
    Hi Monica!
    Next girl
    Hi Phoebe!
    Next girl
    Hi Ola!
    Next girl
    Hi You!
    Next girl
    

Como você pode ver, tudo o que você vai colocar dentro de uma instrução `for` com espaço será repetido para cada elemento da lista `girls`.

Você também pode usar o `for` em números usando a função `range`:

    for i in range(1, 6):
        print(i)
    

Que iria imprimir:

    1
    2
    3
    4
    5
    

`range` é uma função que cria uma lista de números que se seguem um após o outro (esses números são dados por você como parâmetros).

Note que o segundo desses dois números não está incluído na lista que o Python mostrou (em `range(1, 6)`, conta de 1 a 5, mas o 6 não é incluído). Isso porque o intervalo é semi-aberto, o que significa que ele inclui o primeiro valor, mas não o último.

## Sumário

É isso. **Você mandou muito bem!** Esse foi um capítulo difícil, então você deve estar orgulhosa. Nós estamos orgulhosas de você por ter conseguido ir tão longe!

Talvez você queira brevemente fazer algo mais - espreguiçar, andar um pouco, descansar os olhos - antes de ir para o próximo capítulo. :)

![Cupcake][5]

 []: ../intro_to_command_line/README.md
 [2]: /intro_to_command_line/README.html
 []: ../code_editor/README.md
 [4]: code_editor/README.md
 [5]: images/cupcake.png