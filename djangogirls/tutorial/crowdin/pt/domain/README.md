# Domínio

O Heroku nos deu um domínio, mas ele é longo, difícil de lembrar e feio. Seria melhor ter um nome de domínio curto e fácil de lembrar, certo?

Neste capítulo nós ensinaremos a você como comprar um domínio e direcioná-lo ao Heroku!

## Onde registrar um domínio?

Um domínio normal custa mais ou menos 15 dólares por ano. Existem domínios mais caros e mais baratos dependendo do provedor. Existem uma série de empresas das quais você pode comprar um domínio: uma simples [pesquisa no google][1] pode listar uma série delas.

 [1]: https://www.google.com/search?q=register%20domain

O nosso favorito é o [I want my name][2] (eu quero meu nome). Eles anunciam seu serviço como "gestão de domínio indolor", e ele, realmente, é indolor.

 [2]: https://iwantmyname.com/

## Como registrar domínio no IWantMyName?

Acesse [iwantmyname][3] e digite o domínio que você quer ter na caixa de pesquisa.

 [3]: http://iwantmyname.com

![][4]

 [4]: images/1.png

Você deve ver uma lista com todos os domínios disponíveis com o termo que foi posto no campo de pesquisa. Como você pode notas, uma carinha feliz indica que o domínio está disponível para compra e uma carinha triste indica que o domínio já foi comprado por alguém.

![][5]

 [5]: images/2.png

Nós decidimos comprar o domínio `djangogirls.in`:

![][6]

 [6]: images/3.png

Vá para "checkout". Agora, você deve se cadastrar no iwantmyname caso ainda não possua uma conta. Depois disso, insira os dados do seu cartão de crédito e compre um domínio!

Depois, clique em `Domains` no menu e escolha o domínio que você acabou de comprar. Localize e clique no link `manage DNS records`:

![][7]

 [7]: images/4.png

Agora você precisa localizar este formulário:

![][8]

 [8]: images/5.png

E preencher os seguintes detalhes: - Hostname: www - Type: CNAME - Value: o seu domínio do Heroku (por exemplo djangogirls.herokuapp.com) - TTL: 3600

![][9]

 [9]: images/6.png

Clique no botão Adicionar e salve as mudanças na parte de baixo.

Pode levar um bom tempo para que o seu domínio comece a funcionar, então seja paciente!

## Configurar o domínio no Heroku

Você também precisa dizer ao Heroku que você quer usar o seu domínio personalizado.

Vá para [Heroku Dashboard][10], acesse sua conta do Heroku e escolha um aplicativo (app). Depois, vá para as configurações do aplicativo (app Settings), adicione seu domínio na seção `Domains` e salve suas mudanças.

 [10]: https://dashboard.heroku.com/apps

É isso!