# Testes automatizados de API

Projeto de exemplo para automação de testes de APIs com Python, `pytest`,
Tavern, HTTPX e FastAPI, que faz parte da disciplina de **Automação de Testes de Software**.

## O que é testado

### Fluxo de tarefas com Tavern

O arquivo `test_fluxo_todos.tavern.yaml` testa a API pública
[JSONPlaceholder](https://jsonplaceholder.typicode.com):

1. Busca os To-Dos com os IDs `1`, `5` e `15`.
2. Verifica se cada resposta retorna status HTTP `200`.
3. Salva o `userId` da tarefa encontrada.
4. Usa o `userId` salvo para buscar as tarefas do usuário.
5. Valida, por meio de `utils.validar_lista_tarefas`, se a resposta é uma
   lista e se pelo menos uma tarefa possui a chave `completed`.

### Performance assíncrona

O arquivo `test_performance.py` testa o endpoint `/processar` da aplicação
FastAPI definida em `api_pagamentos.py`.

O teste dispara simultaneamente `5`, `20` e `50` requisições usando
`asyncio.gather` e `httpx.ASGITransport`. Todas as respostas devem retornar
status `200`, e cada execução deve terminar em menos de `3,5` segundos.

O teste usa `ASGITransport`, portanto a aplicação é executada diretamente em
memória e não é necessário iniciar um servidor Uvicorn.

## Requisitos

- Python 3.9 ou superior
- Acesso à internet para os testes do JSONPlaceholder

As dependências estão listadas em `requirements.txt`:

- `fastapi`
- `httpx`
- `tavern`
- `pytest`
- `pytest-asyncio`

## Instalação

Recomenda-se criar um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Linux ou macOS

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Execução dos testes

Execute toda a suíte:

```bash
python -m pytest
```

Execute apenas o teste de performance:

```bash
python -m pytest test_performance.py
```

Execute apenas o fluxo do Tavern:

```bash
python -m pytest test_fluxo_todos.tavern.yaml
```

## Estrutura do projeto

```text
.testes_api
├── api_pagamentos.py
├── test_fluxo_todos.tavern.yaml
├── test_performance.py
├── utils.py
├── requirements.txt
├── .gitignore
└── assets/
    └── Exercício ATS10.pdf
```

## Controle de arquivos temporários

O `.gitignore` ignora caches gerados pelo Python e pelo Pytest, incluindo:

- `__pycache__/`
- `.pytest_cache/`

## Autor

**Ryan Rodrigues Cordeiro**