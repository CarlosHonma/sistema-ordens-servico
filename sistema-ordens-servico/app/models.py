from datetime import datetime

class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome} ({self.telefone})"


class OrdemServico:
    def __init__(self, cliente, descricao):
        self.cliente = cliente
        self.descricao = descricao
        self.status = "Aberta"
        self.data_criacao = datetime.now()

    def finalizar(self):
        self.status = "Finalizada"

    def __str__(self):
        return (
            f"Cliente: {self.cliente}\n"
            f"Descrição: {self.descricao}\n"
            f"Status: {self.status}\n"
            f"Criada em: {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"
        )
