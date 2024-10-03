from conta_pessoal import ContaBancaria
from utilidade import limparTerminal

possuiConta = False

while True:

    print("-"*20)
    print("        MENU        ")
    print("-"*20)
    inputUsuario = int(input("\n[1] - Criar Conta\n[2] - Depositar\n[3] - Sacar\n[4] - Consultar Saldo\n[5] - Histórico de Transações\n[6] - Sair\n\nEscolha sua opção: "))

    if inputUsuario < 1 or inputUsuario > 6:
         limparTerminal()
         print("\nOpção Inválida!\n")
    elif inputUsuario != 1 and possuiConta == False and inputUsuario != 6:
                limparTerminal()
                print("\nAção inválida! Crie uma conta.\n")
    else:
        match inputUsuario:
            case 1:
                if inputUsuario == 1 and possuiConta == True:
                    limparTerminal()
                    print("\nVocê ja possui uma conta!\n")
                else:
                    inputNome = input("\nDigite Seu nome: ")
                    conta1 = ContaBancaria(inputNome)
                    possuiConta = True
                    limparTerminal()
                    print("\nConta Criada!\n")
            case 2:
                limparTerminal()
                valorDeposito = float(input("Digite o valor a ser depositado: "))
                conta1.depositar(valorDeposito)
            case 3: 
                limparTerminal()
                valorSaque = float(input("Digite o valor a ser sacado: "))
                conta1.sacar(valorSaque)
            case 4:
                limparTerminal()
                conta1.consultarSaldo()
            case 5: 
                if conta1.historico_transacao == []:
                    limparTerminal()
                    print("Você não possui transações! ")
                else:
                    limparTerminal()
                    conta1.exibirHistorico()
            case 6:
                break
            

    