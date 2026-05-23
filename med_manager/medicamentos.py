from functools import reduce

def gerar_horarios(dia_inicial, horario_inicial, intervalo, duracao_tratamento):
    dias_semana = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]
    
    dia_limpo = dia_inicial.strip().lower().replace("ç", "c").replace("á", "a").replace("ã", "a")
    dia_index = dias_semana.index(dia_limpo)
    
    total_doses = (duracao_tratamento * 24) // intervalo
    
    # Função pura que calcula o horário de cada dose individualmente
    def calcular_dose(numero_da_dose):
        horas_passadas = numero_da_dose * intervalo
        horas_totais = horario_inicial + horas_passadas
        
        dia_calculado = (dia_index + (horas_totais // 24)) % 7
        hora_calculada = horas_totais % 24
        
        nome_dia = dias_semana[dia_calculado].capitalize()
        return f"{nome_dia} {hora_calculada:02d}:00"

    # map substitui o while
    return list(map(calcular_dose, range(total_doses)))


def criar_medicamento(nome, dosagem, intervalo, comprimidos_por_dose, duracao_tratamento, quantidade_caixa, dia_inicial, horario_inicial):
    horarios = gerar_horarios(dia_inicial, horario_inicial, intervalo, duracao_tratamento)
    total_doses = len(horarios)
    
    return {
        "nome": nome,
        "dosagem": dosagem,
        "intervalo": intervalo,
        "horarios": horarios,
        "comprimidos_por_dose": comprimidos_por_dose,
        "duracao_tratamento": duracao_tratamento,
        "total_doses": total_doses,
        "total_necessario": total_doses * comprimidos_por_dose
    }


def adicionar_medicamento(lista, medicamento):
    # Retorna uma NOVA lista (imutabilidade)
    return lista + [medicamento]


def gerar_rotina_diaria(medicamentos):
    # Extrai todos os pares (horário, nome do remédio) usando list comprehension
    pares_horario_nome = [
        (horario, med["nome"]) 
        for med in medicamentos 
        for horario in med["horarios"]
    ]
    
    # Função pura para acumular os dados no dicionário sem alterar o original
    def agrupar_horarios(acumulador, par):
        horario, nome = par
        novo_dict = acumulador.copy() # Cria uma cópia para manter a imutabilidade
        novo_dict[horario] = novo_dict.get(horario, []) + [nome]
        return novo_dict

    # reduce aplica a função em todos os itens e constrói o dicionário final
    return reduce(agrupar_horarios, pares_horario_nome, {})