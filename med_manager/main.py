from medicamentos import (
    criar_medicamento,
    adicionar_medicamento,
    formatar_horarios,
    gerar_rotina_diaria
)

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

        intervalo = int(
            input("Intervalo em horas: ")
        )

        comprimidos_por_dose = int(
            input("Comprimidos por dose: ")
        )

        duracao_tratamento = int(
            input("Duração do tratamento (dias): ")
        )

        quantidade_caixa = int(
            input("Quantidade na caixa: ")
        )

        horario_inicial = int(
            input("Horário inicial: ")
        )

        novo = criar_medicamento(
            nome,
            dosagem,
            intervalo,
            comprimidos_por_dose,
            duracao_tratamento,
            quantidade_caixa,
            horario_inicial
        )

        medicamentos = adicionar_medicamento(
            medicamentos,
            novo
        )

        print("\nMedicamento cadastrado!")

    elif opcao == "2":

        if not medicamentos:

            print("\nNenhum medicamento cadastrado.")

        else:

            print("\n=== LISTA DE MEDICAMENTOS ===")

            for med in medicamentos:

                print(
                    "\nNome:",
                    med["nome"]
                )

                print(
                    "Dosagem:",
                    med["dosagem"]
                )

                horarios_formatados = (
                    formatar_horarios(
                        med["horarios"]
                    )
                )

                print(
                    "Horários:",
                    horarios_formatados
                )

                print(
                    "Total necessário:",
                    med["total_necessario"]
                )

    elif opcao == "3":

        rotina = gerar_rotina_diaria(
            medicamentos
        )

        print("\n=== QUADRO DE HORÁRIOS ===")

        for horario in sorted(rotina):

            print(
                f"\n{horario:02d}:00"
            )

            for nome in rotina[horario]:

                print("-", nome)

    elif opcao == "0":

        break

    else:

        print("Opção inválida")