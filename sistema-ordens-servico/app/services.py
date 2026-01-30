from app.database import ordens_servico

def criar_ordem(ordem):
    ordens_servico.append(ordem)

def listar_ordens():
    return ordens_servico

def listar_por_status(status):
    return [os for os in ordens_servico if os.status == status]

def finalizar_ordem(indice):
    try:
        ordens_servico[indice].finalizar()
        return True
    except IndexError:
        return False
