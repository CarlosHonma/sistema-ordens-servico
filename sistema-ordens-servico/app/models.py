from datetime import datetime

class Cliente:
    def __init__(self, nome, telefone):
        if not nome.strip():
            raise ValueError("Nome do cliente não pode ser vazio.")

        if not telefone.strip():
            raise ValueError("Telefone não pode ser vazio.")

        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome} ({self.telefone})"


class OrdemServico:
    def __init__(self, cliente, descricao):
        if not descricao.strip():
            raise ValueError("Descrição do serviço não pode ser vazia.")

        self.cliente = cliente
        self.descricao = descricao
        self.status = "Aberta"
        self.data_criacao = datetime.now()

    def finalizar(self):
        if self.status == "Finalizada":
            raise ValueError("Ordem já está finalizada.")
        self.status = "Finalizada"

    def __str__(self):
        return (
            f"Cliente: {self.cliente}\n"
            f"Descrição: {self.descricao}\n"
            f"Status: {self.status}\n"
            f"Criada em: {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"
        )
