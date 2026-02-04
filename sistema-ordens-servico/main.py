from app.models import Cliente, OrdemServico
import app.services as services
from app.database import carregar_dados

def menu():
    print("\n=== Sistema de Ordens de Serviço ===")
    print("1 - Criar ordem de serviço")
    print("2 - Listar ordens")
    print("3 - Finalizar ordem")
    print("0 - Sair")

def main():
    carregar_dados()

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                nome = input("Nome do cliente: ")
                telefone = input("Telefone: ")
                descricao = input("Descrição do serviço: ")

                cliente = Cliente(nome, telefone)
                ordem = OrdemServico(cliente, descricao)

                services.criar_ordem(ordem)
                print("\n✅ Ordem criada com sucesso!")

            except ValueError as e:
                print(f"\n❌ Erro: {e}")

        elif opcao == "2":
            ordens = services.listar_ordens()
            if not ordens:
                print("\nNenhuma ordem cadastrada.")
            else:
                for i, ordem in enumerate(ordens):
                    print(f"\nOrdem #{i}")
                    print(ordem)
                    print("-" * 30)

        elif opcao == "3":
            try:
                indice = int(input("Informe o número da ordem: "))
                sucesso, mensagem = services.finalizar_ordem(indice)
                print(f"\n{'✅' if sucesso else '❌'} {mensagem}")
            except ValueError:
                print("\n❌ Informe um número válido.")

        elif opcao == "0":
            print("\nSaindo do sistema...")
            break

        else:
            print("\n❌ Opção inválida.")

if __name__ == "__main__":
    main()
