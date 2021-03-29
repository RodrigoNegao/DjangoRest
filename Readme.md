### **Projeto de uso de Modelo Django Restaurante Simples (Docker REST API)** :snake: :whale:

### Para uma boa instalação e testes siga a ordem abaixo.

### Ambiente Django no Windows

[Configurar Ambiente (Env) no Python](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)

### Criar Ambiente com Conda
- Instale o ANACONDA 
- Primeiro Configure cmd [Configurar Ambiente(Env) Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- Digite: 
```bash
activate base
```
- Crie um Env no cmd: 
```bash
conda create -name DjangoRest
```
- Ative:
```bash
 activate DjangoRest
 ```
- Instale os Modulos:
```bash
 pip install -r requirements.txt
 ```
### Config DB
```bash
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
### Caso use db.sqlite3 disponivel 
Login
- Username: admin
- Password: admin

### Criar novo Super Usuario
```bash
python manage.py createsuperuser
```

### Ambiente Docker para Django :whale:
### Instalação do DockerTOOLS (Docker para Windows Home)
- 1º [Tutorial do DockerTOOLS](https://docs.docker.com/toolbox/toolbox_install_windows/)
- 2º [Programa DockerTOOLS](https://github.com/docker/toolbox/releases)
- Quando for Instalar, Habilite 'Kitematic' na Instalação.

### Configuração Docker para Django
- Abra **Docker Quickstart Terminal** :
    - o caminho do raiz sempre minuscula e caso de espaço use '\ '
    - ex: *cd /c/Users/rodrigo\ negao/desktop/DockerDjangoApi*
    ```bash
    cd /diretorio
    ```
    - Vai Construir um Docker a partir do Arquivo **DockerFile**:
             (este comando serve para atualizar também)
    ```bash
    docker-compose build
    ```
    - Rode no Terminal para Criar as config do *docker-compose.yml*:
    ```bash
    docker-compose up
    ```
    - Caso tenha algum problema, Control+C para parar o Server (Terminal pode ser Instavel para rodar o **db**)

- Pode haver problemas de Conflito em rodar o Docker no Terminal, então abra **Kitematic** que foi instalado :
    - Quando você usou Terminal, vai estar criado os Dockers do **db** e da **web**;
    1. Inicialize o dockerdjangoapi_db_1
    2. Inicialize o dockerdjangoapi_web_1

- Vai abrir o exemplo no lado , mas tera a opção de abrir no Browser Padrão.

- **Modelo do Tutorial [Docker Compose para Django](https://docs.docker.com/compose/django/)**

## :calling: Teste no Celular - Windows
- Abra cmd 
- Digite 
```bash
ipconfig
``` 
- Abra no projeto settings.py - digite o ip encontrado no ipconfig
```bash 
- ALLOWED_HOSTS = ['ip-address']
``` 
- Digite o camando 
```bash 
python manage.py runserver 0.0.0.0:8000
```
- digite no Browser do seu celular o ip encontrado - 'http://ip-address:8000'

### Testes Unitario , Regressão,Integração e Funcional
- Foram feitos manualmente.
- Usado Método get_absolute_url()
- Mozila Developer [Tutorial](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Testing)

> Similarmente, você deve verificar se os métodos personalizados  get_absolute_url() e > __str__() se comportam como desejado, porque els são sua lógica de código/negócios.  > No caso de get_absolute_url() você pode confiar que o método reverse() de Django, 
> foi  implementado corretamente, portanto, o que você esta testando é se a view
> associada foi realmente definida.


## Implementar aplicativo em um Web Service
- no Ubuntu 18.04 [Tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-pt)

