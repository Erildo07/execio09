from cliente import Cliente
from conta import Conta

# Criando um cliente Sicred 
cliente_sicred = Cliente('Jhosy', '123.456.789-00', 21, 98000)

print("Nome: ", cliente_sicred.nome)
print("Idade: ", cliente_sicred.idade)
print("CPF",cliente_sicred.cpf)

# Criando uma conta no Sicred para o cliente 'Jhosy'
conta_sicred = Conta('Jhosy', '123.456.789-00', 21, 98000)

# Realizando um depósito
conta_sicred.deposito(50)
print("Seu novo saldo é de: ", conta_sicred.saldo)

# Realizando um saque
conta_sicred.saque(1500)
print("Seu novo saldo é de: ", conta_sicred.saldo)

# Mostrando o saldo final
print("Saldo final: ", conta_sicred.saldo)