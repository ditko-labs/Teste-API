# ATS10 — Testes Automatizados de API

Conjunto de testes automatizados em Python para validar um fluxo com Tavern e um cenário assíncrono de performance com FastAPI e HTTPX.

O enunciado está em [assets/Exercício ATS10.pdf](assets/Exercício%20ATS10.pdf).

## Ambiente

Lembrando..

```bash
python -m venv .venv
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

No Windows:

```bash
.venv\Scripts\activate
```

```bash
python -m pip install -r requirements.txt
```

As dependências do projeto são:

- `fastapi`
- `httpx`
- `tavern`
- `pytest`
- `pytest-asyncio`

## Execução

Na raiz do projeto, com o ambiente ativo:

```bash
python -m pytest
```

Esse comando executa toda a suíte, incluindo o fluxo do Tavern e o teste assíncrono da API local.

Se quiser rodar apenas o fluxo do Tavern:

```bash
python -m pytest test_fluxo_todos.tavern.yaml
```

Se quiser rodar apenas o teste de performance:

```bash
python -m pytest test_perfomance.py
```

## O que os testes fazem

### Fluxo com Tavern

O arquivo `test_fluxo_todos.tavern.yaml` valida a API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com) em duas etapas:

1. Busca os To-Dos com os IDs `1`, `5` e `15`.
2. Confere se cada resposta volta com status HTTP `200`.
3. Salva o `userId` retornado na primeira consulta.
4. Usa esse `userId` para consultar todas as tarefas do mesmo usuário.
5. Delega a validação da estrutura para `utils.validar_lista_tarefas`, que confirma se o retorno é uma lista e se existe ao menos uma tarefa com a chave `completed`.

### Performance assíncrona

O arquivo `test_perfomance.py` valida o endpoint `/processar` da aplicação FastAPI definida em `api_pagamentos.py`.

O teste dispara simultaneamente `5`, `20` e `50` requisições com `asyncio.gather` e `httpx.ASGITransport`. A aplicação roda em memória, então não é necessário subir servidor externo para a validação.

Para cada quantidade de requisições, o teste exige duas coisas:

1. Todas as respostas precisam retornar status HTTP `200`.
2. O tempo total precisa ficar abaixo de `3,5` segundos.

## Saída esperada

O fluxo do Tavern deve concluir sem falhas de validação e o teste de performance deve mostrar que a chamada concorrente ao endpoint continua dentro do limite definido.

Na execução completa, o projeto verifica tanto integração com um serviço externo quanto comportamento local da API simulada, sem depender de Uvicorn.

## Estrutura do projeto

```text
TESTE-API
├── api_pagamentos.py
├── test_fluxo_todos.tavern.yaml
├── test_perfomance.py
├── utils.py
├── requirements.txt
└── assets/
	└── Exercício ATS10.pdf
```

## Observações

- O acesso à internet é necessário para o teste que consulta a JSONPlaceholder.
- O teste de performance usa a aplicação em memória, então ele roda sem subir servidor adicional.
- O arquivo `test_perfomance.py` mantém o nome original do repositório.

## Autor

**Ryan Rodrigues Cordeiro**