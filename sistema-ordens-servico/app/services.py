from database import ordens_servico, salvar_dados

def criar_ordem(ordem):
    ordens_servico.append(ordem)
    salvar_dados()

def listar_ordens():
    return ordens_servico

def finalizar_ordem(indice):
    if indice < 0 or indice >= len(ordens_servico):
        return False, "Ordem não encontrada."

    try:
        ordens_servico[indice].finalizar()
        salvar_dados()
        return True, "Ordem finalizada com sucesso."
    except ValueError as e:
        return False, str(e)
