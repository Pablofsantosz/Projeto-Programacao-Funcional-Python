def criar_medicamento(nome,dosagem,intervalo,quantidade,inicio):

    horarios = list(
        range(inicio, 24, intervalo)
    )

    return {
        "nome": nome,
        "dosagem": dosagem,
        "intervalo": intervalo,
        "quantidade": quantidade,
        "horarios": horarios
    }