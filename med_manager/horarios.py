from datetime import timedelta

def calcular_proximo_horario(medicamento):
    return medicamento["ultima_dose"] + timedelta(minutes=medicamento["intervalo"])

def esta_na_hora(medicamento, hora_atual):
    proximo = calcular_proximo_horario(medicamento)
    return hora_atual >= proximo

def obter_medicamentos_pendentes(medicamentos, hora_atual):
    return list(
        filter(
            lambda med: esta_na_hora(med, hora_atual),
            medicamentos
        )
    )

def formatar_data(data):
    return data.strftime("%d/%m/%Y %H:%M:%S")