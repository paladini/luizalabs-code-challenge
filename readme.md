# LuizaLabs-Code-Challenge

Esta aplicação foi construída utilizando Python 3 e o framework Django com banco de dados MySQL 8.0.

## Decisões de Projeto

Premissas e decisões de projeto explicadas abaixo:

- Utilizado banco de dados MySQL, uma vez que teremos poucos registros no banco de dados em uma aplicação de ambiente local. Bancos de dados MySQL em geral suportam bem até milhões de registros cadastrados, tendo um bom desempenho para esse panorama. Caso o número de registros exceda os milhões de registros, um banco de dados otimizado em MySQL pode ser necessário ou o uso de algum outro banco de dados mais robusto, como PostgreSQL, Oracle, MS Server ou mesmo um banco de dados orientado a documentos, como MongoDB. Como esse não é o caso, prosseguiremos com o banco de dados tradicional MySQL/MariaDB.
- Utilizando UTC como timezone padrão da aplicação Django que está sendo desenvolvida. Isso é uma decisão de projeto de padronizar todas as datas e datetimes no back-end como UTC.

## Guias

### 0. Como iniciar ambiente virtual

Rodar os seguintes comandos a partir do seu Terminal, na pasta deste projeto:

```
python3 -m venv env
source env/bin/activate
```

Pronto, ambiente virtual criado e ativado no Terminal sendo utilizado.

### 1. Como instalar dependências

Após ativar o ambiente virtual do Virtualenv, basta rodar o seguinte comando no seu Terminal:

```
pip install -r requirements.txt
```

Além disso, é necessário instalar o banco de dados MySQL e seus conectores para Python 3. Caso esteja utilizando Ubuntu ou alguma distro Debian-based, instalar com o seguinte comando:

```
sudo apt install mysql-server
sudo apt install python3-dev libmysqlclient-dev default-libmysqlclient-dev
```


### 2. Como iniciar aplicação

Para rodar as migrações de banco de dados, executar:

```
python manage.py migrate
```


Para iniciar a aplicação Django, executar os seguintes comandos:

```
python manage.py runserver
```

O servidor/aplicação estará disponível na porta 8000 do Localhost, podendo ser acessado [clicando aqui](127.0.0.1:8000/).

## Sobre

Desenvolvido por [Fernando Paladini](https://github.com/paladini) em Novembro de 2020.