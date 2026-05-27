from datetime import datetime

def criar_medicamento(nome, dosagem, intervalo, comprimidos_por_dose, duracao_tratamento, quantidade_caixa):
    

    total_necessario = (
        comprimidos_por_dose *
        duracao_tratamento
    )
    
    return {
        "nome": nome,
        "dosagem": dosagem,
        "intervalo": intervalo,
        "comprimidos_por_dose": comprimidos_por_dose,
        "duracao_tratamento": duracao_tratamento,
        "quantidade_caixa": quantidade_caixa,
        "total_necessario": total_necessario,
        "ultima_dose": datetime.now()
    }


adicionar_medicamento = lambda lista,medicamento: lista + [medicamento]

def atualizar_medicamento(lista, nome_medicamento, nova_data):
    return list(
        map(
            lambda med: {
                **med, 
                "ultima_dose": nova_data,
                "quantidade_caixa": med["quantidade_caixa"] - med["comprimidos_por_dose"]
            } if med["nome"] == nome_medicamento else med,
            lista
        )
    )