def criar_medicamento(nome,dosagem,intervalo,comprimidos_por_dose,duracao_tratamento,quantidade_caixa,horario_inicial):
    
    # Gera horários automáticos
    horarios = list(
        range(horario_inicial,24,intervalo ) 
        
        # Logica para gerar os horários com base no intervalo e horário inicial
        # exp:range(0, 24, 8) resultado: [0, 8, 16] Horários para tomar o medicamento a cada 8 horas, começando à meia-noite
    )

    # Quantas vezes o remédio é tomado por dia
    doses_por_dia = len(horarios)

    # Quantidade total por dia
    comprimidos_por_dia = (
        doses_por_dia *
        comprimidos_por_dose
    )

    # Quantidade total necessária
    total_necessario = (
        comprimidos_por_dia *
        duracao_tratamento
    )

    # Verifica se a caixa é suficiente
    caixa_suficiente = (
        quantidade_caixa >= total_necessario
    )

    # Quantos comprimidos faltam
    faltam = max(
        0,
        total_necessario - quantidade_caixa
    )

    return {

        "nome": nome,

        "dosagem": dosagem,

        "intervalo": intervalo,

        "horarios": horarios,

        "comprimidos_por_dose":
        comprimidos_por_dose,

        "duracao_tratamento":
        duracao_tratamento,

        "quantidade_caixa":
        quantidade_caixa,

        "comprimidos_por_dia":
        comprimidos_por_dia,

        "total_necessario":
        total_necessario,

        "caixa_suficiente":
        caixa_suficiente,

        "faltam":
        faltam
    }