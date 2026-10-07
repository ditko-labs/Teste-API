def validar_lista_tarefas(response):

    dados = response.json()

    assert isinstance(dados, list) == True
    assert any("completed" in tarefa for tarefa in dados)