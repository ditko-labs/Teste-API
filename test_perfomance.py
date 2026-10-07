import pytest
import httpx
import asyncio
import time
from api_pagamentos import app

@pytest.mark.asyncio
@pytest.mark.parametrize("requisicoes", [5, 20, 50])
async def test_processar_pagamento(requisicoes):
    inicio = time.time()
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        tarefas = [client.get("/processar") for _ in range(requisicoes)]

        respostas = await asyncio.gather(*tarefas)

        for res in respostas:
            assert res.status_code == 200

    tempo_total = time.time() - inicio

    assert tempo_total < 3.5