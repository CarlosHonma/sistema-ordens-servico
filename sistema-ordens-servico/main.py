from app.models import Cliente, OrdemServico
import app.services as services

def menu():
    print("\n=== Sistema de Ordens de Serviço ===")
    print("1 - Criar ordem de serviço")
    print("2 - Listar ordens")
    print("3 - Finalizar ordem")
    print("0 - Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            telefone = input("Telefone: ")
            descricao = input("Descrição do serviço: ")

            cliente = Cliente(nome, telefone)
            ordem = OrdemServico(cliente, descricao)
            services.criar_ordem(ordem)

            print("\n✅ Ordem criada com sucesso!")

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
            indice = int(input("Informe o número da ordem: "))
            if services.finalizar_ordem(indice):
                print("\n✅ Ordem finalizada!")
            else:
                print("\n❌ Ordem não encontrada.")

        elif opcao == "0":
            print("\nSaindo do sistema...")
            break

        else:
            print("\n❌ Opção inválida.")

if __name__ == "__main__":
    main()
