import json
import os
from app.models import Cliente, OrdemServico

ARQUIVO = "ordens.json"

ordens_servico = []

def salvar_dados():
    dados = []

    for ordem in ordens_servico:
        dados.append({
            "cliente": {
                "nome": ordem.cliente.nome,
                "telefone": ordem.cliente.telefone
            },
            "descricao": ordem.descricao,
            "status": ordem.status,
            "data_criacao": ordem.data_criacao.isoformat()
        })

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)

    for item in dados:
        cliente = Cliente(
            item["cliente"]["nome"],
            item["cliente"]["telefone"]
        )

        ordem = OrdemServico(cliente, item["descricao"])
        ordem.status = item["status"]
        ordem.data_criacao = ordem.data_criacao.fromisoformat(
            item["data_criacao"]
        )

        ordens_servico.append(ordem)
