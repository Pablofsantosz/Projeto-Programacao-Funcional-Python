def criar_medicamento(nome,dosagem,intervalo,comprimidos_por_dose,duracao_tratamento,quantidade_caixa,horario_inicial):
    
    # Gera horários automáticos
    horarios = list(
        range(horario_inicial,24,intervalo ) 
        
        # Logica para gerar os horários com base no intervalo e horário inicial
        # exp:range(0, 24, 8) resultado: [0, 8, 16] Horários para tomar o medicamento a cada 8 horas, começando à meia-noite
    )

    # Quantas vezes o remédio é tomado por dia
    doses_por_dia = len(horarios)

    # Total de comprimidos por dia
    comprimidos_por_dia = (
        doses_por_dia *
        comprimidos_por_dose
    )


    # Quantidade total necessária
    total_necessario = (
        comprimidos_por_dia *
        duracao_tratamento
    )

    return {

        "nome": nome,
        "dosagem": dosagem,
        "intervalo": intervalo,
        "horarios": horarios,
        "comprimidos_por_dose": comprimidos_por_dose,
        "duracao_tratamento": duracao_tratamento,
        "quantidade_caixa": quantidade_caixa,
        "comprimidos_por_dia": comprimidos_por_dia,
        "total_necessario": total_necessario,
        
    }
    
def adicionar_medicamento(
    lista,
    medicamento
):

    # Retorna uma NOVA lista
    return lista + [medicamento]



def gerar_rotina_diaria(medicamentos):

    rotina = {}

    for med in medicamentos:

        for horario in med["horarios"]:

            rotina[horario] = (
                rotina.get(horario, [])
                + [med["nome"]]
            )

    return rotina


def formatar_horarios(horarios):

    return list(
        map(
            lambda hora:
            f"{hora:02d}:00",

            horarios
        )
    )