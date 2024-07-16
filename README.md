# FastAPI TODO ASYNC API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-100000?style=for-the-badge&logo=sqlalchemy&logoColor=red)

## API em Produção

A API está disponível para testes em produção no seguinte endereço:  <a href="https://todo-fastapi-one.vercel.app" target="_blank">https://todo-fastapi-one.vercel.app</a>

## Descrição

Esta é uma API de gerenciamento de tarefas (TODO) construída com FastAPI e SQLAlchemy. A API é assíncrona e foi projetada para ser rápida, eficiente e fácil de usar.

## Funcionalidades

- **Criar Tarefa**: Cria uma nova tarefa.
- **Obter Todas as Tarefas**: Recupera todas as tarefas com paginação.
- **Obter Tarefa por ID**: Recupera uma tarefa específica pelo seu ID.
- **Atualizar Tarefa**: Atualiza uma tarefa existente pelo seu ID.
- **Deletar Tarefa**: Deleta uma tarefa pelo seu ID.

## Endpoints

### Criar Tarefa

- **URL**: `/api/v1/todos/`
- **Método**: `POST`

### Obter Todas as Tarefas

- **URL:** `/api/v1/todos/`
- **Método:** `GET`
- **Parâmetros de Query:**
    - skip (opcional): Número de registros a serem ignorados (padrão é 0).
    - limit (opcional): Número máximo de registros a serem retornados (padrão é 100).
 
### Obter Tarefa por ID

- **URL:** `/api/v1/todos/{id}`
- **Método:** `GET`

### Atualizar Tarefa

- **URL:** `/api/v1/todos/{id}`
- **Método:** `PUT`

  ### Deletar Tarefa
  
  - **URL:** `/api/v1/todos/{id}`
  - **Método:** `DELETE`
 
  ## Como Executar o Projeto

  ### Pré-requisitos

  - Python 3.8+
  - Algum ambiente virtual para gerenciamento de dependências
 
  ## Instalação

  1. Clone o repositório:
     git clone https://github.com/thiagoregueira/to-do_async_backend_python.git
     cd to-do_async_backend_python

  2. Instale as dependências:
     ``` pip install -r requirements.txt ```

  3. Configure as variáveis de ambiente no arquivo .env:
     ```
     DB_USER=seu_usuario
     DB_PASSWORD=sua_senha
     DB_HOST=seu_host
     DB_PORT=5432
     DB_NAME=seu_banco_de_dados ```
    
  4. Execute as migrações do banco de dados:
     ` alembic upgrade head `

  5. Inicie o servidor:
     ` uvicorn app.main:app --reload `


## Melhor Práticas

- **Documentação:** API utiliza a documentação automática do FastAPI disponível em /docs e /redoc.
- **Validação:** API utiliza Pydantic para validação de dados.
- **Segurança:** API configura CORS adequadamente e utilize variáveis de ambiente para informações sensíveis.
- **Desempenho:** API utiliza conexões assíncronas com o banco de dados para melhorar o desempenho.

## Contato
- **Nome:** Thiago Regueira
- **Email:** thiago.regueira@yahoo.com.br
- **GitHub:** [thiagoregueira](https://github.com/thiagoregueira) 
