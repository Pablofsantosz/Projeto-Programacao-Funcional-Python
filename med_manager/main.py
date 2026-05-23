from medicamentos import (
    criar_medicamento,
    adicionar_medicamento,
    formatar_horarios,
    gerar_rotina_diaria
)


medicamentos = []

#tbm quero uma funcionalidade de tipo quando eu for add um novo medicamente pergunta se eu ja tomei ele antes de colocalo no programa, se sim, mostra os horarios que eu tomei e pergunta se quero manter ou alterar
while True:

    print("\n==== GERENCIADOR DE MEDICAMENTOS ====")
    print("1 - Cadastrar medicamento")
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

        novo = criar_medicamento(
            nome,
            dosagem,
            intervalo,
            comprimidos_por_dose,
            duracao_tratamento,
            quantidade_caixa,
            0
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
            print("\n=== Lista de Medicamentos ===")
            for med in medicamentos:
                print(
                        "Nome:",med["nome"]
                    )

                print(
                    "Dosagem:",med["dosagem"]
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
                        "Total necessário:",med["total_necessario"]
                    )

                print(
                    "Quantidade na caixa:",med["quantidade_caixa"]
                )

                if med["caixa_suficiente"]:

                    print("Caixa suficiente")

                else:

                    print(
                        "Faltam",med["faltam"],"comprimidos para o final do tratamento"
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
        