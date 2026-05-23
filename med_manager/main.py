from medicamentos import (
    criar_medicamento,
    adicionar_medicamento,
    gerar_rotina_diaria
)

def main():
    medicamentos = []

    while True:
        print("\n==== GERENCIADOR DE MEDICAMENTOS ====")
        print("1 - Cadastrar medicamento")
        print("2 - Mostrar medicamentos")
        print("3 - Mostrar quadro do dia")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            dosagem = input("Dosagem: ")
            intervalo = int(input("Intervalo em horas: "))
            comprimidos_por_dose = int(input("Comprimidos por dose: "))
            duracao_tratamento = int(input("Duração do tratamento (dias): "))
            
            dia_inicial = input("Dia da semana que pretende começar o tratamento: ")
            horario_inicial = int(input("Horário inicial (ex: 8): "))

            medicamento = criar_medicamento(
                nome, dosagem, intervalo, comprimidos_por_dose, 
                duracao_tratamento, dia_inicial, horario_inicial
            )

            # O estado da lista é atualizado de forma controlada
            medicamentos = adicionar_medicamento(medicamentos, medicamento)
            print("\nMedicamento cadastrado com sucesso!")

        elif opcao == "2":
            print("\n=== LISTA DE MEDICAMENTOS ===")
            for med in medicamentos:
                print(f"\nNome: {med['nome']} | Dosagem: {med['dosagem']}")
                
                dia_anterior = ""
                for horario in med["horarios"]:
                    dia, hora = horario.split(" ", 1)
                    if dia != dia_anterior:
                        print(f"\n{dia} Horários:")
                        dia_anterior = dia
                    print(f"  {hora}")

        elif opcao == "3":
    
            rotina = gerar_rotina_diaria(medicamentos)
            print("\n=== QUADRO DE HORÁRIOS ===")
            
            # Dicionário para mapear cada dia para um peso numérico
            ordem_dias = {
                "Segunda": 0, "Terca": 1, "Quarta": 2, "Quinta": 3, 
                "Sexta": 4, "Sabado": 5, "Domingo": 6
            }
            
            # Função anônima (lambda) que ensina o sorted() a ordenar certo
            # Ele separa "Segunda 08:00" em dia="Segunda", hora="08:00"
            # E ordena primeiro pelo peso do dia (0 a 6), depois pela hora (00:00 a 23:59)
            chaves_ordenadas = sorted(
                rotina.keys(), 
                key=lambda k: (ordem_dias.get(k.split()[0], 7), k.split()[1])
            )

            for horario in chaves_ordenadas:
                print(f"\n[{horario}]")
                for nome in rotina[horario]:
                    print(f" - {nome}")
        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

# Boa prática em Python para executar a aplicação
if __name__ == "__main__":
    main()