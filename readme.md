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
- Como esta é uma aplicação que não estará em Produção, não acredito que seja necessário seguir o Git Flow com branches e PRs antes de uma primeira versão estável da aplicação sendo desenvolvido. Como será desenvolvido um MVP para este desafio, não será necessário utilizar essas funcionalidades do protocolo Git.
- Os serializadores estão retornando o `id` dos registros, para possibilidade de consulta GET em `endpoint/:id`. O correto seria não disponibilizar esse tipo de informação na API ou atualizar o código para apenas funcionar com alguma função hash para a chave primária das tabelas, ao invés de ID numérico. Entretanto, como esse é apenas um desafio rápido e a API está protegida por autenticação básica, não acreditei que havia necessidade de implementar neste momento. Essa seria uma melhoria futura sugerida.
- A API poderia realizar consulta de registros específicos (`GET endpoint/:pk`) para outros campos, permitindo por exemplo consulta por e-mail ou marca do produto. Essa seria uma melhoria futura sugerida.

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
- [API de Favorites List: http://127.0.0.1:8000/api/v1/favorites/](http://127.0.0.1:8000/api/v1/favorites/)

### X. Comandos Úteis

**Executar migrações do Django:**

```
docker-compose run web python manage.py migrate
```

**Gerar migrações do Django:**

```
docker-compose run web python manage.py makemigrations
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