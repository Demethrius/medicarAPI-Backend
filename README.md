# Introdução

Tecnologias:

- Python, como linguagem de programação;

- Django Framework, como framework de desenvolvimento web para o backend;

- Django Rest Framework, como biblioteca para o Django Framework para criação de APIs Restful;

- Django Rest Framework JWT, como biblioteca para o Django Framework para criação de tokens para autenticar um usuário ao fazer o login;

- Django Environ, como biblioteca para manipular variáveis de ambiente sensíveis à aplicação;

- PostgreSQL, como SGBD para armazenar, acessar, atualizar e deletar informações no banco de dados;

- Insomnia, para realizar as requisições HTTP

# Configurações

### Ambiente Virtual

Ao ter acesso aos arquivos, primeiro deve-se criar o ambiente de desenvolvimento (vitualenv) e instalar todas as dependências, utilizando:

```bash
python3 -m venv env
pip install -r requirements.txt
```

### Variáveis de ambiente

Depois de ter todas as dependências instaladas, deve-se acrescentar algumas variáveis de ambiente:

- Primeiro deve-se criar um arquivo '.env' na pasta medicarAPI, ou seja, na mesma pasta do arquivo settings.py
- No arquivo '.env' colocar as seguintes variáveis:

```bash
SECRET_KEY=89o4$wv3g)y)w1ym81wfgt7b@7twpq3!&o^kef7)o9-itpqu%e
DB_NAME='nome do banco criado'
DB_USER='nome do usuário do banco'
DB_PASSWORD='senha do banco'
DB_HOST='endereço do banco'
DB_PORT='porta que o banco está rodando'
```

### Migrations

- Agora deve-se rodar as migrações para o banco ser preenchido com as tabelas necessárias à aplicação:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Django Admin

- Após estas configurações iniciais, o projeto já estará pronto para uso, logo, deve-se criar um super user para o acesso do Django Admin:

```bash
python manage.py createsuperuser
```


# Problema

- Criei 2 Django Apps, a primeira é a 'user', com as informações de cadastro de usuário, e a segunda é a 'core', com as informações médicas; 
- Herdei o model User do Django Framework para a criação de novos usuários, e utilizei uma flag booleana para indicar se é cliente;
- A modelagem do banco com as lógicas da parte médica estão na app 'core';
- Com a conta criada, deve-se informar os campos 'username' e 'password' para a rota de autenticação (login) para receber um JWT para conseguir ter acesso às outras rotas da API.

# Rotas

### Autenticação
- Registration/Signup
```bash
url: localhost:8000/api/auth/cadastrar_cliente/
body: "username", "password", "email", "first_name", "last_name"
```

- Login/Authentication
```bash
url: localhost:8000/api/token
body: "username", "password"
retorno: JWT
```


> As próximas rotas só poderão ser acessadas passando o token na variável Authorization do header da requisição: 'JWT + token recebido no login'


### Rotas
- Especialidades List (GET)
```bash
url: localhost:8000/api/especialidades/
```

- Médicos List (GET)
```bash
url: localhost:8000/api/medicos/
```

- Consultas List (GET)
```bash
url: localhost:8000/api/consultas/
```

- Consultas Create (POST)
```bash
url: localhost:8000/api/consultas/
body: "agenda", "horario"
```

- Agendas List (GET)
```bash
url: localhost:8000/api/agendas/
```


# Testes

- Os testes de Registration e Authentication estão na app 'user', e os testes de endpoints estão na app 'core';


# Considerações Finais

- Por questões de melhor visualização coloquei um paginator de tamanho 2, que pode ser alterado na variável 'PAGE_SIZE' no arquivo settings.py;
- Todas as validações e filtragens de endpoints foram implementados.