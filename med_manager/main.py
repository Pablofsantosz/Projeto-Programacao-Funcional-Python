from medicamentos import criar_medicamento
medicamentos = []

#tbm quero uma funcionalidade de tipo quando eu for add um novo medicamente pergunta se eu ja tomei ele antes de colocalo no programa, se sim, mostra os horarios que eu tomei e pergunta se quero manter ou alterar
while True:

    print("\n==== GERENCIADOR DE MEDICAMENTOS ====")
    print("1 - Cadastrar medicamento")
    print("2 - Listar medicamentos")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        print("Cadastrar")

    elif opcao == "2":
        print("Listar")

    elif opcao == "0":
        break

    else:
        print("Opção inválida")