from app.database import (
    ordens_servico,
    salvar_dados
)

def criar_ordem(ordem):
    ordens_servico.append(ordem)
    salvar_dados()

def listar_ordens():
    return ordens_servico

def listar_por_status(status):
    return [os for os in ordens_servico if os.status == status]

def finalizar_ordem(indice):
    try:
        ordens_servico[indice].finalizar()
        salvar_dados()
        return True
    except IndexError:
        return False
