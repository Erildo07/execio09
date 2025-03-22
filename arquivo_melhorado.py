from cliente import Cliente
from conta import Conta

# Criando um cliente Sicred 
cliente_sicred = Cliente('Jhosy', '123.456.789-00', 21, 98000)

print("Nome: ", cliente_sicred.nome)
print("Idade: ", cliente_sicred.idade)

conta_sicred = Conta('Jhosy', '123.456.789-00', 21, 98000)

# Função para interagir com o usuário
def interagir():
    while True:
        print("\nEscolha uma opção:")
        print("1. Depósito")
        print("2. Saque")
        print("3. Ver saldo")
        print("4. Sair")
        
        escolha = input("Digite o número da opção escolhida: ")

        if escolha == '1':
            try:
                valor_deposito = float(input("Digite o valor do depósito: R$ "))
                conta_sicred.deposito(valor_deposito)
                print(f"Depósito realizado com sucesso! Seu novo saldo é: R$ {conta_sicred.saldo}")
            except ValueError:
                print("Por favor, digite um valor válido para o depósito.")
        
        elif escolha == '2':
            try:
                valor_saque = float(input("Digite o valor do saque: R$ "))
                conta_sicred.saque(valor_saque)
                print(f"Saque realizado com sucesso! Seu novo saldo é: R$ {conta_sicred.saldo}")
            except ValueError:
                print("Por favor, digite um valor válido para o saque.")
        
        elif escolha == '3':
            print(f"Seu saldo atual é: R$ {conta_sicred.saldo}")
        
        elif escolha == '4':
            print("Saindo... Até logo!!!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

interagir()
