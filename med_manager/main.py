import time
import winsound
from datetime import datetime
from medicamentos import criar_medicamento, adicionar_medicamento, atualizar_medicamento
from horarios import calcular_proximo_horario, obter_medicamentos_pendentes, formatar_data

medicamentos = []

while True:
    print("\n==== GERENCIADOR DE MEDICAMENTOS ====")
    print("1 - Cadastrar medicamento")
    print("2 - Mostrar status dos medicamentos")
    print("3 - Iniciar Monitoramento (Dinâmico)")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        dosagem = input("Dosagem: ")
        intervalo = int(input("Intervalo em minutos: "))        
        comprimidos_por_dose = int(input("Comprimidos por dose: "))
        duracao_tratamento = int(input("Duração do tratamento (dias): "))
        quantidade_caixa = int(input("Quantidade na caixa: "))

        novo = criar_medicamento(
            nome, dosagem, intervalo, comprimidos_por_dose, duracao_tratamento, quantidade_caixa
        )
        medicamentos = adicionar_medicamento(medicamentos, novo)
        print("\nMedicamento cadastrado! O relógio começou a contar a partir de agora.")

    elif opcao == "2":
        if not medicamentos:
            print("\nNenhum medicamento cadastrado.")
        else:
            print("\n=== LISTA DE MEDICAMENTOS ===")
            for med in medicamentos:
                proximo = calcular_proximo_horario(med)
                print(f"\nNome: {med['nome']}")
                print(f"Dosagem: {med['dosagem']}")
                print(f"Última dose: {formatar_data(med['ultima_dose'])}")
                print(f"Próxima dose: {formatar_data(proximo)}")

    elif opcao == "3":
        if not medicamentos:
            print("\nCadastre um medicamento primeiro.")
            continue

        print("\nMonitoramento iniciado. Pressione Ctrl+C para voltar ao menu.")
        
        try:
            while True:
                agora = datetime.now()
                pendentes = obter_medicamentos_pendentes(medicamentos, agora)

                for med in pendentes:
                    print(f"\n[ALERTA] Hora de tomar: {med['nome']} ({med['dosagem']})")
                    
                    winsound.PlaySound("Assobio-WhatsApp.wav", winsound.SND_FILENAME)
                    
                    confirmacao = input("Pressione ENTER para confirmar que tomou (ou digite 's' para pular): ")
                    
                    if confirmacao.lower() != 's':
                        nova_dose = datetime.now()
                        
                        medicamentos = atualizar_medicamento(medicamentos, med['nome'], nova_dose)
                        
                        
                        med_atualizado = next(m for m in medicamentos if m['nome'] == med['nome'])
                        
                        
                        if med_atualizado["quantidade_caixa"] <= 0:
                            print(f"\n[AVISO] A caixa de {med['nome']} acabou. O medicamento foi removido do monitoramento.")
                            winsound.PlaySound("zoeira-efeito-mario-morre.wav", winsound.SND_FILENAME)
                            medicamentos = list(filter(lambda m: m['nome'] != med['nome'], medicamentos))
                        else:
                            proximo = calcular_proximo_horario(med_atualizado)
                            print(f"Dose confirmada. Restam {med_atualizado['quantidade_caixa']} comprimidos na caixa.")
                            print(f"Próxima dose será às {formatar_data(proximo)}")

                time.sleep(5)
        except KeyboardInterrupt:
            print("\nMonitoramento pausado.")