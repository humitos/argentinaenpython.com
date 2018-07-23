# Django Admin

Para adicionar, editar e remover postagens que nós criamos usaremos o Django admin.

Vamos abrir o arquivo `blog/admin.py` e substituir seu conteúdo por:

    python
    from django.contrib import admin
    from .models import Post
    
    admin.site.register(Post)
    

Como você pode ver, nós importamos (incluímos) o modelo Post definido no capítulo anterior. Para tornar nosso modelo visível na página de administração, nós precisamos registrá-lo com: `admin.site.register(Post)`.

OK, hora de olhar para o nosso modelo de Post. Lembre-se de executar `python manage.py runserver` no console para executar o servidor web. Vá para o navegador e digite o endereço http://127.0.0.1:8000/admin/ Você verá uma página de login assim:

![Página de login][1]

 [1]: images/login_page2.png

Para fazer login você precisa criar uma conta *superuser* - um usuário que tem controle sobre tudo dentro do site. Volte pra linha de comando e digite `python manage.py createsuperuser`, e tecle enter. Quando questionado, digite seu username (minúsculas, sem espaços), endereço de email, e senha. Não se preocupe que você não pode ver a senha que você está digitando - é assim que deve ser. Apenas digite a senha e pressione `enter` pra continuar. A saída deve parecer com essa (onde Username e Email devem ser os seus):

    (myvenv) ~/djangogirls$ python manage.py createsuperuser
    Username: admin
    Email address: admin@admin.com
    Password:
    Password (again):
    Superuser created successfully.
    

Volte ao seu navegador. Faça login com as credenciais de superusuário que você escolheu; você deverá ver a dashboard de administração do Django.

![Django Admin][2]

 [2]: images/django_admin3.png

Vá em Posts e experimente um pouco. Adicione cinco ou seis posts no blog. Não se preocupe com o conteúdo - você pode simplesmente copiar e colar textos desse tutorial para poupar tempo :).

Certifique-se que pelo menos duas ou três postagens (mas não todas) têm a data de publicação definida. Isso será útil depois.

![Django Admin][3]

 [3]: images/edit_post3.png

Se você quiser saber mais sobre o Django admin, você deve conferir a documentação do Django: https://docs.djangoproject.com/en/1.6/ref/contrib/admin/

Este é provavelmente um bom momento para tomar um café (ou chocolate) ou algo para comer para repora as energias. Você criou seu primeiro modelo de Django - você merece um pouco de descanso!