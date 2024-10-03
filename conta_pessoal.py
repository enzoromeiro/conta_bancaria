class ContaBancaria: 
    def __init__(self, nome_titular):
        self.nome_titular = nome_titular
        self.saldo = 0
        self.historico_transacao = []
    
    def depositar(self, valor):
        if valor <= 0:
            print("\nValor de depósito inválido!")
        else:
            self.saldo += valor
            print(f"\nDepósito concluído!")
            self.historico_transacao.append({f"   + {valor}R$   "})

    def sacar(self, valor):
        if valor <= 0:
            print("\nValor de saque inválido!")
        elif valor > self.saldo:
            print("\nSaldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"\nSaque concluído!")
            self.historico_transacao.append({f"   - {valor}R$   "})
            
    def consultarSaldo(self):
        print(f"\nSeu saldo atual {self.nome_titular}: {self.saldo}R$\n")
    
    def exibirHistorico(self):
        print(f"\n{self.historico_transacao}\n")


 
