# LuizaLabs-Code-Challenge

Esta aplicação foi construída utilizando Python 3 e o framework Django com banco de dados PostgreSQL. 

## Pré-requisitos

- Docker
- Docker-compose

## Decisões de Projeto

Premissas e decisões de projeto explicadas abaixo:

- O projeto e suas dependências estão dockerizadas, permitindo uma fácil execução, manutenção e publicação (deployment) da aplicação em diversas plataformas Cloud, como AWS e GCP (Google Cloud Platform).
- Uma vez que teremos poucos registros no banco de dados em uma aplicação de ambiente local, apenas para fins do desafio, um banco de dados como SQLite e MySQL/MariaDB suportariam muito bem em termos de performance. Bancos de dados MySQL em geral suportam bem até milhões de registros cadastrados. Caso o número de registros exceda os milhões de registros, um banco de dados otimizado em MySQL pode ser necessário ou o uso de algum outro banco de dados mais robusto, como PostgreSQL, Oracle, MS Server ou mesmo um banco de dados orientado a documentos, como MongoDB. Nesse caso, por decisão de projeto, utilizaremos a robustez do PostgreSQL.
- Utilizando UTC como timezone padrão da aplicação Django que está sendo desenvolvida. Isso é uma decisão de projeto de padronizar todas as datas e datetimes no back-end como UTC.
- A explicação de como funcionaria a autenticação e o reviewScore dos produtos estavam meio vagas e mesmo tirando essas dúvidas por e-mail com a equipe do processo seletivo, não ficou muito bem especificado. Dessa forma, tomei algumas liberdades referentes a esses dois pontos. É necessário criar um usuário de acesso à API antes que possa se utilizar os endpoints de Produtos (`/api/v1/products/`), Clientes (`/api/v1/clients/`) e Produtos Favoritos (`/api/v1/favorites/`).
- Como esta é uma aplicação que não estará em Produção, não acredito que seja necessário seguir o Git Flow com branches e PRs antes de uma primeira versão estável da aplicação sendo desenvolvido. Como será desenvolvido um MVP para este desafio, não será necessário utilizar essas funcionalidades do protocolo Git.
- Alguns validadores de senha foram removidos para facilitar o registro de um novo usuário da API. 
- A paginação de todos os modelos, após autenticação na API, pode ser feita via `?page=<numero_pagina>` ou através do próprio retorno do endpoint.
- [Melhoria Planejada] Os serializadores estão retornando o `id` dos registros, para possibilidade de consulta GET em `endpoint/:id`. O correto seria não disponibilizar esse tipo de informação na API ou atualizar o código para apenas funcionar com alguma função hash para a chave primária das tabelas, ao invés de ID numérico. Entretanto, como esse é apenas um desafio rápido e a API está protegida por autenticação básica, não acreditei que havia necessidade de implementar neste momento. Essa seria uma melhoria futura sugerida.
- [Melhoria Planejada] A API poderia realizar consulta de registros específicos (`GET endpoint/:pk`) para outros campos, permitindo por exemplo consulta por e-mail ou marca do produto.
- [Melhoria Planejada] Os logs e metrificação poderiam ser melhorados/configurados/integrados com serviços de APM como NewRelic. Configurações para pipeline de deploy também poderiam ser realizados em um serviço como Jenkins. Por fim, em uma arquitetura de microserviços seria necessário o lançamento/leitura de eventos para comunicação via mensageria (utilizando RabbitMQ, por exemplo). Além disso, os eventos também forneceriam dados importantes para inteligência de mercado, equipe de Data Science e afins, podendo compilar dashboards e fazer análises interessantes das modificações do estado dos modelos/sistema.
- [Melhoria Planejada] Desenvolver testes unitários e de integração, além de registrar os modelos no Admin do Django para acesso/gerenciamento.
- [Melhoria Planejada] Melhoria nos endpoints de produtos favoritos, de acordo com as especificações/demandas do projeto.
- [Melhoria Planejada] Sistema de load de dados iniciais (*populate*) melhorado/padronizado.
  

## Guias


### 1. Como iniciar aplicação

Para iniciar a aplicação Django, executar os seguintes comandos:

```
docker-compose up
```

Após iniciar a aplicação com o docker-compose, note que:

- O servidor/aplicação estará disponível na porta 8000 do Localhost, podendo ser acessado [clicando aqui](127.0.0.1:8000/).
- A documentação da API está disponível em [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)


**Também existe uma documentação padrão do Django-Rest-Framework disponível em:**

- [API de Products: http://127.0.0.1:8000/api/v1/products/](http://127.0.0.1:8000/api/v1/products/)
- [API de Clients: http://127.0.0.1:8000/api/v1/clients/](http://127.0.0.1:8000/api/v1/clients/)


### 2. Como Utilizar a API

Antes de mais nada, registrar um usuário de acesso à API no endpoint [/api/v1/auth/registration/](http://127.0.0.1:8000/api/docs#auth-registration-create). Na resposta dessa requisição receberá um `Token`, que deverá ser utilizado no header `Authorization` das requisições para qualquer uso das endpoints da API. 

Caso precise realizar login para um usuário de API já registrado (ou seja, um usuário registrado com `username` / `password`), utilizar o endpoint [/api/v1/auth/login/](http://127.0.0.1:8000/api/docs#auth-login-create). Assim como no processo de `registration`, você receberá uma resposta com um Token que deverá ser utilizado nas demais requisições para a API.

Após configurar o header `Authorization` para as demais chamadas da API, poderão ser utilizadas as APIs de Products, Clients e Favorites List.

Após isso, cadastrar produtos e clientes através da API em questão, utilizando o Token de autorização fornecido previamente. Por fim, pode-se utilizar a API de associação de produtos com listas de favoritos (`GET /api/v1/clients/{id}/favorites/{product_id}/`) e remoção de produtos já associados com listas de usuários (`GET /api/v1/clients/{id}/favorites/{product_id}/remove`).


### X. Comandos Úteis

**Executar migrações do Django:**

```
docker-compose run web python manage.py migrate
```

**Gerar migrações do Django:**

```
docker-compose run web python manage.py makemigrations
```

**Resetar migrações do Django (Opção 1):**

```
docker-compose run web python manage.py migrate --fake web zero
```

**Resetar migrações do Django (Opção 2):**

Caso não seja possível executar o comando acima, conecte no seu banco de dados PostgreSQL e execute a seguinte query:

```
DROP SCHEMA public CASCADE;

CREATE SCHEMA public;

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
```

Após isso, gere e execute as migrações do Django:

```
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```

**Exportar dados previamente registrados no banco PostgreSQL:**

```
docker-compose run web python manage.py dumpdata --format=json favorites_list > favorites_list/fixtures/initial_data.json
```

**Sync do banco de dados:**

```
docker-compose run web python manage.py migrate --run-syncdb
```

**Atualizar bibliotecas da instância Docker:**

```
docker-compose run web pip install -r requirements.txt
```

**Atualizar requirements-lock.txt da instância Docker:**

```
docker-compose run web pip freeze > requirements-lock.txt && cat requirements-lock.txt
```

**Recriar instâncias do Docker + Build + Start:**

```
docker-compose up --build --force-recreate
```

## Sobre

Desenvolvido por [Fernando Paladini](https://github.com/paladini) em Novembro de 2020.