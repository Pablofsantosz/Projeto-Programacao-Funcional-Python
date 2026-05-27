from datetime import timedelta

calcular_proximo_horario = lambda medicamento: medicamento["ultima_dose"] + timedelta(hours=medicamento["intervalo"])

esta_na_hora = lambda medicamento, hora_atual: calcular_proximo_horario(medicamento) <= hora_atual

def obter_medicamentos_pendentes(medicamentos, hora_atual):
    return list(
        filter(
            lambda med: med["quantidade_caixa"] > 0 and esta_na_hora(med, hora_atual),
            medicamentos
        )
    )


formatar_data = lambda data: data.strftime("%d/%m/%Y %H:%M:%S")