from medicamentos import (
    criar_medicamento,
    adicionar_medicamento
)

medicamentos = []

#tbm quero uma funcionalidade de tipo quando eu for add um novo medicamente pergunta se eu ja tomei ele antes de colocalo no programa, se sim, mostra os horarios que eu tomei e pergunta se quero manter ou alterar
while True:

    print("\n==== GERENCIADOR DE MEDICAMENTOS ====")
    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
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
        print("Listar")

    elif opcao == "0":
        break

    else:
        print("Opção inválida")